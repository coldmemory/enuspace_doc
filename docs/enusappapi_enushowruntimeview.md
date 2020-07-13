---
layout: default
title: enuShowRuntimeView
parent: Application API
---
# bool enuShowRuntimeView\(HWND hWnd\)

bool enuShowRuntimeView\(HWND hWnd\)

#### Parameters

Type : HWND hWnd

윈도우 핸들을 전달합니다. NULL값을 전달할 경우 별도의 창으로 디스플레이 됩니다.

#### Return Value

Type : bool

정상 여부를 판단하는 플래그 정보를 반환합니다.

#### Remarks

윈도우 핸들을 전달합니다. NULL값을 전달할 경우 별도의 창으로 디스플레이 됩니다.

RuntimeView는 프로젝트의 \*.enup 파일의 정보를 이용하여 윈도우를 배치합니다.

```js
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

#### 

#### Examples

```cpp
void CSampleView::OnInitialUpdate() 
{ 
    CView::OnInitialUpdate(); 

    enuCreateProject(); 

    // Load Project
    enuLoadProjectFile(L"Project\\sample.enup"); 

    // Runtime view display
    enuShowRuntimeView(NULL);
}
```



