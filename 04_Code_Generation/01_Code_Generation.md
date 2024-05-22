# 실습 1: Bedrock CodeGeneration
## 실습 소개
이 실습에서는 Amazon Bedrock 에서 CodeGeneration을 위한 Claude v2 모델을 활용하여, Code Generation을 실습해봅니다.
 

**이 실습을 실행하려면 aws account가 Claude v2을 구독하고 있어야 합니다. Bedrock 콘솔을 통해 구독할 수 있습니다.**
<BR>
<BR>
<BR>


## Bedrock PlayGround에서 코드 생성 실습하기
#### 1. Amazon Bedrock 콘솔 > Example에서 'Code Generation'을  검색하여, Claude v2를 선택합니다.
![alt text](images/27433F29-4210-435F-804F-BE83159130E8.jpeg)

Promt와 Response의 예제를 확인하고 내가 찾던 모델인지 확인해봅니다.
![alt text](images/0C88DB09-95F3-4105-83D2-1C7546805CFF.jpeg)

실습을 위해 'Open in Playground'를 클릭하여 실습 환경을 생성합니다.
<BR>
<BR>
<BR>

## Text2Python
**1. 다음과 같이 Single-line 코드 생성을 실습해봅니다.**

~~~
create the python program to create sales.csv file
create the python program to write date to sales.csv
~~~

![alt text](/images/image.png)
 
Bedrock의 답변을 확인해봅니다.
![alt text](images/image-1.png) 

이와 같은 방법으로 여러가지 코드 생성을 테스트 해보겠습니다.

**2. 다음과 같이 Full function 코드 생성을 실습해봅니다.** 

- 버그가 없을 것, 표준 라이브라리를 쓸 것 등에 대한 요청사항을 추가해봅니다.
~~~
You have a CSV, sales.csv, with columns:
- date (YYYY-MM-DD)
- product_id
- price
- units_sold
Create a python program to analyze the sales data from a CSV file. The program should be able to read the data, and determine below:
- Total revenue for the year
- The product with the highest revenue
- The date with the highest revenue
- Visualize monthly sales using a bar chart
Ensure the code is syntactically correct, bug-free, optimized, not span multiple lines unnessarily, and prefer to use standard libraries. Return only python code without any surrounding text, explanation or context.
~~~
<BR>
<BR>
<BR>

## Text2SQL : 대화로 DB를 검색하기
 
 Code Generation 을 통해 우리는 Python 과 같은 일반 프로그래밍 언어를 작성할 수 있을 뿐만 아니라 SQL 도 생성할 수 있습니다. 한 마디로 우리는 이제 대화로 DataBase를 검색할 수 있게 되었습니다. 이 섹션에서는  SQL Query Generation을 실습해 보겠습니다.



**1.어느 회사의 영업데이터(sales_data)에서, 2023년 Top5 제품을 알려주는 쿼리와, 2023년 평균 월별 영업 통계를 계산해달라고 요청해봅시다.** </br> 
~~~
AnyCompany has a database with a table named sales_data containing sales records. The table has following columns:
- date (YYYY-MM-DD)
- product_id
- price
- units_sold
Can you generate SQL queries for the below: 
- Identify the top 5 best selling products by total sales for the year 2023
- Calculate the monthly average sales for the year 2023
~~~

예) ![alt text](images/1529F259-5D25-4E91-BF46-B30DF6D73B5B.jpeg)

<br>
<br>
<br>

**2.어느 병원의 환자 관리 시스템의 테이블 스키마를 알려주고, 2023년 4월 1일에 5개 이상의 서로 다른 약을 처방받은 모든 환자를 가져오는 SQL 쿼리를 작성해달라고 해보겠습니다.**


~~~
You're provided with a database schema representing any hospital's patient management system.
The system holds records about patients, their prescriptions, doctors, and the medications prescribed.

Here's the schema:

sql
CREATE TABLE Patients (
    PatientID int,
    FirstName varchar(50),
    LastName varchar(50),
    DateOfBirth datetime,
    Gender varchar(10),
    PRIMARY KEY (PatientID)
);

CREATE TABLE Doctors (
    DoctorID int,
    FirstName varchar(50),
    LastName varchar(50),
    Specialization varchar(50),
    PRIMARY KEY (DoctorID)
);

