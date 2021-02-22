---
layout: default
title: DeleteObject
parent: Script API
last_modified_date: now
---
# DeleteObject\(objects\)

DeleteObject\(\)


#### Parameters

* objects : 제거하고자 하는 객체의 ID를 입력합니다. 여러개의 객체를 입력하고자 하는경우에는 ","을 이용합니다.

#### Return Value

* none

#### Remarks

* javascript, lua 스크립트를 통하여 객체를 동적으로 제거합니다.

#### Reference

* SDK API : [void enuDeleteObjectByName\(HSVG pSvg, wchar_t* pVariable\)](/enuspace_doc/docs/enusappapi_enudeleteobjectbyname/)

#### Examples

JavaScript

```js
// javascript
function setvalue_package()
{
    DeleteObject("ID_OBJ1, ID_OBJ2");    
}
```

```lua
-- lua
function _onmousedown()
    DeleteObject("ID_OBJ1, ID_OBJ2")
end
```





