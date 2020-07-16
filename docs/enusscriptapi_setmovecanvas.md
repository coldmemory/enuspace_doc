---
layout: default
title: SetMoveCanvas
parent: Script API
---
# SetMoveCanvas\(window, transx, transy\)

SetMoveCanvas\(\)

#### Parameters

window : 켄버스를 이둉하고자하는 윈도우의 이름을 입력합니다.

transx : x축 이동값을 입력합니다.

transy : y축 이동값을 입력합니다.

#### Return Value

none

#### Remarks

SetMoveCanvas\(\)함수는 [GetMoveCanvas\(\)](./enusscriptapi_getmovecanvas.md)함수와 조합하여 활용됩니다.

```lua
-- lua
SetMoveCanvas("window", 500, 500)
```

```js
// javascript
SetMoveCanvas("window", 500, 500);
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    SetMoveCanvas("window", 500, 500)
end
```

```js
// JavaScript
function _onmousedown()
{    
    SetMoveCanvas("window", 500, 500);
}
```



