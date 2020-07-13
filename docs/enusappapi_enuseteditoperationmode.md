---
layout: default
title: enuSetEditOperationMode
parent: Application API
---
# void enuSetEditOperationMode\(HVIEW pENUView, bool bFlag\)

void enuSetEditOperationMode\(HVIEW pENUView, bool bFlag\)

#### Parameters

Type : HVIEW

뷰 핸들을 전달합니다.

Type : bool

뷰의 편집모드를 지정합니다. \(true : 편집모드, false : 동작모드\)

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

    // edit mode unactivate.
    enuSetEditOperationMode(ViewHandle , false);

    // New Page Create. 
    CString strPicture = L"picture\\KoreaAIP.svg"; 
    HSVG SvgHandle = enuNewSvgPageFile(strPicture.GetBuffer(0)); 

    // ENU View Attach Set Page 
    enuSetSvgPageView(ViewHandle , strPicture.GetBuffer(0)); 
}
```



