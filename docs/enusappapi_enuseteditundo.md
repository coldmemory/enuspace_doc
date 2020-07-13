---
layout: default
title: enuSetEditUndo
parent: Application API
---
# void enuSetEditUndo\(HVIEW pENUView\)

void enuSetEditUndo\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

Undo 명령을 수행합니다. 

#### Examples

```cpp
void CenuSpaceView::OnEditUndo()
{
	enuSetEditUndo(m_pENUView);
}
```



