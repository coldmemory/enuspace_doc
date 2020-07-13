---
layout: default
title: enusetvariablevaluebynode
parent: Application API
---
# void enuSetVariableValueByNode\(HSVG pSvgHandler, HNODE hnode, wchar\_t\* strVariable, wchar\_t\* strValue\)

void enuSetVariableValueByNode\(HSVG pSvgHandler, HNODE, hnode, wchar\_t\* strVariable, wchar\_t\* strValue\)

#### Parameters

Type : HSVG

페이지 핸들을 전달합니다.

Type : HNODEG

객체 핸들을 전달합니다.

Type : wchar\_t\* strVariable

픽쳐파일 내부의 변수를 지정합니다.

Type : wchar\_t\* strValue

변수의 값을 지정합니다.

#### Remarks

노드 객체내에서의 변수값을 변경하는 함수입니다. 

벼경되는 정보는 객체의 속성, 페이지 내부 변수 그리고 데이터베이스 변수입니다. 

데이터베이스 변수는 첫문자가 @로 정의됩니다.

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

    HNODE pUse = enuCreateUse(hsvg, L"OBJECT", 0, 0, L"Div", L"logic", 0, 0);		
    // set variable value
    enuSetVariableValueByNode(hsvg, pUse, L"In2_r", L"34");
}
```



