<BR><BR><BR><BR>
## 라이브러리 스크립트 만들기

먼저 Streamlit 프론트엔드와 Bedrock 백엔드를 연결하기 위한 지원 라이브러리를 생성합니다.

**1. AWS Cloud9에서 workshop/labs/image_prompts 폴더로 이동하여 image_prompts_lib_kr.py 파일을 엽니다.**


**2.import 구문을 추가합니다.**
- 이 명령문을 통해 LangChain을 사용하여 FAISS 데이터베이스를 관리하고 Boto3를 사용하여 Bedrock을 호출 할 수 있습니다.
- 아래 상자의 복사 버튼을 사용하면 해당 코드를 자동으로 복사할 수 있습니다:
~~~python
import os
import boto3
import json
import base64
from io import BytesIO
from random import randint
~~~

**3. Request body 빌더 함수를 추가합니다.**
- 이 함수는 Bedrock에 제출할 요청 페이로드를 준비합니다:
~~~python
#InvokeModel API 호출에 대한 문자열화된 리퀘스트 바디를 가져옵니다.
def get_titan_image_generation_request_body(prompt, negative_prompt=None):
    
    body = { #InvokeModel API에 전달할 JSON 페이로드를 생성합니다.
        "taskType": "TEXT_IMAGE",
        "textToImageParams": {
            "text": prompt,
        },
        "imageGenerationConfig": {
            "numberOfImages": 1,  # 생성할 이미지 개수
            "quality": "premium",
            "height": 512,
            "width": 512,
            "cfgScale": 8.0,
            "seed": randint(0, 100000),  # 랜덤 시드 사용
        },
    }
    
    if negative_prompt:
        body['textToImageParams']['negativeText'] = negative_prompt
    
    return json.dumps(body)
~~~


**4. 이미지 변환 기능을 추가합니다.**
- 이 함수는 반환된 페이로드에서 이미지 데이터를 추출하여 Streamlit에서 사용할 수 있는 형식으로 변환합니다.
~~~python
#Titan Image Generator 응답에서 BytesIO 객체를 가져옵니다.
def get_titan_response_image(response):

    response = json.loads(response.get('body').read())
    
    images = response.get('images')
    
    image_data = base64.b64decode(images[0])

    return BytesIO(image_data)
~~~


**5. 이 함수를 추가하여 Bedrock을 호출합니다.**
- Streamlit 프론트엔드 애플리케이션에서 호출할 수 있는 함수를 만들고 있습니다. 이 함수는 입력 콘텐츠를 Bedrock에 전달하고 이미지를 반환합니다.
~~~python
#Amazon Titan Image Generator를 사용하여 이미지 생성
def get_image_from_model(prompt_content, negative_prompt=None):
    session = boto3.Session(
        profile_name=os.environ.get("BWB_PROFILE_NAME")
    ) #AWS 자격 증명에 사용할 프로필 이름 설정
    
    bedrock = session.client(
        service_name='bedrock-runtime', #Bedrock 클라이언트를 생성
        region_name=os.environ.get("BWB_REGION_NAME"),
        endpoint_url=os.environ.get("BWB_ENDPOINT_URL")
    ) 
    
    body = get_titan_image_generation_request_body(prompt_content, negative_prompt=negative_prompt)
    
    response = bedrock.invoke_model(body=body, modelId="amazon.titan-image-generator-v1", contentType="application/json", accept="application/json")
    
    output = get_titan_response_image(response)
    
    return output
~~~

**6.파일을 저장합니다.**
환상적입니다! 백킹 라이브러리가 완성되었습니다. 이제 프론트엔드 애플리케이션을 만들어 보겠습니다.


<BR><BR><BR><BR> 
## Streamlit 프론트엔드 앱 만들기
**1. lib 파일과 같은 폴더에서 image_prompts_app_kr.py 파일을 엽니다.**

**2. import 구문을 추가 합니다.**
이 구문을 사용하면 백킹 라이브러리 스크립트에서 Streamlit 요소를 사용하고 함수를 호출할 수 있습니다.
~~~python
import streamlit as st
import image_prompts_lib_kr as glib
~~~
 
**3. 페이지 제목, 구성 및 열 레이아웃을 추가합니다.**
여기서는 실제 페이지의 페이지 제목과 브라우저 탭에 표시되는 제목을 설정하고 있습니다. 왼쪽에 입력을 수집하고 오른쪽에 출력을 표시하기 위해 두 개의 열을 만들고 있습니다.

~~~python
st.set_page_config(layout="wide", page_title="Image Generation")

st.title("Image Generation")

col1, col2 = st.columns(2)
~~~
 

**4. 입력 요소를 추가합니다.**
첫 번째 열에는 사용자의 프롬프트를 가져와서 Bedrock으로 전송하는 멀티라인 텍스트 상자와 버튼을 만들고 있습니다.
~~~python
with col1:
    st.subheader("Image parameters")
    
    prompt_text = st.text_area("What you want to see in the image:", height=100, help="The prompt text")
    negative_prompt = st.text_input("What shoud not be in the image:", help="The negative prompt")

    generate_button = st.button("Generate", type="primary")
~~~
 
**5. 출력 요소를 추가합니다.**
두 번째 열에서는 if 블록을 사용하여 버튼 클릭을 처리합니다. 백킹 함수가 호출되는 동안 스피너를 표시한 다음 웹 페이지에 출력을 씁니다.
~~~python
with col2:
    st.subheader("Result")

    if generate_button:
        with st.spinner("Drawing..."):
            generated_image = glib.get_image_from_model(
                prompt_content=prompt_text, 
                negative_prompt=negative_prompt,
            )
        
        st.image(generated_image)
~~~
 
**6. 파일을 저장합니다.**
탁월합니다! 이제 애플리케이션을 실행할 준비가 되었습니다!

<BR><BR><BR><BR> 
## Streamlit 앱 실행
**1. AWS Cloud9 혹은 EC2에서 bash terminal을 선택하고 디렉토리를 변경합니다.**
~~~bash
cd ~/environment/workshop/labs/image_prompts
~~~
 
**2. 터미널에서 streamlit 명령을 실행합니다.**
~~~bash
streamlit run image_prompts_app_kr.py --server.port 8501
~~~
Streamlit 명령에 의해 표시되는 Network URL 및 External URL 링크를 무시합니다. 대신 AWS Cloud9의 프리뷰 기능을 사용하겠습니다.

**3. AWS Cloud9에서 Preview -> Preview Running Application을 선택합니다.**
![cloud9-preview.png](images/cloud9-preview.png)

아래와 같은 웹 페이지가 표시됩니다:
![app01.png](images/app01.png)
