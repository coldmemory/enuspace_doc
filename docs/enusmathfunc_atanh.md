---
layout: default
title: Atanh
parent: Math functions
grand_parent: Math & Statistics
---

# Atanh

Ensor.Atanh\(Ensor\* pEnsor\)

#### Parameters

* Ensor\* pEnsor

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다.

#### Return Value

Ensor\* pRetEnsor : pEnsor의 엘리먼트에 대한 hyperbolic arc tangent Ensor\*를 반환합니다.

#### Remarks

#### Examples

```lua
function MathEquation()
	local x = ensor.new("[21]","double","-0.99:0.99")
 	local y = ensor.Atanh(x)

 	ensor.Plot(x, y)
 	ensor.Table(y)
end
```

#### Result

![](./MathAPI/AtanhResult.png)

