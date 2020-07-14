---
layout: default
title: AverageIf
parent: Statistics functions
grand_parent: Math & Statistics
---

# AverageIf

Ensor.AverageIf\(Ensor\* pEnsor, string strCond \)

#### Parameters

* Ensor\* pEnsor

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다.

* string strCond 

평균을 구할 데이터의 조건을 text로 입력합니다.

#### Return Value

Ensor\* pRetEnsor : 엘리먼트의 갯수가 1인 Ensor\*를 반환합니다.

#### Remarks

데이터포인트에서 조건에 맞는 데이터포인트들의 산술 평균을 반환합니다.

#### Examples

```lua
function MathEquation()
     local ensor_x = ensor.new("{10,7,9,27,2}")
     local ensor_y = ensor.AverageIf(ensor_x,"d>5 and d<20")
     ensor.Table(ensor_y)
 end
```

#### Result

![](./StatisticsAPI/AverageIfResultTable.png)

조건에 만족하는 10,7,9에 대한 평균값을 반환합니다.

