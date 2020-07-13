---
layout: default
title: enuGetGlobalPgAttributeList
parent: Application API
---
# void\* enuGetGlobalPgAttributeList\(wchar\_t\* pStrFileName, wchar\_t\* pStrStructName\)

void\* enuGetGlobalPgAttributeList\(wchar\_t\* pStrFileName, wchar\_t\* pStrStructName\)

#### Parameters

* wchar\_t\* pStrFileName

Global영역의 SVG 파일을 입력합니다.

* wchar\_t\* pStrStructName

Global영역의 정의된 구조체 이름을 입력합니다.

#### Return Value

Type : void\*

CPtrList의 포인터를 반환합니다. CPtrList의 포인터를 통하여 구조체 정보의 Attribute 노드들의 정보를 취득합니다.

#### Remarks

정의된 구조체 정보 획득시 활용합니다.

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
</svg>
```

#### Examples

```cpp
CPtrList* pList = NULL;
pList = (CPtrList*)enuGetGlobalPgAttributeList(L"global\\global.svg", L"DataIO");

CString strInformation;
if (pList)
{
    CString strMessage;
    strInformation.Format(L"struct %s\r\n{", L"DataIO");
    POSITION pos = pList->GetHeadPosition();
    while(pos)
    {
        CSvgNodePgAttribute* PgAttribute = (CSvgNodePgAttribute *)pList->GetAt(pos);

        strMessage.Format(L"\t%s %s; //%s\r\n", PgAttribute->Get_type(), PgAttribute->Get_variable(), PgAttribute->Get_desc());
        strInformation= strInformation+ strMessage;

        pList->GetNext(pos);
    }

    strInformation= strInformation + L"};";
}
```



