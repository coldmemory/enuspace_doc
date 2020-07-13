---
layout: default
title: enuWebServerStart
parent: Application API
nav_order: 16f
---
# void enuWebServerStart\(\)

void enuWebServerStart\(\)

#### Parameters

NONE

#### Return Value

Type : NONE

#### Remarks

웹 서버를 기동합니다.

#### Examples

```cpp
void CMainFrame::OnComConnectWeb()
{
	bool bReady = enuIsWebServerStart();
	if (bReady == false)
		enuWebServerStart();
}
```



