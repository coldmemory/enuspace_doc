---
layout: default
title: enuDeleteUseObjectByHref
parent: Application API
---
# void enuDeleteUseObjectByHref\(HSVG pSvgHandler, wchar\_t\* pStrHref\)

void enuDeleteUseObjectByHref\(HSVG pSvgHandler, wchar\_t\* pStrHref\)

#### Parameters

* HSVG pSvgHandler

SVG 핸들을 입력합니다.

* wchar\_t\* pStrHref

심볼의 이름을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

SVG 핸들에 특정 심볼을 모두 제거하는 함수입니다. 

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
    enuSetSvgPageView(ViewHandle , strPicture.GetBuffer(0)); 

    // object create
    HNODE hnode1 = enuCreateUse(SvgHandle, L"MyObject1", "#ID_GAUGE", "hmi", 300, 300);
    HNODE hnode2 = enuCreateUse(SvgHandle, L"MyObject2", "#ID_GAUGE", "hmi", 300, 300);   
    
    enuDeleteUseObjectByHref(SvgHandle, L"#ID_GAUGE");
}
```



