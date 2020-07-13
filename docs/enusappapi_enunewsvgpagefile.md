---
layout: default
title: enuNewSvgPageFile
parent: Application API
---
# HSVG enuNewSvgPageFile\(wchar\_t\* pStrFileName\)

HSVG enuNewSvgPageFile\(wchar\_t\* pStrFileName\)

#### Parameters

* wchar\_t\* pStrFileName

PICTURE영역의 새로운 SVG파일이름을 입력합니다.

#### Return Value

Type : HSVG

생성된 SVG핸들을 반환합니다.

#### Remarks

PICTURE영역에 새로운 SVG파일을 생성합니다.

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

    // New picture svg. 
    CString strPicture = L"picture\\user_picture.svg"; 
    HSVG SvgHandle = enuNewSvgPageFile(strPicture.GetBuffer(0)); 
}
```



