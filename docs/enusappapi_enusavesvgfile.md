---
layout: default
title: enuSaveSvgFile
parent: Application API
---
# bool enuSaveSvgFile\(HSVG pSvgHandler, wchar\_t\* strFileName= L""\)

bool enuSaveSvgFile\(HSVG pSvgHandler, wchar\_t\* strFileName= L""\)

#### Parameters

* HSVG pSvgHandler

SVG 핸들을 입력합니다.

* wchar\_t\* strFileName= L""

저장하고자하는 파일명을 입력합니다.

#### Return Value

Type : bool

SVG 파일의 정상 저장여부를 반환합니다.

#### Remarks

#### Examples

```cpp
HVIEW ViewHandle = NULL; 
HSVG SvgHandle = NULL;
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
    SvgHandle = enuNewSvgPageFile(strPicture.GetBuffer(0)); 

    // ENU View Attach Set Page 
    enuSetSvgPageView(ViewHandle , strPicture.GetBuffer(0)); 

    // object create
    HNODE hnode = enuCreateLine(SvgHandle, L"MyObject", 50, 50, 100, 100, 0, 0);
}

void CSampleView::SaveSvg()
{
    enuSaveSvgFile(SvgHandle);
}
```



