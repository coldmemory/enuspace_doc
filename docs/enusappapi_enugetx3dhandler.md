---
layout: default
title: enuGetX3DHandler
parent: Application API
---
# HX3D enuGetX3DHandler\(HVIEW pENUView\)

HX3D enuGetX3DHandler\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

3D 뷰의 핸들을 입력합니다.

#### Return Value

Type : HX3D

X3D 픽쳐의 핸들을 반환합니다.

#### Remarks

3D뷰로부터 연결된 X3D픽쳐의 핸들을 반환하는 함수입니다.

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
    HNODE cone = enuCreate3DCone(pX3D,"MyCone", 100, 100, 10, 0, 0, 0);        
}
```



