---
layout: default
title: CreateLine
parent: Script API
---
# CreateLine\(id, x1, y1, x2, y2, transx, transy\)

CreateLine\(\)

#### Parameters

id : id값을 입력합니다.

x1 : 첫번째 x의 좌표를 입력합니다.

y1 : 첫번째 y의 좌표를 입력합니다.

x2 : 두번째 x의 좌표를 입력합니다.

y2 : 두번째 y의 좌표를 입력합니다.

transx : x축의 이동값을 입력합니다.

transy : y축의 이동값을 입력합니다.

#### Return Value

none

#### Remarks

스크립트를 이용하여 동적으로 라인 객체를 생성합니다. 생성된 객체의 속성을 변경하고자 하는 경우에는 [SetAttribute\(\)](enusscriptapi_setattribute.md)함수를 이용합니다.

```lua
-- lua
CreateLine("ID_LINE", 0, 0, 100, 100, 0, 0)
```

```js
// javascript
CreateLine("ID_LINE", 0, 0, 100, 100, 0, 0);
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    CreateLine("ID_LINE", 0, 0, 100, 100, 0, 0)
end
```

```js
// JavaScript
function _onmousedown()
{    
    CreateLine("ID_LINE", 0, 0, 100, 100, 0, 0);
}
```



