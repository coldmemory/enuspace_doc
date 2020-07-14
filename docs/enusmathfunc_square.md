---
layout: default
title: Square
parent: Math functions
grand_parent: enuSpace Tutorial
---

# Square

Ensor.Square\(Ensor\* pEnsor\)

#### Parameters

* Ensor\* pEnsor

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다.

#### Return Value

Ensor\* pRetEnsor : pEnsor의 엘리먼트에 대한 square  Ensor\*를 반환합니다.

#### Remarks

#### Examples

```lua
function MathEquation()
     local x = ensor.new("[21]","double","0:100")
     local y = ensor.Square(x)

     ensor.Plot(x, y)
     ensor.Table(y)
end
```

#### Result

![](./MathAPI/SquareResult.png)

