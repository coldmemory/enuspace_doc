---
layout: default
title: enuSetSelectFillcolor
parent: Application API
---
# void enuSetSelectFillcolor\(HVIEW pENUView, wchar\_t\* strColor\)

void enuSetSelectFillcolor\(HVIEW pENUView, wchar\_t\* strColor\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

* wchar\_t\* strColor

색상값을 입력합니다. \(ex. "RGB\(255,255,255\)" or "\#FFFFFF"

#### Return Value

Type : NONE

#### Remarks

SVG의 선택 객체의 fill 색상을 지정합니다.

```xml
<?xml version="1.0" encoding="UTF-16"?>
<svg
    id="ID_1enfXB"
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
    pg-create-time="2018-2-19 7:6:45.663"
    width="1920"
    height="1080"
>
    <rect
        id="ID_BOX"
        stroke="rgb(0,119,189)"
        stroke-opacity="1.00"
        stroke-width="2.00"
        transform="translate(286.00,118.00) rotate(0.00) scale(1.0000, 1.0000)"
        pg-xcenter="0.00"
        pg-ycenter="0.00"
        stroke-linecap="butt"
         stroke-linejoin="miter"
         x="0.00"
        y="0.00"
        width="137.00"
        height="93.00"
        rx="0.00"
        ry="0.00"
        fill="rgb(0,174,238)"
        fill-opacity="1.00"
    >
    </rect>
</svg>
```

#### Examples

```cpp
void CenuSpaceView::OnFillColor()
{
    CMFCRibbonBar* pRibbon = ((CMDIFrameWndEx*) AfxGetMainWnd())->GetRibbonBar(); 
    ASSERT_VALID(pRibbon); 

    CMFCRibbonColorButton* pFillColorBtn = DYNAMIC_DOWNCAST(CMFCRibbonColorButton, pRibbon->FindByID(ID_OBJECT_FILLCOLOR));

    if (pFillColorBtn != NULL)
    {
        COLORREF color = pFillColorBtn->GetColor();
        int R = 0, G = 0, B = 0; 

        R = GetRValue(color); 
        G = GetGValue(color);
        B = GetBValue(color); 

        CString strColor;
        strColor.Format(L"#%2x%2x%2x", R, G, B);

        enuSetSelectFillcolor(m_pENUView, strColor.GetBuffer(0));
    }
}
```



