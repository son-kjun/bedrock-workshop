# 실습 1. 이미지 생성 [![Next](images/next.png)](02_Image_Pattern.md)
## 실습 소개
**최종 결과물:**
![app-in-use-ko.png](images/app-in-use-ko.png)

Stable Diffusion은 텍스트 프롬프트에서 이미지를 생성합니다. 무작위 노이즈로 시작하여 일련의 단계에 걸쳐 점차적으로 이미지를 형성합니다. 또한 프롬프트를 기반으로 기존 이미지를 변환하는 데에도 사용할 수 있으며, 이는 이후 실습에서 다루겠습니다.

**이 실습을 실행하려면 aws account가 Stable Diffusionr과 Titan Image Generator를 구독하고 있어야 합니다. Bedrock 콘솔을 통해 구독할 수 있습니다.**

## 사용 사례
- 이미지 생성 패턴은 다음과 같은 사용 사례에 적합합니다:
  - 웹사이트, 이메일 등을 위한 사용자 지정 이미지 생성.
  - 다양한 미디어 형식의 컨셉 아트 제작
<BR><BR>
<BR><BR>

## 프롬프트를 통한 이미지 생성 테스트
~~~
Bedrock Console의 Playground 혹은 Demo 앱을 기동해서 프롬프트를 확인해보세요.
Demo URL클릭시 Ctrl 키를 누르고 새탭이나 새창에서 띄워주세요
~~~~
## Bedrock Console Playground - Image Generation
~~~
AWS Console > Bedrock > Image 선택
~~~
<BR><BR>
## Demo > Lab1_Image_Generation
**http://myrpc09-lb-443169224.us-east-1.elb.amazonaws.com** 

![picasso.png](images/picasso.png)
<BR>
다음의 몇 가지 프롬프트를 베드락 콘솔에서 하나씩 사용해 보고 결과를 확인합니다.순차적으로 결과를 테스트 해보세요. (이미지 생성은 텍스트 생성보다 시간이 걸리므로 조금만 기다려 주셔요!!)
> A cat and a person, in the style of Picasso

> a beautiful mountain landscape

> A little (girl) with long blond hair, ((her dad)), and a little dog, the girl looks like (Emma Watson), and her dad looks like (Leonardo DiCaprio), like a (photograph), [[digital]]

[곤충에 포커스를 가진]
> photorealistic image taken with a Nikon D850, 105mm macro lens, a vibrant and intricate butterfly resting on a flower

[눈덮인 산 정상]
> photorealistic image taken with a Fujifilm GFX100, 24mm lens, a breathtaking panoramic view from the summit of a snow-covered mountain

[산호초와 바닷속]
> photorealistic image taken with a Fujifilm GFX 50S, 24mm lens, a vibrant coral reef teeming with marine life beneath the clear, turquoise waters

[산위의 호수]
> photorealistic image taken with a Canon 5D Mark III, 24mm lens, a serene mountain lake surrounded by rugged cliffs, reflecting the vivid colors of the surrounding wilderness

[마녀]
> a beautiful and powerful mysterious sorceress, smile, sitting on a rock, lightning magic, hat, detailed leather clothing with gemstones, dress, castle background

<BR><BR>
**아래의 프롬프트 엔지니어링 팁을 참조해서 창의적인 프롬프트를 만들어 보세요(영문만 가능합니다.)**
  ![prompt_tip.png](images/prompt_tip.png)





<!--
Demo Code는 Bedrock을 Python API방식으로 작성된 Client Code입니다.
Cloud9이나 EC2로 Bedrock API를 이용해서 데모와 같은 python client를 구성해보고 싶으신 경우 아래 내용을 참조하셔요

[1] [Amazon Bedrock구성](https://catalog.us-east-1.prod.workshops.aws/workshops/10435111-3e2e-48bb-acb4-0b5111d7638e/ko-KR/prerequisites/bedrock-setup)

[2] [AWS Cloud9구성](https://catalog.us-east-1.prod.workshops.aws/workshops/10435111-3e2e-48bb-acb4-0b5111d7638e/ko-KR/prerequisites/cloud9-setup)

[3] [실습환경설정(관련패키지 설치)](https://catalog.us-east-1.prod.workshops.aws/workshops/10435111-3e2e-48bb-acb4-0b5111d7638e/ko-KR/prerequisites/lab-setup)

[4] [데모코드](codes/Lab_1.Image_Generation.md)

[5] [workshop 전체 예제 코드 다운로드](https://ws-assets-prod-iad-r-icn-ced060f0d38bc0b0.s3.ap-northeast-2.amazonaws.com/10435111-3e2e-48bb-acb4-0b5111d7638e/workshop.zip)  
--> 
<BR><BR>
<!--데모에서 오류가 발생하시는 경우 (정상 호출되는 인스턴스 직접 호출) <BR>
http://54.205.45.29:8501 <BR>
http://54.205.45.29:18501 <BR><BR><BR> -->

[![Next](images/next.png)](02_Image_Pattern.md)
