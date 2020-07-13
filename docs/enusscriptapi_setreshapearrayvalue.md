---
layout: default
title: SetReShapeArrayValue
parent: Script API
---
# SetReShapeArrayValue\(pinid, type, dimension, value\)

SetReShapeArrayValue\(\)

#### Parameters

pinid : pin id값을 입력합니다.

type : 변수의 타입을 지정합니다. \(int, float, double, bool\) 

dimension : 배열 정보를 지정합니다.

value : 초기값을 지정합니다.

#### Return Value



#### Remarks

로직 pin객체의 변수 배열정보를 변경합니다. 본 스크립트 함수는 심볼에서 호출하여 적용합니다.

```lua
-- lua
SetReShapeArrayValue("OUTPUT", "double", [2][2]}, "1;2;3;4")
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
    SetReShapeArrayValue("OUTPUT", "double", [2][2]}, "1;2;3;4")    -- OUTPUT PIN Array size and value change event.
end
```

```js
// JavaScript
function _onmousedown()
{        
    // not support.
}
```



