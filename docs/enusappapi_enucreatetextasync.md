---
layout: default
title: enuCreateTextAsync
parent: Application API
---
# void enuCreateTextAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float dx, float dy, wchar\_t\* text, float transx, float transy\)

void enuCreateTextAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float dx, float dy, wchar\_t\* text, float transx, float transy\)

#### Parameters

* HSVG pSvgHandler

2d svg 픽쳐 핸들을 입력합니다.

* wchar\_t\* strID

생성객체의 ID를 지정합니다.

* float x

x의 좌표를 입력합니다.

* float y

y의 좌표를 입력합니다.

* float dx

dx의 값을 입력합니다.

* float dy

dy의 값을 입력합니다.

* wchar\_t\* text

문자열 값을 입력합니다.

* float transx

x축의 이동값을 입력합니다.

* float transy

y축의 이동값을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

비동기식 호출을 통하여 동적으로 문자 객체를 생성합니다. 

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
    enuCreateTextAsync(SvgHandle, L"MyObject", 0, 0, 100, 100, L"Input the Text", 0, 0);
}
```



