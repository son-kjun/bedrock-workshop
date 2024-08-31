** 실습용 에셋 다운로드 및 구성 **
** AWS Cloud9 IDE에서 bash terminal을 선택합니다. **
![alt text](images/cloud9-terminal.png)
 

터미널에 다음을 붙여넣고 실행하여 코드를 다운로드하고 압축을 풉니다.
~~~python
cd ~/environment/
curl 'https://ws-assets-prod-iad-r-icn-ced060f0d38bc0b0.s3.ap-northeast-2.amazonaws.com/10435111-3e2e-48bb-acb4-0b5111d7638e/workshop.zip' --output workshop.zip
unzip workshop.zip
~~~
  
완료되면 터미널에 압축 해제 결과가 표시됩니다:
~~~python
Terminal results from zip download & unzip
~~~

![alt text](images/zip.png)
 

실습에 필요한 종속성을 설치합니다.
~~~python
pip3 install -r ~/environment/workshop/setup/requirements.txt -U
~~~
모든 것이 정상적으로 작동하면 성공 메시지가 표시됩니다(아래와 같은 경고는 무시해도 됩니다):


![alt text](images/reqs.png)

 

AWS Cloud9 터미널에 다음을 붙여넣고 실행하여 구성을 확인합니다:
~~~python
cd ~/environment/
python ~/environment/workshop/completed/api/bedrock_api.py
~~~
모든 것이 정상적으로 작동하면 뉴햄프셔주 맨체스터에 대한 응답이 표시됩니다:

![alt text](images/test.png)

 

축하합니다!
이제 실습을 시작할 수 있습니다.
실습을 완료하고 AWS Cloud9 사용을 마치면, 리소스 정리에 따라 AWS Cloud9 환경을 삭제할 수 있습니다.

Previous
Next
© 2008 - 2024, Amazon Web Services, Inc. or its affiliates. All rights reserved.
