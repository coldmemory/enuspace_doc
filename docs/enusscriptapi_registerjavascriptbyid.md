---
layout: default
title: RegisterJavaScriptById
parent: Script API
---
# RegisterJavaScriptById\(id, function, script\)

RegisterJavaScriptById\(\)

#### Parameters

id : 등록하고자하는 노드의 id값을 입력합니다.

function : 함수명을 입력합니다.

script : 함수구현 내용을 입력합니다.

#### Return Value

none

#### Remarks

javascript의 함수를 동적으로 등록하여 활용할 수 있습니다.

```lua
-- lua
local script = "function BlickFunction()\r\n{PrintMessage(\"call...\")\r\n}"        -- javascript function

RegisterJavaScriptById("ID_RECT", "BlickFunction", script)
ID_RECT.BlickFunction()
```

```js
// javascript
var script = "function BlickFunction()\r\n{PrintMessage(\"call...\")\r\n}"        // javascript function

RegisterJavaScriptById("ID_RECT", "BlickFunction", script);
ID_RECT.BlickFunction();
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    local script = "function BlickFunction()\r\n{PrintMessage(\"call...\")\r\n}"        -- javascript function

    RegisterJavaScriptById("ID_RECT", "BlickFunction", script)
    ID_RECT.BlickFunction()
end
```

```js
// JavaScript
function _onmousedown()
{    
    var script = "function BlickFunction()\r\n{PrintMessage(\"call...\")\r\n}"        // javascript function

    RegisterJavaScriptById("ID_RECT", "BlickFunction", script);
    ID_RECT.BlickFunction();
}
```



