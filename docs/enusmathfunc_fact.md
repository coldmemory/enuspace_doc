---
layout: default
title: Fact
parent: Math functions
grand_parent: Math & Statistics
---

# Fact

Ensor.Fact\(Ensor\* pEnsor\)

#### Parameters

* Ensor\* pEnsor

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다.

#### Return Value

Ensor\* pRetEnsor : pEnsor의 엘리먼트에 대한 Factorial Ensor\*를 반환합니다.

#### Remarks



#### Examples

```lua
function MathEquation()
	local x = ensor.new("{1,2,5,170,171}")
	local y = ensor.Fact(x)

	ensor.Table(y)
end
```

#### Result

![](./MathAPI/FactResultTable.png)

