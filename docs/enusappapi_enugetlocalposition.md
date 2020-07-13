---
layout: default
title: enuGetLocalPosition
parent: Application API
---
# POINTF enuGetLocalPosition\(HVIEW pENUView, POINT point\)

POINTF enuGetLocalPosition\(HVIEW pENUView, POINT point\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

* POINT point

Desktop기준의 좌표값을 입력합니다.

#### Return Value

Type : POINTF

뷰기준의 좌표값을 반환합니다.

#### Remarks

Desktop기준의 좌표를 View기준의 좌표로 반환합니다.

#### Examples

```cpp
POINT point;
point.x = 400;
point.y = 400;
POINTF calPos = enuGetLocalPosition(m_pENUView, point);
```



