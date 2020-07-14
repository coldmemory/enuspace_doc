---
layout: default
title: Atan
parent: Math functions
grand_parent: Math & Statistics
---

# Atan

Ensor.Atan\(Ensor\* pEnsor\)

#### Parameters

* Ensor\* pEnsor

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다.

#### Return Value

Ensor\* pRetEnsor : pEnsor의 엘리먼트에 대한 arc tangent Ensor\*를 반환합니다.

#### Remarks

#### Examples

```lua
function MathEquation()
     local ensor_x = ensor.new("[21]","double","-10:10")
     local ensor_y = ensor.Atan(ensor_x)

     ensor.Plot(ensor_x, ensor_y)
     ensor.Table(ensor_y)
end
```

#### Result

![](./MathAPI/AtanResult.png)

