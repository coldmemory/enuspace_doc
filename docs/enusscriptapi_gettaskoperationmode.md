---
layout: default
title: GetScriptOperationMode
parent: Script API
---
# GetTaskOperationMode\(\)

GetScriptOperationMode\(\)

#### Parameters

none

#### Return Value

mode : TASK 실행 및 정지등 태스크 상태 정보를 전달합니다.

"EDIT", "FREEZE", "STEP", "RUN"

#### Remarks

태스를 제어하는 함수는 [SetTaskOperationMode\(\)](./enusscriptapi_settaskoperationmode.md)를 이용합니다.

#### Examples

```lua
-- lua
function _ontaskview()
	
	local task_status = GetTaskOperationMode()
	if (task_status == "RUN") then
		ID_RECT_RUN.fill = "#ffbf28"
		ID_RECT_FRZ.fill = "#b1b0a7"
	else
		ID_RECT_FRZ.fill = "#ffbf28"
		ID_RECT_RUN.fill = "#b1b0a7"
	end
end
```

```js
// javascript
function _ontaskview()
{	
	var task_status = GetTaskOperationMode()
	if (task_status == "RUN")
	{
		ID_RECT_RUN.fill = "#ffbf28"
		ID_RECT_FRZ.fill = "#b1b0a7"
	}
	else
	{
		ID_RECT_FRZ.fill = "#ffbf28"
		ID_RECT_RUN.fill = "#b1b0a7"
	}

}
```

#### 



