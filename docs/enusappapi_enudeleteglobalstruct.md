---
layout: default
title: enuDeleteGlobalStruct
parent: Application API
---
# bool enuDeleteGlobalStruct\(wchar\_t\* pStrFileName, wchar\_t\* strStruct\)

bool enuDeleteGlobalStruct\(wchar\_t\* pStrFileName, wchar\_t\* strStruct\)

#### Parameters

* wchar\_t\* pStrFileName

제거하고자 하는 global 파일명을 입력합니다.

* wchar\_t\* strStruct

제거하고자 하는 구조체 이름을 입력합니다.

#### Return Value

Type : bool

구조체 정의 노드의 정상제거 유무를 반환합니다.

#### Remarks

enuAddGlobalStruct\(\)함수를 통하여 추가된 구조체 정의를 제거하거나, enuSpace 스튜디오를 통하여 추가한 구조체 정보를 제거합니다.

#### Examples

```cpp
CString m_strFileName = L"picture\\global.svg";
CString strStructName= L"InOutStruct";
CPtrList ItemList;

StructList var1;
wcscpy_s(var1.strType, L"int");
wcscpy_s(var1.strVariable, L"intput");
wcscpy_s(var1.strInitial, L"0");
wcscpy_s(var1.strDescription, L"input variable");
ItemList.AddTail(&var1);

StructList var2;
wcscpy_s(var2.strType, L"int");
wcscpy_s(var2.strVariable, L"output");
wcscpy_s(var2.strInitial, L"0");
wcscpy_s(var2.strDescription, L"output variable");
ItemList.AddTail(&var2);

if (enuAddGlobalStruct(m_strFileName.GetBuffer(0), strStructName.GetBuffer(0), &ItemList))
{
    // struct 등록 성공
    // 구조체 정의 정보 제거.
    enuDeleteGlobalStruct(m_strFileName.GetBuffer(0), strStructName.GetBuffer(0));
}
else
{
    // struct 등록 실패.
}
```



