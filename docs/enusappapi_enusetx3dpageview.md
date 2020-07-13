---
layout: default
title: enuSetX3dPageView
parent: Application API
---
# bool enuSetX3dPageView\(HVIEW pENUView, wchar\_t\* pStrFileName\)

bool enuSetX3dPageView\(HVIEW pENUView, wchar\_t\* pStrFileName\)

#### Parameters

Type : HVIEW

뷰 핸들을 전달합니다.

Type : wchar\_t\*

뷰에 연결할 픽쳐 파일이름을 전달합니다.

#### Return Value

Type : bool

연결된 상태 정보를 반환합니다.

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



