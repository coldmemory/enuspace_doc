---
layout: default
title: ChisqDistRt
parent: Statistics functions
grand_parent: Math & Statistics
---

# ChisqDistRt

Ensor.ChisqDistRt\(Ensor\* pEnsor, int df\)

#### Parameters

* Ensor\* pEnsor

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다.

* int df

자유도\(Degree of Freedom\)값을 입력합니다.

#### Return Value

Ensor\* pRetEnsor : pEnsor의 엘리먼트에 맞는 갯수만큼 계산된 Ensor\*를 반환합니다.

#### Remarks

Returns the left-tailed probability of the chi-squared distribution.

* **PDF**

![](./StatisticsAPI/ChisqDistRtPdfGraph.png)

#### Examples1

```lua
function MathEquation()
     local ensor_x = ensor.new("{0.5,1,1.5,2,2.5,3,3.5,4,4.5,5}")
    local ensor_y = ensor.ChisqDistRt(ensor_x,3)

     ensor.Table(ensor_y)
 end
```

#### Result

![](./StatisticsAPI/ChisqDistRtResultTable.png)

