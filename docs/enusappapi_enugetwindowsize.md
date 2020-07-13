---
layout: default
title: enuGetWindowSize
parent: Application API
---
# bool enuGetWindowSize\(wchar\_t\* strWindowID, RECT\* rect\)

bool enuGetWindowSize\(wchar\_t\* strWindowID, RECT\* rect\)

#### Parameters

* wchar\_t\* strWindowID

윈도우의 ID를 입력합니다.

* RECT\* rect

RECT 구조체의 메모리 포인터를 입력합니다.

#### Return Value

Type : bool

정상 반환 여부를 제공합니다.

#### Remarks

런타임 뷰에서의 윈도우 사이즈를 취득합니다.

project file\(.enup\)에서의 윈도우 정의 예시.

```xml
<?xml-stylesheet 
	type="text/css" version="1.0" encoding="UTF-16"?>
<!--Generator : ENU Co,ltd ENUSpace 1.0.0.0, SVG Export Plug-In -->
<svg 
	xmlns="http://www.w3.org/2000/svg"
	xmlns:xlink="http://www.w3.org/1999/xlink"
	pg-classname="project"
	pg-project="lesson5"
	> 
	<pg-global xlink:href="global\global.svg"/>
	<pg-logic xlink:href="library\logic\IOT_SYMBOL.svg"/>
	<pg-logic xlink:href="library\logic\enuSpaceEigen.svg"/>
	<pg-picture xlink:href="picture\mnistTrain_softmax100.svg"/>
	<pg-window id="window" x="0" y="0" width="1000" height="1080" style="2d view" border="Dialog Frame" xlink:href="picture\mnisttrain_10.svg"/>
	<pg-window id="window3d" x="1000" y="0" width="920" height="1080" style="3d view" border="Dialog Frame" xlink:href="picture\mnist3d.x3d"/>
	<activate-view xlink:href="picture\mnistTrain_softmax100.svg"/>
</svg> 
```

#### Examples

```cpp
void OnMouseDown()
{
    RECT rect;
    enuGetWindowSize(L"window", &rect);
}
```



