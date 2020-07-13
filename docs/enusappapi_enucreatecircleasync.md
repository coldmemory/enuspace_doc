---
layout: default
title: enuCreateCircleAsync
parent: Application API
---
# void enuCreateCircleAsync\(HSVG pSvgHandler, wchar\_t\* strID, float r, float cx, float cy, float transx, float transy\)

void enuCreateCircleAsync\(HSVG pSvgHandler, wchar\_t\* strID, float r, float cx, float cy, float transx, float transy\)

#### Parameters

* HSVG pSvgHandler

2d svg 픽쳐 핸들을 입력합니다.

* wchar\_t\* strID

생성객체의 ID를 지정합니다.

* float r

객체의 반지름을 입력합니다.

* float cx

센터포인터 x값을 입력합니다.

* float cy

센터포인트 y값을 입력합니다.

* float transx

x축의 이동값을 입력합니다.

* float transy

y축의 이동값을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

스크립트를 이용하여 동적으로 원 객체를 생성합니다. 생성된 객체의 속성을 변경하고자 하는 경우에는 enuSetAttribute\(\) 함수를 이용합니다.

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
    ViewHandle = enuCreateView(this->m_hWnd); 

    // New Page Create. 
    CString strPicture = L"picture\\KoreaAIP.svg"; 
    HSVG SvgHandle = enuNewSvgPageFile(strPicture.GetBuffer(0)); 

    // ENU View Attach Set Page 
    enuSetSvgPageView(ViewHandle , strPicture.GetBuffer(0)); 

    // object create
    enuCreateCircleAsync(SvgHandle, L"MyObject", 30, 10, 10, 0, 0);
}
```



