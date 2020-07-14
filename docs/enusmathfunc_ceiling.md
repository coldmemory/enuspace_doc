---
layout: default
title: Odd
parent: Math functions
grand_parent: Math & Statistics
---

# Odd

Ensor.Odd\(Ensor\* pEnsor,\)

#### Parameters

* Ensor\* pEnsor

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다.

#### Return Value

Ensor\* pRetEnsor : pEnsor의 엘리먼트에 대한 Odd Ensor\*를 반환합니다.

#### Remarks

#### Examples

```lua
function MathEquation()
    local ensor_x = ensor.new("{1.5,3,2,-1,-2}")
    local ensor_y = ensor.Odd(ensor_x)

    ensor.Table(ensor_y)
end
```

#### Result

![](./MathAPI/OddResultTable.png)

