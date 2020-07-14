---
layout: default
title: BinomDistRange
parent: Statistics functions
grand_parent: Math & Statistics
---

# BinomDistRange

Ensor.BinomDistRange\(Ensor\* pEnsor1,Ensor\* pEnsor2, int nTrial,double succesP \)

#### Parameters

* Ensor\* pEnsor1

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다\(From 성공회수\).

* Ensor\* pEnsor2

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다\(To 성공회수\).

* int nTrial

nTrial 값을 입력합니다\(시도회수\)

* double succesP

모집단의 성공확률 succesP 값을 입력합니다.

#### Return Value

Ensor\* pRetEnsor : pEnsor의 엘리먼트에 맞는 갯수만큼 계산된 Ensor\*를 반환합니다.

#### Remarks

각 시도에서 성공확률이 succesP인 모집단에서 nTrial회수만큼 시도를 했을 때 pEnsor1에서 pEnsor2까지의  성공할 확률을 구합니다.

* **CDF**

![](./StatisticsAPI/BinomFunc3.png)

![](./StatisticsAPI/BinomCdfGraph.png)

#### Examples1

```lua
function MathEquation()
     local ensor_x = ensor.new("{48,10,20,30,45,50}")
    local ensor_x2 = ensor.new("{48,20,30,40,50,55}")
     local ensor_y = ensor.BinomDistRange(ensor_x,ensor_x2,60,0.75)

     ensor.Table(ensor_y)
end
```

#### Result

![](./StatisticsAPI/BinomDistRangeResult.png)

