---
layout: default
title: enuSendNetData
parent: Application API
---
# void enuSendNetData\(wchar\_t\* system, char\* data, int length\)

void enuSendNetData\(wchar\_t\* system, char\* data, int length\)

#### Parameters

* wchar\_t\* system

전달하는 시스템의 이름을 입력합니다.

* char\* data

데이터를 입력합니다.

* int length

데이터의 길이를 지정합니다.

#### Return Value

Type : void

#### Remarks

enu server 또는 client로부터 데이터를 받았을 경우 전달 받을 함수 포인터를 설정합니다.  

#### Examples

```cpp
void RecvFunction(wchar_t* system, char* buffer, int length)
{
    // TO DO JOB
}

void SetConnect()
{
    enuLinkServerStart();
    enuRecvNetData(RecvFunction);
}

void SetSendEvent()
{
    char senddata[9];
    strcpy(senddata,"data_1234");
    
    enuSendNetData(L"SYSTEM1", senddata, 9);
}
```



