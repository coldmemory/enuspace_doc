---
layout: default
title: 팝업 윈도우
parent: 저작기 사용방법
grand_parent: enuSpace Tutorial
---

# Popup Window

---

Runtime 뷰상에서 Popup 윈도우를 호출하여 사용하기 위한 방법에 대하여 설명합니다. Runtime 모드에서 Popup 윈도우를 사용하기 위해서는 다음과 같은 절차를 통하여 구성됩니다.

Popup 윈도우를 설정하기 위해서는 프로젝트 파일\(\*.enup\)정보를 수정합니다.

```svg
<?xml-stylesheet 
    type="text/css" version="1.0" encoding="UTF-16"?>
<!--Generator : ENU Co,ltd ENUSpace 1.0.0.0, SVG Export Plug-In -->
<svg 
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    pg-classname="project"
    pg-project="OCEAN"
    > 
    <pg-global xlink:href="global\global.svg"/>
    <pg-hmi xlink:href="library\hmi\ToolBox.svg"/>
    <pg-logic xlink:href="library\logic\IOT_SYMBOL.svg"/>
    <pg-picture xlink:href="picture\main.svg"/>
    <pg-picture xlink:href="picture\core_3d.x3d"/>
    <pg-window id="window" x="0" y="0" width="1920" height="1080" style="2d view" border="Dialog Frame" xlink:href="picture\main.svg"/>
    <pg-window id="popup" x="0" y="0" width="400" height="800" style="popup" border="none" xlink:href=""/>
    <activate-view xlink:href="picture\main.svg"/>
</svg>
```

&lt;pg-window&gt; 앨리먼트를 이용하여 윈도우를 설정합니다.

| Window의 속성 | Description |
| :--- | :--- |
| id | 윈도우의 고유한 id |
| x | X축 좌표 |
| y | Y축 좌표 |
| width | 윈도우의 넓이 |
| height | 윈도우의 높이 |
| style | 윈도우의 스타일 \(3d view, 2d view, popup\) |
| border | 윈도우의 프레임\(Dialog Frame, None, Resizing\) |

윈도우의 스타일은 2d view, 3d view, popup으로 구분되며, 2d view 속성시 2D 그래픽을 위한 프레임으로 설정된다. 3d view속성시 3D 그래픽을 위한 프레임으로 설정되며, popup 속성시 파업을 수행하였을 경우에 디스플레이된다.

윈도우의 border 설정은 Dialog Frame, None, Resizing으로 구분된다. 팝업윈도우에서 본 속성이 적용되며, Dialog Frame 설정된 팝업 윈도우는 윈도우에서 제공하는 캡션바가 나타나는 상태, None으로 설정 시에는 다이얼로그 프레임이 나타나지 않는 상태, Resizing 설정시에는 다이얼로그의 리사이즈 기능을 제공한다.

# Popup Window 호출

---

호출부 \(팝업윈도우를 호출하기 위해서 객체에 스크립트를 추가한다.\)

Step1. Rect 객체를 추가한다.

Step2. Rect 객체의 스크립트를 추가한다. Rect객체에 \_onmousedown이벤트를 추가한다.

Step3. 팝업윈도우의 위치를 설정하기 위해 GetCursorPos\(\)함수를 이용하여 마우스 커서의 위치를 회득한다. 획득한 좌표값을 이용하여, 앞 윈도우 설정된 popup 윈도우를 [OpenWindow](./enusscriptapi_openwindow.md)\(\)함수를 이용하여 호출한다.

Step4. 팝업윈도우의 속성을 설정하기 위해서 [ExecuteString](./enusscriptapi_executestring.md)\(\)함수를 이용하여 전달한다. 

```lua
function _onmousedown()

    local curx, cury
    curx, cury = GetCursorPos()
    OpenWindow("popup",curx,cury,"picture\\popup.svg")
    ExecuteString("SetTitle(\"My Title\")", "SVG", "picture\\popup.svg")

end
```

팝업 픽쳐부 \(팝업윈도우에 해당하는 픽쳐를 제작한다.\)

Step1. Title 텍스트 객체를 추가하고, ID를 지정한다.

Step2. 픽처에 사용자 정의 함수를 추가한다. 호출시 추가된 텍스트 객체를 통하여 입력값을 업데이트 수행한다.

```lua
function SetTitle(title)

    ID_TITLE.text = string.format('%s', title)

end
```



