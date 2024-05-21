1. Amazon Bedrock 기능 둘러보기

1. AWS Bedrock 콘솔에 접근합니다.

https://us-east-1.console.aws.amazon.com/bedrock

1. 로그인이 되어 있지 않은 경우 AWS 계정으로 로그인하세요.
2. Amazon Bedrock 콘솔 화면을 둘러 봅니다. 



1. 왼쪽 메뉴에서 여러 항목들을 눌러보고 어떠한 기능들이 제공되는지 둘러 봅니다 .


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



2. Model access 추가하기

기본적으로 User나 Roles는 Amazon Bedrock 리소스를 생성하거나 변경할 수 있는 권한을 가지고 있지 않습니다. AWS 콘솔이나 CLI, API 등을 수행할 수 없음을 의미합니다. 사용자에게 리소스에 접근 권한을 주려면 IAM 관리자가 IAM policies를 만들고 이를 역할을 추가함으로써, 사용자가 assume roles을 할 수 있게 해야 합니다. 

이에 대해 더 자세히 알고 싶으면 아래 문서 내용을 참고하시기 바랍니다. 

Identity-based policy examples for Amazon Bedrock
https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html

본 실습에서 필요한 Bedrock 모델을 사용하려면 먼저 제공되는 파운데이션 모델(FMs)에 접근할 수 있도록 요청해야 합니다. 

1. Bedrock 콘솔의 좌측 메뉴에서 Model access 항목을 선택합니다. 
2. 화면에서 Manage model access 버튼을 클릭합니다.
3. 모든 모델을 선택한 후 Save changes 버튼을 클릭합니다. 
    (이로써 사용하려는 모델에 대한 EULA에 동의한 것으로 간주합니다.)
4. 아래 그림처럼 모델에 대한 Access status 값이 Access granted로 변경되었는지 확인합니다.



이는 IAM 권한
Amazon Bedrock은 새로운 모델들을 추가하고 또한 기존 모델의 새로운 버전을 계속해서 제공합니다. 각 파운데이션 모델들은 Active, Legacy, EOL 등 라이프사이클로 관리됩니다.


3. Text Playground 사용해보기 : Zero-shot 프롬프트

Amazon Bedrock에서는 AWS 콘솔을 이용해서 Bedrock FMs를 선택해서 직접 실행해보고 결과를 확인할 수 있도록 Playground를 제공합니다. 현재 3가지 종류(Text, Chat, Image)의 플레이그라운드가 제공됩니다.


1. Bedrock 콘솔 메뉴에서 Playgrounds → Text 를 선택합니다.
2. Select model 버튼을 클릭합니다.
3. Category: Anthropic, Model: Claude 2 v2를 선택합니다.
4. Apply 버튼을 클릭합니다. 
5. 다음 내용을 입력하고 > Run 버튼을 클릭해서 결과를 확인합니다. 


[프롬프트 내용]
이 문장들의 감정은 무엇입니까? 
1. 아 정말 넌 도대체 말이 안통하는구나. 
2. 밥 사줘서 고마워. 앞으로도 친하게 지내자 
3. 매일 밤새서 일하니 너무 신난다. 내일도 밤 새야지



1. Configurations의 값을 수정하고 Run 실행을 해봅니다. 어떻게 결과가 달라지는지 확인해 봅니다.

* Temperature - Tunes the degree of randomness in generation. Lower temperatures mean less random generations.
* Top P - If set to float less than 1, only the smallest set of most probable tokens with probabilities that add up to top_p or higher are kept for generation.
* Top K - Can be used to reduce repetitiveness of generated tokens. The higher the value, the stronger a penalty is applied to previously present tokens, proportional to how many times they have already appeared in the prompt or prior generation.



1. Playground 화면의 우측 확장(점 3개) 버튼 > View API request 메뉴를 클릭합니다.


1. Playground에서 실행한 내용을 CLI 명령으로 호출할 수 있는 명령줄을 확인할 수 있습니다. Bedrock 호출 시 어떠한 command와 argument를 전달하는지 확인해봅시다.


플레이그라운드에서 테스트 해 볼 수 있는 것과 AWS Bedrock CLI를 이용해서 모델을 호출할 수 있으며, 또한 같은 방법으로 Bedrock API를 이용해서 Gen AI 애플리케이션을 개발할 수도 있습니다. 

