---
layout: default
title: enuDeleteObjectByNode
parent: Application API
---
# void enuDeleteObjectByNode\(HSVG pSvgHandler, HNODE pTarget\)

void enuDeleteObjectByNode\(HSVG pSvgHandler, HNODE pTarget\)

#### Parameters

* HSVG pSvgHandler

SVG 핸들을 입력합니다.

* HNODE pTarget

객체의 노드 핸들을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

객체의 노드 핸들을 이용하여 객체를 제거합니다.

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
    HNODE hnode = enuCreateRect(SvgHandle, L"MyObject", 0, 0, 100, 100, 0, 0);

    // delete object by name.
    enuDeleteObjectByNode(SvgHandle, hnode);
}
```



