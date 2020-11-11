---
layout: default
title: enuInsertDatabase
parent: Application API
last_modified_date: now
---
# void enuInsertDatabase(wchar_t* OrgTagid, wchar_t* strDevicekey, wchar_t* strVariable, wchar_t* strValue, wchar_t* strType = NULL, wchar_t* strPage = NULL, wchar_t* strMode = NULL, wchar_t* strHistory = NULL, wchar_t* strDescription = NULL);

void enuInsertDatabase(wchar_t* OrgTagid, wchar_t* strDevicekey, wchar_t* strVariable, wchar_t* strValue, wchar_t* strType = NULL, wchar_t* strPage = NULL, wchar_t* strMode = NULL, wchar_t* strHistory = NULL, wchar_t* strDescription = NULL);


#### Parameters

* wchar_t* OrgTagid

기존 TAGID를 입력합니다.

*  wchar_t* strDevicekey

DEVICE KEY값을 입력합니다.

* wchar_t* strVariable

VARIABLE값을 입력합니다.

* wchar_t* strValue

VALUE 값을 입력합니다.

* wchar_t* strType

TYPE을 입력합니다.

wchar_t* strPage

PAGENAME을 입력합니다.

wchar_t* strMode

MODE를 입력합니다.

wchar_t* strHistory

HISTORY값을 입력합니다.

wchar_t* strDescription

DESCRIPTION을 입력합니다.

#### Return Value

Type : void

입력한 값들에 의하여 데이터베이스를 추가 한다

#### Remarks

enuInsertDatabase(OrgTagid,strDevicekey,strVariable,strValue, strType,strPage = NULL,strMode = NULL, strHistory = NULL,strDescription = NULL);
TAGID,DEVICEKEY,VARIABLE,VALUE,TYPE값을 받습니다.
입력한 값들에 의하여 데이터베이스에 추가 합니다. 
PAGE,MODE,HISTORY,DESCRIPTION 은 생략 가능합니다.
#### Examples

```cpp
	enuInsertDatabase(OrgTagid,strDevicekey,strVariable,strValue, strType,strPage = NULL,strMode = NULL, strHistory = NULL,strDescription = NULL);
}
```