다음은 Python 언어를 이용해서 Llama 2 Chat 13B 모델을 호출하는 예를 보여줍니다. 

import boto3
import json
bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

body = json.dumps({
"prompt": "What is the average lifespan of a Llama?",
"max_gen_len": 128,
"temperature": 0.1,
"top_p": 0.9,
})

modelId = 'meta.llama2-13b-chat-v1'
accept = 'application/json'
contentType = 'application/json'

response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

response_body = json.loads(response.get('body').read())
print(response_body)


4. Text Playground 사용해보기 : Few-shot 프롬프트

Gen AI를 사용해서 원하는 결과를 얻기 위해서는 프롬프트를 어떻게 구성하는지가 중요합니다. 더 나은 결과를 위해 프롬프트 작성법을 연구하는 것을 Prompt Engineering 이라고 합니다. 

프롬프트에 제공하는 정보의 양과 질에 따라 Gen AI를 통해 얻게 되는 결과는 달라지게 되는데, 앞서 3번 예에서 사용한 프롬프트처럼 추가적인 학습없이 새로운 데이터를 예측할 수 있게 하는 기법을 Zero-shot prompting이라고 합니다. 반면, LLM에 따라 상당히 다른 결과를 얻게 되는 단점도 있습니다.

효과적인 결과를 얻기 위해 많이 사용되는 기법 중에 모범 예시를 제공해서 결과를 얻는 Few-shot prompting의 예를 알아보도록 하겠습니다. 


1. Bedrock 콘솔 메뉴에서 Playgrounds → Text 를 선택합니다.
2. Select model 버튼을 클릭합니다.
3. Category: Meta, Model: Llama 2 Chat 13B v1를 선택합니다.
4. Apply 버튼을 클릭합니다. 
5. 다음 내용을 입력하고 > Run 버튼을 클릭해서 결과를 확인합니다. 


[프롬프트 내용]
[INST]You are a very intelligent bot with exceptional language skills[/INST]
A "lemurwhat" is a small, furry animal native to Tanzania. An example of a sentence that uses
the word lemurwhat is:
We were traveling in Africa and we saw these very cute lemurwhats
To do a "cuteduddle" means to jump up and down really fast. An example of a sentence that uses 
the word cuteduddle is:



다음은 Few-shot 프롬프팅의 다른 예입니다.

멋지다! // 긍정
나빠! // 부정
그 영화는 굉장했어! // 긍정
이 얼마나 끔찍한 공연인가! //


이 외에도 Chain-of-Thought, Tree of Thoughts, RAG(Retrieval Augemented Generation, Self-Consistency, Directional Stimulus 등) 다양한 프롬프트 기법이 있는데, 이에 대한 상세한 내용은 아래 사이트를 참고하시기 바랍니다.

Prompt Engineering Guide
https://www.promptingguide.ai/


5. Text Generation

Gen AI를 이용해서 여러가지 컨텐츠를 손쉽게 만들어 낼 수 있습니다. 여러가지 활용 사례를 실습을 통해서 알아보도록 하겠습니다. 


5.1 블로그 글쓰기

1. Bedrock 콘솔 메뉴에서 Playgrounds → Text 를 선택합니다.
2. Select model 버튼을 클릭합니다.
3. Category: Anthropic, Model: Claude v2를 선택합니다.
4. Apply 버튼을 클릭합니다. 
5. 다음 내용을 입력하고 > Run 버튼을 클릭해서 결과를 확인합니다. 

[프롬프트 내용]
너는 자동차에 대한 블로그 글을 쓰는 작가야. 전기자동차가 미래에 어떠한 영향을 미칠 지에 대한 글을 써줘


1. 다음과 같이 내용을 변경해서 실행 결과를 확인합니다.

[프롬프트 내용]
선생님이 초등학생에게 설명해주는 듯한 형식으로 전기자동차가 미래에 어떠한 영향을 미칠 지에 대한 글을 써줘

1. 자유주제로 글쓰기 초안을 Bedrock을 이용해서 작성해 봅시다.

5.2 아이디어 도출

1. 위 실습과 같은 방법으로 다음과 같이 프롬프트를 실행해서 결과를 알아봅니다. 
2. Category: Meta, Model: Llama 2 Chat 13B v1


