---
layout: default
title: enuIsWebServerStart
parent: Application API
---
# bool enuIsWebServerStart\(\)

bool enuIsWebServerStart\(\)

#### Parameters

NONE

#### Return Value

Type : bool

웹서버의 실행여부를 반환합니다.

#### Remarks

웹서버의 실행여부를 반환합니다.

#### Examples

```cpp
void CMainFrame::OnUpdateComDisConnectWeb(CCmdUI *pCmdUI)
{
	bool bReady = enuIsWebServerStart();
	pCmdUI->SetCheck(!bReady);
}
```



