---
layout: default
title: SetSelectGroup
parent: Script API
last_modified_date: now
---

# SetSelectGroup\(\"objects\", group_id\)

---
SetSelectGroup\(\)

#### Parameters

* objects : 그룹핑을 수행하고자 하는 객체의 ID를 입력합니다. 그래픽 객체 ID 정보를 "," 단위로 입력합니다.

* group_id(optional) : 생성된 Group 객체의 ID를 입력합니다. 그룹의 ID를 입력하지 않은 경우 자동생성된 ID가 부여됩니다.


#### Return Value

* none

#### Reference

* SDK API : [void enuSetSelectGroup\(HVIEW pENUView\)](/enuspace_doc/docs/enusappapi_enusetselectgroup/)

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










