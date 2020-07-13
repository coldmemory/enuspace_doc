---
layout: default
title: enuDestoryView
parent: Application API
---
# void enuDestoryView\(HVIEW pENUView\)

void enuDestoryView\(HVIEW pENUView\)

#### Parameters

Type : HVIEW

2D뷰의 핸들을 전달합니다.

#### Return Value



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

void CSampleView::OnDestory()
{
    enuDestoryView(ViewHandle);
}
```



