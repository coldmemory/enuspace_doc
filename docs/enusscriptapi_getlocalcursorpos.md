---
layout: default
title: GetLocalCursorPos
parent: Script API
---
# GetLocalCursorPos\(\)

GetLocalCursorPos\(\)

#### Parameters

none

#### Return Value

posx : 현재창 윈도우기준의 마우스 좌표값을 반환합니다.

posy : 현재창 윈도우기준의 마우스 좌표값을 반환합니다.

#### Remarks

```lua
-- lua
local posx, posy
posx, posy = GetLocalCursorPos()
```

```js
// javascript
var posxy;
posxy = GetLocalCursorPos();        // return format "{x:100,y:100}"
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    local posx, posy
    posx, posy = GetLocalCursorPos()
end
```

```js
// JavaScript
function _onmousedown()
{    
    var posxy;
    posxy = GetLocalCursorPos();        // return format "{x:100,y:100}"
    
    var posx;
    var posy;
    posx = GetLocalCursorPosX();
    posy = GetLocalCursorPosY();    
}
```



