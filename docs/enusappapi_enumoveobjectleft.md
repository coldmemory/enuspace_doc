---
layout: default
title: enuMoveObjectLeft
parent: Application API
---
# void enuMoveObjectLeft\(HVIEW pENUView\)

void enuMoveObjectLeft\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

선택객체에 대하여 왼쪽방향으로 한스탭 이동 명령을 수행합니다.

#### Examples

```cpp
void CenuSpaceView::OnMoveLeft()
{
	enuMoveObjectLeft(m_pENUView);
}
```



