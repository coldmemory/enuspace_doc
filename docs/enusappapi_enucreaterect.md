---
layout: default
title: enuCreateRect
parent: Application API
---
# HNODE enuCreateRect\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, float transx, float transy\)

HNODE enuCreateRect\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, float transx, float transy\)

#### Parameters

* HSVG pSvgHandler

2d svg 픽쳐 핸들을 입력합니다.

* wchar\_t\* strID

생성객체의 ID를 지정합니다.

* float x

x축의 값을 입력합니다.

* float y

y축의 값을 입력합니다.

* float width

폭값을 입력합니다.

* float height

높이값을 입력합니다.

* float transx

x축의 이동값을 입력합니다.

* float transy

y축의 이동값을 입력합니다.

#### Return Value

Type : HNODE  
생성된 객체의 핸들을 반환합니다.

#### Remarks

동기식 호출을 통하여 동적으로 사각형 객체를 생성합니다. 생성된 객체의 속성을 변경하고자 하는 경우에는 enuSetAttribute\(\) 함수를 이용합니다.

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
    HNODE hnode = enuCreateRect(SvgHandle, L"MyObject", 0, 0, 100, 100, 0, 0);
}
```



