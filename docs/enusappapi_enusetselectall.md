---
layout: default
title: enuSetSelectAll
parent: Application API
---
# void enuSetSelectAll\(HVIEW pENUView\)

void enuSetSelectAll\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

뷰의 모든객체를 선택합니다.

#### Return Value

Type : NONE

#### Remarks

편집모드시 뷰의 모든 객체를 선택합니다.

#### Examples

```cpp
void CenuSpaceView::OnEditSelectAll()
{
	enuSetSelectAll(m_pENUView);
}
```



