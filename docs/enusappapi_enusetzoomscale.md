---
layout: default
title: enuSetZoomScale
parent: Application API
---
# void enuSetZoomScale\(HVIEW pENUView, float fPercent\)

void enuSetZoomScale\(HVIEW pENUView, float fPercent\)

#### Parameters

* HVIEW pENUView

뷰 핸들을 입력합니다.

* float fPercent

Zoom 설정값을 입력합니다. \(1-&gt;100%\)

#### Return Value

Type : NONE

#### Remarks

뷴 핸들의 스케일정보를 설정 합니다.

#### Examples

```cpp
void OnMouseWheel(float delta)
{
    float fScale = enuGetZoomScale(ViewHandle);

    enuSetZoomScale(ViewHandle, fScale*delta);
}
```



