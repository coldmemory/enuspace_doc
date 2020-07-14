---
layout: default
title: Radian
parent: Math functions
grand_parent: Math & Statistics
---

# Radian

Ensor.Radian\(Ensor\* pEnsor\)

#### Parameters

* Ensor\* pEnsor

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다.

#### Return Value

Ensor\* pRetEnsor : pEnsor의 엘리먼트에 대한 Degree To Radian Ensor\*를 반환합니다.

#### Remarks

#### Examples

```lua
function MathEquation()
	local x = ensor.new("[21]","double","-180:180")
 	local y = ensor.Radian(x)

 	ensor.Plot(x, y)
 	ensor.Table(y)
end
```

#### Result

![](./MathAPI/RadianResult.png)

