---
layout: default
title: enuSetCanvasSize
parent: Application API
---
# void enuSetCanvasSize\(HVIEW pENUView, float cx, float cy\)

void enuSetCanvasSize\(HVIEW pENUView, float cx, float cy\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

* float cx

켄버스의 넓이를 지정합니다.

* float cy

켄버스의 높이를 지정합니다.

#### Return Value

Type : NONE

#### Remarks

켄버스의 사이즈를 지정하는 함수입니다.

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
    
    // Set Canvas Size
    enuSetCanvasSize(ViewHandle, 1920, 1080);

}
```



