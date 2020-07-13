---
layout: default
title: enuSetComponentMode
parent: Application API
---
# void enuSetComponentMode\(HVIEW pView, bool bOper\)

void enuSetComponentMode\(HVIEW pView, bool bOper\)

#### Parameters

* HVIEW pView

뷰 핸들을 입력합니다.

* bool bOper

컨포넌트 심볼을 디스플레이할 경우 true로 설정합니다.

#### Return Value

Type : NONE

#### Remarks

뷰에 심볼을 디스플레이할 경우, 컴포넌트 모드를 true로 설정하여 디스플레이를 수행합니다.

#### Examples

```cpp
void ShowComponent()
{
    HVIEW pView = enuCreateView(this->m_hWnd);
    enuSetComponentMode(pView, true);
    enuSetHmiComponent(pView, L"library\\hmi\\hmi_symbo.svg", L"ID_GAUGE");
}
```



