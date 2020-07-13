---
layout: default
title: enuDeleteSvgPageFile
parent: Application API
---
# bool enuDeleteSvgPageFile\(wchar\_t\* pStrFileName\)

bool enuDeleteSvgPageFile\(wchar\_t\* pStrFileName\)

#### Parameters

* wchar\_t\* pStrFileName

Picture 영역의 SVG 파일을 입력합니다. \(ex "picture\\picture1.svg"\)

#### Return Value

Type : bool

Picture 영역의 SVG 파일의 정상 제거유무를 반환합니다.

#### Remarks

Picture 영역의 SVG 파일을 제거합니다.

#### Examples

```cpp
enuDeleteSvgPageFile(L"picture\\picture.svg");
```



