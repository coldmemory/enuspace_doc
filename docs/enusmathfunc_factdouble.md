---
layout: default
title: FactDouble
parent: Math functions
grand_parent: Math & Statistics
---

# FactDouble

Ensor.Fact\(Ensor\* pEnsor\)

#### Parameters

* Ensor\* pEnsor

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다.

#### Return Value

Ensor\* pRetEnsor : pEnsor의 엘리먼트에 대한 Factorial double Ensor\*를 반환합니다.

#### Remarks



#### Examples

```lua
function MathEquation()
 	local ensor_x = ensor.new("{0,5,6,7,8,300,301}")
 	local ensor_y = ensor.FactDouble(ensor_x)

 	ensor.Table(ensor_y)
end
```

#### Result

![](./MathAPI/FactDoubleResultTable.png)

