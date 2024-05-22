# Lab 2. 이미지 패턴 실습
## 1. 이미지 프롬프팅
**실습소개**
![app-in-use.png](images/app-in-use.png)
이 실습에서는 Amazon Titan Image Generator, Amazon Bedrock, Streamlit을 사용하여 기본 이미지 생성기를 구축하겠습니다. LangChain은 주로 텍스트 생성 모델을 지원하므로, Titan Image Generator와 상호 작용하기 위해 Boto3 라이브러리를 사용할 것입니다.

Titan Image Generator는 텍스트 프롬프트에서 이미지를 생성합니다. 무작위 노이즈로 시작하여 일련의 단계에 걸쳐 점차적으로 이미지를 형성합니다. 또한 프롬프트를 기반으로 기존 이미지를 변형하는 데에도 사용할 수 있으며, 이는 나중에 실습에서 시도해 보겠습니다.

아래 코드 스니펫을 복사하여 지정된 Python 파일에 붙여넣으면 애플리케이션 코드를 작성할 수 있습니다.

<BR><BR><BR><BR>
**사용 사례**

이미지 생성 패턴은 다음과 같은 사용 사례에 적합합니다:

    웹사이트, 이메일 등을 위한 맞춤형 이미지 제작
    다양한 미디어 형식의 컨셉 아트 제작

이 애플리케이션은 두 개의 파일로 구성됩니다: 하나는 Streamlit 프런트엔드용이고 다른 하나는 Bedrock을 호출하기 위한 지원 라이브러리용입니다.

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
![app.png](images/app.png)

<BR><BR><BR><BR>
## 코드 없이 직접 테스트 할수 있게 demo를 미리 준비하였습니다 (아래 데모를 클릭하세요)
<a href="https://bit.ly/my-bedrock" target="_blank"> **https://bit.ly/my-bedrock** </a>

<BR><BR><BR><BR> 
**4. 몇 가지 프롬프트를 사용해 보고 결과를 확인합니다.**
- daguerreotype of robot and cowboy standing side-by-side, directly facing the camera, steampunk, western town in the background, long shot, sepia tone
- photograph of a calico cat, cyberpunk, futuristic cityscape in the background, low angle, long shot, neon sign on building "CALICO CORP", Epic, photorealistic, 4K

<BR><BR><BR><BR>
**5. 다양한 요소를 사용하여 작성된 몇 가지 예시 프롬프트는 아래 표를 참조하세요.**

|Element added|Prompt|Image|Note|
|------|---|---|---|
|Subject|Doctor|![subject.png](images/subject.png)|일반적으로 사진과 같은 이미지로 기본 설정됩니다.|
|Medium|Painting of a doctor|![medium.png](images/medium.png)|생성할 아트 유형 (기타 예: 다게레오타입, 연필 스케치, 수채화, 3D 만화 등)|
|Style|Painting of a doctor, Impressionist style|![style.png](images/style.png)|생성할 예술의 스타일 또는 테마(기타 예: 다다이스트 스타일, 르네상스 스타일 등)|
|Shot type/angle|Painting of a doctor, Impressionist style, low-angle shot|![angle.png](images/angle.png)|이미지의 각도 또는 거리(기타 예: 와이드 샷, 클로즈업 등)|
|Light|Painting of a doctor, Impressionist style, low-angle shot, dim lighting|![lighting.png](images/lighting.png)|이미지의 조명 구성표(기타 예: 골든 아워, 스튜디오 조명 등)|
|Color scheme|Painting of a doctor, Impressionist style, low-angle shot, dim lighting, blue and purple color scheme|![color.png](images/color.png)|이미지의 색 구성표(기타 예: 파스텔 색상, 네온 색상, 그레이 스케일 등)|
|Negative prompt|(Use the What shoud not be in the image field) Stethoscope|![negative.png](images/negative.png)|이미지에 포함하지 말아야 할 항목|
|Text|Painting of a doctor, Impressionist style, low-angle shot, dim lighting, blue and purple color scheme, sign reading "The Doctor is in"|![text.png](images/text.png)|Titan Image Generator의 경우 텍스트는 큰따옴표로 묶어야 합니다. 생성된 이미지에 오타가 있을 수 있습니다.|

**6. AWS Cloud9에서 미리보기 탭을 닫습니다.**

**7. 터미널로 돌아가 Control-C 를 눌러 애플리케이션을 종료합니다.**


## 도전과제 
![challenge02](images/challenge02.png)

[![Next](images/next.png)](02_Image_Pattern.md)
