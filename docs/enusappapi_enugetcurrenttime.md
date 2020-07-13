---
layout: default
title: enuGetCurrentTime
parent: Application API
---
# \_\_int64 enuGetCurrentTime\(\)

\_\_int64 enuGetCurrentTime\(\)

#### Parameters

NONE

#### Return Value

Type : \_\_int64

현재시간을 반환합니다.

#### Remarks

시뮬레이션 설정인 경우에는 시뮬레이션 시간을 반환하며, 시스템 설정인 경우에는 시스템 시간을 반환합니다.

The system time is expressed in Coordinated Universal Time \(UTC\)

#### Examples

```cpp
__int64 time = enuGetCurrentTime();
```



