import json
import boto3

session = boto3.Session()
bedrock = session.client(service_name='bedrock-runtime',region_name='us-east-1') #Bedrock client 생성

bedrock_model_id = "anthropic.claude-3-sonnet-20240229-v1:0" #파운데이션 모델 설정

prompt = "뉴햄프셔에서 가장 큰 도시가 어디인가요?" #모델에 보낼 프롬프트 설정

body = json.dumps({
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 1024,
    "temperature": 0,
    "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ],
}) #요청 payload 설정

response = bedrock.invoke_model(body=body, modelId=bedrock_model_id)


response_body = json.loads(response.get('body').read()) # response 읽기
results = response_body.get("content")[0].get("text")

print(results)
