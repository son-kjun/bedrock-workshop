# 실습 3. RAG를 이용한 챗봇

이 실습에서는 Amazon Bedrock, LangChain, Streamlit 을 사용하여 RAG(Retrieval-Augmented Generation, 검색 증강 생성)를 지원하는 Chatbot을 구축해 보겠습니다.

Amazon Bedrock(및 일반적인 LLM)에는 상태나 메모리에 대한 개념이 없습니다. 모든 채팅 기록은 외부에서 추적한 다음 새 메시지가 들어올 때마다 모델에 전달해야 합니다. 저희는 채팅 기록을 추적하기 위해 LangChain의 **ConversationBufferWindowMemory** 클래스를 사용합니다. 모델에서 처리할 수 있는 토큰 수에는 제한이 있기 때문에 사용자의 메시지와 모델의 응답을 처리할 수 있는 충분한 공간이 남도록 채팅 기록을 잘라내야 합니다. ConversationBufferWindowMemory는 가장 최근 메시지를 추적하여 이를 지원합니다.

또한 검색 증강 생성 (RAG; Retrieval-Augmented Generation) 을 통해 모델의 기본 데이터를 외부 지식으로 보완하고자 합니다. LangChain의 **ConversationalRetrievalChain** 클래스를 사용해 한 번의 호출로 챗봇과 RAG 기능을 결합할 것입니다.

