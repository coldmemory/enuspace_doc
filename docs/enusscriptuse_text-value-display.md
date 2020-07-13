---
layout: default
title: 텍스트 객체 값 출력방법
parent: Script 사용방법
grand_parent: enuSpace Tutorial
---

# 텍스트 객체 값 출력방법

---

#### Lua Script

```lua
-- float, double 값의 소수점 자리수를 지정하여 텍스트 객체에 출력하는 방법
local dTemp = 12.345678                             -- dTemp 변수를 소수점이하 6자리 값 12.345678로 초기화
text = string.format("%4.2f", dTemp)                -- string.format(%4.2f", dTemp) 소수점이상4자리 소수점이하3자리에서 반올림하여 2자리까지 텍스트 객체에 출력

------------------------------------------------------------------------------------------------------------------------
-- 텍스트 객체에 dTemp 변수의 값 12.345678을 String형으로 변환하여 출력
text = tostring(dTemp)
```

#### JavaScript

```js
// float, double 값의 소수점 자리수를 지정하여 텍스트 객체에 출력하는 방법

var dTemp = 12.345678;                             // dTemp 변수를 소수점6자리 값 12.345678로 초기화
textContent = dTemp.toFixed(2);                    // toFixed(2); 소수점이하3자리에서 반올림하여 2자리까지 텍스트 객체에 출력

------------------------------------------------------------------------------------------------------------------------
// 텍스트 객체에 dTemp 변수의 값 12.345678 값을 String형으로 변환하여 출력
textContent = dTemp.toString();
```



