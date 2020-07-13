---
layout: default
title: enuSetSvgPageView
parent: Application API
---
# bool enuSetSvgPageView\(HVIEW pENUView, wchar\_t\* pStrFileName\)

bool enuSetSvgPageView\(HVIEW pENUView, wchar\_t\* pStrFileName\)

#### Parameters

Type : HVIEW

뷰 핸들을 전달합니다.

Type : wchar\_t\* 

뷰에 연결할 픽쳐 파일이름을 전달합니다. 



#### Return Value

Type : bool

연결된 상태 정보를 반환합니다.

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

    // ENU View Attach Set Page 
    enuSetSvgPageView(ViewHandle , strPicture.GetBuffer(0)); 
}
```



