---
layout: default
title: ConfidenceNorm
parent: Statistics functions
grand_parent: Math & Statistics
---

# ConfidenceNorm

Ensor.ConfidenceNorm\(Ensor\* pEnsor, double stddev,int size\)

#### Parameters

* Ensor\* pEnsor

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다\(The significance level used to compute the confidence level\).

* int stddev

The population standard deviation for the data range and is assumed to be known.

* int size

size : 샘플의 크기를 입력합니다.

#### Return Value

Ensor\* pRetEnsor : pEnsor의 엘리먼트에 맞는 갯수만큼 계산된 Ensor\*를 반환합니다.

#### Remarks

* Returns the confidence interval for a population mean, using a normal distribution.
* Normal Distribution curve

![](./StatisticsAPI/ConfidenceNormFuncGraph.png)

#### Examples1

```lua
function MathEquation()
 	local ensor_x = ensor.new("{0.001,0.01,0.02,0.05,0.1,0.2,0.5}")
	local ensor_y = ensor.ConfidenceNorm(ensor_x,2.5,50)

 	ensor.Table(ensor_y)
end	
```

#### Result

![](./StatisticsAPI/ConfidenceNormResultTable.png)

