---
layout: default
title: enuCreateEllipse
parent: Application API
---
# HNODE enuCreateEllipse\(HSVG pSvgHandler, wchar\_t\* strID, float rx, float ry, float cx, float cy, float transx, float transy\)

HNODE enuCreateEllipse\(HSVG pSvgHandler, wchar\_t\* strID, float rx, float ry, float cx, float cy, float transx, float transy\)

#### Parameters

* HSVG pSvgHandler

2d svg 픽쳐 핸들을 입력합니다.

* wchar\_t\* strID

생성객체의 ID를 지정합니다.

* float rx

x축의 반지름값을 입력합니다.

* float ry

y축의 반지름값을 입력합니다.

* float cx

x축의 센터값을 입력합니다.

* float cy

y축의 센터값을 입력합니다.

* float transx

x축의 이동값을 입력합니다.

* float transy

y축의 이동값을 입력합니다.

#### Return Value

Type : HNODE

생성된 객체의 핸들을 반환합니다.

#### Remarks

동기식 호출을 통하여 타원 객체를 생성합니다. 생성된 객체의 속성을 변경하고자 하는 경우에는 enuSetAttribute\(\)함수를 이용합니다.

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
    HNODE hnode = enuCreateEllipse(SvgHandle, L"MyObject", 30, 10, 10, 0, 0);
}
```



