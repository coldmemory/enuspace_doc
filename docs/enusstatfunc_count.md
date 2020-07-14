---
layout: default
title: Count
parent: Statistics functions
grand_parent: Math & Statistics
---

# Count

Ensor.Count\(Ensor\* pEnsor1, string cond\)

#### Parameters

* Ensor\* pEnsor1

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다\(data\).

* string cond

count할 조건을 텍스트로 입력합니다.

#### Return Value

Ensor\* pRetEnsor : 조건에 맞는 수를 가진 Ensor\*를 반환합니다.

#### Remarks

* lua script 문법에 맞는 조건을 입력합니다.

#### Examples1

```lua
function MathEquation()
 	local ensor_x = ensor.new("{3,2,4,5,6,7,6,9,8,10,3,15,12,8,4}")
	local ensor_y = ensor.Count(ensor_x,"d>=3 and d<12")

 	ensor.Table(ensor_y)
end	
```

#### Result

![](./StatisticsAPI/CountResultTable.png)

