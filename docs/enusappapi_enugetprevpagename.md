---
layout: default
title: enuGetPrevPageName
parent: Application API
---
# wchar\_t\* enuGetPrevPageName\(wchar\_t\* pStrFileName\)

wchar\_t\* enuGetPrevPageName\(wchar\_t\* pStrFileName\)

#### Parameters

* wchar\_t\* pStrFileName

PICTURE영역에서 SVG 픽쳐파일을 입력합니다.

#### Return Value

Type : wchar\_t\*

이전 픽쳐파일 이름을 반환합니다.

#### Remarks

로드된 픽쳐의 이전 페이지를 반환하는 함수입니다.

#### Examples

```cpp
CString strPrevFile = enuGetPrevPageName(L"picture\\main.svg");
if (!strPrevFile.IsEmpty())
{
    // TO DO JOB
}
```



