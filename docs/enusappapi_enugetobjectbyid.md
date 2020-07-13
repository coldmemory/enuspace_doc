---
layout: default
title: enuGetObjectById
parent: Application API
---
# HNODE enuGetObjectById\(HSVG pSvgHandler, wchar\_t\* objectid\)

HNODE enuGetObjectById\(HSVG pSvgHandler, wchar\_t\* objectid\)

#### Parameters

* HSVG pSvgHandler

SVG 핸들을 입력합니다.

* wchar\_t\* objectid

객체의 ID를 입력합니다.

#### Return Value

Type : HNODE

해당하는 객체의 핸들을 반환받습니다. 해당하는 객체가 없는경우 NULL값을 반환합니다.

#### Remarks

ID를 이용하여 해당하는 개체의 핸들을 반환하는 함수입니다.

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
    HNODE hnode = enuCreateEllipse(SvgHandle, L"MyObject", 30, 10, 10, 0, 0);

    // hnode와 hSearchNode는 동일한 핸들.
    HNODE hSearchNode = enuGetObjectById(SvgHandle, L"MyObject");
}
```



