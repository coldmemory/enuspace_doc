---
layout: default
title: enuSetSvgExternalPageView
parent: Application API
---
# bool enuSetSvgExternalPageView\(HVIEW pENUView, HSVG pSvg\)

bool enuSetSvgExternalPageView\(HVIEW pENUView, HSVG pSvg\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

* HSVG pSvg

SVG 핸들을 입력합니다.

#### Return Value

Type :

#### Remarks

External용 SVG핸들을 뷰에 적용합니다. External SVG 프로젝트 저장시 프로젝트에 포함되지 않으며, 런타임중에 로드되거나 생성되어 적용됩니다.

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



