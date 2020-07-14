---
layout: default
title: Coth
parent: Math functions
grand_parent: Math & Statistics
---

# Coth

Ensor.Coth\(Ensor\* pEnsor\)

#### Parameters

* Ensor\* pEnsor

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다.

#### Return Value

Ensor\* pRetEnsor : pEnsor의 엘리먼트에 대한 hyperbolic cotangent Ensor\*를 반환합니다.

#### Remarks

#### Examples

```lua
function MathEquation()
    local x = ensor.new("[20]","double","-5:5")
     local y = ensor.Coth(x)

     ensor.Plot(x, y)
     ensor.Table(y)
end
```

#### Result

![](./MathAPI/CothResult.png)

