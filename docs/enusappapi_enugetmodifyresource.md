---
layout: default
title: enuGetModifyResource
parent: Application API
---
# bool enuGetModifyResource\(wchar\_t\* pStrFilename\)

bool enuGetModifyResource\(wchar\_t\* pStrFilename\)

#### Parameters

* wchar\_t\* pStrFilename

RESOURCE영역의 SVG 파일이름을 입력합니다.

#### Return Value

Type : bool

RESOURCE영역의 SVG 파일의 변경유무를 반환합니다.

#### Remarks

RESOURCE영역의 SVG 파일의 변경유무를 반환합니다.

#### Examples

```cpp
bool bModify = enuGetModifyResource(L"style\\style.svg");
```



