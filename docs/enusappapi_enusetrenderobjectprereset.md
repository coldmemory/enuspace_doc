---
layout: default
title: enuSetRenderObjectPreReset
parent: Application API
---
# void enuSetRenderObjectPreReset\(HVIEW pENUView\)

void enuSetRenderObjectPreReset\(HVIEW pENUView\)

#### Parameters

HVIEW pENUView

뷰의 핸들을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

뷰에 적용된 노드의 정보가 변경되었을 경우, Popup Table등을 사전에 종료하는 신호를 전송하여 노드가 변경되었을 경우 메모리 릭을 예방한다.

#### Examples

```cpp
void CenuSpaceView::SetRenderObjectPreReset()
{
	if (m_pENUView)	
		enuSetRenderObjectPreReset(m_pENUView);
}
```



