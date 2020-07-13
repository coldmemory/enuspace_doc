---
layout: default
title: enuLinkServerStart
parent: Application API
---
# void enuLinkServerStart\(\)

void enuLinkServerStart\(\)

#### Parameters

NONE

#### Return Value

Type : NONE

#### Remarks

enu server를 실행합니다. enuIsEnuServerStart\(\)함수를 통하여 실행여부를 확인합니다.

#### Examples

```cpp
void CMainFrame::OnComConnectEnu()
{
    bool bReady = enuIsEnuServerStart();
    if (bReady == false)
        enuLinkServerStart();
}
```



