---
layout: default
title: enuDeleteSvgGlobalFile
parent: Application API
---
# bool enuDeleteSvgGlobalFile\(wchar\_t\* pStrFileName\)

bool enuDeleteSvgGlobalFile\(wchar\_t\* pStrFileName\)

#### Parameters

* wchar\_t\* pStrFileName

글러벌 영역의 SVG 파일을 입력합니다. \(ex "global\global.svg"\)

#### Return Value

Type : bool

글러벌 영역의 SVG 파일의 정상 제거유무를 반환합니다.

#### Remarks

글러벌 영역의 SVG 파일을 제거합니다.

#### Examples

```cpp
enuDeleteSvgGlobalFile(L"global\\global.svg");
```



