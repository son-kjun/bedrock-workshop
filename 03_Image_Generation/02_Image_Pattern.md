# 실습 2. 이미지 패턴 실습 [![Next](images/next.png)](03_Advanced_Pattern.md)
## 1. 이미지 프롬프팅
**실습소개**
![app-in-use.png](images/app-in-use.png)

[1] [Cloud9 바로가기 ](https://us-west-2.console.aws.amazon.com/cloud9control/home?region=us-west-2#/)

[2] [Cloud9 셋팅하기](https://catalog.us-east-1.prod.workshops.aws/workshops/10435111-3e2e-48bb-acb4-0b5111d7638e/ko-KR/prerequisites/cloud9-setup)

[3] [실습 관련패키지 설치](https://github.com/son-kjun/bedrock-workshop/blob/main/03_Image_Generation/cloud9settings.md)


[4] [데모코드](codes/Lab_1.Image_Generation.md)





Titan Image Generator는 텍스트 프롬프트에서 이미지를 생성합니다. 무작위 노이즈로 시작하여 일련의 단계에 걸쳐 점차적으로 이미지를 형성합니다. 또한 프롬프트를 기반으로 기존 이미지를 변형하는 데에도 사용할 수 있으며, 이는 나중에 실습에서 시도해 보겠습니다.

<BR><BR>
**사용 사례**

이미지 생성 패턴은 다음과 같은 사용 사례에 적합합니다:

    웹사이트, 이메일 등을 위한 맞춤형 이미지 제작
    다양한 미디어 형식의 컨셉 아트 제작

<BR><BR>
## Demo > Lab_2_Image_Pattern 선택
<!--<a href="[https://bit.ly/bedrock-image](https://bit.ly/bedrock-image)" target="_blank"> **https://bit.ly/bedrock-image** </a>-->
<BR><BR>
**몇 가지 프롬프트를 사용해 보고 결과를 확인합니다.**
**아래의 요소들을 응용하여 프롬프트를 입력해 보세요(영문만 가능합니다.)**

~~~python
daguerreotype of robot and cowboy standing side-by-side, directly facing the camera, steampunk, western town in the background, long shot, sepia tone
~~~
(한국어 번역: 카메라를 정면으로 바라보며 나란히 서 있는 로봇과 카우보이의 다게레오타입, 스팀펑크, 배경의 서부 마을, 긴 샷, 세피아 톤)

~~~python
photograph of a calico cat, cyberpunk, futuristic cityscape in the background, low angle, long shot, neon sign on building "CALICO CORP", Epic, photorealistic, 4K
~~~
(한국어 번역: 옥양목 고양이 사진, 사이버 펑크, 배경의 미래 도시 풍경, 낮은 각도, 긴 샷, "CALICO CORP" 건물의 네온 사인, Epic, 포토리얼리스틱, 4K)


<!-- 아래 프롬프트 중에는 오류가 발생하는 프롬프트가 있습니다. 오류가 발생하는 원인과 조치 방법을 생각해보세요--> 

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
|Text|Painting of a doctor, Impressionist style, low-angle shot, dim lighting, blue and purple color scheme, sign reading "The Doctor is in"|![text.png](images/text.png)|Titan Image Generator의 경우 텍스트는 큰따옴표로 묶어야 합니다. 생성된 이미지에 오타가 있을 수 있습니다.|

<BR><BR>
<!--## 코드예제 : [codes/Lab_2.Image_Pattern.md](codes/Lab_2.Image_Pattern.md)-->

<BR><BR>
## 도전과제 
![도전과제](https://simyung.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fbcfc9a33-741c-4cf8-88e2-7fc3d778fb45%2F96fec6d1-6b2f-491b-9a81-77f4212b0378%2FScreenshot_2024-05-21_at_7.32.06_PM.png?table=block&id=51d868fa-3d3e-4e85-9e5b-c60197e8bda4&spaceId=bcfc9a33-741c-4cf8-88e2-7fc3d778fb45&width=2000&userId=&cache=v2)

<!--데모에서 오류가 발생하시는 경우 (정상 호출되는 인스턴스 직접 호출) <BR>
http://54.205.45.29:8501 <BR>
http://54.205.45.29:18501 <BR><BR><BR>-->

[![Next](images/next.png)](03_Advanced_Pattern.md)
