---
layout: default
title: enuIsEnuServerStart
parent: Application API
nav_order: a9
---
# bool enuIsEnuServerStart\(\)

bool enuIsEnuServerStart\(\)

#### Parameters

NONE

#### Return Value

Type : bool

enu server의 기동여부를 반환합니다.

#### Remarks

enu server의 기동여부를 반환합니다.

#### Examples

```cpp
void CMainFrame::OnComConnectEnu()
{
	bool bReady = enuIsEnuServerStart();
	if (bReady == false)
		enuLinkServerStart();
}
```



