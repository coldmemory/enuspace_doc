---
layout: default
title: enuLoadSvgPageFile
parent: Application API
---
# HSVG enuLoadSvgPageFile\(wchar\_t\* pStrFileName\)

HSVG enuLoadSvgPageFile\(wchar\_t\* pStrFileName\)

#### Parameters

* wchar\_t\* pFileName

로드할 PICTURE영역의 픽쳐이름을 입력합니다.

#### Return Value

Type : HSVG

로드된 PICTURE픽쳐 핸들을 반환합니다.

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

    // Page Load. 
    HSVG SvgHandle = enuLoadSvgLogicFile(L"picture\\picture.svg");
}
```



