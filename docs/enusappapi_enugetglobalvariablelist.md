---
layout: default
title: enuGetGlobalVariableList
parent: Application API
---
# void\* enuGetGlobalVariableList\(wchar\_t\* pStrFileName\)

void\* enuGetGlobalVariableList\(wchar\_t\* pStrFileName\)

#### Parameters

* wchar\_t\* pStrFileName

Global영역의 SVG 파일을 입력합니다.

#### Return Value

Type : void\*

CPtrList의 포인터를 반환합니다. CPtrList의 포인터를 통하여 전역변수 리스트를 취득합니다.

#### Remarks

전역변수 리스트 획득시 활용합니다.

```xml
<?xml version="1.0" encoding="UTF-16"?>
<svg
    id="ID_1enaBg"
    stroke="rgb(0,119,189)"
    stroke-opacity="1.00"
    stroke-width="1.00"
    transform="translate(0.00,0.00) rotate(0.00) scale(1.0000, 1.0000)"
    pg-xcenter="0.00"
    pg-ycenter="0.00"
    enuspace-version="3.0.2.0"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    pg-classname="global"
>
    <defs
        id="ID_1enaBg0"
    >
        <pg-struct
            id="ID_1enbGj"
            type="DataIO"
            desc=""
        >
            <pg-attribute
                id="ID_1enbGj0"
                type="double"
                variable="Input"
                initial=""
                desc="input variable"
            >
            </pg-attribute>
            <pg-attribute
                id="ID_1enbGj1"
                type="double"
                variable="Output"
                initial=""
                desc="output variable"
            >
            </pg-attribute>
        </pg-struct>
    </defs>
    <pg-attribute
        id="ID_1enbNS"
        type="DataIO"
        variable="g_IO1"
        initial="g_IO1.Input=0.000000 g_IO1.Output=0.000000"
        desc=""
    >
    </pg-attribute>
    <pg-attribute
        id="ID_1enbNj"
        type="DataIO"
        variable="g_IO2"
        initial="g_IO2.Input=0.000000 g_IO2.Output=0.000000 "
        desc=""
    >
    </pg-attribute>
</svg>
```

#### Examples

```cpp
CPtrList* pVarList = (CPtrList*)enuGetGlobalVariableList(L"global\\global.svg");
if (pVarList)
{
    POSITION posVar = pVarList->GetHeadPosition();
    while (posVar)
    {
        CSvgNodePgAttribute* PgAttribute = (CSvgNodePgAttribute *) pVarList->GetAt(posVar);

        CString strData;
        strData.Format(L"%s %s%s", PgAttribute->Get_type(), PgAttribute->Get_variable(), PgAttribute->GetArrayDimension());

        // tvstruct.item.pszText = strData.GetBuffer(0);
        // tvstruct.item.lParam = DEF_VARIABLE;
        // tvstruct.item.iImage = 11;
        // tvstruct.item.iSelectedImage = 11;
        // m_wndFileView.InsertItem(&tvstruct);

        (DataItemStruct *)pVarList->GetNext(posVar);    
    }
}
```



