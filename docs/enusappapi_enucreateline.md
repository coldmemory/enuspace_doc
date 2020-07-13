---
layout: default
title: enuCreateLine
parent: Application API
---
# HNODE enuCreateLine\(HSVG pSvgHandler, wchar\_t\* strID, float x1, float y1, float x2, float y2, float transx, float transy\)

HNODE enuCreateLine\(HSVG pSvgHandler, wchar\_t\* strID, float x1, float y1, float x2, float y2, float transx, float transy\)

#### Parameters

* HSVG pSvgHandler

2d svg 픽쳐 핸들을 입력합니다.

* wchar\_t\* strID

생성객체의 ID를 지정합니다.

* float x1

첫번째 x의 좌표를 입력합니다.

* float y1

첫번째 y의 좌표를 입력합니다.

* float x2

두번째 x의 좌표를 입력합니다.

* float y2

두번째 y의 좌표를 입력합니다.

* float transx

x축의 이동값을 입력합니다.

* float transy

y축의 이동값을 입력합니다.

#### Return Value

Type : HNODE  
생성된 객체의 핸들을 반환합니다.

#### Remarks

동기식 방법으로  동적 라인 객체를 생성합니다. 생성된 객체의 속성을 변경하고자 하는 경우에는 enuSetAttribute\(\) 함수를 이용합니다.

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
    HNODE hnode = enuCreateLine(SvgHandle, L"MyObject", 50, 50, 100, 100, 0, 0);
}
```



