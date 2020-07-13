---
layout: default
title: enuSetCallBackSelectToolBar
parent: Application API
---
# void enuSetCallBackSelectToolBar\(void fcbSelectToolBar\(int\)\)

void enuSetCallBackSelectToolBar\(void fcbSelectToolBar\(int\)\)

#### Parameters

* void fcbSelectToolBar\(int\)

2D 객체 생성을 위한 툴바 선택 신호를 받고자하는 경우, 함수포인터를 지정합니다.

#### Return Value

Type : NONE

#### Remarks

2D 객체 생성을 위한 툴바 선택 신호를 받고자하는 경우, 함수포인터를 지정합니다.

#### Examples

```cpp
void SelectToolBarCallBack(int iSel)
{
	if (g_pMainFrame)
		g_pMainFrame->SetSelectToolBar(iSel, false);
}

HVIEW ViewHandle = NULL; 
void CSampleView::OnInitialUpdate() 
{ 
    CView::OnInitialUpdate(); 

    enuCreateProject(); 

    // Load Project
    enuLoadProjectFile(L"Project\\sample.enup"); 

    enuSetCallBackSelectToolBar(SelectToolBarCallBack);

    // Create View
    ViewHandle = enuCreateView(this->m_hWnd); 

    // New Page Create. 
    CString strPicture = L"picture\\KoreaAIP.svg"; 
    HSVG SvgHandle = enuNewSvgPageFile(strPicture.GetBuffer(0)); 

    // ENU View Attach Set Page 
    enuSetSvgPageView(ViewHandle , strPicture.GetBuffer(0)); 

    // object create
    HNODE hnode = enuCreateRect(SvgHandle, L"MyObject", 0, 0, 100, 100, 0, 0);
}
```



