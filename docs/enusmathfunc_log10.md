---
layout: default
title: Log10
parent: Math functions
grand_parent: Math & Statistics
---

# Log10

Ensor.Log10\(Ensor\* pEnsor\)

#### Parameters

* Ensor\* pEnsor

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다.

#### Return Value

Ensor\* pRetEnsor : pEnsor의 엘리먼트에 대한 Base10 Logarithm Ensor\*를 반환합니다.

#### Remarks

#### Examples

```lua
function MathEquation()
     local x = ensor.new("[21]","double","0.1:50.1")
     local y = ensor.Log10(x)

     ensor.Plot(x, y)
     ensor.Table(y)
end
```

#### Result

![](./MathAPI/Log10Result.png)

