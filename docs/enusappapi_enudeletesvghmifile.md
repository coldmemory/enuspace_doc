---
layout: default
title: enuDeleteSvgHmiFile
parent: Application API
---
# bool enuDeleteSvgHmiFile\(wchar\_t\* pStrFileName\)

bool enuDeleteSvgHmiFile\(wchar\_t\* pStrFileName\)

#### Parameters

* wchar\_t\* pStrFileName

HMI 영역의 SVG 파일을 입력합니다. \(ex "hmi\hmi\_symbol.svg"\)

#### Return Value

Type : bool

HMI 영역의 SVG 파일의 정상 제거유무를 반환합니다.

#### Remarks

HMI 영역의 SVG 파일을 제거합니다.

#### Examples

```cpp
enuDeleteSvgHmiFile(L"hmi\\hmi_symbol.svg");
```



