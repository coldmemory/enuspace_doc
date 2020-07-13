---
layout: default
title: enuSetTaskOperationMode
parent: Application API
---
# void enuSetTaskOperationMode\(int iMode, int iStep\)

void enuSetTaskOperationMode\(int iMode, int iStep\)

#### Parameters

int iMode

Task의 모드를 지정합니다.

int iStep

Task의 모드가 Step인 경우, Step값을 지정합니다.

#### Return Value

Type : NONE

#### Remarks

Task의 실행 모드를 지정합니다.

```
#define DEF_MODE_EDIT							0
#define DEF_MODE_FREEZE						1
#define DEF_MODE_STEP							2
#define DEF_MODE_RUN							3
```

#### Examples

```cpp
void CMainFrame::OnModeEdit()
{
	enuSetScriptOperationMode(false);
	enuSetTaskOperationMode(DEF_MODE_EDIT, 24, false);
}

void CMainFrame::OnModeFreeze()
{
	enuSetScriptOperationMode(false);
	enuSetTaskOperationMode(DEF_MODE_FREEZE, 24, false);
}

void CMainFrame::OnModeStep()
{
	enuSetScriptOperationMode(true);
	enuSetTaskOperationMode(DEF_MODE_STEP);
}

void CMainFrame::OnModeRun()
{
	FileSaveSolution();
	enuSetScriptOperationMode(true);
	enuSetTaskOperationMode(DEF_MODE_RUN);
}
```



