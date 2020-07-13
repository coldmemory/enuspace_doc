---
layout: default
title: CreateGlobalVariable
parent: Script API
---
# CreateGlobalVariable\(type, variable, value\)

CreateGlobalVariable\(\)

#### Parameters

type : 변수의 타입정보를 입력합니다. \(int, float, double, bool, string\) 

variable : 변수명을 입력합니다. 

value : 변수의 값을 입력합니다.

#### Return Value

none

#### Remarks

"global\\global.svg" 페이지에 전역변수를 등락하는 함수입니다. 등록된 변수는 모든 페이지에서 접근이 가능합니다. 



```lua
-- lua
CreateGlobalVariable("int", "g_GlobalVariable", "10")
```

```js
// javascript
CreateGlobalVariable("int", "g_GlobalVariable", "10");
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    CreateGlobalVariable("int", "g_GlobalVariable", "10")
end
```

```js
// JavaScript
function _onmousedown()
{    
    CreateGlobalVariable("int", "g_GlobalVariable", "10");
}
```



