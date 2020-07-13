---
layout: default
title: enuLoadSvgExternalPageFile
parent: Application API
---
# HSVG enuLoadSvgExternalPageFile\(wchar\_t\* pFileName\)

HSVG enuLoadSvgExternalPageFile\(wchar\_t\* pFileName\)

#### Parameters

* wchar\_t\* pFileName

로드할 external용 픽쳐이름을 입력합니다.

#### Return Value

Type : HSVG

로드된 external 픽쳐 핸들을 반환합니다.

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

    // External Page Load. 
    HSVG SvgHandle = enuLoadSvgExternalPageFile(L"picture\\external_pic.svg");

    // ENU View Attach Set External Page 
    enuSetSvgExternalPageView(ViewHandle , SvgHandle); 
}
```



