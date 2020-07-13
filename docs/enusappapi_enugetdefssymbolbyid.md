---
layout: default
title: enuGetDefsSymbolById
parent: Application API
---
# HNODE enuGetDefsSymbolById\(HSVG pSvgHandler, wchar\_t\* objectid\)

HNODE enuGetDefsSymbolById\(HSVG pSvgHandler, wchar\_t\* objectid\)

#### Parameters

HSVG pSvgHandler : 로직 및 HMI 라이브러리 픽쳐의 핸들을 입력합니다.

wchar\_t\* objectid : 취득하고자하는 심볼의 ID를 입력합니다.

#### Return Value

HNODE

해당객체의 노드를 반환합니다.

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

    // edit mode unactivate.
    enuSetEditOperationMode(ViewHandle , false);

    // default mouse wheel control set.
    enuSetDefaultWheelControl(ViewHandle , true);

    // view activate
    enuActivateView(ViewHandle );

    // New Page Create. 
    CString strPicture = L"library\\logic\\logic.svg"; 
    HSVG hsvg = enuGetLogicClass(strPicture.GetBuffer(0));
    if (hsvg)
    {
        HNODE hnode = enuGetDefsSymbolById(hsvg, L"AND_LOGIC");
        if (hnode)
        {
            enuSetAttributeByNode(hsvg, hnode, L"id", L"AND_CU"); 
        }
    }
}
```



