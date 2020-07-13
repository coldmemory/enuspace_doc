---
layout: default
title: GetArrayValue
parent: Script API
---
# GetArrayValue\(variable\)

GetArrayValue\(\)

#### Parameters

variable : 배열변수 이름을 입력합니다.

#### Return Value

value : 해당변수의 배열값을 반환합니다.

#### Remarks

일반적으로 변수배열값을 가져올 경우 data\[10\]와 같이 표기하여 값을 취득합니다. 

본 함수는 GetArrayValue\(data\[10\]\)\)는 data\[10\]의 값을 가져오는 역할을 수행합니다.

```lua
-- lua
local localvar
localvar = data[10]

. eq .
localvar = GetArrayValue(data[10])
```

```js
// javascript
var localvar
localvar = data[10];

. eq .
localvar = GetArrayValue(data[10]);
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    local localvar    
    localvar = GetArrayValue(data[10])
end
```

```js
// JavaScript
function _onmousedown()
{    
    var localvar;
    localvar = GetArrayValue(data[10]);
}
```



