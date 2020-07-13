---
layout: default
title: enuSetDefaultWheelControl
parent: Application API
---
# void enuSetDefaultWheelControl\(HVIEW pENUView, bool bDefault\)

void enuSetDefaultWheelControl\(HVIEW pENUView, bool bDefault\)

#### Parameters

Type : HVIEW

뷰 핸들을 전달합니다.

Type : bool

마우스 휠 기능에 대한 기본 모드 설정 여부를 지정합니다.

#### Return Value

#### Remarks

bDefault를 true 설정시 마우스 휠에 따른 줌인, 줌아웃 기능 제공.

마우스 휠 버튼클릭을 이용한 캔버스 이동 기능을 제공합니다.

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

    // New Page Create. 
    CString strPicture = L"picture\\KoreaAIP.svg"; 
    HSVG SvgHandle = enuNewSvgPageFile(strPicture.GetBuffer(0)); 

    // ENU View Attach Set Page 
    enuSetSvgPageView(ViewHandle , strPicture.GetBuffer(0)); 
}
```



