# 실습 1. 텍스트 생성

Gen AI를 이용해서 여러가지 텍스트 컨텐츠를 손쉽게 만들어 낼 수 있습니다. 보고서를 작성하거나 프로젝트를 수행할 때 아이디어를 얻는 등 다양한 작업에 사용할 수 있습니다. 여러가지 활용 사례를 실습을 통해서 알아보도록 하겠습니다. 


## 5.1 블로그 글쓰기

1. Bedrock 콘솔 메뉴에서 **Playgrounds** → **Text** 를 선택합니다.
2. **Select model** 버튼을 클릭합니다.
3. Category: **Anthropic**, Model: **Claude 3 Sonnet**를 선택합니다.
4. **Apply** 버튼을 클릭합니다. 
5. 다음 내용을 입력하고 **Run** 버튼을 클릭해서 결과를 확인합니다. 

[프롬프트 내용]
~~~
너는 자동차에 대한 블로그 글을 쓰는 작가야. 전기자동차가 미래에 어떠한 영향을 미칠 지에 대한 글을 써줘
~~~

6. 기존 텍스트 내용을 지우고 다음과 같이 프롬프트를 변경합니다.
7. **Run** 버튼을 클릭해서 결과를 확인합니다. 

[프롬프트 내용]
~~~
선생님이 초등학생에게 설명해주는 듯한 형식으로 전기자동차가 미래에 어떠한 영향을 미칠 지에 대한 글을 써줘
~~~


## 도전과제

개인 블로그에 글을 올리려고 합니다. 본인만의 취미나 관심사에 대한 주제를 자유롭게 정하고 텍스트 생성 기능을 이용해서 블로그 내용을 생성합니다. 원하는 느낌이나 문체(tone and manner)에 맞게 다양한 방법으로 프롬프트를 실행해 보세요. 
<img src="images/text-challenge-1.png" width="500">


## 5.2 아이디어 도출

1. 위 실습과 같은 방법으로 다음과 같이 프롬프트를 실행해서 결과를 알아봅니다. 
2. Category: Meta, Model: Llama 2 Chat 13B v1


[프롬프트 내용]
~~~
IT 고객사를 대상으로 Gen AI에 대한 기술 세션을 2시간 정도 진행하려고 해. 어떠한 것을 준비해야 될지 알려줄래
~~~

1. 다음 프롬프트를 실행해 봅니다.

[프롬프트 내용]
~~~
회사내에 직원 분들이 쉬면서 책을 읽을 수 있는 북카페를 만들려고 하는데 어떤 것들을 준비해야 되는지 알려줘

1. 다른 Bedrock FM 모델로 변경해서 결과가 어떻게 다른지 알아봅니다. (한글인식 정도, 한글 텍스트 작성이 되는지 등..)
2. 자유주제로 아이디어 도출하는 예를 Bedrock을 이용해서 작성해 봅시다.
~~~


## 5.3 광고 카피 만들기

1. 위 실습과 같은 방법으로 다음과 같이 프롬프트를 실행해서 결과를 알아봅니다. 
2. Category: Amazon, Model: Titan Text G1 - Lite v1

[프롬프트 내용]
~~~
An AI/ML company has launched a new character recognition mobile application. Even young children can use it easily and it supports several languages. Please create a TV commercial to promote this application. A famous female idol singer will appear in the advertisement.
~~~

1. Model: Titan Text G1 - Express v1 으로 변경 후 다시 실행해 봅니다. 
2. 자유로운 주제로 광고 카피를 직접 만들어 봅시다.



이 외에도 Narrative writing, Q&A(chat), Role play 등 다양한 용도로 텍스트 생성을 위해 Gen AI를 사용할 수 있습니다.


# 6. Text Summarization

Gen AI를 이용하면 긴 컨텐츠 내용을 요약하는 것도 간단히 진행할 수 있습니다. 몇 가지 실습 사례를 통해 알아보도록 하겠습니다.


## 6.1 기술 블로그 내용 요약

1. Bedrock 콘솔 메뉴에서 Playgrounds → Text 를 선택합니다.
2. Select model 버튼을 클릭합니다.
3. Category: Cohere, Model: Command Lite v14.7 을 선택합니다.
4. Apply 버튼을 클릭합니다. 
5. 다음 내용을 입력하고 > Run 버튼을 클릭해서 결과를 확인합니다. 

