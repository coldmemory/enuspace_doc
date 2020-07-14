---
layout: default
title: Acoth
parent: Math functions
grand_parent: Math & Statistics
---

# Acoth

Ensor.Acoth\(Ensor\* pEnsor\)

#### Parameters

* Ensor\* pEnsor

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다.

#### Return Value

Ensor\* pRetEnsor : pEnsor의 엘리먼트에 대한 hyperbolic arc cotangent Ensor\*를 반환합니다.

#### Remarks

#### Examples

```lua
function MathEquation()
     local ensor_x = ensor.new("[20]","double","1.01:10.01")
     local ensor_y = ensor.Acoth(ensor_x)

     ensor.Plot(ensor_x, ensor_y)
     ensor.Table(ensor_y)
 end
```

#### Result

![](./MathAPI/AcothResult.png)

