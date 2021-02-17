---
layout: default
title: SetSelectGroup
parent: Script API
last_modified_date: now
---

# SetSelectGroup\(\"objects\", (optional)group_id\)

---
SetSelectGroup\(\)

#### Parameters

* objects : 수행하고자 하는 객체의 ID를 입력합니다. 여러개의 객체를 입력하고자 하는경우에는 ","을 이용합니다.

* group_id(optional) : 만들어질 Group의 id를 입력합니다. 그룹의 id를 입력하지 않은 경우 자동생성된 id가 부여됩니다.


#### Return Value
* none

#### Reference
SDK API : 
[void enuSetSelectGroup\(HVIEW pENUView\)](/enusscriptapi_setselectgroup/)

#### Remarks
```lua
-- lua
    SetSelectGroup("ID_OBJ1, ID_OBJ2", "ID_GROUP")
    SetSelectGroup("ID_OBJ1, ID_OBJ2")
```

```js
// JavaScript  
    SetSelectGroup("ID_OBJ1, ID_OBJ2", "ID_GROUP");
    SetSelectGroup("ID_OBJ1, ID_OBJ2");
```
#### Examples


```lua
-- lua
function _onmousedown()
    SetSelectGroup("ID_OBJ1, ID_OBJ2", "ID_GROUP")
end
```

```js
// JavaScript
function _onmousedown()
{    
    SetSelectGroup("ID_OBJ1, ID_OBJ2", "ID_GROUP");
}
```










