# 실습 4. 텍스트에서 JSON 데이터 추출하기
실습에서는 Bedrock, LangChain, Streamlit을 사용해 JSON 생성기를 만들어 보겠습니다.
Text to JSON을 사용하면 비정형 콘텐츠에서 계층적 데이터를 추출할 수 있습니다. 예를 들어, 고객의 이메일에서 언급된 제품, 언급된 직원, 감정, 계좌 번호 및 프롬프트에 따라 모델이 감지할 수 있는 기타 모든 정보를 추출할 수 있습니다.

아래 코드 스니펫을 복사하여 지정된 Python 파일에 붙여넣으면 애플리케이션 코드를 빌드할 수 있습니다.

이 애플리케이션은 Streamlit 프론트엔드용 파일과 지원 라이브러리가 Bedrock을 호출하기 위한 파일 두 개로 구성됩니다.

### 사용 사례
텍스트에서 JSON으로 변환하는 패턴은 다음과 같은 사용 사례에 적합합니다:

* 이메일 데이터 추출
* 통화 기록 데이터 추출
* 문서 데이터 추출

### 아키텍처
![image](https://github.com/user-attachments/assets/b1f62def-1545-4ea5-a7ed-3e11a8a8826a)

아키텍처 관점에서 볼 때, Text to JSON 변환은 Text to Text 변환과 동일합니다. LLM에서 반환된 텍스트를 JSON 출력으로 안전하게 변환하기만 하면 됩니다.

# 1. 라이브러리 스크립트 만들기

Streamlit 프론트 엔드와 Bedrock 백엔드를 연결하기 위한 지원 라이브러리를 생성합니다.

1. **text_summarization** 폴더로 이동하여 json_lib_kr.py 파일을 엽니다.

2. import 문을 추가합니다.
   * 이 문을 사용하면 LangChain을 사용하여 Bedrock을 호출하고 출력을 JSON으로 안전하게 변환 할 수 있습니다.
   * 아래 상자의 복사 버튼을 사용하면 해당 코드를 자동으로 복사할 수 있습니다
  
~~~python
import json
from json import JSONDecodeError
from langchain_community.chat_models import BedrockChat
~~~

3. Bedrock LangChain 클라이언트를 생성하는 함수를 추가합니다.
   여기에는 사용하려는 추론 매개변수가 포함됩니다.

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

4. 함수를 추가하여 텍스트 결과를 JSON 객체로 변환을 시도합니다.
   이렇게 하면 LLM이 유효한 JSON 형식의 텍스트를 생성하지 못하는 상황을 정상적으로 처리할 수 있습니다.


5. 이 함수를 추가하여 Bedrock을 호출합니다.
   이 코드는 Bedrock을 호출하고 JSON 변환기에 응답을 전달합니다.

~~~python
def get_json_response(input_content): #text-to-text client 함수
    
    llm = get_llm()

    response = llm.invoke(input_content).content #프롬프트에 대한 텍스트 응답
    
    return validate_and_return_json(response)
~~~

6. 파일을 저장합니다.
   * 백킹 라이브러리가 완성되었습니다. 이제 프론트엔드 애플리케이션을 만들겠습니다.

# 2. Streamlit 프론트엔드 앱 만들기

1. 라이브러리 파일과 같은 폴더에서 json_app_kr.py 파일을 엽니다.
 
2. import 문을 추가합니다.
   * 이 문은 백킹 라이브러리 스크립트에서 Streamlit 요소를 사용하고 함수를 호출할 수 있도록 해줍니다.

~~~python
import streamlit as st #모든 Streamlit 명령은 "st" 별칭을 통해 사용할 수 있습니다.
import json_lib_kr as glib #로컬 라이브러리 스크립트에 대한 참조
~~~

3. 페이지 제목, 구성 및 2열 레이아웃을 추가합니다.
   * 여기서는 실제 페이지의 페이지 제목과 브라우저 탭에 표시되는 제목을 설정합니다.
  
~~~python
st.set_page_config(page_title="Text에서 JSON 데이터 추출하기", layout="wide")  #열을 수용하기 위해 페이지 너비를 더 넓게 설정합니다.

st.title("Text에서 JSON 데이터 추출하기")  #페이지 제목

col1, col2 = st.columns(2)  #열 2개 생성
~~~

4. 입력 요소를 추가합니다.
   * 사용자의 프롬프트를 가져와서 Bedrock으로 전송하기 위해 여러 줄의 텍스트 상자와 버튼을 만듭니다.

~~~python
with col1: #이 with 블록의 모든 내용이 열 1에 배치됩니다.
    st.subheader("프롬프트") #이 열의 서브헤드
    
    input_text = st.text_area("텍스트 입력", height=500, label_visibility="collapsed")

    process_button = st.button("Run", type="primary") #기본 버튼 표시
~~~

5. 출력 요소를 추가합니다.
   * 아래 if 블록을 사용하여 버튼 클릭을 처리합니다. 백킹 함수가 호출되는 동안 스피너를 표시한 다음 웹 페이지에 출력을 씁니다. 형식이 지정된 JSON을 표시합니다.

~~~python
with col2: #이 with 블록의 모든 내용이 열 2에 배치됩니다.
    st.subheader("결과") #이 열의 서브헤드
    
    if process_button: #버튼을 클릭하면 이 if 블록의 코드가 실행됩니다.
        with st.spinner("Running..."): #이 if 블록의 코드가 실행되는 동안 스피너를 표시합니다.
            has_error, response_content, err = glib.get_json_response(input_content=input_text) #지원 라이브러리를 통해 모델을 호출합니다.

        if not has_error:
            st.json(response_content) #오류가 없는 경우 JSON을 렌더링합니다.
        else:
            st.error(err) #그렇지 않으면 오류를 렌더링합니다.
            st.write(response_content) #그리고 모델의 원시 응답을 렌더링합니다.
~~~

6. 파일을 저장합니다.
   * 이제 애플리케이션을 실행할 준비가 되었습니다!

# 3. Streamlit 앱 실행

1. AWS Cloud9에서 bash terminal을 선택하고 터미널에서 streamlit 명령을 실행합니다.

```
streamlit run json_app_kr.py --server.port 8080
```
스트림릿 명령에 표시되는 네트워크 URL 및 외부 URL 링크는 무시합니다. 대신 AWS Cloud9의 미리보기 기능을 사용하겠습니다.

2. AWS Cloud9에서 Preview -> Preview Running Application를 선택합니다.
![image](https://github.com/user-attachments/assets/c9852793-1b62-4665-8545-9bc7946c3a91)

아래와 같은 웹 페이지가 표시됩니다.

![image](https://github.com/user-attachments/assets/a857129e-d832-4d06-b701-90849815c552)

3. 몇 가지 프롬프트를 시도하고 결과를 확인합니다.

```
이름, 정당, 임기를 포함한 미국의 초대 대통령부터 5명의 대통령을 JSON 형식의 배열로 반환합니다.다른 답변하지 말고 바로 JSON 형식의 배열로 반환합니다.
```

```
Acme Investments에게,
저는 귀하의 계좌 관리자 중 한 명인 로저 롱바텀의 비윤리적이라고 생각되는 상황을 알려드리기 위해 이 글을 씁니다.
최근 로저를 만나 제 투자 포트폴리오에 대해 논의하던 중 로저가 특정 주식에 투자할 것을 제안했다는 말을 듣고 매우 우려했습니다. 왜 이 주식이 좋은 투자라고 생각하냐고 물었더니 현재 저평가되어 있고 가까운 장래에 가치가 상승할 가능성이 높다고 말했습니다.
하지만 추가 조사를 통해 해당 주식의 평판이 의심스럽다는 사실을 알게 되었습니다. 이 회사는 여러 건의 소송에 휘말렸으며 의심스러운 비즈니스 관행에 연루된 것으로 밝혀졌습니다.
저는 로저가 이러한 사실을 알고 있었지만 저에게 공개하지 않았다고 생각합니다. 그 결과 저는 현명하지 못한 투자 결정을 내리도록 오해를 받았다고 생각합니다.
따라서 로저가 비윤리적인 행동을 했는지 조사하고 필요한 경우 적절한 조치를 취해 주시기 바랍니다.
진심으로 부탁드립니다,
카슨 브래드포드

위의 텍스트를 바탕으로 다음 값을 JSON 형식으로 반환해 주세요.다른 답변하지 말고 바로 JSON 형식의 배열로 반환합니다.:
Sentiment: 긍정, 중립 또는 부정
카테고리: 영업, 운영, 고객 서비스 또는 펀드 관리
요약: (텍스트를 요약한 1~2개 문장)
우려: (위 내용에 대한 우려 수준을 1~10점 척도로 평가하세요.)
고객_이름: (고객의 이름)
직원_이름: (본문에서 처음 언급된 직원의 이름)
```

4. AWS Cloud9에서 미리보기 탭을 닫습니다. 터미널로 돌아가서 Control-C를 눌러 애플리케이션을 종료합니다.
