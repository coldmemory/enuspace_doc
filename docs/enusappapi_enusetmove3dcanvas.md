---
layout: default
title: enuSetMove3DCanvas
parent: Application API
---
# void enuSetMove3DCanvas\(HVIEW pENUView, float transx, float transy, float transz\)

void enuSetMove3DCanvas\(HVIEW pENUView, float transx, float transy, float transz\)

#### Parameters

* HVIEW pENUView

뷰의 해들을 입력합니다.

* float transx

켄버스의 X축 이동값을 입력합니다.

* float transy

켄버스의 Y축 이동값을 입력합니다.

* float transz

켄버스의 Z축 이동값을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

켄버스의 이동값을 설정합니다.

#### Examples

```cpp
void OnMouseDown()
{
    float ftransx = 100;
    float ftransy = 100;
    float ftransz = 100;    
    enuSetMove3DCanvas(ViewHandle, ftransx, ftransy, ftransz);
}
```



