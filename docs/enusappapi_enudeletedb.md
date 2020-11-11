---
layout: default
title: enuDeleteDatabase
parent: Application API
last_modified_date: now
---
# void enuDeleteDatabase(wchar_t* strDeviceKey, wchar_t* strVariable);

void enuDeleteDatabase(wchar_t* strDeviceKey, wchar_t* strVariable);


#### Parameters


*  wchar_t* strDevicekey

DEVICE KEY값을 입력합니다.

* wchar_t* strVariable

VARIABLE값을 입력합니다.


#### Return Value

Type : void

입력한 값들에 의하여 데이터베이스 ROW를 삭제한다

#### Remarks

void enuDeleteDatabase(wchar_t* strDeviceKey, wchar_t* strVariable);
DEVICE KEY 값과 VARIABLE 값을 입력 받습니다.
KEY 와 VARIABLE 값을 이용해 TAGID를 만들고 TAGID를 검색하여 해당 ROW를 삭제한다
#### Examples

```cpp
	void enuDeleteDatabase(strDeviceKey, strVariable);
}
```



