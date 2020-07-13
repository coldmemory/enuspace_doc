---
layout: default
title: enuSetWindowPos
parent: Application API
---
# void enuSetWindowPos\(HVIEW pENUView, int x, int y, int cx, int cy\)

void enuSetWindowPos\(HVIEW pENUView, int x, int y, int cx, int cy\)

#### Parameters

Type : HVIEW

뷰의 핸들을 전달합니다.

Type : int x, int y, int cx, int cy

뷰의 좌표와 width, height 값을 전달합니다.

#### Return Value



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

    // View ID set
    enuSetViewID(ViewHandle , L"window");

    // View Position set
    RECT rect;
    GetClientRect(&rect);
    enuSetWindowPos(ViewHandle , rect.left, rect.top, rect.right, rect.bottom);

    // New Page Create. 
    CString strPicture = L"picture\\KoreaAIP.svg"; 
    HSVG SvgHandle = enuNewSvgPageFile(strPicture.GetBuffer(0)); 

    // ENU View Attach Set Page 
    enuSetSvgPageView(ViewHandle , strPicture.GetBuffer(0)); 
}
```



