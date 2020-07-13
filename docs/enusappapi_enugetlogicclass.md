---
layout: default
title: enuGetLogicClass
parent: Application API
---
# HSVG enuGetLogicClass\(wchar\_t\* pStrFileName\)

HSVG enuGetLogicClass\(wchar\_t\* pStrFileName\)

#### Parameters

* wchar\_t\* pStrFileName

LOGIC영역의 SVG 파일을 입력합니다.

#### Return Value

Type : HSVG

LOGIC영역의 SVG 파일 핸들을 반환합니다.

#### Remarks

LOGIC의 SVG파일 핸들을 취득하여 LOGIC심볼의 속성을 변경할 수 있습니다.

#### Examples

```cpp
HSVG hsvg = enuGetLogicClass(L"library\\logic\\logic_symbol.svg");
if (hsvg)
{
    // TO DO JOB.
}
```



