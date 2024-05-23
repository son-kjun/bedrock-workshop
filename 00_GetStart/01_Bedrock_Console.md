# 실습 1: Bedrock Console 둘러보기
## 실습 소개
이 실습에서는 Amazon Bedrock 콘솔의 몇 가지 주요 기능에 대해 살펴보겠습니다.
 

1. Amazon Bedrock에 액세스할 수 있는 계정에 로그인하고 US West (Oregon) 리전을 선택합니다.
<img src="images/select-region.png" width="500">
  
2. 다음 Amazon Bedrock 콘솔로 이동해서 **Get Started**를 선택합니다.
<img src="images/bedrock-welcome.png" width="700">

Amazon Bedrock Console은 다양한 모델, 프롬프트 및 추론 매개변수를 실험해 볼 수 있는 좋은 방법 중 하나입니다. 몇 분만 시간을 내어 콘솔의 다른 기능을 살펴보세요.


With Amazon Bedrock, you can explore the following capabilities:

* Text playground – A hands-on text generation application in the AWS Management Console.
* Image playground – A hands-on image generation application in the console.
* Chat playground – A hands-on conversation generation application in the console.
* Examples library – Example use cases to load.
* Amazon Bedrock API – Explore with the AWS CLI, or use the API to access the base models.
* Embeddings – Use the API to generate embeddings from the Titan text and image models.
* Agents for Amazon Bedrock – Build agents to perform orchestration and carry out tasks for your customers.
* Knowledge base for Amazon Bedrock – Draw from data sources to help your agent find information for your customers.
* Provisioned Throughput – Purchase throughput to run inference on models at discounted rates.
* Fine-tuning and Continued Pre-training – Customize an Amazon Bedrock base model to improve its performance and create a better customer experience.
* Model invocation logging – Collect invocation logs, model input data, and model output data for all invocations in your AWS account used in Amazon Bedrock.
* Model versioning – Benefit from continuous updates and improvements in foundation models to enhance your applications' capabilities, accuracy, and safety.


The following capabilities are in public preview release. These features are subject to change.

* Batch inference – Run model inference on a large dataset of prompts. Currently available only through the API.
* Model evaluation – Create model evaluation jobs to evaluate the responses of 1 or models to either built-in or custom prompt datasets. To evaluate a model's response you can use either human workers or automatic metrics.

The following capabilities are in limited preview release. To request access, contact your AWS account manager.

* Guardrails – Implement safeguards for your generative AI applications.



1. 왼쪽 메뉴에서 Foundation models > Base models 를 클릭하여 Bedrock에서 어떠한 모델들이 제공되는지 확인합니다. 


Amazon Bedrock에서 지원하는 모델들

* AI21 Labs - Jurassic-2 Ultra v1, Jurassic-2 Mid v1
* Amazon - Titan Text Express, Lite, Embeddings, Multimodal Embeddings, Image Generator(preview)
* Anthopic - Claude v1.x, v2.x, Instance v1.x
* Cohere - Command v14.x, Command Light v14.x, Embed English v3.x, Embed Multilingual v3.x
* Meta - Llama 2 Chat 13B v1, Llama 2 13B v1, Llama 2 70B v1
* Stability.ai - Stable Diffusion XL v0.8, v1.x


# 2. Model access 추가하기

기본적으로 User나 Roles는 Amazon Bedrock 리소스를 생성하거나 변경할 수 있는 권한을 가지고 있지 않습니다. AWS 콘솔이나 CLI, API 등을 수행할 수 없음을 의미합니다. 사용자에게 리소스에 접근 권한을 주려면 IAM 관리자가 IAM policies를 만들고 이를 역할을 추가함으로써, 사용자가 assume roles을 할 수 있게 해야 합니다. 

TODO: 모델 액세스 추가하는 과정 설명 및 이미지 추가

이에 대해 더 자세히 알고 싶으면 아래 문서 내용을 참고하시기 바랍니다. 

Identity-based policy examples for Amazon Bedrock<br>
https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html


# 3. 예제 실행해보기

1. **Amazon Bedrock** 사이드 메뉴를 열고 Examples를 선택합니다.

각 예제에서 프롬프트, 추론 구성, 샘플 응답 및 API 요청 세부 정보를 확인할 수 있습니다.
![bedrock-examples](images/bedrock-examples.png)


2. 예제를 선택한 다음 Open in Playground 를 선택하면 예제가 실제로 작동하는 모습을 볼 수 있습니다.
![bedrock-playground](images/bedrock-playground.png)

 
3. **Run** 을 선택하고 응답을 검토합니다.

**Temperature** 매개변수를 사용하면 응답을 구성할 때 모델이 보다 "창의적"으로 응답할 수 있습니다. 온도가 0이면 무작위성이 없으며 매번 가장 가능성이 높은 단어가 선택됩니다. 응답의 다양성을 높이려면 Temperature 값을 더 높게 설정하고 동일한 요청을 여러 번 실행할 수 있습니다.
**Response length** 매개변수는 응답에 반환할 토큰의 수를 결정합니다. 이를 사용하여 모델에서 반환되는 콘텐츠의 양을 줄이거나 늘릴 수 있습니다. 길이를 너무 낮게 설정하면 응답이 완료되기 전에 끊어질 수 있습니다.
**Info** 링크를 통해 각 파라미터에 대한 설명을 확인할 수 있습니다.

 
4. **View API request** 를 선택하면 지정된 프롬프트 및 구성에 대한 JSON 페이로드를 확인할 수 있습니다.
![bedrock-api](images/bedrock-api.png) 

