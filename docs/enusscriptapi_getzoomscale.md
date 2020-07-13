---
layout: default
title: GetZoomScale
parent: Script API
---
# GetZoomScale\(\)

GetZoomScale\(\)

#### Parameters

none

#### Return Value

scale : 그래픽의 스케일값을 반환합니다.

#### Remarks



```lua
-- lua
local scale
scale = GetZoomScale()
```

```js
// javascript
var scale;
scale = GetZoomScale();
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    local scale
    scale = GetZoomScale()
end
```

```js
// JavaScript
function _onmousedown()
{    
    var scale;
    scale = GetZoomScale();
}
```



