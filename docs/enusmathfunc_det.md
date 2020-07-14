---
layout: default
title: Det
parent: Math functions
grand_parent: Math & Statistics
---

# Det

Ensor.Det\(Ensor\* pEnsor\)

#### Parameters

* Ensor\* pEnsor

Ensor.new\(\) 함수등에 의해 만들어진 2차원 정방행렬 배열 포인터를 입력합니다.

#### Return Value

Ensor\* pRetEnsor : pEnsor의 엘리먼트에 대한 Determinant Ensor\*를 반환합니다.

#### Remarks

* 
#### Examples

```lua
function MathEquation()
     local x = ensor.new("/{/{3,4,1/},/{2,3,1/},/{5,4,7/}/}")
     local y = ensor.Det(x)

     ensor.Table(y)
end
```

#### Result

![](./MathAPI/DetResult.png)

