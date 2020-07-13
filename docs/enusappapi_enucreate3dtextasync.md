---
layout: default
title: enuCreate3DTextAsync
parent: Application API
---
# void enuCreate3DTextAsync\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strString, wchar\_t\* strValue, float fontSize, float transx, float transy, float transz\)

void enuCreate3DTextAsync\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strString, wchar\_t\* strValue, float fontSize, float transx, float transy, float transz\)

#### Parameters

* HX3D pX3DHandler

3d 픽쳐 핸들을 입력합니다.

* wchar\_t\* strID

생성객체의 ID를 지정합니다.

* wchar\_t\* strString

3D Text객체의 문자열을 입력합니다.

* wchar\_t\* strValue

3d Text객체의 폰트 스타일을 입력합니다. "BOLD", "ITALIC", "BOLDITALIC"

* float fontSize

3d Text객체의 폰트 사이즈를 입력합니다.

* float transx

3d Text객체의 x축 이동값을 입력합니다.

* float transy

3d Text객체의 y축 이동값을 입력합니다.

* float transz

3d Text객체의 z축 이동값을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

3d 픽쳐 핸들을 이용하여 3d Text객체를 생성합니다.

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

    // Create 3D Text.
    enuCreate3DTextAsync(pX3D,L"MyObject", L"text label", L"BOLD", 30, 0, 0, 0);        // 비동기식 호출    
}
```



