---
layout: default
title: enuRemoveTask
parent: Application API
---
# extern "C" \_\_declspec\(dllexport\) bool enuRemoveTask\(wchar\_t\* pStrTaskID\)

extern "C" \_\_declspec\(dllexport\) bool enuRemoveTask\(wchar\_t\* pStrTaskID\)

#### Parameters

* wchar\_t\* pStrTaskID

제거하고자하는 TASK의 ID값을 입력합니다. \(ex : "mytask"\)

#### Return Value

Type : bool

Task 제거 여부를 반환합니다.

#### Remarks

Task를 제거하고자 하는 경우 본 함수를 활용합니다.

#### Examples

```cpp
if (enuRemoveTask(L"mytask")
{
    // task 제거 완료.
}
```



