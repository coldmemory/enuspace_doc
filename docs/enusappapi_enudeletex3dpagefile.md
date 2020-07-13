---
layout: default
title: enuDeleteX3dPageFile
parent: Application API
---
# bool enuDeleteX3dPageFile\(wchar\_t\* pStrFileName\)

bool enuDeleteX3dPageFile\(wchar\_t\* pStrFileName\)

#### Parameters

wchar\_t\* pStrFileName

제거할 X3D 파일이름을 입력합니다. \(ex "picture\\x3d\_picture.x3d"\)

#### Return Value

Type : bool

X3D 파일 제거 유무를 반환합니다.

#### Remarks

X3D 픽쳐파일을 제거합니다.

#### Examples

```cpp
HVIEW ViewHandle = NULL; 
void CSampleView::OnInitialUpdate() 
{ 
    CView::OnInitialUpdate(); 

    enuCreateProject(); 

    // Load Project
    enuLoadProjectFile(L"Project\\sample.enup"); 

    // x3d picture delete    
    enuDeleteX3dPageFile(L"picture\\core_3d.x3d");
}
```



