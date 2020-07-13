---
layout: default
title: enuWebServerStop
parent: Application API
---
# void enuWebServerStop\(\)

void enuWebServerStop\(\)

#### Parameters

NONE

#### Return Value

Type : NONE

#### Remarks

웹 서버를 중지합니다.

#### Examples

```cpp
void CMainFrame::OnComDisConnectWeb()
{
	bool bReady = enuIsWebServerStart();
	if (bReady == true)
		enuWebServerStop();
}
```



