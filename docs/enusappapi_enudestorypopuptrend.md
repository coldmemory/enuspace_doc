---
layout: default
title: enuDestoryPopupTrend
parent: Application API
---
# void enuDestoryPopupTrend\(void\* pTrend\)

void enuDestoryPopupTrend\(void\* pTrend\)

#### Parameters

void\* pTrend

팝업 트랜드의 클래스 핸들을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

PopupTrend의 창을 종료합니다.

#### Examples

```cpp
void* m_PopupTrend  = NULL;
_CreatePopupTrend()
{
    m_PopupTrend = enuCreatePopupTrend(DEF_CHART_LOGIC, L"ID_ADD.output");
}

_DestoryPopupTrend()
{
    if (m_PopupTrend)
    {
        enuDestoryPopupTrend(m_PopupTrend);
    }
}
```



