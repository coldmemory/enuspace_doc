---
layout: default
title: enuShowDebugMessage
parent: Application API
---
# void enuShowDebugMessage\(bool bShow\)

void enuShowDebugMessage\(bool bShow\)

#### Parameters

Type : bool

디버그창의 디스플레이 플래그를 지정합니다. \(true : 보이기, false : 안 보이기\)

#### Return Value

NONE

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

    // Debug window show.
    enuShowDebugMessage(true);
    
    // Create View
    ViewHandle = enuCreateView(this->m_hWnd); 

    // New Page Create. 
    CString strPicture = L"picture\\KoreaAIP.svg"; 
    HSVG SvgHandle = enuNewSvgPageFile(strPicture.GetBuffer(0)); 

    // ENU View Attach Set Page 
    enuSetSvgPageView(ViewHandle , strPicture.GetBuffer(0)); 
}
```



