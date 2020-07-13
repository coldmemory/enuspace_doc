---
layout: default
title: enuIsSelectObject
parent: Application API
---
# bool enuIsSelectObject\(HVIEW pENUView\)

bool enuIsSelectObject\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

#### Return Value

Type : bool

선택 객체의 여부를 반환합니다.

#### Remarks

선택된 객체가 있는 경우 true를 반환합니다. 선택 객체가 없는 경우 false를 반환합니다.

#### Examples

```cpp
void CenuSpaceView::OnUpdateEditDelete(CCmdUI* pCmdUI)
{
	bool bEnable = enuIsSelectObject(m_pENUView);
	pCmdUI->Enable(bEnable);
}
```



