---
layout: default
title: Create3DTerrain
parent: Script API
last_modified_date: now
---
# Create3DTerrain\("Relative"\)

RelativePath\(\)

#### Parameters

RelativePath : 프로젝트 패스를 기준으로 상대패스를 입력한다.

#### Return Value

함수를 통해 만들어진 절대패스를 출력한다.

#### Remarks
프로젝트 패스를 기준으로 상대패스를 입력할 경우, 입력된 상대패스를 절대패스로 바꿔준다.


```lua
-- lua
local path = RelativePath("..\\Simulation\\OCEAN_PCA(PROGRAM)\\OCEAN_PCA.exe")
```

```js
// javascript
var path = RelativePath("..\\Simulation\\OCEAN_PCA(PROGRAM)\\OCEAN_PCA.exe")
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()

    --프로젝트 패스가 D:\\Development\\GIT 라면
    local path = RelativePath("..\\Simulation\\OCEAN_PCA(PROGRAM)\\OCEAN_PCA.exe")
    -- path : D:\\Development\\Simulation\\OCEAN_PCA(PROGRAM)\\OCEAN_PCA.exe

end
```

```js
// JavaScript
function _onmousedown()
{    
    //프로젝트 패스가 D:\\Development\\GIT 라면
    var path = RelativePath("..\\Simulation\\OCEAN_PCA(PROGRAM)\\OCEAN_PCA.exe");
    //path : D:\\Development\\Simulation\\OCEAN_PCA(PROGRAM)\\OCEAN_PCA.exe
}
```



