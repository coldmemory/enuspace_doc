---
layout: default
title: enuDeleteGlobalVariable
parent: Application API
---
# bool enuDeleteGlobalVariable\(wchar\_t\* pStrFileName, wchar\_t\* strVariable\)

bool enuDeleteGlobalVariable\(wchar\_t\* pStrFileName, wchar\_t\* strVariable\)

#### Parameters

* wchar\_t\* pStrFileName

global 파일명을 입력합니다

* wchar\_t\* strVariable

제거하고자하는 변수명을 입력합니다.

#### Return Value

Type : bool

전역변수 제거 유무를 반환합니다.

#### Remarks

enuAddGlobalVariable\(\)을 통하여 추가된 전역변수를 제거하거나, enuSpace 스튜디오를 이용하여 차가된 전역변수를 제거하는 경우에 사용합니다.

#### Examples

```cpp
if (enuAddGlobalVariable(L"picture//global.svg", L"double", L"g_input", L"55.45", L"global variable input1"))
{
    enuDeleteGlobalVariable(L"picture//global.svg", L"g_input");
}
else
{
    AfxMessageBox(L"Global variable create failed.");
}
```



