---
layout: default
title: Large
parent: Statistics functions
grand_parent: Math & Statistics
---

# Large

Ensor.Large\(Ensor\* pEnsor, int value \)

#### Parameters

* Ensor\* pEnsor

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다\(data\).

* int value

value를 입력합니다.

#### Return Value

Ensor\* pRetEnsor : 가장 큰수로부터의 value번째의 값을 가진 Ensor\*를 반환합니다.

#### Remarks

#### Examples

```lua
function MathEquation()
	local ensor_x = ensor.new("/{/{3,4/},/{5,2/},/{3,4/},/{5,6/},/{4,7/}/}")
	local ensor_y = ensor.Large(ensor_x,3)

 	ensor.Table(ensor_y)
end
```

#### Result

![](./StatisticsAPI/LargeresultTable.png)

