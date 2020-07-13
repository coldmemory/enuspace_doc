---
layout: default
title: enuGetSvgHandler
parent: Application API
---
# HSVG enuGetSvgHandler\(HVIEW pENUView\)

HSVG enuGetSvgHandler\(HVIEW pENUView\)

#### Parameters

Type : HWND

윈도우 핸들을 전달합니다.

#### Return Value

Type : HSVG

뷰에 연결된 픽쳐파일의 핸들을 반환합니다.

#### Remarks

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

    // get picture handle
    HSVG hsvg = enuGetSvgHandler(ViewHandle )
}
```



