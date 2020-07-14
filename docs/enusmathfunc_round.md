---
layout: default
title: Round
parent: Math functions
grand_parent: Math & Statistics
---

# Round

Ensor.Round\(Ensor\* pEnsor, int dizit\)

#### Parameters

* Ensor\* pEnsor

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다.

* int dizit

반올림을 할 자릿수를 입력합니다.

#### Return Value

Ensor\* pRetEnsor : pEnsor의 엘리먼트에 대한 dizit 자릿수에서 반올림 한 값을 가진 Ensor\*를 반환합니다.

#### Remarks

#### Examples1

```lua
function MathEquation()
	--TODO Add your lua script code here
 	local ensor_x = ensor.new("{2.15, 2.149, -1.48,-1.43, 21.5,-50.5}")
 	local ensor_y1 = ensor.Round(ensor_x,1)
	local ensor_y2 = ensor.Round(ensor_x,-2)

 	ensor.Table(ensor_y1)
	ensor.Table(ensor_y2)
 end
```

#### Result1

![](./MathAPI/RounResult.png)



