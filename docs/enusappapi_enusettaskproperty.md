---
layout: default
title: enuSetTaskProperty
parent: Application API
---
# bool enuSetTaskProperty\(wchar\_t\* pStrTaskID, wchar\_t\* pStrProp, wchar\_t\* pStrValue\)

bool enuSetTaskProperty\(wchar\_t\* pStrTaskID, wchar\_t\* pStrProp, wchar\_t\* pStrValue\)

#### Parameters

* wchar\_t\* pStrTaskID

Task의 ID를 입력합니다.

* wchar\_t\* pStrProp

Task의 속성이름을 입력합니다.

* wchar\_t\* pStrValue

속성값을 입력합니다.

#### Return Value

Type : bool

#### Remarks

Task의 속성값을 지정합니다.

```
cycle = "1,2,4,6,8,12,24"
active = "In,Out"
```

#### Examples

```cpp
enuSetTaskProperty(L"task1", L"cycle", L"12");
enuSetTaskProperty(L"task1", L"active", L"In");
```



