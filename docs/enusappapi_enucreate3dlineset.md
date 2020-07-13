---
layout: default
title: enuCreate3DLineSet
parent: Application API
---
# HNODE enuCreate3DLineSet\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy, float transz\)

HNODE enuCreate3DLineSet\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy, float transz\)

#### Parameters

* HX3D pX3DHandler

3d 픽쳐 핸들을 입력합니다.

* wchar\_t\* strID

생성객체의 ID를 지정합니다.

* wchar\_t\* strPoints

3D LineSet객체의 포인트를 입력합니다.

* float transx

3d LineSet객체의 x축 이동값을 입력합니다.

* float transy

3d LineSet객체의 y축 이동값을 입력합니다.

* float transz

3d LineSet객체의 z축 이동값을 입력합니다.

#### Return Value

Type : HNODE

생성된 LineSet객체의 핸들을 반환합니다.

#### Remarks

3d 픽쳐 핸들을 이용하여 3d LineSet객체를 생성합니다.

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

    // Create 3D LineSet
    CString points = L"-10 -5 0 -9 -5 1 -8 -5 2 -7 -5 3 -6 -5 8 -5 -5 2 -4 -5 9 -3 -5 1 -2 -5 5 -1 -5 7 0 0 5 1 5 3 2 5 3 3 5 6 4 5 1 5 5 10 6 5 6 7 5 9 8 5 2 9 5 7 10 5 2";
    HNODE hnode = enuCreate3DLineSet(pX3D,L"MyObject", points.GetBuffer(0), 0, 0, 0);        // 동기식 호출    
}
```



