---
layout: default
title: BinomDist
parent: Statistics functions
grand_parent: Math & Statistics
---

# BinomDist

Ensor.BinomDist\(Ensor\* pEnsor, int nTrial,double succesP,bool cumulative \)

#### Parameters

* Ensor\* pEnsor

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다\(성공회수\).

* int nTrial

nTrial 값을 입력합니다\(시도회수\).

* double succesP

succesP 값을 입력합니다\(성공확률\).

* bool cumulative 

cumulative  : true 이면 누적분포값을 반환합니다.

cumulative  : false이면 ,확률 밀도값을 반환합니다.

#### Return Value

Ensor\* pRetEnsor : pEnsor의 엘리먼트에 맞는 갯수만큼 계산된 Ensor\*를 반환합니다.

#### Remarks

각 시도에서 성공확률이 succesP인 모집단에서 nTrial회수만큼 시도를 했을 때 pEnsor만큼 성공할 확률을 구합니다.

* **PDF**

![](./StatisticsAPI/BinomFunc1.png)

![](./StatisticsAPI/BinomFunc2.png)

![](./StatisticsAPI/BinomPdfGraph.png)

* **CDF**

![](./StatisticsAPI/BinomFunc3.png)

![](./StatisticsAPI/BinomCdfGraph.png)

#### Examples1

```lua
function MathEquation()
     local ensor_x = ensor.new("{0,1,2,3,4,5,6,7,8,9,10}")
     local ensor_y = ensor.BinomDist(ensor_x,10,0.5,false)
     local ensor_y2 = ensor.BinomDist(ensor_x,10,0.5,true)

     ensor.Plot(ensor_x, ensor_y)
     ensor.Plot(ensor_x, ensor_y2)
     ensor.Table(ensor_y)
     ensor.Table(ensor_y2)
end
```

#### Result

![](./StatisticsAPI/BinomResult1.png)

