---
layout: default
title: SetSelectGroup
parent: Script API
last_modified_date: now
---

# BringForwardObject\(objects\)

---
SetSelectGroup\(\)

#### Parameters

objects

수행하고자 하는 객체의 ID를 입력합니다. 여러개의 객체를 입력하고자 하는경우에는 ","을 이용합니다.

#### Return Value

none
#### Remarks
```lua
-- lua
    SetSelectGroup("ID_OBJ1, ID_OBJ2")
```

```js
// JavaScript  
    SetSelectGroup_JS("ID_OBJ1, ID_OBJ2")
```
#### Examples


```lua
-- lua
function _onmousedown()
    SetSelectGroup("ID_OBJ1, ID_OBJ2")
end
```

```js
// JavaScript
function _onmousedown()
{    
    SetSelectGroup_JS("ID_OBJ1, ID_OBJ2")
}
```










