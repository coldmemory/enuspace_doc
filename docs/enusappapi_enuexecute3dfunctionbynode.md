---
layout: default
title: enuExecute3DFunctionByNode
parent: Application API
---
# void enuExecute3DFunctionByNode\(HX3D pX3D, HNODE pNode, wchar\_t\* strFunction\)

void enuExecute3DFunctionByNode\(HX3D pX3D, HNODE pNode, wchar\_t\* strFunction\)

#### Parameters

HX3D pX3D :X3D 픽쳐 핸들러를 지정합니다.

HNODE pNode : 픽쳐 내부의 NODE 핸들러를 지정합니다.

wchar\_t\* strFunction : 픽쳐파일 내부의 함수를 지정합니다.

#### Return Value

none

#### Remarks

X3D 핸들정보와 객체의 NODE정보를 이미 알고있는 경우에는 직접 호출하여 함수를 수행합니다.

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
    m_p3DView = enuCreate3DView(this->m_hWnd);
    enuSetX3dPageView(m_p3DView, L"picture\\core_3d.x3d");

    HX3D hX3D = enuGetX3DHandler(m_p3DView);
    HNODE hNode = enuCreate3DBox(hX3D, L"ID_BOX", 30, 0, 0, 50);

    enuExecute3DFunctionByNode(hX3D, hNode , L"_onmousedown()"); 
}
```



