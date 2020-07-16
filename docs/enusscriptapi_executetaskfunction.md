---
layout: default
title: ExecuteTaskFunction
parent: Script API
---
# ExecuteTaskFunction\(task, function\)

ExecuteTaskFunction\(\)

#### Parameters

task : 외부 태스크의 이름을 입력합니다. \(ex "taskname_"\)_

function: 외부태스크에 전달할 함수이름 및 파라미터를 입력합니다. \("ShowDebugMessage\(true\)"\)

#### Return Value

none

#### Remarks

ExecuteTaskFunction\(\)함수는 외부 태스크로 등록된 모듈에 ExecuteFunction\(\)함수 구현부가 존재하여야 합니다. 해당 모듈에 ExecuteFunction\(\)함수가 구현되었을 경우, 스크립트에서 본 함수를 사용하는 경우 구현된 ExecuteFunction\(\)함수를 호출합니다.

외부 태스크 만들기 참조 :[ External Task](./enuspace_external-task.md)

```cpp
// 해당 TASK의 extern함수의 구현 예시
// sample task
extern "C" __declspec(dllexport) void ExecuteFunction(wchar_t* pStrFunction)
{
	CString strFunction = pStrFunction;
	if (strFunction.Find(L"ShowDebugMessage") == 0)
	{
		CString Value = strFunction.Right(strFunction.GetLength() - 16);
		Value.Trim();
		Value.Trim(L"(");
		Value.Trim(L")");
		Value.Trim();
		Value.MakeLower();
		if (Value == L"true" || Value == L"1")
			m_bShowDebugMessage = true;
		else
			m_bShowDebugMessage = false;
	}
}
```

```lua
-- lua
ExecuteTaskFunction("sample", "ShowDebugMessage(true)")    -- external function call
```

```js
// javascript
ExecuteTaskFunction("sample", "ShowDebugMessage(true)");    // external function call
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    ExecuteTaskFunction("sample", "ShowDebugMessage(true)")
end
```

```js
// JavaScript
function _onmousedown()
{    
    ExecuteTaskFunction("sample", "ShowDebugMessage(true)");  
}
```



