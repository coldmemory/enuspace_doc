---
layout: default
title: GetMouseWheelDelta
parent: Script API
---
# GetMouseWheelDelta\(\)

GetMouseWheelDelta\(\)

#### Parameters

none

#### Return Value

value : 마우스 휠의 델타값을 가져옵니다.

#### Remarks

그래픽에서 마우스 휠정보의 델타정보를 이용하는 경우 활용합니다.

```lua
-- lua
local delta
delta = GetMouseWheelDelta()
```

```js
// javascript
var delta;
delta = GetMouseWheelDelta();
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    local delta
    delta = GetMouseWheelDelta()
end
```

```js
// JavaScript
function _onmousedown()
{    
    var delta;
    delta = GetMouseWheelDelta();
}
```



