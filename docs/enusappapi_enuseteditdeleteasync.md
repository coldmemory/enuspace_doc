---
layout: default
title: enuSetEditDeleteAsync
parent: Application API
---
# void enuSetEditDeleteAsync\(HVIEW pENUView\)

void enuSetEditDeleteAsync\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

Delete 명령을 비동기식 이벤트로 수행합니다. 선택 객체에 대하여 제거 루틴을 수행합니다.

#### Examples

```cpp
void CenuSpaceView::OnEditDelete()
{
    enuSetEditDeleteAsync(m_pENUView);
}
```



