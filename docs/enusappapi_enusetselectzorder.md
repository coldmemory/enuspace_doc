---
layout: default
title: enuSetSelectZOrder
parent: Application API
---
# void enuSetSelectZOrder\(HVIEW pENUView, int iType\)

void enuSetSelectZOrder\(HVIEW pENUView, int iType\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

* int iType

정렬의 타입을 지정합니다. 

#### Return Value

Type : NONE

#### Remarks

선택 객체의 정렬을 수행합니다.

```
#define DEF_BRINGTOFRONT						0
#define DEF_SENDTOBACK							1
#define DEF_BRINGFORWARD						2
#define DEF_SENDBACKWARD						3
```

#### Examples

```cpp
void CenuSpaceView::OnBringToFront()
{
	enuSetSelectZOrder(m_pENUView, DEF_BRINGTOFRONT);
}
void CenuSpaceView::OnSendToBack()
{
	enuSetSelectZOrder(m_pENUView, DEF_SENDTOBACK);
}
void CenuSpaceView::OnBringForward()
{
	enuSetSelectZOrder(m_pENUView, DEF_BRINGFORWARD);
}
void CenuSpaceView::OnSendBackward()
{
	enuSetSelectZOrder(m_pENUView, DEF_SENDBACKWARD);
}
```



