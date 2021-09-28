---
layout: default
title: 사용 시 주의 사항
parent: SDK Tutorial
has_children: true
nav_order: c
last_modified_date: now
---

# 주의사항

## Deadlock 발생 가능성
---

![](./SDK/warning/Warning_0.PNG)

Application이나 ExternalFunction.dll에서 등록한 외부함수로 작동하는 함수 내부에서

비동기 함수가 아닌 동기 함수(예: enuGetObjectById)를 사용 시 

지속적인 return 대기가 발생, 즉 DeadLock 발생 가능성이 있다.

이러한 상황에서 동기 함수를 사용하기 위해서는 Therad를 사용하는 방법이 있다.


 


