---
layout: default
title: enuSetSelectLinecolor
parent: Application API
---
# void enuSetSelectLinecolor\(HVIEW pENUView, wchar\_t\* strColor\)

void enuSetSelectLinecolor\(HVIEW pENUView, wchar\_t\* strColor\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

* wchar\_t\* strColor

객체의 라인 색상값을 입력합니다. \(ex. "rgb\(0,0,0\)" or \(\#000000\)\)

#### Return Value

Type : NONE

#### Remarks

선택 객체의 라인 색상 설정을 수행합니다. SVG에서는 stroke 속성입니다.

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
    <polyline
        id="ID_1enn320"
        stroke="rgb(0,119,189)"
        stroke-opacity="1.00"
        stroke-width="2.00"
        transform="translate(170.00,185.00) rotate(0.00) scale(1.0000, 1.0000)"
        pg-xcenter="0.00"
        pg-ycenter="0.00"
        stroke-linecap="butt"
         stroke-linejoin="miter"
         points="0,0 96.000000,-47.000000 133.000000,-5.000000 193.000000,-23.000000 260.000000,16.000000"
        pg-begin-arrow-type="none"
        pg-begin-arrow-size="5.00"
        pg-begin-arrow-angle="60.00"
        pg-begin-arrow-span="medium2"
        pg-end-arrow-type="none"
        pg-end-arrow-size="5.00"
        pg-end-arrow-angle="60.00"
        pg-end-arrow-span="medium2"
    >
    </polyline>
</svg>
```

#### Examples

```cpp
void CenuSpaceView::OnLineColor()
{
    CMFCRibbonBar* pRibbon = ((CMDIFrameWndEx*) AfxGetMainWnd())->GetRibbonBar(); 
    ASSERT_VALID(pRibbon); 

    CMFCRibbonColorButton* pFillColorBtn = DYNAMIC_DOWNCAST(CMFCRibbonColorButton, pRibbon->FindByID(ID_OBJECT_LINECOLOR));

    if (pFillColorBtn != NULL)
    {
        COLORREF color = pFillColorBtn->GetColor();
        int R = 0, G = 0, B = 0; 

        R = GetRValue(color); 
        G = GetGValue(color);
        B = GetBValue(color); 

        CString strColor;
        strColor.Format(L"#%2x%2x%2x", R, G, B);

        enuSetSelectLinecolor(m_pENUView, strColor.GetBuffer(0));
    }
}
```



