---
layout: default
title: Create3DTerrain
parent: Script API
---
# Create3DTerrain\(id, size, subdivision, transx, transy, transz\)

Create3DTerrain\(\)

#### Parameters

id : id값을 입력합니다.

size : 객체의 사이즈값을 입력합니다.

subdivision : Terrain객체의 subdivision의 값을 입력합니다.

transx : x축의 이동값을 입력합니다.

transy : y축의 이동값을 입력합니다.

trnasz : z축의 이동값을 입력합니다.

#### Return Value

none

#### Remarks

스크립트를 이용하여 동적으로 Terrain 객체를 생성합니다. 생성된 객체의 속성을 변경하고자 하는 경우에는 [SetAttribute3D\(\)](./enusscriptapi_setattribute3d.md)함수를 이용합니다.

```lua
-- lua
Create3DTerrain("ID_TERRAIN", 100, 10, 0, 0, 0)
```

```js
// javascript
Create3DTerrain("ID_TERRAIN", 100, 10, 0, 0, 0);
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    Create3DTerrain("ID_TERRAIN", 100, 10, 0, 0, 0)
end
```

```js
// JavaScript
function _onmousedown()
{    
    Create3DTerrain("ID_TERRAIN", 100, 10, 0, 0, 0);
}
```



