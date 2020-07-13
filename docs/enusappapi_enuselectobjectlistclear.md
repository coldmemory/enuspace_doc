---
layout: default
title: enuSelectObjectListClear
parent: Application API
---
# void enuSelectObjectListClear\(HVIEW pENUView\)

void enuSelectObjectListClear\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

선택객체를 모두 해제합니다.

#### Examples

```cpp
void CenuSpaceView::OnUnSelect()
{
    if (m_pENUView)
        enuSelectObjectListClear(m_pENUView);
}
```



