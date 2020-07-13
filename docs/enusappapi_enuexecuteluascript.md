---
layout: default
title: enuExecuteLuaScript
parent: Application API
---
# wchar\_t\* enuExecuteLuaScript\(wchar\_t\* pStrExecute\)

wchar\_t\* enuExecuteLuaScript\(wchar\_t\* pStrExecute\)

#### Parameters

* wchar\_t\* pStrExecute

실행하고자하는 Lua Script 함수 이름을 입력합니다.

#### Return Value

Type : wchar\_t\*

Lua Script 함수 호출후 Return값을 문자열 형태로 반환받습니다.

#### Remarks

Lua Script 함수를 호출합니다. enuRegisterLuaScript\(\)함수를 통하여 스크립트를 등록하고 enuExecuteLuaScript\(\)함수를 통하여 호출을 수행합니다.

#### Examples

```cpp
CString strScript;

strScript.Format(L"function add()\n\
\tlocal x = 5;\n \
\tlocal y = 6;\n \
\tlocal z = x + y;\n \
\treturn z;\n \
end\n");

// lua script register
enuRegisterLuaScript(strScript.GetBuffer(0));

// lua script execute
CString strValue = enuExecuteLuaScript(L"add()");
// return L"11"
```



