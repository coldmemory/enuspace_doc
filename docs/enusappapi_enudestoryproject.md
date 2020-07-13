---
layout: default
title: enuDestoryProject
parent: Application API
---
# void enuDestoryProject\(HPROJECT pProject\)

HPROJECT enuDesooryProject\(\)

#### Parameters

Type : HPROJECT

#### 

#### Return Value

NONE



#### Remarks

enuCreateProject\(\)로부터 생성된 HPROJECT를 이용하여 프로젝트를 제거한다.



#### Examples

```cpp
HPROJECT hProject = NULL;
HVIEW ViewHandle = NULL; 
void CSampleView::OnInitialUpdate() 
{ 
    CView::OnInitialUpdate(); 

    hProject = enuCreateProject(); 

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
    enuDestoryProject(hProject);
}
```



