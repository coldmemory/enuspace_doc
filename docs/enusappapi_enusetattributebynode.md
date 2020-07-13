---
layout: default
title: enuSetAttributeByNode
parent: Application API
---
# void enuSetAttributeByNode\(HSVG pSvgHandler, HNODE pObject, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)

void enuSetAttributeByNode\(HSVG pSvgHandler, HNODE pObject, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)

#### Parameters

* HSVG pSvgHandler

SVG핸들을 입력합니다.

* HNODE pObject

객체의 노드 핸들을 입력합니다.

* wchar\_t\* pStrVariable

설정하고자하는 변수를 입력합니다.

* wchar\_t\* pStrValue

변수의 값을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

주어진 변수의 ID정보를 이용하여 속성값을 변경합니다.

```xml
<?xml version="1.0" encoding="UTF-16"?>
<svg
    id="ID_1enfXB"
    stroke="rgb(0,119,189)"
    stroke-opacity="1.00"
    stroke-width="1.00"
    transform="translate(0.00,0.00) rotate(0.00) scale(1.0000, 1.0000)"
    pg-xcenter="0.00"
    pg-ycenter="0.00"
    style="stroke:rgb(127,127,127);stroke-opacity:1.00;stroke-width:2.00;stroke-dasharray:1,1,1;"
    enuspace-version="3.0.2.0"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    pg-create-time="2018-2-19 7:6:45.663"
    width="1920"
    height="1080"
>
    <rect
        id="ID_BOX"
        stroke="rgb(0,119,189)"
        stroke-opacity="1.00"
        stroke-width="2.00"
        transform="translate(301.00,140.00) rotate(0.00) scale(1.0000, 1.0000)"
        pg-xcenter="0.00"
        pg-ycenter="0.00"
        stroke-linecap="butt"
         stroke-linejoin="miter"
         x="0.00"
        y="0.00"
        width="100"
        height="100"
        rx="0.00"
        ry="0.00"
        fill="rgb(0,174,238)"
        fill-opacity="1.00"
    >
    </rect>
</svg>
```

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
    HNODE hnode = enuCreateRect(SvgHandle, L"ID_BOX", 0, 0, 100, 100, 0, 0);

    enuSetAttribute(SvgHandle, L"ID_BOX.width", L"300");              

    enuSetAttributeByNode(SvgHandle, hnode, L"width", L"300");        // 비동기식 호출

    enuSetAttributeByNodeSync(SvgHandle, hnode, L"width", L"300");    // 동기식 호출

}
```



