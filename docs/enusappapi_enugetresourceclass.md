---
layout: default
title: enuGetResourceClass
parent: Application API
---
# HSVG enuGetResourceClass\(wchar\_t\* pStrFileName\)

HSVG enuGetResourceClass\(wchar\_t\* pStrFileName\)

#### Parameters {#parameters}

* wchar\_t\* pStrFileName

RESOURCE영역의 SVG 파일을 입력합니다.

#### Return Value {#return-value}

Type : HSVG

RESOURCE영역의 SVG 파일 핸들을 반환합니다.

#### Remarks {#remarks}

RESOURCE의 SVG파일 핸들을 취득하여 RESOURCE의 속성을 변경할 수 있습니다.

#### Examples {#examples}

```cpp
HSVG hsvg = enuGetResourceClass(L"style\\style.svg");
if (hsvg)
{
    // TO DO JOB.
}
```



