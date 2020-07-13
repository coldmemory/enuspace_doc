---
layout: default
title: enuLoadX3DPageFile
parent: Application API
---
# HSVG enuLoadX3DPageFile\(wchar\_t\* pStrFileName\)

HX3D enuLoadX3DPageFile\(wchar\_t\* pStrFileName\)

#### Parameters

* wchar\_t\* pFileName

로드할 PICTURE영역의 픽쳐이름을 입력합니다.

#### Return Value

Type : HX3D

로드된 X3D PICTURE픽쳐 핸들을 반환합니다.

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
    ViewHandle = enuCreate3DView(this->m_hWnd); 

    // Page Load. 
    HX3D X3DHandle = enuLoadX3DPageFile(L"picture\\picture_x3d.x3d");
}
```



