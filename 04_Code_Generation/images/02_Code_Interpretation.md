## 실습 소개
이 실습에서는 그동안 배운 내용으로 코드 취약점을 분석해보겠습니다.
Amazon CodeGuru Reviewer를 사용해서 코드의 결점을 식별하여 이를 사용자에게 제공하는 서비스입니다. 내 회사의 보안팀은 Amazon CodeGuru Reviewer를 사용하여, 전사 시스템의 코드 취약점을 주기적으로 점검하고 담당자에게 전달하여, 이에 대한 조치일정 계획을 수립합니다. 우리가 기존 레거시 시스템의 운영자라고 가정해봅시다. 전임자가 작성한 코드를 이해가 안되지만, 코드취약점 대상 서비스에 나의 담당 시스템에서 아래 코드가 SQL Injection에 취약하다고 적발되어 당장 오늘까지 내가 수정을 해야합니다. 하지만 나는 비전공자에 코딩이 처음인 사람입니다. 오늘 수정하지 않으면 집에갈 수 없습니다.



![alt text](images/Screenshot-2023-10-05-at-2.20.12-PM.png)



```
Def execute_query_noncompliant(request):
    import sqlite3
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + name + ";"
    with sqlite3.connect("example.db") as connection:
        cursor = connection.cursor()
        # Noncompliant: user input is used without sanitization.
        cursor.execute(query)
        connection.commit()
        connection.close()
```

## 도전 과제

1) Bedrock을 통해 이 코드의 내용을 해석해보세요. 
<br/>
<br/>

2) 해당 코드가 SQL Injection에  취약한 이유를 확인해 보세요.
<br/>
<br/>
(ㅈ(()))
