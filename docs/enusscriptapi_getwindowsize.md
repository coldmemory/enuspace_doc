---
layout: default
title: GetWindowSize
parent: Script API
---
# GetWindowSize\(\)

GetWindowSize\(\)

#### Parameters

none

#### Return Value

left : 윈도우의 left값을 반환합니다.

top : 윈도우의 top값을 반환합니다.

right : 윈도우의 right값을 반환합니다.

bottom : 윈도우의 bottom값을 반환합니다.

#### Remarks



```lua
-- lua
local left, top, right, bottom
left, top, right, bottom = GetWindowSize()
```

```js
// javascript
var winsize
winsize = GetWindowSize();        // return format "{rect.left:0,rect.top:0,rect.right:1920,rect.bottom:1080}"
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    local left, top, right, bottom
    left, top, right, bottom = GetWindowSize()
end
```

```js
// JavaScript
function _onmousedown()
{    
    var winsize
    winsize = GetWindowSize();        // return format "{rect.left:0,rect.top:0,rect.right:1920,rect.bottom:1080}"
}
```