1. Amazon Bedrock : Anthropic Claude 3 Sonnet
2. Amazon Titan Embeddings
3. LangChain : ConversationBufferWindowMemory / ConversationalRetrievalChain
4. Streamlit
5. 인메모리 [FAISS](https://github.com/facebookresearch/faiss) 데이터베이스

이 애플리케이션은 두 개의 파일로 구성되어 있는데, 하나는 Streamlit 프론트엔드용 파일이고 다른 하나는 베드락을 호출하기 위한 지원 라이브러리용 파일입니다.

## 1. 라이브러리 스크립트 만들기
먼저 Streamlit 프론트엔드와 Bedrock 백엔드를 연결하기 위한 지원 라이브러리를 생성합니다.

1. **workshop/labs/rag_chatbot** 폴더로 이동하여 rag_chatbot_lib_kr.py 파일을 엽니다.
![image](https://github.com/user-attachments/assets/b7a67ff8-2977-4c28-86e2-32ee5c164be8)

2. import 구문을 추가합니다.
   * 이 명령문을 사용하면 LangChain을 사용하여 Bedrock을 호출하고 환경 변수를 읽을 수 있습니다.
   * 아래 상자의 복사 버튼을 사용하면 해당 코드를 자동으로 복사할 수 있습니다.

~~~python
from langchain.memory import ConversationBufferWindowMemory
from langchain_community.chat_models import BedrockChat
from langchain.chains import ConversationalRetrievalChain

from langchain_community.embeddings import BedrockEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
~~~

3. Bedrock Langchain 클라이언트를 생성하는 함수를 추가합니다.
     * 여기에는 챗봇에 사용하려는 추론 매개변수가 포함됩니다.

~~~python
def get_llm():
        
    model_kwargs = { #anthropic
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1024, 
        "temperature": 0
    }
    
    llm = BedrockChat(
        model_id="anthropic.claude-3-sonnet-20240229-v1:0", #파운데이션 모델 지정
        model_kwargs=model_kwargs) #Claude 속성 구성
    
    return llm
~~~

4. 인메모리 벡터 저장소를 생성하는 함수를 추가합니다.
   * 자세한 내용은 아래 코드의 인라인 주석을 참조하세요.

~~~python
def get_index(): #애플리케이션에서 사용할 인메모리 벡터 저장소를 생성하고 반환합니다.
    
    embeddings = BedrockEmbeddings() #Titan 임베딩 클라이언트를 생성합니다.
    
    pdf_path = "2022-Shareholder-Letter.pdf" #이 이름을 가진 로컬 PDF 파일을 가정합니다.

    loader = PyPDFLoader(file_path=pdf_path) #PDF 파일 로드하기
    
    text_splitter = RecursiveCharacterTextSplitter( #텍스트 분할기 만들기
        separators=["\n\n", "\n", ".", " "], #(1) 단락, (2) 줄, (3) 문장 또는 (4) 단어 순서로 청크를 분할합니다.
        chunk_size=1000, #위의 구분 기호를 사용하여 1000자 청크로 나눕니다.
        chunk_overlap=100 #이전 청크와 겹칠 수 있는 문자 수입니다.
    )
    
    index_creator = VectorstoreIndexCreator( #벡터 스토어 팩토리 만들기
        vectorstore_cls=FAISS, #데모 목적으로 인메모리 벡터 저장소를 사용합니다.
        embedding=embeddings, #Titan 임베딩 사용
        text_splitter=text_splitter, #재귀적 텍스트 분할기 사용하기
    )
    
    index_from_loader = index_creator.from_loaders([loader]) #로드된 PDF에서 벡터 스토어 인덱스를 생성합니다.
    
    return index_from_loader #클라이언트 앱에서 캐시할 인덱스를 반환합니다.
~~~

5. LangChain 메모리 객체를 초기화하는 함수를 추가합니다.
     * 이 경우 ConversationBufferWindowMemory 클래스를 사용하고 있습니다. 이를 통해 가장 최근 메시지를 추적하고 이전 메시지를 요약하여 긴 대화 동안 채팅 컨텍스트가 유지되도록 할 수 있습니다.
  
~~~python
def get_memory(): #이 채팅 세션을 위한 메모리 만들기
    
    memory = ConversationBufferWindowMemory(memory_key="chat_history", return_messages=True) #이전 메시지의 기록을 유지합니다.
    
    return memory
~~~

6. 이 함수를 추가하여 Bedrock을 호출합니다.
     * Streamlit 프런트엔드 애플리케이션에서 호출할 수 있는 함수를 만들고 있습니다. 이 함수는 LangChain으로 Bedrock 클라이언트를 생성한 다음 입력 콘텐츠를 Bedrock으로 전달합니다.
  
~~~python
def get_rag_chat_response(input_text, memory, index): #chat client 함수
    
    llm = get_llm()
    
    conversation_with_retrieval = ConversationalRetrievalChain.from_llm(llm, index.vectorstore.as_retriever(), memory=memory)
    
    chat_response = conversation_with_retrieval.invoke({"question": input_text}) #사용자 메시지, 기록 및 지식을 모델에 전달합니다.
    
    return chat_response['answer']
~~~

7. 파일을 저장합니다.
   백킹 라이브러리가 완성되었습니다. 이제 프론트엔드 애플리케이션을 만들겠습니다.

## 2. Steamlit 프론트엔드 앱 만들기

1. 라이브러리 파일과 같은 폴더에서 rag_chatbot_app_kr.py 파일을 엽니다.

2. import 문을 추가합니다.

이 문은 백킹 라이브러리 스크립트에서 Streamlit 요소를 사용하고 함수를 호출할 수 있도록 해줍니다.

~~~python
import streamlit as st #모든 Streamlit 명령은 "st" 별칭을 통해 사용할 수 있습니다.
import rag_chatbot_lib_kr as glib #로컬 라이브러리 스크립트에 대한 참조
~~~

3. 페이지 제목, 구성을 추가합니다.
   여기서는 실제 페이지의 페이지 제목과 브라우저 탭에 표시되는 제목을 설정합니다.

~~~python
st.set_page_config(page_title="RAG Chatbot") #HTML 제목
st.title("RAG Chatbot") #페이지 제목 
~~~

4. 세션 캐시에 LangChain 메모리를 추가합니다.
이를 통해 사용자 세션당 고유한 채팅 메모리를 유지할 수 있습니다. 그렇지 않으면 챗봇이 사용자와의 과거 메시지를 기억할 수 없습니다.
Streamlit에서는 세션 상태가 서버 측에서 추적됩니다. 브라우저 탭이 닫히거나 애플리케이션이 중지되면 세션과 채팅 기록이 손실됩니다. 실제 애플리케이션에서는 Amazon DynamoDB 와 같은 데이터베이스에서 채팅 기록을 추적할 수 있습니다.

~~~python
if 'memory' not in st.session_state: #메모리가 아직 생성되지 않았는지 확인합니다.
    st.session_state.memory = glib.get_memory() #메모리를 초기화합니다.
~~~


5. UI 채팅 기록을 세션 캐시에 추가합니다.
이렇게 하면 사용자 상호작용이 있을 때마다 Streamlit 앱이 다시 실행될 때 채팅 기록을 UI에 다시 렌더링할 수 있습니다. 그렇지 않으면 새 채팅 메시지와 함께 이전 메시지가 사용자 인터페이스에서 사라집니다.

~~~python
if 'chat_history' not in st.session_state: #채팅 기록이 아직 생성되지 않았는지 확인하기
    st.session_state.chat_history = [] #채팅 기록 초기화하기
~~~

6. 세션 캐시에 벡터 인덱스를 추가합니다.
이를 통해 사용자 세션당 인메모리 벡터 데이터베이스를 유지할 수 있습니다.

~~~python
if 'vector_index' not in st.session_state: #벡터 인덱스가 아직 생성되지 않았는지 확인합니다.
    with st.spinner("Indexing document..."): #이 블록의 코드가 실행되는 동안 스피너를 표시합니다.
        st.session_state.vector_index = glib.get_index() #지원 라이브러리를 통해 인덱스를 검색하고 앱의 세션 캐시에 저장합니다.
~~~


7. for 루프를 추가하여 이전 채팅 메시지를 렌더링합니다.
chat_history 세션 상태 개체를 기반으로 이전 메시지를 다시 렌더링합니다.

~~~python
#채팅 기록 다시 렌더링(Streamlit은 이 스크립트를 다시 실행하므로, 이전 채팅 메시지를 보존하려면 이 기능이 필요합니다.)
for message in st.session_state.chat_history: #채팅 기록을 반복해서 살펴보기
    with st.chat_message(message["role"]): #지정된 역할에 대한 채팅 줄을 렌더링하며, with 블록의 모든 내용을 포함합니다.
        st.markdown(message["text"]) #채팅 콘텐츠를 표시합니다.
~~~

8. 입력 요소를 추가합니다.
   아래 if 블록을 사용하여 사용자 입력을 처리합니다. 자세한 내용은 아래 인라인 코멘트를 참조하세요.

~~~python
input_text = st.chat_input("당신의 봇과 여기서 대화하세요") #채팅 입력 상자를 표시합니다.

if input_text: #사용자가 채팅 메시지를 제출한 후 이 if 블록의 코드를 실행합니다.
    
    with st.chat_message("user"): #사용자 채팅 메시지를 표시합니다.
        st.markdown(input_text) #사용자의 최신 메시지를 렌더링합니다.
    
    st.session_state.chat_history.append({"role":"user", "text":input_text}) #사용자의 최신 메시지를 채팅 기록에 추가합니다.

    chat_response = glib.get_rag_chat_response(input_text=input_text, memory=st.session_state.memory, index=st.session_state.vector_index,) #지원 라이브러리를 통해 모델을 호출합니다.

    with st.chat_message("assistant"): #봇 채팅 메시지를 표시합니다.
        st.markdown(chat_response) #봇의 최신 답변을 표시합니다.
    
    st.session_state.chat_history.append({"role":"assistant", "text":chat_response}) #봇의 최신 메시지를 채팅 기록에 추가합니다.
~~~

9. 파일을 저장합니다.
멋지네요! 이제 애플리케이션을 실행할 준비가 되었습니다!

## 3. Streamlit 앱 실행

1. AWS Cloud9에서 bash terminal을 선택하고 디렉터리를 변경합니다.

```
cd ~/environment/workshop/labs/rag_chatbot
```

2. 터미널에서 streamlit 명령을 실행합니다.
   
```
streamlit run rag_chatbot_app_kr.py --server.port 8080
```

스트림릿 명령에 표시되는 네트워크 URL 및 외부 URL 링크는 무시합니다. 대신 AWS Cloud9의 미리보기 기능을 사용하겠습니다.

3.AWS Cloud9에서 Preview -> Preview Running Application를 선택합니다.
![image](https://github.com/user-attachments/assets/c397a168-2a38-43c0-a71d-43543bccf630)

아래와 같은 웹 페이지가 표시됩니다:
![image](https://github.com/user-attachments/assets/d98d8e6a-68b6-4992-943b-ca8bf54f3796)

4. 몇 가지 프롬프트를 시도하고 결과를 확인합니다.
   CEO는 누구인가요?
   언제부터 시작했나요?
   회사의 Generative AI 전략은 무엇인가요?

   ![image](https://github.com/user-attachments/assets/11019a3e-67b4-4c72-8cb5-82a6eaffbe82)

5. AWS Cloud9에서 미리보기 탭을 닫습니다. 터미널로 돌아가서 Control-C를 눌러 애플리케이션을 종료합니다.
