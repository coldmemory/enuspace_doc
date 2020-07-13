---
layout: default
title: enuSaveX3DFile
parent: Application API
---
# bool enuSaveX3DFile\(HX3D pX3DHandler, wchar\_t\* strFileName = L""\)

bool enuSaveX3DFile\(HX3D pX3DHandler, wchar\_t\* strFileName = L""\)

#### Parameters

* HX3D pX3DHandler

X3D 핸들을 입력합니다.

* wchar\_t\* strFileName= L""

저장하고자하는 파일명을 입력합니다.

#### Return Value

Type : bool

X3D 파일의 정상 저장여부를 반환합니다.

#### Remarks

#### Examples

```cpp
HVIEW ViewHandle = NULL; 
HX3D pX3D = NULL;
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
    pX3D = enuGetX3DHandler(ViewHandle);

    // Create 3D Box.
    HNODE box = enuCreate3DBox(pX3D,"MyBox", 100, 0, 0, 0);        
}

void CSampleView::SaveSvg()
{
    enuSaveX3DFile(pX3D);
}
```



