---
layout: default
title: enuSetEditDelete
parent: Application API
---
# void enuSetEditDelete\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

Delete 명령을 수행합니다. 선택 객체에 대하여 제거 루틴을 수행합니다. 

#### Examples

```cpp
void CenuSpaceView::OnEditDelete()
{
	enuSetEditDelete(m_pENUView);
}
```



