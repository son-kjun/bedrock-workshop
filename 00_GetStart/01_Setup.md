# 실습 1: Bedrock Console
## 실습 소개
이 실습에서는 Amazon Bedrock 콘솔의 몇 가지 주요 기능에 대해 살펴보겠습니다.
![bedrock-welcome](images/bedrock-welcome.png)
 

Amazon Bedrock에 액세스할 수 있는 계정에 로그인하고 적절한 리전을 선택한 다음 Amazon Bedrock 콘솔로 이동합니다.
Screenshot of the welcome page in the Bedrock console

 

Amazon Bedrock 사이드 메뉴를 열고 Examples를 선택합니다.

각 예제에서 프롬프트, 추론 구성, 샘플 응답 및 API 요청 세부 정보를 확인할 수 있습니다.
Screenshot of examples page in the Bedrock console

 

예제를 선택한 다음 Open in Playground 를 선택하면 예제가 실제로 작동하는 모습을 볼 수 있습니다.
Screenshot of text playground in the Bedrock console

 

Run 을 선택하고 응답을 검토합니다.

Temperature 매개변수를 사용하면 응답을 구성할 때 모델이 보다 "창의적"으로 응답할 수 있습니다. 온도가 0이면 무작위성이 없으며 매번 가장 가능성이 높은 단어가 선택됩니다. 응답의 다양성을 높이려면 Temperature 값을 더 높게 설정하고 동일한 요청을 여러 번 실행할 수 있습니다.
Response length 매개변수는 응답에 반환할 토큰의 수를 결정합니다. 이를 사용하여 모델에서 반환되는 콘텐츠의 양을 줄이거나 늘릴 수 있습니다. 길이를 너무 낮게 설정하면 응답이 완료되기 전에 끊어질 수 있습니다.
Info 링크를 통해 각 파라미터에 대한 설명을 확인할 수 있습니다.
 

View API request 를 선택하면 지정된 프롬프트 및 구성에 대한 JSON 페이로드를 확인할 수 있습니다.
Screenshot of API request example dialog in the Bedrock console

 

Amazon Bedrock Console은 다양한 모델, 프롬프트 및 추론 매개변수를 실험해 볼 수 있는 좋은 방법 중 하나입니다. 몇 분만 시간을 내어 콘솔의 다른 기능을 살펴보세요.

