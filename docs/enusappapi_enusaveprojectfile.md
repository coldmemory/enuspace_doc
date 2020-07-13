---
layout: default
title: enuSaveProjectFile
parent: Application API
---
# bool enuSaveProjectFile\(\)

bool enuSaveProjectFile\(\)

#### Parameters

NONE

#### Return Value

Type : bool

Project 파일의 정상 저장여부를 반환합니다.

#### Remarks

project 파일 저장 예시.

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
    <pg-window id="window_2d" x="0" y="0" width="920" height="1080" style="2d view" border="Dialog Frame" xlink:href="picture\core_2d.svg"/>
    <pg-window id="window_3d" x="920" y="0" width="1000" height="1080" style="3d view" border="Dialog Frame" xlink:href="picture\core_3d.x3d"/>
    <activate-view xlink:href="picture\tensorflow_symbols.svg"/>
</svg>
```

#### Examples

```cpp
void SaveEvent()
{    
    enuSaveProjectFile();
}
```



