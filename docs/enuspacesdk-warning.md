---
layout: default
title: 사용 시 주의 사항
parent: SDK Tutorial
has_children: true
nav_order: c
last_modified_date: now
---

# 주의사항

* Deadlock 발생 가능성

![](./SDK/warning/warning_0.PNG) 

특정 Enu SDK API를 사용한 외부 함수를 Script에서 사용할 시, Deadlock이 발생할 가능성이 있다.

만약 Deadlock이 발생하는 상황에서 Enu SDK API를 외부함수에서 계속 사용하기를 원한다면, Thread를 사용하기 바란다.

 


