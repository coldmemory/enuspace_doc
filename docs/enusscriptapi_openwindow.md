---
layout: default
title: OpenWindow
parent: Script API
---
# OpenWindow\(window, posx, posy, href\)

OpenWindow\(\)

#### Parameters

window : 윈도우이름을 입력합니다. 

posx : 오픈하고자 하는 위치의 좌표를 지정합니다.

posy : 오픈하고자 하는 위치의 좌표를 지정합니다.

href : 오픈시 연결할 픽쳐의 이름을 지정합니다.

#### Return Value



#### Remarks



```lua
-- lua
OpenWindow("window", 500, 500, "picture\\popup.svg")
```

```js
// javascript
OpenWindow("window", 500, 500, "picture\\popup.svg");
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    OpenWindow("window", 500, 500, "picture\\popup.svg")
end
```

```js
// JavaScript
function _onmousedown()
{    
    OpenWindow("window", 500, 500, "picture\\popup.svg");
}
```



