---
layout: default
title: enuSetEditPaste
parent: Application API
---
# void enuSetEditPaste\(HVIEW pENUView\)

void enuSetEditPaste\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

Paste 명령을 수행합니다. enuSetEditCopy\(\)함수로 부터 복사된 객체를 붙여넣기를 수행합니다. 

#### Examples

```cpp
void CenuSpaceView::OnEditPaste()
{
	enuSetEditPaste(m_pENUView);
}
```



