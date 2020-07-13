---
layout: default
title: enuSaveImageToFile
parent: Application API
---
# void enuSaveImageToFile\(HVIEW pENUView, wchar\_t\* strFileName, wchar\_t\* strFileType\)

void enuSaveImageToFile\(HVIEW pENUView, wchar\_t\* strFileName, wchar\_t\* strFileType\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

* wchar\_t\* strFileName

저장하고자하는 파일의 이름을 입력합니다. 전체 패스이름.

* wchar\_t\* strFileType

저장하고자하는 파일의 확장자를 입력합니다. \("png" or "bmp"\)

#### Return Value

Type : NONE

#### Remarks

뷰에 디스플레이되는 화면을 그림파일로 저장합니다.

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
    HNODE hnode = enuCreateLine(SvgHandle, L"MyObject", 50, 50, 100, 100, 0, 0);
}

enuSaveImageToFile(ViewHandle, L"C:\\sample.png", L"png");
```



