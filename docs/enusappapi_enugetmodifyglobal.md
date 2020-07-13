---
layout: default
title: enuGetModifyGlobal
parent: Application API
---
# bool enuGetModifyGlobal\(wchar\_t\* pStrFilename\)

bool enuGetModifyGlobal\(wchar\_t\* pStrFilename\)

#### Parameters

* wchar\_t\* pStrFilename

GLOBAL영역의 SVG 파일이름을 입력합니다.

#### Return Value

Type : bool

GLOBAL영역의 SVG 파일의 변경유무를 반환합니다.

#### Remarks

GLOBAL영역의 SVG 파일의 변경유무를 반환합니다.

#### Examples

```cpp
bool bModify = enuGetModifyGlobal(L"global\\global.svg");
```



