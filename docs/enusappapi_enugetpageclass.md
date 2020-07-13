---
layout: default
title: enuGetPageClass
parent: Application API
---
# void\* enuGetPageClass\(wchar\_t\* pStrFileName\)

void\* enuGetPageClass\(wchar\_t\* pStrFileName\)

#### Parameters

Type : wchar\_t\*

픽처의 파일이름을 입력합니다.

#### Return Value

none

#### Remarks

해당 픽쳐의 SVG 또는 X3D 핸들을 void\* 로 반환합니다.

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

    // view activate
    enuActivateView(ViewHandle );

    // New Page Create. 
    CString strPicture = L"picture\\KoreaAIP.svg"; 
    void* pHandle = enuGetPageClass(strPicture.GetBuffer(0)); 

    // ENU View Attach Set Page 
    enuSetSvgPageView(ViewHandle , strPicture.GetBuffer(0)); 
}
```



