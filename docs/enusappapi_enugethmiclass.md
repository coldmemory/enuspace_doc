---
layout: default
title: enuGetHmiClass
parent: Application API
---
# HSVG enuGetHmiClass\(wchar\_t\* pStrFileName\)

HSVG enuGetHmiClass\(wchar\_t\* pStrFileName\)

#### Parameters

* wchar\_t\* pStrFileName

HMI영역의 SVG 파일을 입력합니다.

#### Return Value

Type : HSVG

HMI영역의 SVG 파일 핸들을 반환합니다.

#### Remarks

HMI의 SVG파일 핸들을 취득하여 HMI 심볼의 속성을 변경할 수 있습니다.

#### Examples

```cpp
HSVG hsvg = enuGetHmiClass(L"library\\hmi\\hmi_symbol.svg");
if (hsvg)
{
    // TO DO JOB.
}
```



