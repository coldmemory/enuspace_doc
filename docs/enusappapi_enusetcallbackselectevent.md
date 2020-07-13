---
layout: default
title: enuSetCallBackSelectEvent
parent: Application API
---
# void enuSetCallBackSelectEvent\(void fcbSelectObject\(CPtrList\*, void\*\)\)

void enuSetCallBackSelectEvent\(void fcbSelectObject\(CPtrList\*, void\*\)\)

#### Parameters

* void fcbSelectObject\(CPtrList\*, void\*\)

선택 객체의 정보를 받고자하는 함수 포인터를 지정합니다.

#### Return Value

Type : NONE

#### Remarks

뷰로부터 객체 선택시, 선택객체의 정보를 받고자하는 함수 포인터를 지정합니다.

#### Examples

```cpp
void SelectObjectCallBack(CPtrList* pSelectList, void* pObject)
{
    if (pSelectList)
    {
        int iCount = pSelectList->GetCount();
        if (iCount == 1)
        {
            POSITION pos = pSelectList->GetHeadPosition();
            if (pos)
            {
                CSvgNodeBase* pData = (CSvgNodeBase  *)pSelectList->GetAt(pos);

                if (g_pMainFrame)
                    g_pMainFrame->SendCommand(ID_PROPERTY_VIEW, pData, NULL);
            }
        }
        else if (iCount == 0)            
        {
            if (g_pMainFrame)
                g_pMainFrame->SendCommand(ID_PROPERTY_VIEW, NULL, NULL);
        }
    }
    else
    {
        if (g_pMainFrame)
        {
            g_pMainFrame->SendCommand(ID_PROPERTY_VIEW, pObject, NULL);
        }
    }
}

HVIEW ViewHandle = NULL; 
void CSampleView::OnInitialUpdate() 
{ 
    CView::OnInitialUpdate(); 

    enuCreateProject(); 

    // Load Project
    enuLoadProjectFile(L"Project\\sample.enup"); 

    enuSetCallBackSelectEvent(SelectObjectCallBack);

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



