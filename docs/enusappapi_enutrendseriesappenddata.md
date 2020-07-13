---
layout: default
title: enutrendseriesappenddata
parent: Application API
---
# void enuTrendSeriesAppendData\(HNODE SeriesNode, double fValue\)

void enuTrendSeriesAppendData\(HNODE SeriesNode, double fValue\)

#### Parameters

HNODE SeriesNode

시리즈의 노드 정보입니다.

double value

값을 입력합니다.

#### Return Value

Type : void

#### Remarks

트랜드의 시리즈에 데이터를 적재합니다.

#### Examples

```cpp
HNODE hnode = enuGetObjectById(enuGetSvgHandler(m_pENUView), L"ID_AN_LONGSTRIP");
HNODE hSereis = enuGetTrendSeriesNode(enuGetSvgHandler(m_pENUView), hnode, L"Series1");

double value = 100;
enuTrendSeriesAppendData(hSereis, value);
```



