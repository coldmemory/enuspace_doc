---
layout: default
title: enuModifyGlobalStruct
parent: Application API
---
# bool enuModifyGlobalStruct\(wchar\_t\* pStrFileName, wchar\_t\* strStruct, wchar\_t\* strNewStruct, CPtrList\* pItem\)

bool enuModifyGlobalStruct\(wchar\_t\* pStrFileName, wchar\_t\* strStruct, wchar\_t\* strNewStruct, CPtrList\* pItem\)

#### Parameters

* wchar\_t\* pStrFileName

GLOBAL영역의 SVG파일이름을 입력합니다.

* wchar\_t\* strStruct

GLOBAL영역의 구조체 정의 이름을 입력합니다.

* wchar\_t\* strNewStruct

GLOBAL영역의 새로운 구조체 정의 이름을 입력합니다.

* CPtrList\* pItem

GLOBAL영역의 새로운 구조체 정보를 입력합니다.

#### Return Value

Type : bool

구조체 정보 변경의 정상적용 유무를 반환합니다.

#### Remarks

구조체 정보를 변경하고자하는 경우에 위 함수를 활용합니다.

```cpp
struct StructList
{
    wchar_t strType[DEF_NAME_LEN];
    wchar_t strVariable[DEF_NAME_LEN];
    wchar_t strInitial[DEF_MAXTEXT_LEN];
    wchar_t strDescription[DEF_MAXTEXT_LEN];

    public :StructList()
    {
        wcscpy_s(strType, L"");
        wcscpy_s(strVariable, L"");
        wcscpy_s(strInitial, L"");
        wcscpy_s(strDescription, L"");
    }
};
```

#### Examples

```cpp
void CFileView::OnModifyGlobalStruct()
{
    CString strFileName = L"global\\global.svg";
    CString strStructName= L"InOutStruct";
    CString strNewStructName= L"IOStruct";

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

    if (enuModifyGlobalStruct(strFileName .GetBuffer(0), strStructName.GetBuffer(0), strNewStructName.GetBuffer(0), &ItemList))
    {
        // TO DO JOB
    }
}
```



