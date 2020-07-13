---
layout: default
title: enuSetPageProperty
parent: Application API
---
# bool enuSetPageProperty\(void\* pPage, wchar\_t\* pAttribute, wchar\_t\* pValue\)

bool enuSetPageProperty\(void\* pPage, wchar\_t\* pAttribute, wchar\_t\* pValue\)

#### Parameters

void\* pPage : 픽쳐 페이지 핸들을 입력합니다.

wchar\_t\* pAttribute : 속성 정보를 입력합니다. \("filename"\)

wchar\_t\* pValue : 속성 값을 입력합니다.



#### Return Value

none

#### Remarks

활성화된 뷰는 taskview\(\) 의 스크립트 함수가 동작합니다.

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
    CString strPicture = L"picture\\KoreaAIP.svg"; 
    
    void* pPage = enuGetPageClass(strPicture .GetBuffer(0));
    if (pPage)
    {
        enuSetPageProperty(pPage, L"filename", L"picture\\newname.svg");
    }
}
```



