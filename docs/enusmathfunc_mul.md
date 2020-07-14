---
layout: default
title: Mul
parent: Math functions
grand_parent: Math & Statistics
---

# Mul

Ensor.Mul\(Ensor\* pEnsor1,Ensor\* pEnsor2\)

Ensor.Mul\(Ensor\* pEnsor1,double dValue\)

#### Parameters

* Ensor\* pEnsor1

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다.

* Ensor\* pEnsor2

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다.

* double dValue

각 엘러먼트에 더해질 값을 입력합니다.

#### Return Value

Ensor\* pRetEnsor : pEnsor의 엘리먼트에 대한 Multifly 결과를 가진 Ensor\*를 반환합니다.

#### Remarks

pEnsor1 과 pEnsor2는 같은 엘러먼트 수를 가져야 합니다.

#### Examples

```lua
function MathEquation()
    local x1 = ensor.new("[10][4]","double","-10:10")
    local x2 = ensor.new("[10][4]","double","10:30")
    local y1 = ensor.Mul(x1,x2)
    local y2 = ensor.Mul(x1,-5)
    ensor.Name(y1,"Mul(x1,x2)")
    ensor.Name(y2,"Mul(x1,-5)")
    ensor.Name(x1,"x1")
    ensor.Name(x2,"x2")

     ensor.Table(x1)
    ensor.Table(x2)
    ensor.Table(y1)
    ensor.Table(y2)
end
```

#### Result

![](./MathAPI/MulResult.png)

