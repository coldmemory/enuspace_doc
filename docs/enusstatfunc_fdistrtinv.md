---
layout: default
title: FRtInv
parent: Statistics functions
grand_parent: Math & Statistics
---

# FRtInv

Ensor.FRtInv\(Ensor\* pEnsor, int df1,int df2 \)

#### Parameters

* Ensor\* pEnsor

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다\(Probability\).

* int df1

자유도1\(Degrees of Freedom 1\)값을 입력합니다\( numerator\).

* int df2

자유도2\(Degrees of Freedom 2\)값을 입력합니다\(denominator\).

#### Return Value

Ensor\* pRetEnsor : pEnsor의 엘리먼트에 맞는 갯수만큼 계산된 Ensor\*를 반환합니다.

#### Remarks

* **CDF**

**FInv**\(_x, df1, df2_\) = 1 – FDist\(_x, df1, df2,_ true\)

![](./StatisticsAPI/FRtInvFuncGraph.png)

#### Examples1

```lua
function MathEquation()
 	local ensor_x = ensor.new("{0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95}")
 	local ensor_y = ensor.FRtInv(ensor_x,6,4)

 	ensor.Plot(ensor_x, ensor_y)
 	ensor.Table(ensor_y)
end
```

#### Result

![](./StatisticsAPI/FRtInvResult.png)

