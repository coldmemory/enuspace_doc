---
layout: default
title: enuRegisterJavaScriptById
parent: Application API
---
# void enuRegisterJavaScriptById\(wchar\_t\* strPagename, wchar\_t\* strID, wchar\_t\* strFunction, wchar\_t\* strScript\)

void enuRegisterJavaScriptById\(wchar\_t\* strPagename, wchar\_t\* strID, wchar\_t\* strFunction, wchar\_t\* strScript\)

#### Parameters

* wchar\_t\* strPagename

픽쳐의 파일이름을 입력합니다.

* wchar\_t\* strID

객체의 ID값을 입력합니다.

* wchar\_t\* strFunction

추가하고자하는 함수의 이름을 입력합니다.

* wchar\_t\* strScript

스크립트의 내용을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

객체의 ID정보를 이용하여 스크립트를 등록합니다.

#### Examples

```cpp
void OnAddScript()
{    
    CString script = L"function BlickFunction()\r\n{PrintMessage(\"call...\")\r\n}"        // javascript function

    RegisterJavaScriptById(L"picture\\picture.svg", L"ID_RECT", L"BlickFunction", script.GetBuffer(0));
    enuExecuteFunction(L"ID_RECT.BlickFunction()");
}
```



