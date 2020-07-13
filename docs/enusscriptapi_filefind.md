---
layout: default
title: FileFind
parent: Script API
---
# FileFind\(filename\)

FileFind\(\)

#### Parameters

filename : 파일 존재유무를 확인하고자하는 파일명을 입력합니다.

#### Return Value

파일 존재유무를 제공합니다.

#### Remarks

```lua
-- lua
local bExist = false
bExitst = FileFind("picture\\sample.svg")
if (bExist) then
    PrintMessage("File Existed")
else
    PrintMessage("File Not Existed")
end
```

```js
// javascript
// not support
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    local bExist = false
    bExitst = FileFind("picture\\sample.svg")
    if (bExist) then
        PrintMessage("File Existed")
    else
        PrintMessage("File Not Existed")
    end
end
```

```js
// JavaScript
function _onmousedown()
{    
    // not support
}
```



