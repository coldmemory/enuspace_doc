---
layout: default
title: enuSetCallBackDebugMessage
parent: Application API
---
# void enuSetCallBackDebugMessage\(void fcbDebugMessage\(wchar\_t\*\)\)

void enuSetCallBackDebugMessage\(void fcbDebugMessage\(wchar\_t\*\)\)

#### Parameters

* void fcbDebugMessage\(wchar\_t\*\)

디버그 메세지정보를 받을 함수 포인터를 설정합니다.

#### Return Value

Type : NONE

#### Remarks

디버그 메세지를 받고자하는 경우 함수포인터를 지정합니다.

#### Examples

```cpp
void DebugMessageCallBack(wchar_t* pStrMessage, wchar_t* pStrParam)
{
    if (g_pMainFrame)
    {
        if (g_pMainFrame->m_bMainThread)
            g_pMainFrame->SendCommand(ID_DEBUG_MESSAGE, pStrMessage, pStrParam);
    }
}

HVIEW ViewHandle = NULL; 
void CSampleView::OnInitialUpdate() 
{ 
    CView::OnInitialUpdate(); 

    enuCreateProject(); 

    // Load Project
    enuLoadProjectFile(L"Project\\sample.enup"); 

    enuSetCallBackDebugMessage(DebugMessageCallBack);

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



