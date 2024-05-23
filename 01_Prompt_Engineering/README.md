# 1. Zero-shot 프롬프트 사용해보기

Amazon Bedrock에서는 AWS 콘솔을 이용해서 Bedrock FMs를 선택해서 직접 실행해보고 결과를 확인할 수 있도록 Playground를 제공합니다. 현재 3가지 종류(Text, Chat, Image)의 플레이그라운드가 제공됩니다.


1. Bedrock 콘솔 메뉴에서 Playgrounds → Text 를 선택합니다.
2. Select model 버튼을 클릭합니다.
3. Category: Anthropic, Model: Claude 2 v2를 선택합니다.
4. Apply 버튼을 클릭합니다. 
5. 다음 내용을 입력하고 > Run 버튼을 클릭해서 결과를 확인합니다. 

[프롬프트 내용]
~~~
이 문장들의 감정은 무엇입니까? 
1. 아 정말 넌 도대체 말이 안통하는구나. 
2. 밥 사줘서 고마워. 앞으로도 친하게 지내자 
3. 매일 밤새서 일하니 너무 신난다. 내일도 밤 새야지
~~~


1. Configurations의 값을 수정하고 Run 실행을 해봅니다. 어떻게 결과가 달라지는지 확인해 봅니다.

* Temperature - Tunes the degree of randomness in generation. Lower temperatures mean less random generations.
* Top P - If set to float less than 1, only the smallest set of most probable tokens with probabilities that add up to top_p or higher are kept for generation.
* Top K - Can be used to reduce repetitiveness of generated tokens. The higher the value, the stronger a penalty is applied to previously present tokens, proportional to how many times they have already appeared in the prompt or prior generation.



1. Playground 화면의 우측 확장(점 3개) 버튼 > View API request 메뉴를 클릭합니다.


1. Playground에서 실행한 내용을 CLI 명령으로 호출할 수 있는 명령줄을 확인할 수 있습니다. Bedrock 호출 시 어떠한 command와 argument를 전달하는지 확인해봅시다.


플레이그라운드에서 테스트 해 볼 수 있는 것과 AWS Bedrock CLI를 이용해서 모델을 호출할 수 있으며, 또한 같은 방법으로 Bedrock API를 이용해서 Gen AI 애플리케이션을 개발할 수도 있습니다. 

다음은 Python 언어를 이용해서 Llama 2 Chat 13B 모델을 호출하는 예를 보여줍니다. 

~~~python
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
~~~

# 2. Few-shot 프롬프트 사용해보기

Gen AI를 사용해서 원하는 결과를 얻기 위해서는 프롬프트를 어떻게 구성하는지가 중요합니다. 더 나은 결과를 위해 프롬프트 작성법을 연구하는 것을 Prompt Engineering 이라고 합니다. 

프롬프트에 제공하는 정보의 양과 질에 따라 Gen AI를 통해 얻게 되는 결과는 달라지게 되는데, 앞서 3번 예에서 사용한 프롬프트처럼 추가적인 학습없이 새로운 데이터를 예측할 수 있게 하는 기법을 Zero-shot prompting이라고 합니다. 반면, LLM에 따라 상당히 다른 결과를 얻게 되는 단점도 있습니다.

효과적인 결과를 얻기 위해 많이 사용되는 기법 중에 모범 예시를 제공해서 결과를 얻는 Few-shot prompting의 예를 알아보도록 하겠습니다. 


1. Bedrock 콘솔 메뉴에서 Playgrounds → Text 를 선택합니다.
2. Select model 버튼을 클릭합니다.
3. Category: Meta, Model: Llama 2 Chat 13B v1를 선택합니다.
4. Apply 버튼을 클릭합니다. 
5. 다음 내용을 입력하고 > Run 버튼을 클릭해서 결과를 확인합니다. 

[프롬프트 내용]
~~~
[INST]You are a very intelligent bot with exceptional language skills[/INST]
A "lemurwhat" is a small, furry animal native to Tanzania. An example of a sentence that uses
the word lemurwhat is:
We were traveling in Africa and we saw these very cute lemurwhats
To do a "cuteduddle" means to jump up and down really fast. An example of a sentence that uses 
the word cuteduddle is:
~~~


다음은 Few-shot 프롬프팅의 다른 예입니다.

~~~
멋지다! // 긍정
나빠! // 부정
그 영화는 굉장했어! // 긍정
이 얼마나 끔찍한 공연인가! //
~~~

# 3. 페르소나(Persona) 프롬프트 사용해보기


~~~
우리는 지금부터 롤플레이를 시작할거야. AI가 아니라 사람인 것처럼 자연스럽게 대답을 해줘. 대화의 시작부분에 누가 얘기하는지는 말하지 말아줘. 비지니스 미팅 대화를 연습하는 것을 가정하는거야. 나는 고급 수준의 영어 대화를 진행하고 싶어. 한 문장을 답하고 나의 응답을 기다려줘. 내가 응답하면 다음 대화를 진행해줘.
~~~

~~~
안녕하세요. 저는 무한상사의 유길동 부장이라고 합니다.
~~~

~~~
네 반갑습니다. 우리 무한상사에서는 일본과 중국으로 저희 제품을 수출하기 위한 업무를 함께 할 수 있는 파트너 회사를 찾는 중입니다. 귀사와 이 부분에 대한 얘기를 나누고 싶습니다.
~~~


이 외에도 Chain-of-Thought, Tree of Thoughts, RAG(Retrieval Augemented Generation, Self-Consistency, Directional Stimulus 등) 다양한 프롬프트 기법이 있는데, 이에 대한 상세한 내용은 아래 사이트를 참고하시기 바랍니다.

Prompt Engineering Guide
https://www.promptingguide.ai/