CREATE TABLE Prescriptions (
    PrescriptionID int,
    PatientID int,
    DoctorID int,
    DateIssued datetime,
    PRIMARY KEY (PrescriptionID)
);

CREATE TABLE Medications (
    MedicationID int,
    MedicationName varchar(50),
    Dosage varchar(50),
    PRIMARY KEY (MedicationID)
);

CREATE TABLE PrescriptionDetails (
    PrescriptionDetailID int,
    PrescriptionID int,
    MedicationID int,
    Quantity int,
    PRIMARY KEY (PrescriptionDetailID)
);


Write a SQL query that fetches all the patients who were prescribed more than 5 different medications on 2023-04-01.
~~~

Claude가 어떻게 SQL을 작성해 주는지 확인해보겠습니다. <br>

예) 
![alt text](images/5A42CCBC-63F5-4BD3-A591-2C41B7AF0885.jpeg)

<br>
<br>
<br>

## Code Intepretation

Code Generation을 이야기 할 때, 우리는 단순히 코드의 생성 뿐 아니라 코드를 이해할 수 있게되었다고 말할 수 있습니다. 개발자에게 프로그래밍이란 단순히 어떤 기능을 만드는데 그치지 않고, Best Practice를 준수하는 코딩을 하는 능력뿐만 아니라 동시에 다른 사람의 코드를 이해하는 능력도 못지않게 중요합니다. CodeLLM 이 가진 Code Intepretation 기능이 강조되는 이유입니다. 이번 실습에서는 Code Intepretation을 실습해 보겠습니다. 

**1.이번에는 코드에 대한 해석/설명을 시도해 보겠습니다.
무언가 잘못되어있거나, best practice가 아니면 알려달라고 이야기 해보겠습니다.** </br> 




~~~python
explain below code and highlight if any red flags or not following best practices.

#include <iostream>
#include <string>
#include <vector>

class Vehicle {
protected:
    std::string registrationNumber;
    int milesTraveled;
    int lastMaintenanceMile;

public:
    Vehicle(std::string regNum) : registrationNumber(regNum), milesTraveled(0), lastMaintenanceMile(0) {}

    virtual void addMiles(int miles) {
        milesTraveled += miles;
    }

    virtual void performMaintenance() {
        lastMaintenanceMile = milesTraveled;
        std::cout << "Maintenance performed for vehicle: " << registrationNumber << std::endl;
    }

    virtual void checkMaintenanceDue() {
        if ((milesTraveled - lastMaintenanceMile) > 10000) {
            std::cout << "Vehicle: " << registrationNumber << " needs maintenance!" << std::endl;
        } else {
            std::cout << "No maintenance required for vehicle: " << registrationNumber << std::endl;
        }
    }

    virtual void displayDetails() = 0;

    ~Vehicle() {
        std::cout << "Destructor for Vehicle" << std::endl;
    }
};

class Truck : public Vehicle {
    int capacityInTons;

public:
    Truck(std::string regNum, int capacity) : Vehicle(regNum), capacityInTons(capacity) {}

    void displayDetails() override {
        std::cout << "Truck with Registration Number: " << registrationNumber << ", Capacity: " << capacityInTons << " tons." << std::endl;
    }
};

class Car : public Vehicle {
    std::string model;

public:
    Car(std::string regNum, std::string carModel) : Vehicle(regNum), model(carModel) {}

    void displayDetails() override {
        std::cout << "Car with Registration Number: " << registrationNumber << ", Model: " << model << "." << std::endl;
    }
};

int main() {
    std::vector<Vehicle*> fleet;

    fleet.push_back(new Truck("XYZ1234", 20));
    fleet.push_back(new Car("ABC9876", "Sedan"));

    for (auto vehicle : fleet) {
        vehicle->displayDetails();
        vehicle->addMiles(10500);
        vehicle->checkMaintenanceDue();
        vehicle->performMaintenance();
        vehicle->checkMaintenanceDue();
    }

    for (auto vehicle : fleet) {
        delete vehicle; 
    }

    return 0;
}
~~~

몇 가지 개선포인트가 있지만 전반적으로 코드 디자인이 괜찮다고 알려줍니다.
![alt text](images/4B8704A1-759B-42BA-8A07-9964FBA1A9A2.jpeg)
