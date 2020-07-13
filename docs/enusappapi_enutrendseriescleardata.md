---
layout: default
title: enutrendseriescleardata
parent: Application API
---
# void enuTrendSeriesClearData\(HNODE SeriesNode\)

void enuTrendSeriesClearData\(HNODE SeriesNode\)

#### Parameters

HNODE SeriesNode

시리즈의 노드 정보입니다.

#### Return Value

Type : void

#### Remarks

트랜드의 시리즈에 데이터를 제거합니다.

#### Examples

```cpp
HNODE hnode = enuGetObjectById(enuGetSvgHandler(m_pENUView), L"ID_AN_LONGSTRIP");
HNODE hSereis = enuGetTrendSeriesNode(enuGetSvgHandler(m_pENUView), hnode, L"Series1");

double value = 100;
enuTrendSeriesClearData(hSereis);
```



