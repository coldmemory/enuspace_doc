---
layout: default
title: Tutorial
parent: External Task
nav_order: a
---


# External Task - Tutorial

---

본 튜터리얼은 enuSpace for jupiter version 기반으로 작성되었습니다.

reference c-task code : [https://github.com/EXPNUNI/enuSpace-Article/blob/master/sample\_task/c\_task/Task/CoreTask/CoreTask/CoreTask.cpp](https://github.com/EXPNUNI/enuSpace-Article/blob/master/sample_task/c_task/Task/CoreTask/CoreTask/CoreTask.cpp)

reference fortran-task code1 : [https://github.com/EXPNUNI/enuSpace-Article/blob/master/sample\_task/fortran\_task/Task/CoreTaskF/CoreTask/CoreTask.cpp](https://github.com/EXPNUNI/enuSpace-Article/blob/master/sample_task/fortran_task/Task/CoreTaskF/CoreTask/CoreTask.cpp)

reference fotran\_task code2 : [https://github.com/EXPNUNI/enuSpace-Article/blob/master/sample\_task/fortran\_task\_x64/Task/CoreTaskF/CoreTask/CoreTask.cpp](https://github.com/EXPNUNI/enuSpace-Article/blob/master/sample_task/fortran_task_x64/Task/CoreTaskF/CoreTask/CoreTask.cpp)

## Mixed language - C and Fortran Task

[https://github.com/EXPNUNI/enuSpace-Article/tree/master/sample\_task/fortran\_task](#) 다운

### Project Open

fortran\_task.enup 프로젝트를 오픈합니다.

![](./assets/externaltask/project_open.png)

### Database Tag 추가

데이터베이스 Tag를 추가합니다.

![](./assets/externaltask/database_add.png)

프로젝트 닫기를 수행하고 코드를 수정합니다.

### 연동 코드 수정

fortran\_task\Task\CoreTaskF\CoreTask\CoreTask.vcproj 파일 오픈

FortranModule 프로젝트 내의 Calculation.f 파일을 수정합니다.

추가된 enuSpace Tag의 값을 취득하고 값을 설정하기 위하여 아래와 같이 코드를 추가합니다.

```fortran
      SUBROUTINE MAIN_PROC()

      USE globals                       
      REAL*8 DATA_VALUE 
      REAL*8 ARRAY_VALUE(3,3)

      CALL GetValue('@CORE.analog', DATA_VALUE)
      IF (DATA_VALUE .GT. 1.0) THEN
        DATA_VALUE = 0
      ELSE
        DATA_VALUE = DATA_VALUE+0.01
      ENDIF
      CALL SetValue('@CORE.analog', DATA_VALUE)      

      CALL Message('Call Main Proc')
      END
```

**빌드 수행시 enuSpace 64bit를 이용하는 경우, 64bit 환경으로 컴파일 및 빌드를 수행합니다.**

FortranModule 프로젝트 빌드를 수행합니다.

FortranModule.lib 파일이 정상적으로 생성되었는지 확인합니다.

CoreTask 프로젝트 빌드를 수행합니다.

fortran\_task\Task\CoreTaskF\CoreTaskF.dll 파일이 정상적으로 생성되었는지 확인합니다.

### Array 변수값에 대한 연동

데이터베이스의 Tag정보를 배열 변수 double 형 @CORE.flux\[3\]\[3\] 등록하였다면, GetArrayValue\(\)함수와 SetArrayValue\(\)함수를 통하여 데이터를 연동할 수 있다.

GetArrayValue\(\)함수는 하나의 배열 변수에 대하여 값을 취득하며, SetArrayValue\(\)함수는 주어진 형의 사이즈만큼 전달을 수행한다.

이때 Fortran의 배열의 메모리 인덱스 와 C배열의 메모리 인덱스가 다르다.

예\)

fortran ARRAY\_\_VALUE\(1,1\)  =&gt; C ARRAY\_\_VALUE\[0\]\[0\]

fortran ARRAY\_\_VALUE\(2,1\)  =&gt; C ARRAY\_\_VALUE\[0\]\[1\]

fortran ARRAY\_\_VALUE\(3,1\)  =&gt; C ARRAY\_\_VALUE\[0\]\[2\]

```fortran
      SUBROUTINE MAIN_PROC()

      USE globals                       
      REAL*8 DATA_VALUE 
      REAL*8 ARRAY_VALUE(3,3)

      ARRAY_VALUE(1,1) = 0
      ARRAY_VALUE(1,2) = 0
      ARRAY_VALUE(1,3) = 0      
      CALL GetArrayValue('@CORE.flux[0][0]', ARRAY_VALUE(1,1))
      CALL GetArrayValue('@CORE.flux[0][1]', ARRAY_VALUE(2,1))
      CALL GetArrayValue('@CORE.flux[0][2]', ARRAY_VALUE(3,1))

      ARRAY_VALUE(1,1) = ARRAY_VALUE(1,1) + 0.1
      ARRAY_VALUE(1,2) = ARRAY_VALUE(1,2) + 0.1
      ARRAY_VALUE(1,3) = ARRAY_VALUE(1,3) + 0.1

      CALL SetArrayValue('@CORE.flux[0][0]', ARRAY_VALUE(1,1), 2, 3*3);

      END
```

SetArrayValue\(\)함수의 세번째 파라미터는 정의된 아래의 타입정보를 입력한다.

```fortran
#define DEF_INT                0
#define DEF_FLOAT            1
#define DEF_DOUBLE            2
#define DEF_BOOL            3
```

**Data Sizes \(Fortran And C\)**

| FORTRAN | C |
| :--- | :--- |
| INTEGER X | int x |
| INTERGER\*4 X | int x |
| REAL X | float x |
| REAL\*4 X | float x |
| REAL\*8 X | double x |

### 연동 테스트

프로젝트를 오픈하여 Task를 기동합니다.

![](./assets/externaltask/test.png)추가된 Database Tag 변수 @CORE.analog의 값이 변경되는지 확인합니다.

