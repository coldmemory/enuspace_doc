---
layout: default
title: enuLoadSvgGlobalFile
parent: Application API
---
# HSVG enuLoadSvgGlobalFile\(wchar\_t\* pStrFileName\)

HSVG enuLoadSvgGlobalFile\(wchar\_t\* pStrFileName\)

#### Parameters

* wchar\_t\* pFileName

로드할 GLOBAL영역의 픽쳐이름을 입력합니다.

#### Return Value

Type : HSVG

로드된 GLOBAL픽쳐 핸들을 반환합니다.

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

    // global Load. 
    HSVG SvgHandle = enuLoadSvgGlobalFile(L"global\\user_global.svg");
}
```



