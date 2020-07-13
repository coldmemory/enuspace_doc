---
layout: default
title: enuCreateUse
parent: Application API
---
# HNODE enuCreateUse\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, wchar\_t\* xlink\_href, wchar\_t\* strType, float transx = 0, float transy = 0\)

HNODE enuCreateUse\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, wchar\_t\* xlink\_href, wchar\_t\* strType, float transx = 0, float transy = 0\)

#### Parameters

* HSVG pSvgHandler

2d svg 픽쳐 핸들을 입력합니다.

* wchar\_t\* strID

생성객체의 ID를 지정합니다.

* float x

x축의 값을 입력합니다.

* float y

y축의 값을 입력합니다.

* wchar\_t\* xlink\_href

정의된 심볼이름을 입력합니다. \(ex. \#ID\_GAUGE\)

* wchar\_t\* strType

정의된 심볼의 타입을 입력합니다. \(hmi, logic\)

* float transx

x축의 이동값을 입력합니다.

* float transy

y축의 이동값을 입력합니다.

#### Return Value

Type : HNODE  
생성된 객체의 핸들을 반환합니다.

#### Remarks

동기식 호출을 통하여 동적으로 Use객체를 생성합니다. 생성된 객체의 속성을 변경하고자 하는 경우에는 enuSetAttribute\(\) 함수를 이용합니다.

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
    HNODE hnode = enuCreateUse(SvgHandle, L"MyObject", "#ID_GAUGE", "hmi", 300, 300);
}
```



