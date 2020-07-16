---
layout: default
title: SetZoomScale
parent: Script API
---
# SetZoomScale\(scale\)

SetZoomScale\(\)

#### Parameters

scale : 스케일값을 입력합니다.

#### Return Value

none

#### Remarks

픽쳐의 스케일값을 조정합니다. 현재 스케일정보를 받아오려면 [GetZoomScale\(\)](./enusscriptapi_getzoomscale.md)함수를 이용합니다.

```lua
-- lua
SetZoomScale(1)
```

```js
// javascript
SetZoomScale(1);
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()    
    SetZoomScale(1)
end
```

```js
// JavaScript
function _onmousedown()
{    
    SetZoomScale(1);
}
```



