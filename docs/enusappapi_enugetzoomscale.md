---
layout: default
title: enuGetZoomScale
parent: Application API
---
# float enuGetZoomScale\(HVIEW pENUView\)

float enuGetZoomScale\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

뷰 핸들을 입력합니다.

#### Return Value

Type : float

뷰의 스케일정보를 반환합니다. \(1-&gt; 100%\)

#### Remarks

뷴 핸들의 스케일정보를 반환합니다.

#### Examples

```cpp
void OnMouseWheel(float delta)
{
    float fScale = enuGetZoomScale(ViewHandle);

    enuSetZoomScale(ViewHandle, fScale*delta);
}
```



