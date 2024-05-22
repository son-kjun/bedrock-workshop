# 실습 1: Bedrock CodeGeneration
## 실습 소개
이 실습에서는 Amazon Bedrock 에서 CodeGeneration 모델을 활용하여, Code Generation을 실습해봅니다.
 

**이 실습을 실행하려면 aws account가 Claude을 구독하고 있어야 합니다. Bedrock 콘솔을 통해 구독할 수 있습니다.**


## Bedrock PlayGround에서 코드 생성 실습하기
#### 1. Amazon Bedrock 콘솔 > Example에서 'Code Generation'을  검색하여, Claude v2를 선택합니다.
![alt text](27433F29-4210-435F-804F-BE83159130E8.jpeg)

Promt와 Response의 예제를 확인하고 내가 찾던 모델인지 확인해봅니다.
![alt text](images/0C88DB09-95F3-4105-83D2-1C7546805CFF.jpeg)

실습을 위해 'Open in Playground'를 클릭하여 실습 환경을 생성합니다.

## Text2Python
#### 1. 다음과 같이 Single-line 코드 생성을 실습해봅니다.

~~~
create the python program to create sales.csv file
create the python program to write date to sales.csv
~~~

![alt text](image.png)
 
Bedrock의 답변을 확인해봅니다.
![alt text](image-1.png) 

이와 같은 방법으로 여러가지 코드 생성을 테스트 해보겠습니다.
#### 4. 다음과 같이 Full function 코드 생성을 실습해봅니다.
* 버그가 없을 것, 표준 라이브라리를 쓸 것 등에 대한 요청사항을 추가해봅니다.
```
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
```
 <!-- **Temperature** 매개변수를 사용하면 응답을 구성할 때 모델이 보다 "창의적"으로 응답할 수 있습니다. 온도가 0이면 무작위성이 없으며 매번 가장 가능성이 높은 단어가 선택됩니다. 응답의 다양성을 높이려면 Temperature 값을 더 높게 설정하고 동일한 요청을 여러 번 실행할 수 있습니다.
**Response length** 매개변수는 응답에 반환할 토큰의 수를 결정합니다. 이를 사용하여 모델에서 반환되는 콘텐츠의 양을 줄이거나 늘릴 수 있습니다. 길이를 너무 낮게 설정하면 응답이 완료되기 전에 끊어질 수 있습니다.
**Info** 링크를 통해 각 파라미터에 대한 설명을 확인할 수 있습니다.-->

## Text2SQL
 
5. 다음과 같이 SQL Query Generation 코드 생성을 실습해봅니다.</br>
![alt text](1529F259-5D25-4E91-BF46-B30DF6D73B5B.jpeg)
```
AnyCompany has a database with a table named sales_data containing sales records. The table has following columns:
- date (YYYY-MM-DD)
- product_id
- price
- units_sold
Can you generate SQL queries for the below: 
- Identify the top 5 best selling products by total sales for the year 2023
- Calculate the monthly average sales for the year 2023
```

어느 병원의 환자 관리 시스템의 테이블 스키마를 알려주고, 2023년 4월 1일에 5개 이상의 서로 다른 약을 처방받은 모든 환자를 가져오는 SQL 쿼리를 작성해달라고 해보겠습니다. 

```
You're provided with a database schema representing any hospital's patient management system.
The system holds records about patients, their prescriptions, doctors, and the medications prescribed.

Here's the schema:

```sql
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
```

![alt text](5A42CCBC-63F5-4BD3-A591-2C41B7AF0885.jpeg)


## Code Intepretation
6. 이번에는 코드에 대한 해석/설명을 시도해 보겠습니다.
무언가 잘못되어있거나, best practice가 아니면 알려달라고도 추가해보겠습니다.

```
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
```

몇 가지 개선포인트가 있지만 전반적으로 코드 디자인이 괜찮다고 알려줍니다.
![alt text](4B8704A1-759B-42BA-8A07-9964FBA1A9A2.jpeg)
