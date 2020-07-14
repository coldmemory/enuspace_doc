---
layout: default
title: Mod
parent: Math functions
grand_parent: Math & Statistics
---

# Mod

Ensor.Mod\(Ensor\* pEnsor, double dValue\)

#### Parameters

* Ensor\* pEnsor

Ensor.new\(\) 함수등에 의해 만들어진 포인터를 입력합니다.

* double dValue

Denominator를 입력합니다.

#### Return Value

Ensor\* pRetEnsor : pEnsor의 엘리먼트에 대한 Denominator\(dValue\)에 의해 나누어진 나머지를 가진 Ensor\*를 반환합니다.

#### Remarks

#### Examples1

```lua
function MathEquation()
    local x = ensor.new("[21]","double","10:30")
    local y = ensor.Mod(x,3)

    ensor.Name(x,"x")
    ensor.Table(x)
    ensor.Table(y)
end
```

#### Result1

![](./MathAPI/ModResult.png)

#### Examples2

```lua
function MathEquation()
    local x = ensor.new("[20]","double","10:30")
    local y = ensor.Mod(x,3)

    ensor.Name(x,"x")
    ensor.Table(x)
    ensor.Table(y)
end
```

#### Result2

![](./MathAPI/ModResult2.png)

