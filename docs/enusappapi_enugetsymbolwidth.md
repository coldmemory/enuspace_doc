---
layout: default
title: enuGetSymbolWidth
parent: Application API
---
# float enuGetSymbolWidth\(HVIEW pENUView, wchar\_t\* strSymbol\)

float enuGetSymbolWidth\(HVIEW pENUView, wchar\_t\* strSymbol\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

* wchar\_t\* strSymbol

심볼의 ID값을 입력합니다.

#### Return Value

Type : float

심볼의 넓이값을 반환합니다. \* 본 함수는 HMI, LOGIC영역에 대해서만 뷰를 통하여 수행합니다.

#### Remarks

```xml
<?xml version="1.0" encoding="UTF-16"?>
<svg
    id="ID_1enc0p"
    stroke="rgb(0,119,189)"
    stroke-opacity="1.00"
    stroke-width="1.00"
    transform="translate(0.00,0.00) rotate(0.00) scale(1.0000, 1.0000)"
    pg-xcenter="0.00"
    pg-ycenter="0.00"
    style="stroke:rgb(127,127,127);stroke-opacity:1.00;stroke-width:2.00;stroke-dasharray:1,1,1;"
    enuspace-version="3.0.2.0"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    pg-create-time="2018-2-19 3:21:7.19"
    width="1920"
    height="1080"
>
    <defs
        id="ID_1enc0p1"
    >
        <symbol
            id="SYMBOL1"
            type="node"
            stroke="rgb(0,119,189)"
            stroke-opacity="1.00"
            stroke-width="1.00"
            transform="translate(0.00,0.00) rotate(0.00) scale(1.0000, 1.0000)"
            pg-xcenter="0.00"
            pg-ycenter="0.00"
        >
            <rect
                id="ID_1enc0z0"
                stroke="rgb(0,119,189)"
                stroke-opacity="1.00"
                stroke-width="2.00"
                transform="translate(2.00,-1.00) rotate(0.00) scale(1.0000, 1.0000)"
                pg-xcenter="0.00"
                pg-ycenter="0.00"
                stroke-linecap="butt"
                 stroke-linejoin="miter"
                 x="0.00"
                y="0.00"
                width="82.00"
                height="55.00"
                rx="0.00"
                ry="0.00"
                fill="rgb(0,174,238)"
                fill-opacity="1.00"
            >
            </rect>
        </symbol>
    </defs>
</svg>
```

#### Examples

```cpp
float fHeight = enuGetSymbolHeight(m_pENUView, L"SYMBOL1");
float fWidth = enuGetSymbolWidth(m_pENUView, L"SYMBOL1");
```



