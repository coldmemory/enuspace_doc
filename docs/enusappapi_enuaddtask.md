---
layout: default
title: enuAddTask
parent: Application API
---
# bool enuAddTask\(wchar\_t\* pStrTaskID, wchar\_t\* pStrTaskModule, wchar\_t\* pStrCycle\)

bool enuAddTask\(wchar\_t\* pStrTaskID, wchar\_t\* pStrTaskModule, wchar\_t\* pStrCycle\)

#### Parameters

* wchar\_t\* pStrTaskID

등록하고자하는 TASK의 ID값을 입력합니다. \(ex : "mytask"\)

* wchar\_t\* pStrTaskModule

등록하고자하는 TASK의 dll 이름을 입력합니다. \(ex. "mytask.dll"\)

* wchar\_t\* pStrCycle

TASK의 호출 주기를 입력합니다. \(ex. "24"\)

#### Return Value

Type : bool

Task 등록 여부를 반환합니다.

#### Remarks

사용자가 개발한 Task를 추가하거나, plugin Task를 추가하고자 하는 경우 본 함수를 활용합니다.

#### Examples

```cpp
if (enuAddTask(L"mytask", L"mytask.dll", L"24"))
{
    // task 등록 완료.
}	
```



