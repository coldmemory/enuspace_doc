---
layout: default
title: GetWorldCursorPos
parent: Script API
---
# GetWorldCursorPos\(\)

GetWorldCursorPos\(\)

#### Parameters

none

#### Return Value

posx : 현재 데스크탑 기준의 마우스 좌표를 반환합니다.

posy : 현재 데스크탑 기준의 마우스 좌표를 반환합니다.

#### Remarks



```lua
-- lua
local posx, posy
posx, posy = GetWorldCursorPos()
```

```js
// javascript
var posxy;
posxy = GetWorldCursorPos();        // return format "{x:100,y:100}"
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    local posx, posy
    posx, posy = GetWorldCursorPos()
end
```

```js
// JavaScript
function _onmousedown()
{    
    var posxy;
    posxy = GetWorldCursorPos();        // return format "{x:100,y:100}"

    var posx;
    var posy;
    posx = GetWorldCursorPosX();
    posy = GetWorldCursorPosY(); 

}
```



