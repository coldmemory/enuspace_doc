---
layout: default
title: enuNewSvgGlobalFile
parent: Application API
---
# HSVG enuNewSvgGlobalFile\(wchar\_t\* pStrFileName\)

HSVG enuNewSvgGlobalFile\(wchar\_t\* pStrFileName\)

#### Parameters

* wchar\_t\* pStrFileName

GLOBAL영역의 새로운 SVG파일이름을 입력합니다.

#### Return Value

Type : HSVG

생성된 SVG핸들을 반환합니다.

#### Remarks

GLOBAL영역에 새로운 SVG파일을 생성합니다.

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

    // New global svg. 
    CString strPicture = L"global\\user_global.svg"; 
    HSVG SvgHandle = enuNewSvgGlobalFile(strPicture.GetBuffer(0)); 

    enuAddGlobalVariable(strPicture.GetBuffer(0), L"double", L"g_input1", L"55.45", L"global variable input1");
    enuAddGlobalVariable(strPicture.GetBuffer(0), L"double", L"g_input2", L"55.45", L"global variable input2");
    
    enuSetGlobalValue(SvgHandle, L"g_input1", L"99");
}
```



