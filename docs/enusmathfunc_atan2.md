---
layout: default
title: Atan2
parent: Math functions
grand_parent: Math & Statistics
---

# Atan2

Ensor.Atan2\(Ensor\* pEnsor1,Ensor\* pEnsor2\)

#### Parameters

* Ensor\* pEnsor1

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다\(y data\).

* Ensor\* pEnsor2

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다\(x data\).

#### Return Value

Ensor\* pRetEnsor : pEnsor의 엘리먼트에 대한 arc tangent2 Ensor\*를 반환합니다.

#### Remarks

#### Examples

```lua
function MathEquation()
    --TODO Add your lua script code here
     local ensor_x = ensor.new("{-1,1}")
     local ensor_y = ensor.Atan2(ensor_x,ensor_x)

     ensor.Table(ensor_y)
 end
```

#### Result

![](./MathAPI/Atan2Result.png)

