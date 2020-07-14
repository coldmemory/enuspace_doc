---
layout: default
title: FTest
parent: Statistics functions
grand_parent: Math & Statistics
---

# FTest

Ensor.FTest\(Ensor\* pEnsor1, Ensor\* pEnsor2\)

#### Parameters

* Ensor\* pEnsor1

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다\(first data\).

* Ensor\* pEnsor2

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다\(second data\).

#### Return Value

Ensor\* pRetEnsor : Fcalc, 0.05 two tailed F,two tailedd probability P를 가진 Ensor\*를 반환합니다.

#### Remarks

* Degrees of freedom\(df1,df2\)

  ```
  varianceP(pEnsor1) >= varianceP(pEnsor1) 이면  df1 = n1-1,df2=n2-1.

  varianceP(pEnsor1) < varianceP(pEnsor1) 이면 df1 = n2-1,df2=n1-1.

  n1 : first data elements' number

  n2 : second data elements' number

  ```

* **PDF**

![](./StatisticsAPI/FTestGraph.png)

#### Examples1

```lua
function MathEquation()
 	local ensor_x = ensor.new("{6,7,9,15,21}")
	local ensor_x2 = ensor.new("{20,28,31,38,40}")
 	local ensor_y = ensor.FTest(ensor_x,ensor_x2)

 	ensor.Table(ensor_y)
end 
```

#### Result

![](./StatisticsAPI/FTestResultTable.png)

