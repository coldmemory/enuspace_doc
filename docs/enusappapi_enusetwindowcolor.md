---
layout: default
title: enuSetWindowColor
parent: Application API
---
# void enuSetWindowColor\(HVIEW pENUView, byte iR, byte iG, byte iB\)

void enuSetWindowColor\(HVIEW pENUView, byte iR, byte iG, byte iB\)

#### Parameters

Type : HVIEW

뷰의 핸들을 전달합니다.

Type : byte iR, byte iG, byte iB

윈도우의 색상값을 지정합니다.

#### Return Value



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
    
    // View Color Set
    enuSetWindowColor(m_pMainView, 46, 46, 46);
}
```



