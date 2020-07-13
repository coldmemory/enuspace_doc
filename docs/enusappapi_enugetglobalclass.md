---
layout: default
title: enuGetGlobalClass
parent: Application API
---
# HSVG enuGetGlobalClass\(wchar\_t\* pStrFileName\)

HSVG enuGetGlobalClass\(wchar\_t\* pStrFileName\)

#### Parameters

* wchar\_t\* pStrFileName

Global영역의 SVG 파일을 입력합니다.

#### Return Value

Type : HSVG

Global영역의 SVG 핸들을 반환합니다.

#### Remarks

Global영역의 SVG핸들을 반환합니다.

#### Examples

```cpp
HSVG hsvg = enuGetGlobalClass(L"global\\global.svg");
```



