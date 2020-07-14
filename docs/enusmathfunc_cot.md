---
layout: default
title: Cot
parent: Math functions
grand_parent: Math & Statistics
---

# Cot

Ensor.Cot\(Ensor\* pEnsor\)

#### Parameters

* Ensor\* pEnsor

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다.

#### Return Value

Ensor\* pRetEnsor : pEnsor의 엘리먼트에 대한 cotangent Ensor\*를 반환합니다.

#### Remarks

#### Examples

```lua
function MathEquation()
	local x = ensor.new("[20]","double","-1.56:1.56")
 	local y = ensor.Cot(x)

 	ensor.Plot(x, y)
 	ensor.Table(y)
end
```

#### Result

![](./MathAPI/CotResult.png)

