---
layout: default
title: enuCreate3DView
parent: Application API
---
# HVIEW enuCreate3DView\(HWND hWnd\)

HVIEW enuCreate3DView\(HWND hWnd\)

#### Parameters

Type : HWND

윈도우 핸들을 전달합니다.

#### Return Value

Type : HVIEW

생성된 뷰의 핸들을 반환합니다.

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

    // ENU View Attach Set Page 
    enuSetX3dPageView(ViewHandle , L"picture\\core_3d.x3d");
}
```



