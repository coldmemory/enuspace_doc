---
layout: default
title: enuGetMoveCanvas
parent: Application API
---
# void enuGetMoveCanvas\(HVIEW pENUView, float\* transx, float\* transy\)

void enuGetMoveCanvas\(HVIEW pENUView, float\* transx, float\* transy\)

#### Parameters

* HVIEW pENUView

뷰의 해들을 입력합니다.

* float\* transx

뷰의 X축 이동값을 반환 받고자 하는 변수 포인터를 입력합니다.

* float\* transy

뷰의 Y축 이동값을 반환 받고자 하는 변수 포인터를 입력합니다.

#### Return Value

Type : void

입력 transx, transy의 변수 포인터를 통하여 값을 전달 받습니다.

#### Remarks

켄버스의 이동값을 취득합니다. 켄버스의 이동값 적용시 enuSetMoveCanvas\(\)함수를 활용합니다.

#### Examples

```cpp
void OnMouseDown()
{
    float ftransx = 0;
    float ftransy = 0;
    enuGetMoveCanvas(ViewHandle, &ftransx, &ftransy);
}
```



