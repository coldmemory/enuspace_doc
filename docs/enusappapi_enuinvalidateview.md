---
layout: default
title: enuInvalidateView
parent: Application API
---
# void enuInvalidateView\(HVIEW pENUView\)

void enuInvalidateView\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

뷰의 영역을 기존 리소스를 이용하여 화면을 갱신합니다.

#### Examples

```cpp
void OnDraw()
{
    enuInvalidateView(ViewHandle)
}
```



