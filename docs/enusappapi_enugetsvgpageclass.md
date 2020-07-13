---
layout: default
title: enuGetSvgPageClass
parent: Application API
---
# HSVG enuGetSvgPageClass\(wchar\_t\* pStrFileName\)

HSVG enuGetSvgPageClass\(wchar\_t\* pStrFileName\)

#### Parameters

* wchar\_t\* pStrFileName

PICTURE영역의 픽쳐 SVG 파일이름을 입력합니다.

#### Return Value

Type : HSVG

해당 픽쳐파일의 핸들을 반환합니다.

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

    HSVG SvgGet = enuGetSvgPageClass(strPicture.GetBuffer(0));     // equal SvgHandle == SvgGet 
}
```



