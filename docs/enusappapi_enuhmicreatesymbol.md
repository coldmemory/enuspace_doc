---
layout: default
title: enuHmiCreateSymbol
parent: Application API
---
# bool enuHmiCreateSymbol\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)

bool enuHmiCreateSymbol\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)

#### Parameters

* wchar\_t\* pStrFilename

HMI영역에서 SVG 파일이름을 입력합니다.

* wchar\_t\* pStrSymbol

생성하고자하는 심볼이름을 입력합니다.

#### Return Value

Type : bool

HMI심볼 생성여부를 반환합니다.

#### Remarks

동적으로 심볼을 생성하는 함수입니다.

#### Examples

```cpp
if (enuHmiCreateSymbol(L"library\\hmi\\hmi_symbol.svg", L"ID_GAGUE"))
{
    HVIEW ViewHandle = NULL; 
    ViewHandle = enuCreateView(this->m_hWnd);
    enuSetHmiComponent(ViewHandle, L"library\\hmi\\hmi_symbol.svg", L"ID_GAGUE");
}
```



