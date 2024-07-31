# 실습 3. 문서 요약

이 실습에서는 Amazon Bedrock, LangChain, Streamlit을 사용해 간단한 문서 요약기를 구축해 보겠습니다.

LangChain에는 모델의 토큰 한도를 초과하는 콘텐츠를 처리할 수 있는 맵-리듀스 요약 기능이 포함되어 있습니다. 맵-리듀스 기능은 문서를 작은 조각으로 나누고, 그 조각들을 요약한 다음, 그 조각들의 요약을 요약하는 방식으로 작동합니다.

아래 코드 스니펫을 복사하여 지정된 Python 파일에 붙여넣어 애플리케이션 코드를 작성할 수 있습니다.

이 애플리케이션은 두 개의 파일로 구성되어 있는데, 하나는 Streamlit 프론트엔드용 파일이고 다른 하나는 베드락을 호출하기 위한 지원 라이브러리용 파일입니다.


### 사용 사례
맵-리듀스 요약 패턴은 다음과 같은 사용 사례에 적합합니다

![image](https://github.com/user-attachments/assets/7b0b8093-9ce4-4961-899a-dfbb84ce79d6)


* 긴 문서 요약
* 통화 기록 요약
* 고객 활동 기록 요약

### 아키텍처

![image](https://github.com/user-attachments/assets/71ce2a02-f939-4392-8557-d7703c15bb44)

맵-리듀스 패턴에는 다음 단계가 포함됩니다

* 큰 문서를 작은 청크들로 나눕니다.
* 이 작은 청크를 기반으로 중간 요약을 생성합니다.
* 중간 요약들을 통합 요약으로 요약합니다.

## 1. 라이브러리 스크립트 만들기
Streamlit 프론트엔드와 Bedrock 백엔드를 연결하기 위한 지원 라이브러리를 생성합니다.

1. 먼저 Git Repository로부터 소스를 다운로드 합니다.

```
git clone https://github.com/rudolph6/text_summarization.git
```

2. **text_summarization** 폴더로 이동하여 필수 라이브러리를 설치합니다.
```
cd text_summarization/
pip install -r requirement.txt
```
3. **summarization_lib_kr.py** 파일을 엽니다.

4. import 구문을 추가합니다.
   * 이 명령문을 사용하면 LangChain을 사용하여 PDF 파일을 로드하고, 문서를 분할하고, Bedrock을 호출할 수 있습니다.
   * 아래 상자의 복사 버튼을 사용하면 해당 코드를 자동으로 복사할 수 있습니다

~~~python
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import BedrockChat
from langchain.chains.summarize import load_summarize_chain
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
~~~

3. Bedrock Langchain 클라이언트를 생성하는 함수를 추가합니다.
     * 여기에는 사용하고자 하는 추론 매개변수가 포함됩니다.

~~~python
def get_llm():
    
    model_kwargs =  { #Anthropic 모델
        "max_tokens": 8000, 
        "temperature": 0
        }
    
    llm = BedrockChat(
        model_id="anthropic.claude-3-sonnet-20240229-v1:0", #파운데이션 모델 설정하기
        model_kwargs=model_kwargs) #Claude의 속성을 구성합니다.
    
    return llm
~~~

4. 문서 청크를 생성하는 함수를 추가합니다.
   * 이 코드는 문서를 단락, 줄, 문장 또는 단어별로 분할하려고 시도합니다.

~~~python
pdf_path = "2022-Shareholder-Letter.pdf"

def get_docs():
    
    loader = PyPDFLoader(file_path=pdf_path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " "], chunk_size=4000, chunk_overlap=100 
    )
    docs = text_splitter.split_documents(documents=documents)
    
    return docs
~~~

5. 이 함수를 추가하여 Bedrock을 호출합니다.
   * 이 코드는 맵 및 리듀스 단계에 대한 프롬프트를 생성합니다. 그런 다음 문서를 맵 리듀스 요약기 체인으로 전달하여 결합된 요약을 생성합니다.

~~~python
def get_summary(return_intermediate_steps=False):
    
    map_prompt_template = "{text}\n\n위의 내용을 Korean으로 bullet point 3개로 요약합니다:"
    map_prompt = PromptTemplate(template=map_prompt_template, input_variables=["text"])
    
    combine_prompt_template = "{text}\n\n위의 내용을 Korean으로 간결하게 bullet point 5개로 요약합니다:"
    combine_prompt = PromptTemplate(template=combine_prompt_template, input_variables=["text"])
    
    llm = get_llm()
    docs = get_docs()
    
    chain = load_summarize_chain(llm, chain_type="map_reduce", map_prompt=map_prompt, combine_prompt=combine_prompt, return_intermediate_steps=return_intermediate_steps,verbose=True)
    
    if return_intermediate_steps:
        return chain.invoke({"input_documents": docs}, return_only_outputs=True)
    else:
        return chain.invoke(docs, return_only_outputs=True)

~~~

6. 파일을 저장합니다.
   백킹 라이브러리가 완성되었습니다. 이제 프론트엔드 애플리케이션을 만들겠습니다.

   

## 2. Steamlit 프론트엔드 앱 만들기

1. 라이브러리 파일과 같은 폴더에서 summarization_app_kr.py 파일을 엽니다.

2. import 문을 추가합니다.

이 문은 백킹 라이브러리 스크립트에서 Streamlit 요소를 사용하고 함수를 호출할 수 있도록 해줍니다.

~~~python
import streamlit as st
import summarization_lib_kr as glib
~~~

3. 페이지 제목, 구성을 추가합니다.
   여기서는 실제 페이지의 페이지 제목과 브라우저 탭에 표시되는 제목을 설정합니다.

~~~python
st.set_page_config(layout="wide", page_title="문서 요약")
st.title("문서 요약")
~~~

4. 요약 요소를 추가합니다.
   * 이 섹션은 세션 상태의 has_document 속성이 설정될 때까지 표시되지 않습니다.
   * 사용자의 프롬프트를 가져와서 Bedrock으로 전송하는 체크박스와 버튼을 만들고 있습니다. '중간 단계 반환' 체크박스는 MAP 단계의 요약을 표시할지 여부를 결정합니다.
   * 버튼 클릭을 처리하기 위해 아래의 if 블록을 사용합니다. 백킹 함수가 호출되는 동안 스피너를 표시한 다음 웹 페이지에 출력을 표시합니다.

~~~python
return_intermediate_steps = st.checkbox("중간 단계 반환", value=True)
summarize_button = st.button("요약", type="primary")

if summarize_button:
    st.subheader("통합 요약")

    with st.spinner("Running..."):
        response_content = glib.get_summary(return_intermediate_steps=return_intermediate_steps)


    if return_intermediate_steps:

        st.write(response_content["output_text"])

        st.subheader("Section summaries")

        for step in response_content["intermediate_steps"]:
            st.write(step)
            st.markdown("---")

    else:
        st.write(response_content["output_text"])
~~~


5. 파일을 저장합니다.
멋지네요! 이제 애플리케이션을 실행할 준비가 되었습니다!

## 3. Streamlit 앱 실행

1. AWS Cloud9에서 bash terminal을 선택하고 디렉터리를 변경합니다.

```
cd ~/environment/summarization

```

2. 터미널에서 streamlit 명령을 실행합니다.
   * AWS Cloud9 미리 보기에서 파일을 업로드할 수 있도록 server.enableXsrfProtection=false를 설정했습니다.
   
```
streamlit run summarization_app_kr.py --server.port 8080 --server.enableXsrfProtection=false
```
스트림릿 명령에 표시되는 네트워크 URL 및 외부 URL 링크는 무시합니다. 대신 AWS Cloud9의 미리보기 기능을 사용하겠습니다.

3.AWS Cloud9에서 Preview -> Preview Running Application를 선택합니다.
![image](https://github.com/user-attachments/assets/c397a168-2a38-43c0-a71d-43543bccf630)

아래와 같은 웹 페이지가 표시됩니다:
![image](https://github.com/user-attachments/assets/04281e7e-b695-4721-b085-a4690b283ad0)


4. 요약 버튼을 클릭합니다.
   * 요약은 실행하는 데 약 90초 정도 소요될 수 있습니다
   * 완료되면 문서에 대한 통합 요약이 표시되며, 중간 단계를 반환하기로 선택한 경우 개별 섹션 요약도 함께 표시됩니다.

6. AWS Cloud9에서 미리보기 탭을 닫습니다. 터미널로 돌아가서 Control-C를 눌러 애플리케이션을 종료합니다.
