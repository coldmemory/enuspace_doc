---
layout: default
title: Fisher
parent: Statistics functions
grand_parent: Math & Statistics
---

# Fisher

Ensor.FTest\(Ensor\* pEnsor\)

#### Parameters

* Ensor\* pEnsor1

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다\(-1 &lt; data &lt; 1\).

#### Return Value

Ensor\* pRetEnsor : Fisher 함수에 의해 변환된  Ensor\*를 반환합니다.

#### Remarks

![](./StatisticsAPI/FisherFunc.png)

#### Examples1

```lua
function MathEquation()
 	local ensor_x = ensor.new("{-0.99,-0.75,-0.5,0.25,0,0.25,0.5,0.75,0.99}")
 	local ensor_y = ensor.Fisher(ensor_x)

 	ensor.Plot(ensor_x, ensor_y)
 	ensor.Table(ensor_y)
end 
```

#### Result

![](./StatisticsAPI/FisherResult.png)

