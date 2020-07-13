---
layout: default
title: enuLoadProjectFile
parent: Application API
---
# bool enuLoadProjectFile\(wchar\_t\* pStrFileName\)

bool enuLoadProjectFile\(wchar\_t\* pStrFileName\)

#### Parameters

Type : wchar\_t\* strProjectFilename

프로젝트 파일이름을 입력합니다.

#### Return Value

Type : bool

프로젝트의 로드여부를 반환합니다.

#### Remarks



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
}
```



