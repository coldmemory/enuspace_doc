---
layout: default
title: enuSetGlobalValue
parent: Application API
---
# void enuSetGlobalValue\(HSVG pSvgHandler, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)

void enuSetGlobalValue\(HSVG pSvgHandler, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)

#### Parameters

* HSVG pSvgHandler

GLOBAL영역의 SVG 핸들을 입력합니다.

* wchar\_t\* pStrVariable

변수 정보를 입력합니다.

* wchar\_t\* pStrValue

변수 값을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

GLOBAL영역의 변수값을 설정하는 함수입니다.

#### Examples

```cpp
void SetGlobalValue()
{
    enuSetGlobalValue(hsvg, L"g_input1", L"10");
}
```



