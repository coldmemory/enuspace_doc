---
layout: default
title: enuSetEditCopy
parent: Application API
---
# void enuSetEditCopy\(HVIEW pENUView\)

void enuSetEditCopy\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

Copy 명령을 수행합니다. 선택 객체에 대하여 복사 루틴을 수행합니다. enuSetEditPaste\(\)함수를 통하여 붙여넣기를 수행합니다.

#### Examples

```cpp
void CenuSpaceView::OnEditCopy()
{
    enuSetEditCopy(m_pENUView);
}
```



