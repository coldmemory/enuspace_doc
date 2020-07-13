---
layout: default
title: enuSetSelectFontStrikethough
parent: Application API
---
# void enuSetSelectFontStrikethough\(HVIEW pENUView, bool bFlag\)

void enuSetSelectFontStrikethough\(HVIEW pENUView, bool bFlag\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

* bool bFlag

Strikethough설정 플래그를 입력합니다.

#### Return Value

Type : NONE

#### Remarks

선택 텍스트 객체의 Strikethough설정을 수행합니다.

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
    <text
        id="ID_TEXT"
        stroke="rgb(0,0,0)"
        stroke-opacity="1.00"
        stroke-width="1.00"
        transform="translate(305.00,221.00) rotate(0.00) scale(1.0000, 1.0000)"
        pg-xcenter="0.00"
        pg-ycenter="0.00"
        stroke-linecap="butt"
         stroke-linejoin="miter"
         x="0.00"
        y="0.00"
        dx="0.00"
        dy="0.00"
        font-family="Arial"
        font-size="20.0"
        font-weight=""
        font-style="normal"
        text-anchor="start"
        baseline-shift="0"
        baseline-height="-22.998047"
        fill="rgb(0,0,0)"
        fill-opacity="1.00"
        pg-format=""
        pg-line-count="1"
        pg-oneline-height="22.998047"
        text-decoration="none"
    >
Text Object
    </text>
</svg>
```

#### Examples

```cpp
void CenuSpaceView::OnFontStrikethough()
{
    CMFCRibbonBar* pRibbon = ((CMDIFrameWndEx*) AfxGetMainWnd())->GetRibbonBar(); 
    ASSERT_VALID(pRibbon); 
    CMFCRibbonButton* pButton = DYNAMIC_DOWNCAST(CMFCRibbonButton, pRibbon->FindByID(ID_FONT_STRIKETHROUGH));
    if (pButton == NULL)
        return;

    bool bCheck = false;
    if (pButton->IsChecked() == TRUE)
        bCheck = true;

    enuSetSelectFontStrikethough(m_pENUView, !bCheck);
}
```



