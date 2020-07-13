---
layout: default
title: IsExistGlobalVariable
parent: Script API
---
# IsExistGlobalVariable\(variable\)

IsExistGlobalVariable\(\)

#### Parameters

variable : 전역변수의 이름을 입력합니다.

#### Return Value

value : 전역변수의 존재유무를 제공합니다.

#### Remarks



```lua
-- lua
local bExist = false
bExist = IsExistGlobalVariable("g_GlobalVariable")
```

```js
// javascript
// not support
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    local bExist = false
    bExist = IsExistGlobalVariable("g_GlobalVariable")
end
```

```js
// JavaScript
function _onmousedown()
{        
    // not support
}
```



