---
layout: default
title: enuGetEditOperationMode
parent: Application API
---
# bool enuGetEditOperationMode\(HVIEW pENUVie\)

bool enuGetEditOperationMode\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

View 핸들을 입력합니다.

#### Return Value

Type : bool

VIew의 수정보드 상태를 반환합니다. true시 수정모드 상태, false시 실행 모드 상태

#### Remarks

수정모드 상태시 마우스 및 키보드 설정이 편집 상태로 전환되어 동작을 수행합니다. 실행모드시 마우스 이벤트에 의한 동작을 수행합니다. 

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

    // New Page Create. 
    CString strPicture = L"picture\\KoreaAIP.svg"; 
    HSVG SvgHandle = enuNewSvgPageFile(strPicture.GetBuffer(0)); 

    // ENU View Attach Set Page 
    enuSetSvgPageView(ViewHandle , strPicture.GetBuffer(0)); 
    
    bool bEdit = enuGetEditOperationMode(ViewHandle); 
    // bEdit -> false 실행모드 반환.
}
```



