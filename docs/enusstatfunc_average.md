---
layout: default
title: Average
parent: Statistics functions
grand_parent: Math & Statistics
---

# Average

Ensor.Average\(Ensor\* pEnsor\)

#### Parameters

* Ensor\* pEnsor

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다.

#### Return Value

Ensor\* pRetEnsor : 엘리먼트의 갯수가 1인 Ensor\*를 반환합니다.

#### Remarks

데이터포인트에서 데이터포인트들의 산술 평균을 반환합니다.

![](./StatisticsAPI/AverageFunc.png)

#### Examples

```lua
function MathEquation()
     local ensor_x = ensor.new("{10,7,9,27,2}")
     local ensor_y = ensor.Average(ensor_x)
     ensor.Table(ensor_y)
 end
```

#### Result

![](./StatisticsAPI/AverageResultTable.png)

