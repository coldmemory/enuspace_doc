---
layout: default
title: MoveWindow
parent: Script API
---
# MoveWindow\(window, posx, posy\)

MoveWindow\(\)

#### Parameters

window : 윈도우의 이름을 입력합니다. 

posx : 이동하고자하는 x의 좌표를 입력합니다.

posy : 이동하고자하는 y의 좌표를 입력합니다.

#### Return Value

none

#### Remarks



```lua
-- lua
MoveWindow("window", 500, 500)
```

```js
// javascript
MoveWindow("window", 500, 500);
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    MoveWindow("window", 500, 500)
end
```

```js
// JavaScript
function _onmousedown()
{    
    MoveWindow("window", 500, 500);
}
```



