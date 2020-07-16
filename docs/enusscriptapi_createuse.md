---
layout: default
title: CreateUse
parent: Script API
---
# CreateUse\(id, x, y, href, type, transx, transy\)

CreateUse\(\)

#### Parameters

id : id값을 입력합니다.

x : x축의 값을 입력합니다.

y : y축의 값을 입력합니다.

href : 정의된 심볼이름을 입력합니다. \(ex. \#ID\_GAUGE\)

type : 정의된 심볼의 타입을 입력합니다. \(hmi, logic\)

transx : x축의 이동값을 입력합니다.

transy : y축의 이동값을 입력합니다.

#### Return Value

none

#### Remarks

스크립트를 이용하여 동적으로 라인 객체를 생성합니다. 생성된 객체의 속성을 변경하고자 하는 경우에는 [SetAttribute\(\)](enusscriptapi_setattribute.md)함수를 이용합니다.

```lua
-- lua
CreateUse("ID_USE", 0, 0, "#ID_GAUGE", "hmi", 300, 300)
```

```js
-- javascript
CreateUse("ID_USE", 0, 0, "#ID_GAUGE", "hmi", 300, 300);
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    CreateUse("ID_USE", 0, 0, "#ID_GAUGE", "hmi", 300, 300)
end
```

```js
// JavaScript
function _onmousedown()
{    
    CreateUse("ID_USE", 0, 0, "#ID_GAUGE", "hmi", 300, 300);
}
```



