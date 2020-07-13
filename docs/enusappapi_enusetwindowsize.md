---
layout: default
title: enuSetWindowSize
parent: Application API
---
# bool enuSetWindowSize\(wchar\_t\* window, int x, int y, int width, int height\);

bool enuSetWindowSize\(wchar\_t\* window, int x, int y, int width, int height\);

#### Parameters

window : 윈도우 ID값을 지정합니다.

x : x축의 좌표값을 지정합니다.

y : y축의 좌표값을 지정합니다.

width : 넖이값을 지정합니다.

height : 높이값을 지정합니다.

#### Return Value

bool : 윈도우 사이즈의 설정 반영여부를 반환합니다.

#### Remarks

윈도우의 사이즈를 적용합니다. enuSetWindowPos\(\)함수는 Window용 SetWindowPos\(\)함수를 이용하여 윈도우의 사이즈를 변경하는 반면, enuSetWindowSize\(\)함수는 Project에서 정의된 윈도우의 속성정보 변경과 RunTime View에 대하여 작동합니다.



pg-window element의 x, y, width, height값을 반영하며 RuntimeView\(\)가 활성화 상태이면 화면에  반영합니다.

&lt;project file 예시&gt;

```svg
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
	<pg-logic xlink:href="library\logic\enuSpaceEigen.svg"/>
	<pg-logic xlink:href="library\logic\tf_core.svg"/>
	<pg-picture xlink:href="picture\tensorflow_symbols.svg"/>
	<pg-window id="window" x="0" y="0" width="920" height="1080" style="2d view" border="Dialog Frame" xlink:href="picture\tensorflow_symbols.svg"/>
</svg> 
```

#### Examples

```cpp
void CSampleView::OnInitialUpdate() 
{ 
    RECT rect;
    GetClientRect(&rect);
    enuSetWindowSize(L"window", rect.left, rect.top, rect.right, rect.bottom);
}
```



