---
layout: default
title: enuModifyGlobalVariable
parent: Application API
---
# bool enuModifyGlobalVariable\(wchar\_t\* pStrFileName, wchar\_t\* strVariable, wchar\_t\* strNewType, wchar\_t\* strNewVariable, wchar\_t\* strNewDescription\)

bool enuModifyGlobalVariable\(wchar\_t\* pStrFileName, wchar\_t\* strVariable, wchar\_t\* strNewType, wchar\_t\* strNewVariable, wchar\_t\* strNewDescription\)

#### Parameters

* wchar\_t\* pStrFileName

GLOBAL영역의 SVG파일이름을 입력합니다.

* wchar\_t\* strVariable

GLOBAL영역의 변수이름을 입력합니다.

* wchar\_t\* strNewType

GLOBAL영역의 변수타입을 입력합니다. \(타입종류 "int", "float", "double", "bool", "string"\)

* wchar\_t\* strNewVariable

GLOBAL영역의 새로운 변수이름을 입력합니다.

* wchar\_t\* strNewDescription

GLOBAL영역의 새로운 변수에 대한 설명을 입력합니다.

#### Return Value

Type : bool

#### Remarks

GLOBAL영역의 전역변수의 정보를 변경시 사용합니다.

#### Examples

```cpp
void CFileView::OnModifyGlobalStruct()
{
    if (enuModifyGlobalVariable(L"global\\global.svg", L"g_global", L"int", L"g_newglobal", L"global variable"))
    {
        // TO DO JOB
    }
}
```



