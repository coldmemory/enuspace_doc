---
layout: default
title: CreateImage
parent: Script API
---
# CreateImage\(id, x, y, width, height, href, transx, transy\)

CreateImage\(\)

#### Parameters

id : id값을 입력합니다.

x : x축의 좌표를 입력합니다.

y : y축의 좌표를 입력합니다.

width : 폭의 값을 입력합니다.

height : 높이의 값을 입력합니다.

href : 이미지 파일의 파일이름을 입력합니다.

transx : x축의 이동값을 입력합니다.

transy : y축의 이동값을 입력합니다.

#### Return Value

none

#### Remarks

스크립트를 이용하여 동적으로 이미지 객체를 생성합니다. 생성된 객체의 속성을 변경하고자 하는 경우에는 [SetAttribute\(\)](enusscriptapi_setattribute.md)함수를 이용합니다.

```lua
-- lua
CreateImage("ID_IMAGE", 0, 0, 100, 60, "resource\\image.png", 0, 0)
```

```js
// javascript
CreateImage("ID_IMAGE", 0, 0, 100, 60, "resource\\image.png", 0, 0);
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    CreateImage("ID_IMAGE", 0, 0, 100, 60, "resource\\image.png", 0, 0)
end
```

```js
// JavaScript
function _onmousedown()
{    
    CreateImage("ID_IMAGE", 0, 0, 100, 60, "resource\\image.png", 0, 0);
}
```



