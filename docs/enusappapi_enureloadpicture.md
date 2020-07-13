---
layout: default
title: enuReloadPicture
parent: Application API
---
# void enuReloadPicture\(HVIEW pENUView\)

void enuReloadPicture\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

픽쳐파일을 재로딩후 화면에 갱신한다.

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
    HNODE hnode = enuCreateLine(SvgHandle, L"MyObject", 50, 50, 100, 100, 0, 0);

    enuSaveAsSvgPageFile(strPicture, strPicture);
}

void RefreshEvent()
{
    if (view_handle)
        enuReloadPicture(view_handle);
}
```



