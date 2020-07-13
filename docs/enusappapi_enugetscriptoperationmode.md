---
layout: default
title: enuGetScriptOperationMode
parent: Application API
---
# bool enuGetScriptOperationMode\(\)

bool enuGetScriptOperationMode\(\)

#### Parameters

NONE

#### Return Value

Type : bool

스크립트 기동 상태정보를 반환합니다. true시 스크립트 동작상태, false시 스크립트 정지상태

#### Remarks

현재 스크립트 실행중인지, 정지 상태인지를 반환하는 함수입니다.

#### Examples

```cpp
bool bOperation = enuGetScriptOperationMode();
```



