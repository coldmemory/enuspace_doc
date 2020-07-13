---
layout: default
title: enuSetSvgView
parent: Application API
---
# bool enuSetSvgView\(HVIEW pENUView, HSVG pSvg\)

bool enuSetSvgView\(HVIEW pENUView, HSVG pSvg\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

* HSVG pSvg

SVG 핸들을 입력합니다.

#### Return Value

Type : bool

정상적으로 뷰에 SVG핸들이 적용되었는지를 반환합니다.

#### Remarks

뷰와 SVG핸들을 이용하여 디스플레이를 수행합니다.

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
    enuSetSvgView(ViewHandle, SvgHandle);
    // or
    // enuSetSvgPageView(ViewHandle , strPicture.GetBuffer(0)); 

    // object create
    HNODE hnode = enuCreateEllipse(SvgHandle, L"MyObject", 30, 10, 10, 0, 0);
}
```



