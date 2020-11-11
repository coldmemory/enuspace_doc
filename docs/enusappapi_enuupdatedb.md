---
layout: default
title: enuUpdateDatabase
parent: Application API
last_modified_date: now
---
# void enuUpdateDatabase(wchar_t* OrgTagid, wchar_t* strDevicekey, wchar_t* strVariable, wchar_t* strValue, wchar_t* strType = NULL, wchar_t* strPage = NULL, wchar_t* strMode = NULL, wchar_t* strHistory = NULL, wchar_t* strDescription = NULL);

void enuUpdateDatabase(wchar_t* OrgTagid, wchar_t* strDevicekey, wchar_t* strVariable, wchar_t* strValue, wchar_t* strType = NULL, wchar_t* strPage = NULL, wchar_t* strMode = NULL, wchar_t* strHistory = NULL, wchar_t* strDescription = NULL);


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

입력한 값들에 의하여 데이터베이스를 업데이트 한다

#### Remarks

enuUpdateDatabase(OrgTagid,strDevicekey,strVariable,strValue, strType = NULL,strPage = NULL,strMode = NULL, strHistory = NULL,strDescription = NULL);
TAGID,DEVICEKEY,VARIABLE,VALUE값을 받습니다.
DEVICE KEY 와 VARIABLE 중 하나라도 변경이 된다면 디바이스 정보를 제거하고 새로운 정보를 만든다. 
TYPE,PAGE,MODE,HISTORY,DESCRIPTION 은 생략 가능합니다.
#### Examples

```cpp
	enuUpdateDatabase(OrgTagid,strDevicekey,strVariable,strValue, strType = NULL,strPage = NULL,strMode = NULL, strHistory = NULL,strDescription = NULL);
}
```



