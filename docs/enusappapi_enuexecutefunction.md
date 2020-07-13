---
layout: default
title: enuExecuteFunction
parent: Application API
---
# void enuExecuteFunction\(HSVG pSvgHandler, wchar\_t\* strFunction\)

void enuExecuteFunction\(HSVG pSvgHandler, wchar\_t\* strFunction\)

#### Parameters

HSVG pSvgHandle : 페이지 핸들을 전달합니다.

wchar\_t\* strFunction : 픽쳐파일 내부의 함수를 지정합니다.

#### Return Value

none

#### Remarks

픽쳐에서 구현된 함수를 호출합니다. 객체의 함수를 호출할 경우에는 ID\_OBJECT.UserFunction\(\) 형태로 호출합니다.

SVG 최상위 노드에서 구현된 함수는객체 이름을 포함하지 않고 UserFunction\(\) 형태로 호출합니다.

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

    // get picture handle
    HSVG hsvg = enuGetSvgHandler(ViewHandle )

    // set variable value
    enuSetVariableValue(hsvg, L"@OCEAN.I_BU", strValue.GetBuffer(0))

    // picture page의 _onload() function call
    enuExecuteFunction(hsvg, L"_onload()");    
}
```



