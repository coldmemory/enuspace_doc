---
layout: default
title: enuMoveObjectRight
parent: Application API
---
# void enuMoveObjectRight\(HVIEW pENUView\)

void enuMoveObjectRight\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

선택객체에 대하여 오른쪽방향으로 한스탭 이동 명령을 수행합니다.

#### Examples

```cpp
void CenuSpaceView::OnMoveRight()
{
	enuMoveObjectRight(m_pENUView);
}
```



