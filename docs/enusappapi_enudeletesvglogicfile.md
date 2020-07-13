---
layout: default
title: enuDeleteSvgLogicFile
parent: Application API
---
# bool enuDeleteSvgLogicFile\(wchar\_t\* pStrFileName\)

bool enuDeleteSvgLogicFile\(wchar\_t\* pStrFileName\)

#### Parameters

* wchar\_t\* pStrFileName

LOGIC 영역의 SVG 파일을 입력합니다. \(ex "logic\logic\_symbol.svg"\)

#### Return Value

Type : bool

LOGIC 영역의 SVG 파일의 정상 제거유무를 반환합니다.

#### Remarks

LOGIC 영역의 SVG 파일을 제거합니다.

#### Examples

```cpp
enuDeleteSvgHmiFile(L"logic\\logic_symbol.svg");
```



