---
layout: default
title: CreateRect
parent: Script API
---
# CreateRect\(id, x, y, width, height, transx, transy\)

CreateRect\(\)

#### Parameters

id : id값을 입력합니다.

x : x축의 값을 입력합니다.

y : y축의 값을 입력합니다.

width : 폭값을 입력합니다.

height : 높이값을 입력합니다.

transx : x축의 이동값을 입력합니다.

transy : y축의 이동값을 입력합니다.

#### Return Value

none

#### Remarks

스크립트를 이용하여 동적으로 라인 객체를 생성합니다. 생성된 객체의 속성을 변경하고자 하는 경우에는 [SetAttribute\(\)](enusscriptapi_setattribute.md)함수를 이용합니다.

```lua
-- lua
CreateRect("ID_RECT", 100, 100, 200, 200, 100, 100)
```

```js
// javascript
CreateRect("ID_RECT", 100, 100, 200, 200, 100, 100);
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    CreateRect("ID_RECT", 100, 100, 200, 200, 100, 100)
end
```

```js
// JavaScript
function _onmousedown()
{    
    CreateRect("ID_RECT", 100, 100, 200, 200, 100, 100);
}
```



