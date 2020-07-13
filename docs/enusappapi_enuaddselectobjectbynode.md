---
layout: default
title: enuAddSelectObjectByNode
parent: Application API
---
# void enuAddSelectObjectByNode\(HVIEW pENUView, HNODE hNode\)

void enuAddSelectObjectByNode\(HVIEW pENUView, HNODE hNode\)

#### Parameters

* HVIEW pENUView

2D Render View의 핸들을 입력합니다.

* HNODE hNode

선택하고자하는 노드의 핸들을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

2D View에 특정 객체를 선택 리스트에 추가합니다. 선택된 객체를 이용시 적용합니다.

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

    HNODE hnode = enuCreateRect(ViewHandle, L"MYRECT", 0, 0, 100, 100, 0, 0);  
    enuAddSelectObjectByNode(ViewHandle, hnode);
}
```



