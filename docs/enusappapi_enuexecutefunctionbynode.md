---
layout: default
title: enuExecuteFunctionByNode
parent: Application API
---
# void enuExecuteFunctionByNode\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strFunction\);

void enuExecuteFunctionByNode\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strFunction\);

#### Parameters

HSVG SvgHandler : SVG 픽쳐 핸들러를 지정합니다.

HNODE Node : 픽쳐 내부의 NODE 핸들러를 지정합니다.

wchar\_t\* strFunction : 픽쳐파일 내부의 함수를 지정합니다.

#### Return Value

none

#### Remarks

SVG 핸들정보와 객체의 NODE정보를 이미 알고있는 경우에는 직접 호출하여 함수를 수행합니다.



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
    
    HNODE hnode = enuGetObjectById(hsvg, L"ID_RECT");
    enuExecuteFunctionByNode(hsvg, hnode, L"_onmousedown()");   
}
```



