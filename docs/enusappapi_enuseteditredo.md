---
layout: default
title: enuSetEditRedo
parent: Application API
---
# void enuSetEditRedo\(HVIEW pENUView\)

void enuSetEditRedo\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

Redo 명령을 수행합니다. 

#### Examples

```cpp
void CenuSpaceView::OnEditRedo()
{
	enuSetEditRedo(m_pENUView);
}
```



