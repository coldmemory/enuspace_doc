---
layout: default
title: enuDelete3DObjectByNode
parent: Application API
---
# void enuDelete3DObjectByNode\(HX3D pX3DHandler, HNODE pTarget\)

void enuDelete3DObjectByNode\(HX3D pX3DHandler, HNODE pTarget\)

#### Parameters

* HX3D pX3DHandler

3d X3D 핸들을 입력합니다.

* HNODE pTarget

제거하고자하는 객체의 노드를 입력합니다.

#### Return Value

Type : NONE

#### Remarks

3차원 객체의 핸들을 이용하여 노드를 제거합니다.

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
    ViewHandle = enuCreate3DView(this->m_hWnd); 

    // ENU View Attach Set Page 
    enuSetX3dPageView(ViewHandle , L"picture\\core_3d.x3d");

    // Get X3D picture handle
    HX3D pX3D = enuGetX3DHandler(ViewHandle);

    // Create 3D Box.
    HNODE box = enuCreate3DBox(pX3D,"MyBox", 100, 0, 0, 0);  
    
    // Delete 3D Box.
    enuDelete3DObjectByNode(pX3D, box);
}
```



