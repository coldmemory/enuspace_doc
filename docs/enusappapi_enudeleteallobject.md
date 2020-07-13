---
layout: default
title: enuDeleteAllObject
parent: Application API
---
# void enuDeleteAllObject\(HSVG pSvgHandler\)

void enuDeleteAllObject\(HSVG pSvgHandler\)

#### Parameters

* HSVG pSvgHandler

2D SVG핸들을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

SVG 픽쳐에 존재하는 모든 노드를 제거합니다.

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
    HNODE hnode = enuCreateCircle(SvgHandle, L"MyObject", 30, 10, 10, 0, 0);

    // delete all object
    enuDeleteAllObject(SvgHandle);
}
```



