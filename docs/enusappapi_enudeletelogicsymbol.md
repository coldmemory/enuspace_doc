---
layout: default
title: enuDeleteLogicSymbol
parent: Application API
---
# bool enuDeleteLogicSymbol\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)

bool enuDeleteLogicSymbol\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)

#### Parameters

* wchar\_t\* pStrFilename

SVG Logic 심볼 정의 픽쳐 파일이름을 입력합니다. \(ex L"library\logic\hmi\_symbol.svg"\)

* wchar\_t\* pStrSymbol

Logic 심볼 정의 이름을 입력합니다.

#### Return Value

Type : bool

Logic 심볼 제거 정상 유무를 반환합니다.

#### Remarks

Logic 심볼정의 파일에 대하여 심볼 제거 명령을 수행합니다.

#### Examples

```cpp
enuDeleteHmiSymbol(L"library\\logic\\logic_symbol.svg", L"AND");
```



