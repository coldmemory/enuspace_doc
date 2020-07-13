---
layout: default
title: enuAddGlobalStruct
parent: Application API
---
# bool enuAddGlobalStruct\(wchar\_t\* pStrFileName, wchar\_t\* pStrStructName, CPtrList\* pItem\)

bool enuAddGlobalStruct\(wchar\_t\* pStrFileName, wchar\_t\* pStrStructName, CPtrList\* pItem\)

#### Parameters

* Type : wchar\_t\* pStrFileName

추가하고자 하는 global 파일명을 입력합니다.

* wchar\_t\* pStrStructName

추가하고자 하는 구조체 이름을 입력합니다.

* CPtrList\* pItem

구조체의 아이템 리스트정보를 전달합니다.

**구조체**

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

#### Return Value

Type : bool

성공 여부를 반환합니다.

#### Remarks

사용자 정의 구조체를 추가하고자 하는 경우 사용합니다. 구조체의 전달하면 SVG 상에 구조체 노드가 생성됩니다.

추가된 구조체 정의를 통하여, 구조체 변수를 생성하여 활용합니다.

#### Examples

```cpp
CString m_strFileName = L"global\\global.svg";
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
    // 구조체 이름을 통한 변수 추가.
    enuAddGlobalVariable(m_strFileName.GetBuffer(0), strStructName.GetBuffer(0), L"MyVariable", L"", L"description");
}
else
{
    // struct 등록 실패.
}
```



