---
layout: default
title: enuRegisterLuaScript
parent: Application API
---
# bool enuRegisterLuaScript\(wchar\_t\* pStrScript\)

bool enuRegisterLuaScript\(wchar\_t\* pStrScript\)

#### Parameters

* wchar\_t\* pStrScript

루아 스크립트의 내용을 입력합니다.

#### Return Value

Type : bool

루아 스크립트의 정상 등록여부를 반환합니다.

#### Remarks

루아 스크립트를 등록하고 호출을 수행합니다. 

reference 

```
enuExecuteLuaScript()
```

#### Examples

```cpp
void OnRegisterScript()
{
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
}
```



