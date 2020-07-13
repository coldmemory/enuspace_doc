---
layout: default
title: enuSetRenderObjectReset
parent: Application API
---
# void enuSetRenderObjectReset\(HVIEW pENUView\)

void enuSetRenderObjectReset\(HVIEW pENUView\)

#### Parameters

HVIEW pENUView

뷰의 핸들을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

뷰에 적용된 노드의 정보가 변경되었을 경우, 모든 뷰의 객체를 제거하고 새롭게 생성하라는 신호를 전송한다.

#### Examples

```cpp
void CenuSpaceView::SetRenderObjectReset()
{
	if (m_pENUView)
		enuSetRenderObjectReset(m_pENUView);
}
```



