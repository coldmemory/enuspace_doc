---
layout: default
title: enuCreate3DBoxAsync
parent: Application API
---
# void enuCreate3DBoxAsync\(HX3D pX3DHandler, wchar\_t\* strID, float size, float transx, float transy, float transz\)

void enuCreate3DBoxAsync\(HX3D pX3DHandler, wchar\_t\* strID, float size, float transx, float transy, float transz\)

#### Parameters

* HX3D pX3DHandler

3d 픽쳐 핸들을 입력합니다.

* wchar\_t\* strID

생성객체의 ID를 지정합니다.

* float size

박스의 사이즈를 지정합니다.

* float transx

박스의 x축 이동값을 입력합니다.

* float transy

박스의 y축 이동값을 입력합니다.

* float transz

박스의 z축 이동값을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

3d 픽쳐 핸들을 이용하여 3d box 객체를 생성합니다.

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

    // Create 3D Box.
    enuCreate3DBoxAsync(pX3D,L"MyBox", 100, 0, 0, 0);        // 비동기식 호출    
}
```



