---
layout: default
title: enuMoveWindow
parent: Application API
---
# void enuMoveWindow\(wchar\_t\* strWindow, float posX, float posY\)

void enuMoveWindow\(wchar\_t\* strWindow, float posX, float posY\)

#### Parameters

* wchar\_t\* strWindow

윈도우의 이름을 입력합니다.

* float posX

이동하고자하는 x의 좌표를 입력합니다.

* float posY

이동하고자하는 y의 좌표를 입력합니다.

#### Return Value

Type : NONE

#### Remarks

Runtime View의 윈도우 이동을 수행합니다.

RuntimeView는 프로젝트의 \*.enup 파일의 정보를 이용하여 윈도우를 배치합니다.

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
enuMoveWindow(L"window", 100, 100);
```



