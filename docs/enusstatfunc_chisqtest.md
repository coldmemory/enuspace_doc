---
layout: default
title: ChisqTest
parent: Statistics functions
grand_parent: Math & Statistics
---

# ChisqTest

Ensor.ChisqTest\(Ensor\* pEnsor1, Ensor\* pEnsor2\)

#### Parameters

* Ensor\* pEnsor1

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다\(actual\_range data\).

* Ensor\* pEnsor2

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다\(expected\_range data\).

#### Return Value

Ensor\* pRetEnsor : Right tailed probability 와  계산된 F, df를 가진 Ensor\*를 반환합니다.

#### Remarks

* The χ2 test first calculates a χ2 statistic using the formula:

  ![](./StatisticsAPI/ChisqTestFunc.png)

  where:

  Aij = actual frequency in the i-th row, j-th column

  Eij = expected frequency in the i-th row, j-th column

  r = number or rows

  c = number of columns

* Degrees of freedom\(df\)

  ```
    r > 1 and c > 1 이면  df = (r - 1)(c - 1).

    r = 1 and c > 1 이면 df = c - 1.

    r > 1 and c = 1 이면 df = r - 1.

    r = c= 1은 허용되지 않습니다.
  ```

* **PDF**

![](./StatisticsAPI/ChisqTestFuncPdfGraph.png)

#### Examples1

```lua
function MathEquation()
     local ensor_x = ensor.new("/{/{58.0,35/},/{11,25/},/{10,23/}/}")
     local ensor_x2 = ensor.new("/{/{45.35,47.65/},/{17.56,18.44/},/{16.09,16.91/}/}")
     local ensor_y = ensor.ChisqTest(ensor_x,ensor_x2)

     ensor.Table(ensor_y)
end
```

#### Result

![](./StatisticsAPI/ChisqTestResultTable.png)

