---
layout: default
title: Create3DLineSet
parent: Script API
---
# Create3DLineSet\(id, points, transx, transy, transz\)

Create3DLineSet\(\)

#### Parameters

id : id값을 입력합니다.

points : 좌표값을 입력합니다.

transx : x축의 이동값을 입력합니다.

transy : y축의 이동값을 입력합니다.

transz : z축의 이동값을 입력합니다.

#### Return Value

none

#### Remarks

스크립트를 이용하여 동적으로 라인집합 객체를 생성합니다. 생성된 객체의 속성을 변경하고자 하는 경우에는 [SetAttribute3D\(\)](./enusscriptapi_setattribute3d.md)함수를 이용합니다.

```lua
-- lua
local points = "-10 -5 0 -9 -5 1 -8 -5 2 -7 -5 3 -6 -5 8 -5 -5 2 -4 -5 9 -3 -5 1 -2 -5 5 -1 -5 7 0 0 5 1 5 3 2 5 3 3 5 6 4 5 1 5 5 10 6 5 6 7 5 9 8 5 2 9 5 7 10 5 2"
Create3DLineSet("ID_LINESET", points, 0, 0, 0)
```

```js
-- javascript
var points = "-10 -5 0 -9 -5 1 -8 -5 2 -7 -5 3 -6 -5 8 -5 -5 2 -4 -5 9 -3 -5 1 -2 -5 5 -1 -5 7 0 0 5 1 5 3 2 5 3 3 5 6 4 5 1 5 5 10 6 5 6 7 5 9 8 5 2 9 5 7 10 5 2";
Create3DLineSet("ID_LINESET", points, 0, 0, 0);
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    local points = "-10 -5 0 -9 -5 1 -8 -5 2 -7 -5 3 -6 -5 8 -5 -5 2 -4 -5 9 -3 -5 1 -2 -5 5 -1 -5 7 0 0 5 1 5 3 2 5 3 3 5 6 4 5 1 5 5 10 6 5 6 7 5 9 8 5 2 9 5 7 10 5 2"
    Create3DLineSet("ID_LINESET", points, 0, 0, 0)
end
```

```js
// JavaScript
function _onmousedown()
{    
    var points = "-10 -5 0 -9 -5 1 -8 -5 2 -7 -5 3 -6 -5 8 -5 -5 2 -4 -5 9 -3 -5 1 -2 -5 5 -1 -5 7 0 0 5 1 5 3 2 5 3 3 5 6 4 5 1 5 5 10 6 5 6 7 5 9 8 5 2 9 5 7 10 5 2";
    Create3DLineSet("ID_LINESET", points, 0, 0, 0);
}
```



