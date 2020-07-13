---
layout: default
title: enuExecuteString
parent: Application API
---
# void enuExecuteString\(wchar\_t\* picture, wchar\_t\* event\)

void enuExecuteString\(wchar\_t\* pStrPageName, wchar\_t\* pStrEvent\)

#### Parameters

picture : 픽쳐파일이름을 입력합니다.

event : 수행하고자 하는 함수 또는 변수할당 문자열을 입력합니다.

#### Return Value

none

#### Remarks

외부 프로그램에서 해당 픽쳐에 이벤트를 전달하여 함수를 수행하거나 속성값을 설정합니다.

심볼객체의 PIN변수와 Attribute변의 값도 변경할 수 있습니다.

#### Examples

```cpp
void CSampleView::OnInitialUpdate() 
{
    // sample.svg 픽쳐의 ID_TEST객체의 UserFunction()함수 호출
    enuExecuteString(L"picture\\sample.svg", L"ID_TEST.UserFunction()");

    // ID_TEST객체의 width속성값을 10으로 설정
    enuExecuteString(L"picture\\sample.svg", L"ID_TEST.width=10");   

    // ID_SYMBOL객체의 input속성값을 10으로 설정
    enuExecuteString(L"picture\\sample.svg", L"ID_SYMBOL.input=10");             
}
```



