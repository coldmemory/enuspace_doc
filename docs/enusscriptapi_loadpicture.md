---
layout: default
title: LoadPicture
parent: Script API
---
# LoadPicture\(picture\)

LoadPicture\(\)

#### Parameters

picture : 로드할 픽쳐파일의 이름을 입력합니다.

#### Return Value

none

#### Remarks

프로젝트에 로드되지 않은 픽쳐파일을 동적으로 로드를 수행합니다.



```lua
-- lua
LoadPicture("picture\\sample.svg")
```

```js
// javascript
LoadPicture("picture\\sample.svg");
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    LoadPicture("picture\\sample.svg")
end
```

```js
// JavaScript
function _onmousedown()
{    
    LoadPicture("picture\\sample.svg");
}
```



