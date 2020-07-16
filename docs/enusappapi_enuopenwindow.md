---
layout: default
title: enuOpenWindow
parent: Application API
---
# void enuOpenWindow\(wchar\_t\* strWindow, float posX, float posY, wchar\_t\* strHref\)

void enuOpenWindow\(wchar\_t\* strWindow, float posX, float posY, wchar\_t\* strHref\)

#### Parameters

* wchar\_t\* strWindow

윈도우 이름을 입력합니다.

* float posX

X축의 좌표값을 입력합니다.

* float posY

Y축의 좌표값을 입력합니다.

* wchar\_t\* strHref

오픈시 연결할 픽쳐의 이름을 지정합니다.

#### Return Value

Type : NONE

#### Remarks

Runtime View의 상태에서 project 파일에 정의된 윈도우에서 style의 정보가 popup인 경우 적용.

참고 : [popup window 사용방법](./enuseditoruse_popup-window.md)

```xml
<?xml-stylesheet 
    type="text/css" version="1.0" encoding="UTF-16"?>
<!--Generator : ENU Co,ltd ENUSpace 3.0.0.0, SVG Export Plug-In -->
<svg 
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    pg-classname="project"
    pg-project="lesson5"
    > 
    <pg-global xlink:href="global\global.svg"/>
    <pg-logic xlink:href="library\logic\IOT_SYMBOL.svg"/>
    <pg-picture xlink:href="picture\core_2d.svg"/>
    <pg-picture xlink:href="picture\core_3d.x3d"/>
    <pg-picture xlink:href="picture\popup.svg"/>

    <pg-window id="window_2d" x="0" y="0" width="920" height="1080" style="2d view" border="Dialog Frame" xlink:href="picture\core_2d.svg"/>
    <pg-window id="window_pop" x="0" y="0" width="920" height="1080" style="popup" border="Dialog Frame" xlink:href=""/>
    <pg-window id="window_3d" x="920" y="0" width="1000" height="1080" style="3d view" border="Dialog Frame" xlink:href="picture\core_3d.x3d"/>
    <activate-view xlink:href="picture\tensorflow_symbols.svg"/>
</svg>
```

#### Examples

```cpp
void OnInitialUpdate()
{    
    	HVIEW MainView = enuCreateView(this->m_hWnd);
	enuSetViewID(MainView, L"window_2d");
	enuSetEditOperationMode(MainView, false);

	HVIEW popup = enuCreateView(this->m_hWnd);
	enuSetViewID(popup, L"window_pop");
	enuCloseWindow(L"window_pop");				-- hidden 처리
	enuSetEditOperationMode(popup, false);
	
	enuOpenWindow(L"window_pop", 0, 0, L"picture\\popup.svg")
}
```

Script

```lua
function _onmousedown()
	
	OpenWindow("window_pop",0,0,"picture\\popup.svg")
	
end
```

응용프로그램에서 뷰를 생성하고, [enuSetViewID\(\)](./enusappapi_enusetviewid.md)함수를 이용하여 뷰의 ID값을 적용한다. 뷰의 ID는 프로젝트 파일에서 정의한 설정값에 따라 적용된다. 

[enuCloseWindow\(\)](./enusappapi_enuclosewindow.md)함수는 생성된 뷰에 대하여 HIDE 기능을 수행한다. 