[프롬프트 내용]
IT 고객사를 대상으로 Gen AI에 대한 기술 세션을 2시간 정도 진행하려고 해. 어떠한 것을 준비해야 될지 알려줄래


1. 다음 프롬프트를 실행해 봅니다.

[프롬프트 내용]
회사내에 직원 분들이 쉬면서 책을 읽을 수 있는 북카페를 만들려고 하는데 어떤 것들을 준비해야 되는지 알려줘

1. 다른 Bedrock FM 모델로 변경해서 결과가 어떻게 다른지 알아봅니다. (한글인식 정도, 한글 텍스트 작성이 되는지 등..)
2. 자유주제로 아이디어 도출하는 예를 Bedrock을 이용해서 작성해 봅시다.



5.3 광고 카피 만들기

1. 위 실습과 같은 방법으로 다음과 같이 프롬프트를 실행해서 결과를 알아봅니다. 
2. Category: Amazon, Model: Titan Text G1 - Lite v1

[프롬프트 내용]
An AI/ML company has launched a new character recognition mobile application. Even young children can use it easily and it supports several languages. Please create a TV commercial to promote this application. A famous female idol singer will appear in the advertisement.


1. Model: Titan Text G1 - Express v1 으로 변경 후 다시 실행해 봅니다. 
2. 자유로운 주제로 광고 카피를 직접 만들어 봅시다.



이 외에도 Narrative writing, Q&A(chat), Role play 등 다양한 용도로 텍스트 생성을 위해 Gen AI를 사용할 수 있습니다.


6. Text Summarization

Gen AI를 이용하면 긴 컨텐츠 내용을 요약하는 것도 간단히 진행할 수 있습니다. 몇 가지 실습 사례를 통해 알아보도록 하겠습니다.


6.1 기술 블로그 내용 요약

1. Bedrock 콘솔 메뉴에서 Playgrounds → Text 를 선택합니다.
2. Select model 버튼을 클릭합니다.
3. Category: Cohere, Model: Command Lite v14.7 을 선택합니다.
4. Apply 버튼을 클릭합니다. 
5. 다음 내용을 입력하고 > Run 버튼을 클릭해서 결과를 확인합니다. 

[프롬프트 내용]
Could you please read the website content at the following URL and summarize it in 1000 words?

https://aws.amazon.com/ko/blogs/machine-learning/welcome-to-a-new-era-of-building-in-the-cloud-with-generative-ai-on-aws/


6.2 Earning call 요약

1. Bedrock 콘솔 메뉴에서 Getting Started → Examples 를 선택합니다.
2. Search in examples 항목에 “summarization”을 입력해서 검색합니다. 
3. 검색 결과에서 “Earning call summarization” 을 선택하고 Open in Playground 버튼을 클릭합니다. 
4. > Run 버튼을 클릭해서 실행된 결과를 확인합니다. 



1. 우측 Configurations 에서 Length 값을 1500으로 변경하고 다시 > Run 버튼을 클릭해서 결과를 비교해봅시다. 



6.3 Structured summarization

1. Bedrock 콘솔 메뉴에서 Playgrounds → Text 를 선택합니다.
2. Select model 버튼을 클릭합니다.
3. Category: AI21 Labs, Model: Jurassic-2 Ultra 를 선택합니다.
4. Apply 버튼을 클릭합니다. 
5. 다음 내용을 입력하고 > Run 버튼을 클릭해서 결과를 확인합니다. 

[프롬프트 내용]
Read the document URL below, write a short and concise article about issue. It should include 5 sections:

1. Overview 2. Symptoms 3. Cause 4. Resolution 5. Resources

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstances.html


1. 원문 내용과 요약된 결과를 비교해 봅니다.
2. Configurations 의 여러 항목들을 변경해보고 결과를 확인해 봅니다.  



6.4 회의록 요약

1. Bedrock 콘솔 메뉴에서 Playgrounds → Text 를 선택합니다.
2. Select model 버튼을 클릭합니다.
3. Category: Anthropic, Model: Claude 2 v2 를 선택합니다.
4. Apply 버튼을 클릭합니다. 
5. 다음 내용을 입력하고 > Run 버튼을 클릭해서 결과를 확인합니다.

