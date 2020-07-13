---
layout: default
title: enuGetCanvasWidth
parent: Application API
---
# float enuGetCanvasWidth\(HVIEW pENUView\)

float enuGetCanvasWidth\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

2D 뷰의 핸들을 입력합니다.

#### Return Value

Type : float

켄버스의 넖이값을 반환받습니다.

#### Remarks

뷰의 핸들을 통하여 켄버의 넖이값을 반환받는 함수입니다.

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

    float fHeight = enuGetCanvasHeight(ViewHandle);
    float fWidth = enuGetCanvasWidth(ViewHandle);

}
```



