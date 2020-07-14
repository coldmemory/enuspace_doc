---
layout: default
title: Rand
parent: Math functions
grand_parent: Math & Statistics
---

# Rand

Ensor.Rand\(string shape\)

Ensor.Rand\(string shape,double scale\)

#### Parameters

* string shape

만들어질 차원과 엘러먼트 갯수를 입력합니다.

* double scale

scale : Randomize scale값을 입력합니다.

#### Return Value

Ensor\* pRetEnsor : pEnsor의 엘리먼트에 대한 Randomize 결과를 가진 Ensor\*를 반환합니다.

#### Remarks

#### Examples

```lua
function MathEquation()

 	local ensor_y1 = ensor.Rand("[10][4]")
	local ensor_y2 = ensor.Rand("[10][4]",10)

 	ensor.Table(ensor_y1)
	ensor.Table(ensor_y2)
 end
```

#### Result

![](./MathAPI/RandResult.png)

