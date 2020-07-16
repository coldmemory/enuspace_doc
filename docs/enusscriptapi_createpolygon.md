---
layout: default
title: CreatePolygon
parent: Script API
---
# CreatePolygon\(id, points, transx, transy\)

CreatePolygon\(\)

#### Parameters

id : id값을 입력합니다.

points : 포인트의 좌표를 입력합니다.

transx : x축의 이동값을 입력합니다.

transy : y축의 이동값을 입력합니다.

#### Return Value

none

#### Remarks

스크립트를 이용하여 동적으로 폴리곤 객체를 생성합니다. 생성된 객체의 속성을 변경하고자 하는 경우에는 [SetAttribute\(\)](enusscriptapi_setattribute.md)함수를 이용합니다.

```lua
-- lua
CreatePolygon("ID_POLYGON", "0,0 90,-34 133,-4 179,-35 243,-3 127,40.", 300, 300)
```

```js
// javascript
CreatePolygon("ID_POLYGON", "0,0 90,-34 133,-4 179,-35 243,-3 127,40.", 300, 300);
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    CreatePolygon("ID_POLYGON", "0,0 90,-34 133,-4 179,-35 243,-3 127,40.", 300, 300)
end
```

```js
// JavaScript
function _onmousedown()
{    
    CreatePolygon("ID_POLYGON", "0,0 90,-34 133,-4 179,-35 243,-3 127,40.", 300, 300);
}
```



