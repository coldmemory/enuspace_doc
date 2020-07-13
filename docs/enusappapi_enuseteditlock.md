---
layout: default
title: enuSetEditLock
parent: Application API
---
# void enuSetEditLock\(HVIEW pENUView\)

void enuSetEditLock\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

선택 객체를 잠금 명령을 수행합니다. 잠금처리된 객체는 편집모드에서 선택되지 않습니다.

#### Examples

```cpp
void CenuSpaceView::OnEditLock()
{
    enuSetEditLock(m_pENUView);
}
```



