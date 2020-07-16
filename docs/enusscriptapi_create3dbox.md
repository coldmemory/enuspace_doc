---
layout: default
title: Create3DBox
parent: Script API
---
# Create3DBox\(id, size, transx, transy, transz\)

Create3DBox\(\)

#### Parameters

id : 객체의 ID

size : 박스의 사이즈

transx : x축의 이동값을 입력합니다.

transy : y축의 이동값을 입력합니다.

transz : z축의 이동값을 입력합니다.

#### Return Value

none

#### Remarks

스크립트를 이용하여 동적으로 객체를 생성합니다. 생성된 객체의 속성을 변경하고자 하는 경우에는 [SetAttribute3D\(\)](./enusscriptapi_setattribute3d.md)함수를 이용합니다.



```lua
-- lua
Create3DBox("ID_BOX", 100, 0, 0, 0)
```

```js
// javascript
Create3DBox("ID_BOX", 100, 0, 0, 0);
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    Create3DBox("ID_BOX", 100, 0, 0, 0)
end
```

```js
// JavaScript
function _onmousedown()
{    
    Create3DBox("ID_BOX", 100, 0, 0, 0);
}
```



