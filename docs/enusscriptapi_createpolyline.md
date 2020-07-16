---
layout: default
title: CreatePolyline
parent: Script API
---
# CreatePolyline\(id, points, transx, transy\)

CreatePolyline\(\)

#### Parameters

id : id값을 입력합니다.

points : 폴리라인의 좌표를 입력합니다.

transx : x축의 이동값을 입력합니다.

transy : y축의 이동값을 입력합니다.

#### Return Value

none

#### Remarks

스크립트를 이용하여 동적으로 폴리라인 객체를 생성합니다. 생성된 객체의 속성을 변경하고자 하는 경우에는 [SetAttribute\(\)](enusscriptapi_setattribute.md)함수를 이용합니다.

```lua
-- lua
CreatePolyline("ID_PLYLINE" "0,0 46,-39 76,0 108,-37 139,-3", 500, 500)
```

```js
// javascript
CreatePolyline("ID_PLYLINE" "0,0 46,-39 76,0 108,-37 139,-3", 500, 500);
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    CreatePolyline("ID_PLYLINE" "0,0 46,-39 76,0 108,-37 139,-3", 500, 500)
end
```

```js
// JavaScript
function _onmousedown()
{    
    CreatePolyline("ID_PLYLINE" "0,0 46,-39 76,0 108,-37 139,-3", 500, 500);
}
```



