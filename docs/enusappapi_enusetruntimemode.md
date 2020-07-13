---
layout: default
title: enuSetRuntimeMode
parent: Application API
---
# void enuSetRuntimeMode\(bool bRunTime\)

void enuSetRuntimeMode\(bool bRunTime\)

#### Parameters

* bool bRunTime

런타임 모드를 지정합니다.

#### Return Value

Type : NONE

#### Remarks

RuntimeMode true 설정시, hmi, logic 영역의 스크립트는 별도로 등록하지 않습는다.

RuntimeMode true 설정시, 동적으로 객체를 제거하여도 스크립트가 정지하거나 태스크가 정지되지 않습니다.

응용프로그램을 개발시 런타임 모드를 이용하여 객체를 동적으로 생성하여 구현되어야 하는 경우에 런타임 모드를 true로 설정합니다. 기본설정값은 false 입니다.

#### Examples

```cpp
enuSetRuntimeMode(true);
```



