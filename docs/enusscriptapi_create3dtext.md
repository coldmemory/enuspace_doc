---
layout: default
title: Create3DText
parent: Script API
---
# Create3DText\(id, text, style, fontsize, transx, transy, transz\)

Create3DText\(\)

#### Parameters

id : id값을 입력합니다.

text : 디스플리에할 문자열을 입력합니다.

style : 폰트 스타일을 입력합니다. "BOLD", "ITALIC", "BOLDITALIC"

fontsize : 폰트 사이즈를 입력합니다.

transx : x축의 이동값을 입력합니다.

transy : y축의 이동값을 입력합니다.

transz :  z축의 이동값을 입력합니다.

#### Return Value

none

#### Remarks

스크립트를 이용하여 동적으로 라인집합 객체를 생성합니다. 생성된 객체의 속성을 변경하고자 하는 경우에는 [SetAttribute3D\(\)](./enusscriptapi_setattribute3d.md)함수를 이용합니다.

```lua
-- lua
Create3DText("ID_TEXT", "Input the text", "BOLD", 20, 0, 0, 0)
```

```js
// javascript
Create3DText("ID_TEXT", "Input the text", "BOLD", 20, 0, 0, 0);
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    Create3DText("ID_TEXT", "Input the text", "BOLD", 20, 0, 0, 0)
end
```

```js
// JavaScript
function _onmousedown()
{    
    Create3DText("ID_TEXT", "Input the text", "BOLD", 20, 0, 0, 0);
}
```



