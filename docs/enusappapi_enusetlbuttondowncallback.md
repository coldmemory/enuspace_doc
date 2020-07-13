---
layout: default
title: enuSetLButtonDownCallBack
parent: Application API
---
# void enuSetLButtonDownCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)

void enuSetLButtonDownCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

* void functioncb\(float, float\)

마우스 LButton Down이벤트를 받고자 하는 함수의 포인터를 지정합니다.

#### Return Value

Type : NONE

#### Remarks

뷰의 마우스 LButton Down이벤트 신호를 받고자 하는 경우, 함수 포인터를 지정합니다.

#### Examples

```cpp
HVIEW ViewHandle = NULL; 

void MouseLButtonDown(float posx, float posy)
{
    HSVG pSvg = enuGetSvgHandler(ViewHandle);
    HNODE hnode = enuGetSelectSingleObject(ViewHandle);

    if (hnode )
    {
        // TO DO JOB
    }
}

void CSampleView::OnInitialUpdate() 
{ 
    CView::OnInitialUpdate(); 

    enuCreateProject(); 

    // Load Project
    enuLoadProjectFile(L"Project\\sample.enup");     

    // Create View
    ViewHandle = enuCreateView(this->m_hWnd); 

    enuSetLButtonDownCallBack(ViewHandle, MouseLButtonDown);

    // New Page Create. 
    CString strPicture = L"picture\\KoreaAIP.svg"; 
    HSVG SvgHandle = enuNewSvgPageFile(strPicture.GetBuffer(0)); 

    // ENU View Attach Set Page 
    enuSetSvgPageView(ViewHandle , strPicture.GetBuffer(0)); 

    // object create
    HNODE hnode = enuCreateRect(SvgHandle, L"MyObject", 0, 0, 100, 100, 0, 0);
}
```



