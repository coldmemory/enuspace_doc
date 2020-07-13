---
layout: default
title: enuGetX3dPageClass
parent: Application API
---
# HX3D enuGetX3dPageClass\(wchar\_t\* pStrFileName\)

HX3D enuGetX3dPageClass\(wchar\_t\* pStrFileName\)

#### Parameters

* wchar\_t\* pStrFileName

X3D 파일이름을 입력합니다.

#### Return Value

Type : HX3D

X3D핸들을 반환합니다.

#### Remarks

X3D핸들을 반환합니다.

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
    
    HX3D pX3DGet = enuGetX3dPageClass(L"picture\\core_3d.x3d"); // equal pX3D and pX3DGet  

}
```



