---
layout: default
title: enuCreatePopupTrend
parent: Application API
---
# void\* enuCreatePopupTrend\(int iType, wchar\_t\* strVariables, int x = 0, int y = 0, int width = 0, int height = 0\)

void\* enuCreatePopupTrend\(int iType, wchar\_t\* strVariables, int x = 0, int y = 0, int width = 0, int height = 0\)

#### Parameters

* int iType

Trend의 변수 타입정보를 입력합니다. \(DB Tag : DEF\_CHART\_DB, 로직변수 : DEF\_CHART\_LOGIC\)

* wchar\_t\* strVariables

변수명을 입력합니다.

* int x = 0

Popup Trend의 x좌표 포지션을 입력합니다.

* int y = 0

Popup Trend의 y좌표 포지션을 입력합니다.

* int width = 0

Popup Trend의 넓이값을 입력합니다.

* int height = 0

Popup Trend의 높이값을 입력합니다.

#### Return Value

Type : 생성된 Trend 클래스를 반환합니다.

#### Remarks

동적으로 팝업 Trend를 이용하여 변수를 현시하고자 하는 경우에 본함수를 적용합니다.

#### Examples

```cpp
enuCreatePopupTrend(DEF_CHART_LOGIC, L"ID_ADD.output");            // logic variable

enuCreatePopupTrend(DEF_CHART_DB, L"@CORE.output");                // db variable
```



