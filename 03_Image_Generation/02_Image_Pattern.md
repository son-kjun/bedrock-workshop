# 실습 2. 이미지 패턴 실습
## 1. 이미지 프롬프팅
**실습소개**
![app-in-use.png](images/app-in-use.png)
이 실습에서는 Amazon Titan Image Generator, Amazon Bedrock, Streamlit을 사용하여 기본 이미지 생성기를 구축하겠습니다. LangChain은 주로 텍스트 생성 모델을 지원하므로, Titan Image Generator와 상호 작용하기 위해 Boto3 라이브러리를 사용할 것입니다.

Titan Image Generator는 텍스트 프롬프트에서 이미지를 생성합니다. 무작위 노이즈로 시작하여 일련의 단계에 걸쳐 점차적으로 이미지를 형성합니다. 또한 프롬프트를 기반으로 기존 이미지를 변형하는 데에도 사용할 수 있으며, 이는 나중에 실습에서 시도해 보겠습니다.

아래 코드 스니펫을 복사하여 지정된 Python 파일에 붙여넣으면 애플리케이션 코드를 작성할 수 있습니다.

<BR><BR>
**사용 사례**

이미지 생성 패턴은 다음과 같은 사용 사례에 적합합니다:

    웹사이트, 이메일 등을 위한 맞춤형 이미지 제작
    다양한 미디어 형식의 컨셉 아트 제작

이 애플리케이션은 두 개의 파일로 구성됩니다: 하나는 Streamlit 프런트엔드용이고 다른 하나는 Bedrock을 호출하기 위한 지원 라이브러리용입니다.

<BR><BR>
## Demo > Lab_2_Image_Pattern 선택
<a href="https://bit.ly/my-bedrock" target="_blank"> **https://bit.ly/my-bedrock** </a>
<BR><BR>
**몇 가지 프롬프트를 사용해 보고 결과를 확인합니다.**
> daguerreotype of robot and cowboy standing side-by-side, directly facing the camera, steampunk, western town in the background, long shot, sepia tone

> photograph of a calico cat, cyberpunk, futuristic cityscape in the background, low angle, long shot, neon sign on building "CALICO CORP", Epic, photorealistic, 4K

> 추가적인 프롬프트를 창의적으로 만들어 보세요(영문만 가능합니다.)

<BR><BR>
**다양한 요소를 사용하여 작성된 몇 가지 예시 프롬프트는 아래 표를 참조하세요.**
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

<BR><BR>
## 코드예제 : [codes/Lab_2.Image_Pattern.md](codes/Lab_2.Image_Pattern.md)

[![Next](images/next.png)](03_Advanced_Pattern.md)
