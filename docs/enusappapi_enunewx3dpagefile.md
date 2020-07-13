---
layout: default
title: enuNewX3DPageFile
parent: Application API
---
# HX3D enuNewX3DPageFile\(wchar\_t\* pStrFileName\)

HX3D enuNewX3DPageFile\(wchar\_t\* pStrFileName\)

#### Parameters

* wchar\_t\* pStrFileName

3D PICTURE영역의 새로운 X3D파일이름을 입력합니다.

#### Return Value

Type : HX3D

생성된 X3D핸들을 반환합니다.

#### Remarks

3D PICTURE영역에 새로운 X3D파일을 생성합니다.

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

    // New picture svg. 
    CString strPicture = L"picture\\user_3dpicture.x3d"; 
    HX3D x3d = enuNewX3DPageFile(strPicture.GetBuffer(0)); 
}
```



