---
layout: default
title: enuUpdateScreen
parent: Application API
---
# void enuUpdateScreen\(HVIEW pENUView\)

void enuUpdateScreen\(HVIEW pENUView\)

#### Parameters

HVIEW pENUView

뷰 핸들을 입력합니다.

#### Return Value

Type : void

#### Remarks

화면을 갱신합니다.

#### Examples

```cpp
void CenuSpaceView::OnDraw(CDC* /*pDC*/)
{
	CenuSpaceDoc* pDoc = GetDocument();
	ASSERT_VALID(pDoc);
	if (!pDoc)
		return;

	if (m_pENUView)
	{
		enuUpdateScreen(m_pENUView);
	}
}
```



