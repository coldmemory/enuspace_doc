---
layout: default
title: enuUpdateDatabase
parent: Application API
last_modified_date: now
---
# void enuUpdateDatabase(wchar_t* OrgTagid, wchar_t* strValue);

void enuUpdateDatabase(wchar_t* OrgTagid, wchar_t* strValue);


#### Parameters

* wchar_t* OrgTagid

기존 TAGID를 입력합니다.

* wchar_t* strValue

VALUE 값을 입력합니다.


#### Return Value

Type : void

입력한 값들에 의하여 데이터베이스를 업데이트 한다

#### Remarks

enuUpdateDatabase(OrgTagid, strValue);
TAGID, VALUE값을 받습니다. 

#### Examples

```cpp
	enuUpdateDatabase(OrgTagid,strValue);
}
```



