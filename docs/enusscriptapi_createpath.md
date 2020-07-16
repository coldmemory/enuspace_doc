---
layout: default
title: CreatePath
parent: Script API
---
# CreatePath\(id, points, transx, transy\)

CreatePath\(\)

#### Parameters

id : id값을 입력합니다.

points : 패스정보 포인트를 입력합니다. \(ex : "M69.14,67.28 L0.00,67.28 A69.14,67.28 0 1,0 69.14,-0.00 Z"\)

transx : x축의 이동값을 입력합니다.

transy : y축의 이동값을 입력합니다.

#### Return Value

none

#### Remarks

스크립트를 이용하여 동적으로 패스 객체를 생성합니다. 생성된 객체의 속성을 변경하고자 하는 경우에는 [SetAttribute\(\)](enusscriptapi_setattribute.md)함수를 이용합니다.

```lua
-- lua
CreatePath("ID_PATH", "M69.14,67.28 L0.00,67.28 A69.14,67.28 0 1,0 69.14,-0.00 Z", 0, 0)
```

```js
// javascript
CreatePath("ID_PATH", "M69.14,67.28 L0.00,67.28 A69.14,67.28 0 1,0 69.14,-0.00 Z", 0, 0);
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    CreatePath("ID_PATH", "M69.14,67.28 L0.00,67.28 A69.14,67.28 0 1,0 69.14,-0.00 Z", 0, 0)
end
```

```js
// JavaScript
function _onmousedown()
{    
    CreatePath("ID_PATH", "M69.14,67.28 L0.00,67.28 A69.14,67.28 0 1,0 69.14,-0.00 Z", 0, 0);
}
```



