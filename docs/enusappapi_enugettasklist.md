---
layout: default
title: enuGetTaskList
parent: Application API
---
# wchar\_t\* enuGetTaskList\(\)

wchar\_t\* enuGetTaskList\(\)

#### Parameters

NONE

#### Return Value

Type : wchar\_t\*

등록된 TASK의 리스트를 문자열 정보로 반환합니다. \("task1, task2"\)

#### Remarks

#### Examples

```cpp
CString strTaskList = enuGetTaskList();
CString Seperator = _T(", ");

CString Token;
int Position = 0;
Token = strTaskList.Tokenize(Seperator, Position);
while (Token != L"")
{
	Token.Trim();
	if (Token.IsEmpty() == false)
	{
		// TO DO JOB
	}
	Token = strTaskList.Tokenize(Seperator, Position);
}
```



