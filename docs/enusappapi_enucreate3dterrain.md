---
layout: default
title: enuCreate3DTerrain
parent: Application API
---
# HNODE enuCreate3DTerrain\(HX3D pX3DHandler, wchar\_t\* strID, float size, float subdivision, float transx, float transy, float transz\)

HNODE enuCreate3DTerrain\(HX3D pX3DHandler, wchar\_t\* strID, float size, float subdivision, float transx, float transy, float transz\)

#### Parameters

* HX3D pX3DHandler

3d 픽쳐 핸들을 입력합니다.

* wchar\_t\* strID

생성객체의 ID를 지정합니다.

* float size

3D Terrain객체의 반지름을 입력합니다.

* float subdivision

3d Terrain객체의 slice개수를 입력합니다.

* float transx

3d Terrain객체의 x축 이동값을 입력합니다.

* float transy

3d Terrain객체의 y축 이동값을 입력합니다.

* float transz

3d Terrain객체의 z축 이동값을 입력합니다.

#### Return Value

Type : HNODE

Terrain객체의 핸들을 반환합니다.

#### Remarks

3d 픽쳐 핸들을 이용하여 3d Terrain객체를 생성합니다.

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

    // Create 3D Terrain.
    HNODE hnode = enuCreate3DTerrain(pX3D,L"MyObject", 100, 10, 0, 0, 0);        // 동기식 호출    
}
```



