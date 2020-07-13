---
layout: default
title: enuRecvNetData
parent: Application API
---
# void enuRecvNetData\(void functioncb\(wchar\_t\* system, char\* buffer, int length\)\)

void enuRecvNetData\(void functioncb\(wchar\_t\* system, char\* buffer, int length\)\)

#### Parameters

void functioncb\(wchar\_t\* system, char\* buffer, int length\)

함수 포인터를 설정합니다.

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



