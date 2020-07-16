---
layout: default
title: CloseWindow
parent: Script API
---
# CloseWindow\(window\)

CloseWindow\(\)

#### Parameters

window : 윈도우 이름을 입력합니다.

#### Return Value

none

#### Remarks

RuntimeView에서 호출된 팝업 윈도우를 닫기 수행할시 해당 윈도우 이름을 통하여 윈도우 창을 닫습니다.

참조함수 : [OpenWindow\(\)](./enusscriptapi_openwindow.md)

```lua
-- lua
CloseWindow("popup_window")
```

```js
// javascript
CloseWindow("popup_window");
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    CloseWindow("popup_window")
end
```

```js
// JavaScript
function _onmousedown()
{    
    CloseWindow("popup_window");
}
```



