---
layout: default
title: DeleteDatabase
parent: Script API
last_modified_date: now
---
# DeleteDatabase(wchar_t* tagid);

DeleteDatabase(wchar_t* tagid);


#### Parameters


*  wchar_t* tagid

tagid값을 입력합니다.


#### Return Value

Type : void

입력한 값에 의하여 데이터베이스 ROW를 삭제한다

#### Remarks

```js
// javascript
DeleteDatabase(wchar_t* tagid);
```

#### Examples


```js
// JavaScript
function _onmousedown()
{    
    DeleteDatabase(tagid);
}
```