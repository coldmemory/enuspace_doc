---
layout: default
title: enuSetViewID
parent: Application API
---
# void enuSetViewID\(HVIEW pENUView, wchar\_t\* strID\)

void enuSetViewID\(HVIEW pENUView, wchar\_t\* strID\)

#### Parameters

Type : HVIEW

뷰의 핸들을 전달합니다.

Type : wchar\_t\*

뷰의 ID를 전달합니다.

#### Return Value



#### Remarks

뷰를 조작하는 스크립트 함수들에서 뷰의 이름을 활용하여 스크립트를 작성합니다.

GetZoomScale\("window name"\), GetMoveCanvas\("window name"\) 등.

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

    // New Page Create. 
    CString strPicture = L"picture\\KoreaAIP.svg"; 
    HSVG SvgHandle = enuNewSvgPageFile(strPicture.GetBuffer(0)); 

    // ENU View Attach Set Page 
    enuSetSvgPageView(ViewHandle , strPicture.GetBuffer(0)); 
}
```



