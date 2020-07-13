---
layout: default
title: enuExecute3DFunction
parent: Application API
---
# void enuExecute3DFunction\(HX3D pX3D, wchar\_t\* strFunction\)

void enuExecute3DFunction\(HX3D pX3D, wchar\_t\* strFunction\)

#### Parameters

HX3D pX3D : 3d 픽쳐 페이지 핸들을 지정합니다.

wchar\_t\* strfunction : 픽쳐파일 내부의 함수를 지정합니다.

#### Return Value

none

#### Remarks

픽쳐에서 구현된 함수를 호출합니다. 객체의 함수를 호출할 경우에는 ID\_BOX.UserFunction\(\)형태로 호출합니다.

X3D상의 노드에서 구현된 함수는 객체의 ID정보없이 UserFunction\(\)형태로 호출합니다.

#### Examples

```cpp
HVIEW m_p3DView = NULL; 
void CSampleView::OnInitialUpdate() 
{ 
    CView::OnInitialUpdate(); 

    enuCreateProject(); 

    // Load Project
    enuLoadProjectFile(L"Project\\sample.enup"); 

    // Create View
    m_p3DView = enuCreate3DView(this->m_hWnd);
    enuSetX3dPageView(m_p3DView, L"picture\\core_3d.x3d");

    HX3D hX3D = enuGetX3DHandler(m_p3DView);
    
    // picture page의 _onload() function call    
    enuExecute3DFunction(hX3D, L"_onload()"); 
    
    // picture 내부 객체 function call
    enuExecute3DFunction(hX3D, L"ID_BOX._onmousedown()");           
}
```



