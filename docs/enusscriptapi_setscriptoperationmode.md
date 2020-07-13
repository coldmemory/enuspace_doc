---
layout: default
title: SetScriptOperationMode
parent: Script API
---
# SetScriptOperationMode\(operation\)

SetScriptOperationMode\(\)

#### Parameters

operation : 스크립트를 실행 플래그정보를 전달합니다. \(true, false\)

#### Return Value



#### Remarks

SetScriptOperationMode\(true\) 수행시 픽쳐의 \_taskview\(\)함수를 주기적으로 호출합니다. 더이상 호출하지 않기를 원하면 false값을 전달합니다.

```lua
-- lua
SetScriptOperationMode(true)
```

```js
// javascript-- lua
SetScriptOperationMode(true);
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    SetScriptOperationMode(true)
end
```

```js
// JavaScript
function _onmousedown()
{    
    SetScriptOperationMode(true);
}
```



