---
layout: default
title: enuAddGlobalVariable
parent: Application API
---
# bool enuAddGlobalVariable\(wchar\_t\* pStrFileName, wchar\_t\* pStrType, wchar\_t\* strVariable, wchar\_t\* strInitValue=L"", wchar\_t\* strDescription=L""\)

bool enuAddGlobalVariable\(wchar\_t\* pStrFileName, wchar\_t\* pStrType, wchar\_t\* strVariable, wchar\_t\* strInitValue=L"", wchar\_t\* strDescription=L""\)

#### Parameters

* wchar\_t\* pStrFileName

global 파일명을 입력합니다.

* wchar\_t\* pStrType

추가하고자하는 변수의 타입정보를 입력합니다. \(타입종류 "int", "float", "double", "bool", "string", 사용자가 추가한 구조체 정의 이름\)

* wchar\_t\* strVariable

추가하고자하는 변수명을 입력합니다.

* wchar\_t\* strInitValue

초기값을 입력합니다.

* wchar\_t\* strDescription

변수명에 대한 설명을 추가합니다.

#### Return Value

Type : bool

변수등록의 성공여부를 반환합니다.

#### Remarks

global 파일 영역에 전역변수를 추가하여 활용합니다.

#### Examples

```cpp
if (enuAddGlobalVariable(L"global//global.svg", L"double", L"g_input", L"55.45", L"global variable input1"))
{
    AfxMessageBox(L"Global variable create success.");
}
else
{
    AfxMessageBox(L"Global variable create failed.");
}
```



