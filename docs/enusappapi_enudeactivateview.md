---
layout: default
title: enuDeactivateView
parent: Application API
---
# void enuDeactivateView\(HVIEW pENUView\)

void enuDeactivateView\(HVIEW pENUView\)

#### Parameters

Type : HVIEW

뷰 핸들을 전달합니다.



#### Return Value

#### Remarks

비 활성화된 뷰는 taskview\(\) 스크립트 함수가 동작하지 않습니다.

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

    // default mouse wheel control set.
    enuSetDefaultWheelControl(ViewHandle , true);

    // deactivate view
    enuDeactivateView(ViewHandle );
    
    // New Page Create. 
    CString strPicture = L"picture\\KoreaAIP.svg"; 
    HSVG SvgHandle = enuNewSvgPageFile(strPicture.GetBuffer(0)); 

    // ENU View Attach Set Page 
    enuSetSvgPageView(ViewHandle , strPicture.GetBuffer(0)); 
}
```



