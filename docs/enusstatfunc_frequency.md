---
layout: default
title: Frequency
parent: Statistics functions
grand_parent: Math & Statistics
---

# Frequency

Ensor.Frequency\(Ensor\* pEnsor1, Ensor\* pEnsor2\)

#### Parameters

* Ensor\* pEnsor1

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다\(data\).

* Ensor\* pEnsor2

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다\(class data\).

#### Return Value

Ensor\* pRetEnsor : pEnsor2의 엘러먼트 +1 로 구분된 갯수를 가진 Ensor\*를 반환합니다.

#### Remarks



#### Examples1

```lua
function MathEquation()
 	local ensor_x = ensor.new("{79,85,78,85,50,81,95,88,97}")
	local ensor_x2 = ensor.new("{70,79,89}")
 	local ensor_y = ensor.Frequency(ensor_x,ensor_x2)
 
 	ensor.Table(ensor_y)
end 
```

#### Result

![](./StatisticsAPI/FrequencyResultTable.png)

