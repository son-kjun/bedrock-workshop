# Lab 0 - Introduction to Bedrock

이 랩에서는 파이썬에서 아마존 베드락 서비스에 연결하는 기본 사항을 안내할 것입니다.
먼저 루트 README의 [시작하기] 섹션에서 설정을 완료했는지 확인합니다(.../README.md#Getting-started)
그런 다음 필요한 SDK 설치, Brock 연결 및 모델 호출 방법을 보여주는 노트북 [bedrock_boto3_setup.ipynb](bedrock_boto3_setup.ipynb)을 살펴볼 준비가 됩니다.

이번 실습은 Amazon Bedrock, LangChain 및 Streamlit에 대한 경험이 없다고 가정 합니다. 이번 실습에서 파운데이션 모델과 함께 작업하기 위한 핵심 패턴을 소개할 것 입니다. 워크샵의 모든 실습은 이러한 패턴을 기반으로 진행 됩니다.

이러한 패턴은 몇 가지 기본적인 실제 사용 사례를 해결하는데 사용될 수 있습니다. 이러한 실습은 Bedrock API call 이외에 추가 인프라나 통합과 같은 과정을 필요로 하지 않습니다.

![Stable Diffusion Architecture](./images/sd.png)
