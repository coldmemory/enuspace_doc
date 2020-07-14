---
layout: default
title: Slope
parent: Statistics functions
grand_parent: Math & Statistics
---

# Slope

Ensor.Slope\(Ensor\* pEnsor1, Ensor\* pEnsor2\)

#### Parameters

* Ensor\* pEnsor1

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다\(x data\).

* Ensor\* pEnsor2

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다\(y data\).

#### Return Value

Ensor\* pRetEnsor : x,y data에 의한 선형 함수의 기울기 가진 Ensor\*를 반환합니다.

#### Remarks

* The equation for the intercept of the regression line, a, is:

![](./StatisticsAPI/InterceptFunc1.png)

where the slope, b, is calculated as:

![](./StatisticsAPI/InterceptFunc2.png)

and where x and y are the sample means Average\(known\_x's\) and Average\(known\_y's\).

![](./StatisticsAPI/InterceptFuncGraph.png)

#### Examples1

```lua
function MathEquation()
	local ensor_x = ensor.new("{2,3,9,1,8,7,5}")
  	local ensor_x2 = ensor.new("{6,5,11,7,5,4,4}")
	local ensor_y = ensor.Slope(ensor_x2,ensor_x)

 	ensor.Table(ensor_y)
end	
```

#### Result

![](./StatisticsAPI/SlopeResultTable.png)

