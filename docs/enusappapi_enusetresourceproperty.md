---
layout: default
title: enuSetResourceProperty
parent: Application API
---
# bool enuSetResourceProperty\(HSVG pSvg, wchar\_t\* pAttribute, wchar\_t\* pValue\)

bool enuSetResourceProperty\(HSVG pSvg, wchar\_t\* pAttribute, wchar\_t\* pValue\)

#### Parameters

HSVG pSVG : 리소스 페이지 핸들을 입력합니다.

wchar\_t\* pAttribute : 속성 정보를 입력합니다. \("filename"\)

wchar\_t\* pValue : 속성 값을 입력합니다.

#### Return Value

적용 여부를 반환합니다.

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

    // edit mode unactivate.
    enuSetEditOperationMode(ViewHandle , false);

    // default mouse wheel control set.
    enuSetDefaultWheelControl(ViewHandle , true);

    // view activate
    enuActivateView(ViewHandle );

    // New Page Create. 
    CString strPicture = L"style\\style.svg"; 

    HSVG hsvg = enuGetResourceClass(strPicture .GetBuffer(0));
    if (hsvg)
    {
        enuSetResourceProperty(hsvg, L"filename", L"style\\new_style.svg");
    }
}
```





