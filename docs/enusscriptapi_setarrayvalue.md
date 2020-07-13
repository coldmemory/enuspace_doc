---
layout: default
title: SetArrayValue
parent: Script API
---
# SetArrayValue\(target, source\)

SetArrayValue\(\)

#### Parameters

target : 값을 적용하고자하는 target 변수

source : 값을 적용하고자하는 source 변수

#### Return Value

none

#### Remarks

배열변수에 대한 값을 명시적으로 설정하기 위한 함수입니다. 일반적으로 data\[10\] = org\_data\[9\] 와 같은 표현식으로 구현합니다.

```lua
-- lua

SetArrayValue(data[10], src_data[5])

-- equal expression
data[10] = src_data[5]
```

```js
// javascript

SetArrayValue(data[10], src_data[5]);

// equal expression
data[10] = src_data[5];
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    SetArrayValue(data[10], src_data[5]);
end
```

```js
// JavaScript
function _onmousedown()
{        
    SetArrayValue(data[10], src_data[5]);
}
```



