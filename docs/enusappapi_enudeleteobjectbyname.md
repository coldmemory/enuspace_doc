---
layout: default
title: enuDeleteObjectByName
parent: Application API
---
# void enuDeleteObjectByName\(HSVG pSvgHandler, wchar\_t\* pStrVariable\)

void enuDeleteObjectByName\(HSVG pSvgHandler, wchar\_t\* pStrVariable\)

#### Parameters

* HSVG pSvgHandler

SVG 핸들을 입력합니다.

* wchar\_t\* pStrVariable

SVG 핸들의 변수 또는 객체의 ID를 입력합니다.

Asterisk문자를 이용하여 특정 문자열을 포함한 이름에 대하여 전부 제거를 수행가능합니다. \(ex \*MyObject, MyObject\*\)

#### Return Value

Type : NONE

#### Remarks

SVG 픽쳐내에 추가된 객체 또는 변수를 ID를 통하여 제거를 수행하는 함수입니다.

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

    // delete object by name.
    enuDeleteObjectByName(SvgHandle, L"MyObject");

    // enuDeleteObjectByName(SvgHandle, L"My*");        // ID가 My로 시작하는 모든 객체를 제거합니다.

}
```



