---
layout: default
title: enuSetSelectToolBar
parent: Application API
---
# void enuSetSelectToolBar\(int iSel\)

void enuSetSelectToolBar\(int iSel\)

#### Parameters

* int iSel

2D 객체의 선택 객체를 지정합니다.

#### Return Value

Type : NONE

#### Remarks

편집모드에서 2D 객체를 생성하기 위한 객체 타입을 지정합니다. 뷰에 마우스 다운시 해당객체가 생성됩니다.



#### Examples

```cpp
void CMainFrame::SetSelectToolBar(int iSel, bool bFlag)
{
	m_iSelToolbar = iSel;

	if (!bFlag)
		return;

	enuSetSelectToolBar(iSel);
}
```



