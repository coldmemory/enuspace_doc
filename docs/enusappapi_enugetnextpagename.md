---
layout: default
title: enuGetNextPageName
parent: Application API
---
# wchar\_t\* enuGetNextPageName\(wchar\_t\* pStrFileName\)

wchar\_t\* enuGetNextPageName\(wchar\_t\* pStrFileName\)

#### Parameters

* wchar\_t\* pStrFileName

PICTURE영역에서 SVG 픽쳐파일을 입력합니다.

#### Return Value

Type : wchar\_t\*

다음 픽쳐파일 이름을 반환합니다.

#### Remarks

로드된 픽쳐의 다음 페이지를 반환하는 함수입니다.

#### Examples

```cpp
CString strNextFile = enuGetNextPageName(L"picture\\main.svg");
if (!strNextFile.IsEmpty())
{
    // TO DO JOB
}
```



