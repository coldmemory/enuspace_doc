---
layout: default
title: enuGetModifyLogic
parent: Application API
---
# bool enuGetModifyLogic\(wchar\_t\* pStrFilename\)

bool enuGetModifyLogic\(wchar\_t\* pStrFilename\)

#### Parameters

* wchar\_t\* pStrFilename

LOGIC영역의 SVG 파일이름을 입력합니다.

#### Return Value

Type : bool

LOGIC영역의 SVG 파일의 변경유무를 반환합니다.

#### Remarks

LOGIC영역의 SVG 파일의 변경유무를 반환합니다.

#### Examples

```cpp
bool bModify = enuGetModifyLogic(L"library\\logic\\logic_symbol.svg");
```



