---
layout: default
title: PrintMessage
parent: Script API
---
# PrintMessage\(message\)

PrintMessage\(\)

#### Parameters

message : 디버그창에 출력하고자하는 메세지를 입력합니다.

#### Return Value

none

#### Remarks

```lua
--lua
local message = "my message"
PrintMessage(string.format("%s", message))
```

```js
// javascript
var message = "my message";
PrintMessage(message);
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    local message = "my message"
    PrintMessage(string.format("%s", message))
end
```

```js
// JavaScript
function _onmousedown()
{    
    var message = "my message";
    PrintMessage(message);
}
```



