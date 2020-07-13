---
layout: default
title: enuExecuteJavaScript
parent: Application API
---
# wchar\_t\* enuExecuteJavaScript\(wchar\_t\* pStrExecute\)

wchar\_t\* enuExecuteJavaScript\(wchar\_t\* pStrExecute\)

#### Parameters

* wchar\_t\* pStrExecute

실행하고자하는 JavaScript 함수 이름을 입력합니다.

#### Return Value

Type : wchar\_t\*

JavaScript 함수 호출후 Return값을 문자열 형태로 반환받습니다.

#### Remarks

JavaScript 함수를 호출합니다. enuRegisterJavaScript\(\)함수를 통하여 스크립트를 등록하고 enuExecuteJavaScript\(\)함수를 통하여 호출을 수행합니다.



#### Examples

```cpp
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
```



