---
layout: default
title: GetVariablePointer_str
parent: Script API
last_modified_date: now
---
# GetVariablePointer_str\(variable\)

GetVariablePointer_str\(\)

#### Parameters

variable : 변수명을 입력합니다. 

#### Return Value

void* datapointer : 변수의 포인터 정보를 반환합니다.

int type : 데이터의 타입을 반환합니다.

int size : 데이터의 사이즈를 반환합니다.

#### Remarks

GetVariablePointer_str 함수는 GetVariablePointer와 동일한 기능을 제공합니다.

GetVariablePointer_str 함수는 입력변수를 문자열 형태로 제공하며 제공된 문자열을 기반으로 현재시점의 데이터 정보를 반환합니다.

주) GetVariablePointer 함수는 스크립트가 컴파일된 시점에 대한 데이터 정보를 반환합니다. 프로그램 실행중 동적 메모리 생성시 컴파일된 시점의 메모리 정보가 상이한 경우에는 잘못된 결과를 반환합니다.


```lua
-- lua
local pointer
local itype
local isize
pointer, itype, isize = GetVariablePointer_str("ID_CONTOUR.data")

```



#### 

#### Examples


```lua
function _onmousedown()
-- lua
    local pointer
    local itype
    local isize
    pointer, itype, isize = GetVariablePointer_str("ID_CONTOUR.data")
end
```



