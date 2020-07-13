---
layout: default
title: enuSetMoveCanvas
parent: Application API
---
# void enuSetMoveCanvas\(HVIEW pENUView, float transx, float transy\)

void enuSetMoveCanvas\(HVIEW pENUView, float transx, float transy\)

#### Parameters

* HVIEW pENUView

뷰의 해들을 입력합니다.

* float transx

켄버스의 X축 이동값을 입력합니다.

* float transy

켄버스의 Y축 이동값을 입력합니다.

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
    enuSetMoveCanvas(ViewHandle, ftransx, ftransy);
}
```



