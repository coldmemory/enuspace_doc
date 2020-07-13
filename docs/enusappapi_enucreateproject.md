---
layout: default
title: enuCreateProject
parent: Application API
---
# HPROJECT enuCreateProject\(\)

HPROJECT enuCreateProject\(\)

#### Parameters

NONE



#### Return Value

Type : HPROJECT

생성한 프로젝트의 핸들값이 반환된다.



#### Remarks

enuSpace 응용프로그램을 개발하기 위해서는 프로젝트를 생성하여야 한다.



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



