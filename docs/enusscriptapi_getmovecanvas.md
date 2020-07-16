---
layout: default
title: GetMoveCanvas
parent: Script API
---
# GetMoveCanvas\(\)

GetMoveCanvas\(\)

#### Parameters

none

#### Return Value

transx : 켄버스의 x축의 위치 이동값을 반환합니다.

transy : 켄버스의 y축의 위치 이동값을 반환합니다.

#### Remarks

켄버스의 이동값을 반환합니다. 켄버스의 이동값을 적용하는 함수는 [SetMoveCanvas\(\)](./enusscriptapi_setmovecanvas.md)함수를 활용합니다.

```lua
-- lua
local transx, transy
transx, transy = GetMoveCanvas()
```

```js
// javascript
var transx, transy;

transx = GetMoveCanvasX();
transy = GetMoveCanvasY();
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    local transx, transy
    transx, transy = GetMoveCanvas()
end
```

```js
// JavaScript
function _onmousedown()
{    
    var transx, transy;

    transx = GetMoveCanvasX();
    transy = GetMoveCanvasY();
}
```



