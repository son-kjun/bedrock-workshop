# 실습 1. 프롬프트 엔지니어링

## 1. Zero-shot 프롬프트 사용해보기

Amazon Bedrock에서는 AWS 콘솔을 이용해서 Bedrock FMs를 선택해서 직접 실행해보고 결과를 확인할 수 있도록 Playground를 제공합니다. 현재 3가지 종류(Text, Chat, Image)의 플레이그라운드가 제공됩니다.


1. Bedrock 콘솔 메뉴에서 **Playgrounds** → **Text** 를 선택합니다.
2. **Select model** 버튼을 클릭합니다.
3. Category: **Anthropic**, Model: **Claude 3 Sonnet**를 선택합니다.
4. **Apply** 버튼을 클릭합니다. 
5. 다음 내용을 입력하고 **Run** 버튼을 클릭해서 결과를 확인합니다. 

~~~
이 문장들의 감정은 무엇입니까? 
1. 아 정말 넌 도대체 말이 안통하는구나. 
2. 밥 사줘서 고마워. 앞으로도 친하게 지내자 
3. 매일 밤새서 일하니 너무 신난다. 내일도 밤 새야지
~~~


6. Configurations의 값을 수정하고 Run 실행을 해봅니다. 어떻게 결과가 달라지는지 확인해 봅니다.

Temperature, Top P, Top K는 생성형 AI 모델에서 출력 텍스트의 다양성과 유창성을 제어하기 위해 사용되는 기법입니다.

* **Temperature (온도)** : Temperature는 출력 분포의 엔트로피를 조절하여 출력 텍스트의 창의성과 다양성을 제어합니다. Temperature 값이 높으면 모델은 더 다양하고 예측 불가능한 출력을 생성하지만, 그만큼 유창성이 떨어질 수 있습니다. 반대로 Temperature 값이 낮으면 모델은 더 보수적이고 안정적인 출력을 생성하지만, 창의성이 제한됩니다.

* **Top P (Nucleus Sampling)** : Top P는 확률 분포에서 누적 확률이 특정 임계값(Top P 값)을 넘는 상위 토큰들만 고려하는 기법입니다. 이를 통해 모델이 너무 낮은 확률의 토큰을 선택하는 것을 방지하고, 유창성을 유지하면서도 다양성을 확보할 수 있습니다.

* **Top K (Top-k Sampling)** : Top K는 확률 분포에서 상위 K개의 높은 확률 토큰만을 고려하는 기법입니다. 이 방식은 Top P와 비슷하지만, 누적 확률이 아닌 단순 상위 K개의 토큰만을 선택합니다. Top K 값이 작으면 다양성이 제한되지만, 높은 유창성을 기대할 수 있습니다.

이러한 기법들은 상황과 목적에 따라 적절히 조합되어 사용됩니다. 높은 Temperature와 낮은 Top P/K 값은 더 창의적이고 다양한 출력을 생성하며, 낮은 Temperature와 높은 Top P/K 값은 더 안정적이고 유창한 출력을 생성합니다. 이를 잘 조절하여 원하는 수준의 다양성과 유창성을 확보할 수 있습니다.


7. Playground 화면의 우측 확장(점 3개) 버튼 > View API request 메뉴를 클릭합니다.


8. Playground에서 실행한 내용을 CLI 명령으로 호출할 수 있는 명령줄을 확인할 수 있습니다. Bedrock 호출 시 어떠한 command와 argument를 전달하는지 확인해봅시다.


플레이그라운드에서 테스트 해 볼 수 있는 것과 AWS Bedrock CLI를 이용해서 모델을 호출할 수 있으며, 또한 같은 방법으로 Bedrock API를 이용해서 Gen AI 애플리케이션을 개발할 수도 있습니다. 


# 2. Few-shot 프롬프트 사용해보기

Gen AI를 사용해서 원하는 결과를 얻기 위해서는 프롬프트를 어떻게 구성하는지가 중요합니다. 더 나은 결과를 위해 프롬프트 작성법을 연구하는 것을 Prompt Engineering 이라고 합니다. 

프롬프트에 제공하는 정보의 양과 질에 따라 Gen AI를 통해 얻게 되는 결과는 달라지게 되는데, 앞서 3번 예에서 사용한 프롬프트처럼 추가적인 학습없이 새로운 데이터를 예측할 수 있게 하는 기법을 Zero-shot prompting이라고 합니다. 반면, LLM에 따라 상당히 다른 결과를 얻게 되는 단점도 있습니다.

효과적인 결과를 얻기 위해 많이 사용되는 기법 중에 모범 예시를 제공해서 결과를 얻는 Few-shot prompting의 예를 알아보도록 하겠습니다. 


1. Bedrock 콘솔 메뉴에서 Playgrounds → Text 를 선택합니다.
2. Select model 버튼을 클릭합니다.
3. Category: Meta, Model: Llama 2 Chat 13B v1를 선택합니다.
4. Apply 버튼을 클릭합니다. 
5. 다음 내용을 입력하고 > Run 버튼을 클릭해서 결과를 확인합니다. 

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

<br>

## 도전과제

Few-shot 프롬프팅을 이용해서 원하는 형태의 결과를 얻는 예를 만들어 보세요. 모범 예시를 제공하고 이에 기반한 응답이 생성되는지 확인합니다. 업무에 활용할 수 있다면 반복되는 작업을 빠르게 마무리 할 수 있지 않을까요?
<img src="images/prompt-challenge-1.png">

<br>
<br>


이 외에도 Chain-of-Thought, Tree of Thoughts, RAG(Retrieval Augemented Generation, Self-Consistency, Directional Stimulus 등) 다양한 프롬프트 기법이 있는데, 이에 대한 상세한 내용은 아래 사이트를 참고하시기 바랍니다.

Prompt Engineering Guide
https://www.promptingguide.ai/
