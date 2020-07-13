---
layout: default
title: enuLinkServerStop
parent: Application API
---
# void enuLinkServerStop\(\)

void enuLinkServerStop\(\)

#### Parameters

NONE

#### Return Value

Type : NONE

#### Remarks

enu server를 정지합니다. enuIsEnuServerStart\(\)함수를 통하여 실행여부를 확인합니다.

#### Examples

```cpp
void CMainFrame::OnComDisConnectEnu()
{
	bool bReady = enuIsEnuServerStart();
	if (bReady == true)
		enuLinkServerStop();
}
```



