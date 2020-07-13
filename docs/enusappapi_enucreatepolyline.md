---
layout: default
title: enuCreatePolyline
parent: Application API
---
# HNODE enuCreatePolyline\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy\)

HNODE enuCreatePolyline\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy\)

#### Parameters

* HSVG pSvgHandler

2d svg 픽쳐 핸들을 입력합니다.

* wchar\_t\* strID

생성객체의 ID를 지정합니다.

* wchar\_t\* pStrPoints

패스정보 포인트를 입력합니다. \(ex : "0,0 90,-34 133,-4 179,-35 243,-3 127,40."\)

* float transx

x축의 이동값을 입력합니다.

* float transy

y축의 이동값을 입력합니다.

#### Return Value

Type : HNODE  
생성된 객체의 핸들을 반환합니다.

#### Remarks

동기식 방법으로  동적 폴리라인 객체를 생성합니다. 생성된 객체의 속성을 변경하고자 하는 경우에는 enuSetAttribute\(\) 함수를 이용합니다.

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
    HNODE hnode = enuCreatePolyline(SvgHandle, L"MyObject", "0,0 90,-34 133,-4 179,-35 243,-3 127,40.", 0, 0);
}
```



