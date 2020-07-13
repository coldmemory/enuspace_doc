---
layout: default
title: enuIsRuntimeView
parent: Application API
---
# bool enuIsRuntimeView\(\)

bool enuIsRuntimeView\(\)

#### Parameters

NONE

#### Return Value

Type : bool

RuntimeView의 활성화 정보를 반환합니다.

#### Remarks

RuntimeView가 활성화 되어 있는 경우 RuntimeView창을 실행할수 없습니다.

#### Examples

```cpp
void CMainFrame::OnUpdateModeRunTime(CCmdUI *pCmdUI)
{
	bool bView = enuIsRuntimeView();
	if (bView)
	{
		pCmdUI->Enable(false);
	}
	else
		pCmdUI->Enable(true);
}
```



