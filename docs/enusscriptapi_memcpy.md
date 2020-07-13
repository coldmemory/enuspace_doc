---
layout: default
title: memcpy
parent: Script API
---
# memcpy\(target, source, size\)

memcpy\(\)

#### Parameters

target : 메모리를 복사하고자하는 target을 지정합니다.

source : 메모리를 복사하고자하는 source를 지정합니다.

size : 메모리의 사이즈를 지정합니다.

#### Return Value

none

#### Remarks

memcpy\(\)함수는 동일한 타입에 대하여 복사를 수행합니다. 문자열 변수에 대해서는 메모리 복사 기능을 제공하지 않습니다. 

메모리의 사이즈는 해당하는 메모리 타입의 개수를 입력합니다.

타입이 다른 메모리에 대해서는 복사를 수행하지 마십시요!

```lua
-- lua
-- double target[10]
-- double source[10]

memcpy(target, source, 10)
```

```js
// javascript
// double target[10]
// double source[10]

memcpy(target, source, 10);
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    memcpy(target, source, 10)
end
```

```js
// JavaScript
function _onmousedown()
{    
    memcpy(target, source, 10);
}
```



