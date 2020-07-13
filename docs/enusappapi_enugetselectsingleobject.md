---
layout: default
title: enuGetSelectSingleObject
parent: Application API
---
# HNODE enuGetSelectSingleObject\(HVIEW pENUView\)

HNODE enuGetSelectSingleObject\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

#### Return Value

Type : HNODE

선택객체중 첫번째 객체를 반환합니다.

#### Remarks

뷰에서 선택된 객체를 반환합니다. 하나선택일 경우 선택객체를 반환하나 여러개의 개체가 선택되었을 경우 첫번째 선택 객체를 반환합니다.

#### Examples

```cpp
vod OnMouseMove()
{
    HNODE hnode = enuGetSelectSingleObject(ViewHandle);
    if (hnode)
    {
        // TO DO JOB
    }
}
```



