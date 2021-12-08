---
layout: default
title: enuDeleteFunction
parent: Application API
last_modified_date: now
---
# bool enuDeleteFunction\(wchar\_t\* strFunction, int \(\*pfunc\)\(lua\_State\* L\)\)

bool enuDeleteFunction\(wchar\_t\* strFunction, int \(\*pfunc\)\(lua\_State\* L\)\);

#### 

#### Parameters

Type : wchar\_t\* strFunctionName

스크립트에서 제거할 함수 이름을 지정한다.

Type : lua\_state\* functionPointer

스크립트에서 제거되는 함수포인터값을 지정한다.



#### Return Value

Type : bool

외부 함수 제거 여부를 제공한다. 

#### 

#### Examples

```cpp
#define USE_SDK
#include "enuspace_sdk/x64/header/enuLibrary.h"

int AddFunction(lua_State *L)
{
	const char* str;
	str = luaL_checkstring(L,1);
	CString strPageName(str);

	str = luaL_checkstring(L,2);
	CString strScriptName(str);

	int iInput1 = luaL_checknumber(L,3);
	int iInput2 = luaL_checknumber(L,4);
	int iReturn = iInput1 + iInput2;
	lua_pushnumber(L, iReturn);

	return 1;
}

extern "C" __declspec(dllexport) bool OnUnload()
{
	enuDeleteFunction(L"AddFunction", AddFunction);
	return true;
}

extern "C" __declspec(dllexport) bool OnLoad()
{
	enuRegisterFunction(L"AddFunction", AddFunction);
	return true;
}
```

#### 참조

 [ bool enuRegisterFunction\(wchar\_t\* strFunction, int \(\*pfunc\)\(lua\_State\* L\)\)](./sdk_api_enuregisterfunction.md)
 [ SDK 인터페이스\외부함수 등록 ](./dev_externalfunction.md)