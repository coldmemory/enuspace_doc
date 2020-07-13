---
layout: default
title: enuSetLuaScriptByNode
parent: Application API
---
# void enuSetLuaScriptByNode\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)

void enuSetLuaScriptByNode\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)

#### Parameters

* HSVG pSvgHandler

SVG 핸들을 입력합니다.

* HNODE pNode

객체의 핸들을 입력합니다.

* wchar\_t\* strFunction

함수이름을 입력합니다.

* wchar\_t\* strScript

스크립트의 내용을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

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
		transform="translate(301.00,140.00) rotate(59.00) scale(1.0000, 1.0000)"
		pg-xcenter="0.00"
		pg-ycenter="0.00"
		stroke-linecap="butt"
 		stroke-linejoin="miter"
 		x="0.00"
		y="0.00"
		width="158.00"
		height="96.00"
		rx="0.00"
		ry="0.00"
		fill="rgb(0,174,238)"
		fill-opacity="1.00"
	>
		<script
			id="ID_1enlHk"
			type="text/lua"
		>
				<![CDATA[function _ontaskview()
	rotate = rotate + 1
end]]>
		</script>
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

    CString script = L"function _ontaskview()\r\n rotate = rotate + 1; \r\nend"
    enuSetLuaScriptByNode(SvgHandle, hnode, L"_ontaskview", script.GetBuffer(0));
}
```