[프롬프트 내용]
~~~
Could you please read the website content at the following URL and summarize it in 1000 words?

https://aws.amazon.com/ko/blogs/machine-learning/welcome-to-a-new-era-of-building-in-the-cloud-with-generative-ai-on-aws/
~~~

## 6.2 Earning call 요약

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
~~~
Read the document URL below, write a short and concise article about issue. It should include 5 sections:

1. Overview 2. Symptoms 3. Cause 4. Resolution 5. Resources

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstances.html
~~~

1. 원문 내용과 요약된 결과를 비교해 봅니다.
2. Configurations 의 여러 항목들을 변경해보고 결과를 확인해 봅니다.  



## 6.4 회의록 요약

1. Bedrock 콘솔 메뉴에서 Playgrounds → Text 를 선택합니다.
2. Select model 버튼을 클릭합니다.
3. Category: Anthropic, Model: Claude 2 v2 를 선택합니다.
4. Apply 버튼을 클릭합니다. 
5. 다음 내용을 입력하고 > Run 버튼을 클릭해서 결과를 확인합니다. 

[프롬프트 내용]
~~~
아래 회의록 내용을 읽고 내용을 요약해줘.
####
(11시 48분)
○의장 송미희 의사일정 제5항 「시흥시 전략산업 육성 및 지원에 관한 조례안」부터 의사일정 제11항 「2024년 정기분 공유재산관리계획안」까지 이상 7건의 안건을 일괄 상정합니다.
자치행정위원회 위원장이신 박춘호 의원님 나오셔서 자치행정위원회 소관 안건에 대한 심사 결과를 보고하여 주시기를 바랍니다.
○자치행정위원장 박춘호 자치행정위원회 위원장 박춘호입니다.
제312회 시흥시의회(제2차 정례회) 회기 중 자치행정위원회에서는 총 7건의 조례 및 기타 안건에 대해서 심사하였습니다.
먼저 「시흥시 전략산업 육성 및 지원에 관한 조례안」에 대한 심사 결과입니다.
본 안건은 미래 전략산업의 체계적인 육성과 지원을 위한 법적·제도적 기반을 마련하고자 하는 사안으로 중장기적 관점에서 시흥시 전략산업에 대한 연차별 계획과 예산을 수립해 주실 것과 관내 대학의 인프라를 기반으로 정보화 교육을 전략산업으로 육성하는 방향에 대해 적극적인 검토를 주문하며 원안대로 의결하였습니다.
본 안건은 행정안전부의 종합 지침에 따라 시흥화폐 가맹점 등록 기준 등 조례 내용을 정비하는 사안으로 거북섬 내 숙박 시설 등을 대상으로 시루 가맹점을 확장하는 데 적극적으로 노력해 주실 것과 지역화폐 발행과 잔고 활용에 있어 선진적 기술 도입을 주문합니다.
아울러 유효기간이 경과한 지역화폐로 인해 피해를 보는 시민이 생기지 않도록 유효 기간을 폐지하는 부분에 대해 적극적으로 검토해 주실 것을 주문하며 원안대로 의결하였습니다.
다음은 「시흥시 창업펀드 활성화에 관한 조례안」에 대한 심사 결과입니다.
본 안건은 시흥시 창업펀드 조성 및 운용으로 시흥시 창업 생태계 활성화에 이바지하고자 하는 사안으로 관내 창업 기업에 관련된 객관적 지표를 데이터베이스화 해 주실 것을 주문하며 원안대로 의결하였습니다.
다음은 「시흥시 지역특화 관광축제 지원에 관한 조례안」에 대한 심사 결과입니다.
본 안건은 시민 주도형 관광 축제를 지원하여 주민 화합과 시흥시 주요 관광 명소를 알리고 지역특화 관광축제 육성과 지역 경제 발전에 기여하고자 하는 사안으로 지역특화관광축제심의위원회가 객관적인 평가를 할 수 있도록 주문하며 원안대로 의결하였습니다.
다음은 「시흥시 야외운동기구 설치 및 관리 조례안」에 대한 심사 결과입니다.
본 안건은 야외운동기구의 설치와 유지 관리에 필요한 사항을 규정하는 사안으로 관리되지 못하고 방치된 야외운동기구에 대한 전수 조사를 주문하며 원안대로 의결하였습니다.

~~~
