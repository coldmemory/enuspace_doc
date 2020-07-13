---
layout: default
title: enuSetScriptOperationMode
parent: Application API
---
# void enuSetScriptOperationMode\(bool bFlag\)

void enuSetScriptOperationMode\(bool bFlag\)

#### Parameters

bool bFlag

스크립트 실행 모드를 지정합니다.

#### Return Value

Type : NONE

#### Remarks

스크립트를 실행하고자하는 경우에는 true를 지정한다. 스크립트를 중지하고자하는 경우에는 false를 지정한다.

#### Examples

```cpp
void OnStartProcessing()
{
	enuSetScriptOperationMode(true);
}

void OnStopProcessing()
{
	enuSetScriptOperationMode(false);
}
```



