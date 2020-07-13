---
layout: default
title: enutrendseriesappendtimeanddata
parent: Application API
---
# void enuTrendSeriesAppendTimeAndData\(HNODE SeriesNode, double fTime, double fValue\)

void enuTrendSeriesAppendTimeAndData\(HNODE SeriesNode, double fTime, double fValue\)

#### Parameters

HNODE SeriesNode

시리즈의 노드 정보입니다.

double time

x축의 값을 입력합니다.

double value

y축의 값을 입력합니다.

#### Return Value

Type : void

#### Remarks

트랜드의 시리즈에 데이터를 적재합니다.

#### Examples

```cpp
HNODE hnode = enuGetObjectById(enuGetSvgHandler(m_pENUView), L"ID_AN_LONGSTRIP");
HNODE hSereis = enuGetTrendSeriesNode(enuGetSvgHandler(m_pENUView), hnode, L"Series1");

double time = 0;
double value = 100;
enuTrendSeriesAppendTimeAndData(hSereis, time, value);

time = 10;
value = 150;
enuTrendSeriesAppendTimeAndData(hSereis, time, value);


enuSetAttributeByNode(enuGetSvgHandler(m_pENUView), hnode, L"xview-min", L"0");
enuSetAttributeByNode(enuGetSvgHandler(m_pENUView), hnode, L"xview-max", L"300");
```



