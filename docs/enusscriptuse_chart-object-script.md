---
layout: default
title: 차트객체 Script 사용법
parent: Script 사용방법
grand_parent: enuSpace Tutorial
---

# 차트객체 Script 사용법

---

차트 객체는 자식 객체를 포함하고 있다. 각 \(title, legend, graph, xaxis, yaxis, series\) 자식 객체의 속성값을 변경하는 방법에 대하여 설명한다. 

### 차트 계층도

![](./assets/차트 계층도.png)

---

## 객체 속성 변경

---

자식 객체를 가지고 있는 객체에 스크립트를 사용할 때는 '\(부모객체 ID\).\(자식객체 ID\).\(객체의 속성\)' 으로 사용한다.

차트의 자식 객체 접근 이름

타이틀 객체 : title

범례 객체 : legend

그래프 객체 : graph

X축 객체 : xaxis

Y축 객체 : yaxis

데이터 Series 객체 : seires의 id \(각 시리즈의 이름을 통하여 접근\)

#### Lua Script

LuaScript로 제목을 변경할 때 \(속성창에서 User Function으로 생성하였음\)

```
function ChartTitle()
    ID_CHART.title.title = "test1234"
end
```

#### JavaScript

```js
function ChartTitle()
{
    ID_CHART.title.title = "test1234";
}
```



