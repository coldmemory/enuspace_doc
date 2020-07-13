---
layout: default
title: enuGetActiveProject
parent: Application API
---
# HPROJECT enuGetActiveProject\(\)

HPROJECT enuGetActiveProject\(\);

#### Parameters

NONE

 

#### Return Value

Type : HPROJECT

현재 활성화된 프로젝트 핸들을 반환한다.

#### 

#### Remarks

#### 

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



