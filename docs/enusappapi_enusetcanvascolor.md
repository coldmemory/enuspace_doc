---
layout: default
title: enuSetCanvasColor
parent: Application API
---
# void enuSetCanvasColor\(HVIEW pENUView, byte iR, byte iG, byte iB\)

void enuSetCanvasColor\(HVIEW pENUView, byte iR, byte iG, byte iB\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

* byte iR

켄버스의 Red 색상값을 입력합니다. \(0~255\)

* byte iG

켄버스의 Green 색상값을 입력합니다. \(0~255\)

* byte iB

켄버스의 Blue 색상값을 입력합니다. \(0~255\)

#### Return Value

Type : NONE

#### Remarks

켄버스의 색상을 지정하는 함수입니다.

#### Examples

```cpp
HVIEW ViewHandle = NULL; 
void CSampleView::OnInitialUpdate() 
{ 
    CView::OnInitialUpdate(); 

    enuCreateProject(); 

    // Load Project
    enuLoadProjectFile(L"Project\\sample.enup"); 

    // Create View
    ViewHandle = enuCreateView(this->m_hWnd); 

    // New Page Create. 
    CString strPicture = L"picture\\KoreaAIP.svg"; 
    HSVG SvgHandle = enuNewSvgPageFile(strPicture.GetBuffer(0)); 

    // ENU View Attach Set Page 
    enuSetSvgPageView(ViewHandle , strPicture.GetBuffer(0)); 

    // object create
    HNODE hnode = enuCreateRect(SvgHandle, L"MyObject", 0, 0, 100, 100, 0, 0);
    
    // Set Canvas Color
    enuSetCanvasColor(ViewHandle, 46, 46, 46);
}
```



