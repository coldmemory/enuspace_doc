---
layout: default
title: Skewp
parent: Statistics functions
grand_parent: Math & Statistics
---

# Skew

Ensor.Skew\(Ensor\* pEnsor1\)

#### Parameters

* Ensor\* pEnsor1

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다\(data1\).

#### Return Value

Ensor\* pRetEnsor : skewness 를 가진 Ensor\*를 반환합니다.

#### Remarks

* The equation for the SkewP is:

  ![](./StatisticsAPI/SkewPFunc.png)

* Returns the skewness of a distribution based on a population: a characterization of the degree of asymmetry of a distribution around its mean.

#### Examples1

```lua
function MathEquation()
    local ensor_x = ensor.new("{3,4,5,2,3,4,5,6,4,7}")
    local ensor_y = ensor.SkewP(ensor_x)

     ensor.Table(ensor_y)
end
```

#### Result

![](./StatisticsAPI/SkewPResultTable.png)

