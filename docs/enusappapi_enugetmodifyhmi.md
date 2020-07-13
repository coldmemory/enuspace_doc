---
layout: default
title: enuGetModifyHmi
parent: Application API
---
# bool enuGetModifyHmi\(wchar\_t\* pStrFilename\)

bool enuGetModifyHmi\(wchar\_t\* pStrFilename\)

#### Parameters

* wchar\_t\* pStrFilename

HMI영역의 SVG 파일이름을 입력합니다.

#### Return Value

Type : bool

HMI영역의 SVG 파일의 변경유무를 반환합니다.

#### Remarks

HMI영역의 SVG 파일의 변경유무를 반환합니다.

#### Examples

```cpp
bool bModify = enuGetModifyHmi(L"library\\hmi\\hmi_symbol.svg");
```



