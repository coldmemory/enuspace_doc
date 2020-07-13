---
layout: default
title: enuSetSelectFlip
parent: Application API
---
# void enuSetSelectFlip\(HVIEW pENUView, int iType\)

void enuSetSelectFlip\(HVIEW pENUView, int iType\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

* int iType

FLIP의 타입을 입력합니다. \(DEF\_FLIP\_VERTICAL or DEF\_FLIP\_HORIZONTAL\)

#### Return Value

Type : NONE

#### Remarks

선택 객체의 FLIP 설정을 수행합니다.

#### Examples

```cpp
void CenuSpaceView::OnRotateFlipVer()
{
	enuSetSelectFlip(m_pENUView, DEF_FLIP_VERTICAL);
}
void CenuSpaceView::OnRotateFlipHor()
{
	enuSetSelectFlip(m_pENUView, DEF_FLIP_HORIZONTAL);
}
```



