---
layout: default
title: enuSetActiveProject
parent: Application API
---
# bool enuSetActiveProject\(HPROJECT pHANDLE\)

bool enuSetActiveProject\(HPROJECT pHANDLE\);

#### 

#### Parameters

Type : HPROJECT

#### 

#### Return Value

Type : bool

여러개의 프로젝트중 활성화 하고자하는 프로젝트가 정상적으로 활성화 여부를 반환한다.

#### 

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



