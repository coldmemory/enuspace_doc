---
layout: default
title: enuGetModifyPage
parent: Application API
---
# bool enuGetModifyPage\(wchar\_t\* pStrFilename\)

bool enuGetModifyPage\(wchar\_t\* pStrFilename\)

#### Parameters

* wchar\_t\* pStrFilename

PICTURE영역의 SVG 파일이름을 입력합니다.

#### Return Value

Type : bool

PICTURE영역의 SVG 파일의 변경유무를 반환합니다.

#### Remarks

PICTURE영역의 SVG 파일의 변경유무를 반환합니다.

#### Examples

```cpp
bool bModify = enuGetModifyPage(L"picture\\picture.svg");
```



