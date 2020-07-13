---
layout: default
title: enuDeleteSvgResourceFile
parent: Application API
---
# bool enuDeleteSvgResourceFile\(wchar\_t\* pStrFileName\)

bool enuDeleteSvgResourceFile\(wchar\_t\* pStrFileName\)

#### Parameters

* wchar\_t\* pStrFileName

리소스 영역의 SVG 파일을 입력합니다. \(ex "style\\style.svg"\)

#### Return Value

Type : bool

리소스 영역의 SVG 파일의 정상 제거유무를 반환합니다.

#### Remarks

리소스 영역의 SVG 파일을 제거합니다.

#### Examples

```cpp
enuDeleteSvgGlobalFile(L"style\\style.svg");
```



