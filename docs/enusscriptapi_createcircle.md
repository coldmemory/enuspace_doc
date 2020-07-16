---
layout: default
title: CreateCircle
parent: Script API
---
# CreateCircle\(id, radius, cx, cy, transx, transy\)

CreateCircle\(\)

#### Parameters

id : id값을 입력합니다.

radius : 구의 반지름값을 입력합니다.

cx : 센터포인터 x값을 입력합니다.

cy : 센터포인트 y값을 입력합니다.

transx : x축의 이동값을 입력합니다.

transy : y축의 이동값을 입력합니다.

#### Return Value

none

#### Remarks

스크립트를 이용하여 동적으로 원 객체를 생성합니다. 생성된 객체의 속성을 변경하고자 하는 경우에는[SetAttribute\(\)](enusscriptapi_setattribute.md)함수를 이용합니다.



```lua
-- lua
CreateCircle("ID_CIRCLE", 30, 10, 10, 0, 0)
```

```js
// javascript
CreateCircle("ID_CIRCLE", 30, 10, 10, 0, 0);
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    CreateCircle("ID_CIRCLE", 30, 10, 10, 0, 0)
end
```

```js
// JavaScript
function _onmousedown()
{    
    CreateCircle("ID_CIRCLE", 30, 10, 10, 0, 0);
}
```



