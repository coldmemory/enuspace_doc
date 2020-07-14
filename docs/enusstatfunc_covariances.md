---
layout: default
title: CovaranceS
parent: Statistics functions
grand_parent: Math & Statistics
---

# CovaranceS

Ensor.CovaranceS\(Ensor\* pEnsor1, Ensor\* pEnsor2\)

#### Parameters

* Ensor\* pEnsor1

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다\(data1\).

* Ensor\* pEnsor2

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다\(data 2\).

#### Return Value

Ensor\* pRetEnsor : CovarianceS 값를 가진 Ensor\*를 반환합니다.

#### Remarks

* Returns sample covariance, the average of the products of deviations for each data point pair in two data sets.

* The covariance is:

  ![](./StatisticsAPI/CovarianceSFunc.png)

  where

  ![](https://support.content.office.net/en-us/media/e50bfa35-f7a7-44ee-91eb-d25d79f90f42.png "x and y")

  are the sample means Average\(data1\) and Average\(data2\).

#### Examples1

```lua
function MathEquation()
     local ensor_x = ensor.new("{3,2,4,5,6}")
    local ensor_x2 = ensor.new("{9,7,12,15,17}")
    local ensor_y = ensor.CovarianceS(ensor_x,ensor_x2)

     ensor.Table(ensor_y)
end
```

#### Result

![](./StatisticsAPI/CovarianceSResultTable.png)

