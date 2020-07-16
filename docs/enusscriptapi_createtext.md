---
layout: default
title: CreateText
parent: Script API
---
# CreateText\(id, x, y, dx, dy, text, transx, transy\)

CreateText\(\)

#### Parameters

id : id값을 입력합니다.

x : x의 좌표를 입력합니다.

y : y의 좌표를 입력합니다.

dx : dx의 값을 입력합니다.

dy : dy의 값을 입력합니다.

text : 문자열 값을 입력합니다.

transx : x축의 이동값을 입력합니다.

transy : y축의 이동값을 입력합니다.

#### Return Value

none

#### Remarks

스크립트를 이용하여 동적으로 텍스트 객체를 생성합니다. 생성된 객체의 속성을 변경하고자 하는 경우에는 [SetAttribute\(\)](enusscriptapi_setattribute.md)함수를 이용합니다.

```lua
-- lua
CreateText("ID_TEXT", 100, 100, 0, 0, "Input the Text", 300, 300)
```

```js
// javascript
CreateText("ID_TEXT", 100, 100, 0, 0, "Input the Text", 300, 300);
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    CreateText("ID_TEXT", 100, 100, 0, 0, "Input the Text", 300, 300)
end
```

```js
// JavaScript
function _onmousedown()
{    
    CreateText("ID_TEXT", 100, 100, 0, 0, "Input the Text", 300, 300);
}
```



