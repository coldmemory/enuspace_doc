---
layout: default
title: enuCreateView
parent: Application API
---
#  HVIEW enuCreateView\(HWND hWnd\)

 HVIEW enuCreateView\(HWND hWnd\)

#### Parameters

Type : HWND

윈도우 핸들을 전달합니다.

#### Return Value

Type : HVIEW

생성된 뷰의 핸들을 반환합니다.

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
}
```



