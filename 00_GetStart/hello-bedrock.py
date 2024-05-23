#다음은 Python 언어를 이용해서 Llama 2 Chat 13B 모델을 호출하는 예를 보여줍니다. 

import boto3
import json
bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-west-2')

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
