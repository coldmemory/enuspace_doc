---
layout: default
title: Create3DCone
parent: Script API
---
# Create3DCone\(id, bottomRadius, height, slices, transx, transy, transz\)

Create3DCone\(\)

#### Parameters

id : id값을 입력합니다.

bottomRadius : 바닥면 반지름값을 입력합니다.

height : 높이값을 입력합니다.

slices : 슬라이스 개수를 입력합니다.

transx : x축의 이동값을 입력합니다.

transy : y축의 이동값을 입력합니다.

transz : z축의 이동값을 입력합니다.

#### Return Value

none

#### Remarks

스크립트를 이용하여 동적으로 콘 객체를 생성합니다. 생성된 객체의 속성을 변경하고자 하는 경우에는 [SetAttribute3D\(\)](./enusscriptapi_setattribute3d.md)함수를 이용합니다.

```lua
-- lua
Create3DCone("ID_CONE", 30, 10, 0, 0, 0)
```

```js
// javascript
Create3DCone("ID_CONE", 30, 10, 0, 0, 0);
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    Create3DCone("ID_CONE", 30, 10, 0, 0, 0)
end
```

```js
// JavaScript
function _onmousedown()
{    
    Create3DCone("ID_CONE", 30, 10, 0, 0, 0);
}
```



