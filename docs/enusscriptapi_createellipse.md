---
layout: default
title: CreateEllipse
parent: Script API
---
# CreateEllipse\(id, rx, ry, cx, cy, transx, transy\)

CreateEllipse\(\)

#### Parameters

id : id값을 입력합니다.

rx : x축의 반지름값을 입력합니다.

ry : y축의 반지름값을 입력합니다.

cx : x축의 센터값을 입력합니다.

cy : y축의 센터값을 입력합니다.

transx : x축의 이동값을 입력합니다.

transy : y축의 이동값을 입력합니다.

#### Return Value

none

#### Remarks

스크립트를 이용하여 동적으로 타원 객체를 생성합니다. 생성된 객체의 속성을 변경하고자 하는 경우에는[SetAttribute\(\)](enusscriptapi_setattribute.md)함수를 이용합니다.

```lua
-- lua
CreateEllipse("ID_ELLIPSE", 5, 10, 10, 10, 0, 0)
```

```js
// javascript
CreateEllipse("ID_ELLIPSE", 5, 10, 10, 10, 0, 0);
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    CreateEllipse("ID_ELLIPSE", 5, 10, 10, 10, 0, 0)
end
```

```js
// JavaScript
function _onmousedown()
{    
    CreateEllipse("ID_ELLIPSE", 5, 10, 10, 10, 0, 0);
}
```



