---
layout: default
title: enuRegisterJavaScript
parent: Application API
---
# bool enuRegisterJavaScript\(wchar\_t\* pStrScript\)

bool enuRegisterJavaScript\(wchar\_t\* pStrScript\)

#### Parameters

* wchar\_t\* pStrScript

자바 스크립트의 내용을 입력합니다.

#### Return Value

Type : bool

자바 스크립트의 정상 등록여부를 반환합니다.

#### Remarks

자바 스크립트를 등록하고 호출을 수행합니다.

#### Examples

```cpp
void OnRegisterScript()
{
    CString strScript;

    strScript.Format(L"function add()\n\
    \{\n \
    \t var x = 5;\n \
    \t var y = 6;\n \
    \t var z = x + y;\n \
    \t return z;\n \
    }\n");

    // java script register
    enuRegisterJavaScript(strScript.GetBuffer(0));

    // java script execute
    enuExecuteJavaScript(L"add()");
}
```



