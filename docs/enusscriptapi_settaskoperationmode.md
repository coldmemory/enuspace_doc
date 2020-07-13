---
layout: default
title: SetScriptOperationMode
parent: Script API
---
# SetTaskOperationMode\(mode\)

SetScriptOperationMode\(\)

#### Parameters

mode : TASK 실행 및 정지등 제어정보를 전달합니다.

"EDIT", "FREEZE", "STEP", "RUN"

#### Return Value

none

#### Remarks

SetTaskOperationMode\(\)는 TASK를 제어하는 함수입니다. "STEP" 명려시 12회 TASK를 호출후 FREEZE상태로 전환됩니다.

"EDIT" 모드는 편집 상태로 TASK를 정지합니다.

"FREEZE" 모드는 RUN또는 STEP모드에서 정지 상태로 전환되어 RUN 명령시 TASK의 init\(\)함수를 호출하지 않습니다.

"STEP" 12 Step을 기본으로 호출합니다.

"RUN" 모드는 TASK를 기동합니다.

```lua
-- lua
SetTaskOperationMode("RUN")
```

```js
// javascript-- lua
SetTaskOperationMode("RUN");
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    SetTaskOperationMode("RUN")
end
```

```js
// JavaScript
function _onmousedown()
{    
    SetTaskOperationMode("RUN");
}
```



