---
layout: default
title: ChangePicture
parent: Script API
---
# ChangePicture\(window, picture\)

ChangePicture\(\)

#### Parameters

window

정의된 윈도우의 이름을 입력합니다.

picture

로드된 또는 로드할 픽쳐파일 이름을 입력합니다.

#### Return Value

none

#### Remarks

enuSpace 편집기에서 윈도우 이름을 정의하지 않으면 윈도우 이름은 기본값 "window"로 정의됩니다.

픽쳐 파일이름은 "picture\filename.svg"형태로 picture 디렉토리를 포함하여야 합니다.

ChangePicture\(\)함수는 로드된 픽쳐를 보여주거나, 로드되지 않은 픽쳐를 호출하였을 경우 로드를 수행하고 해당 윈도우에 픽쳐 파일을 보여줍니다. 참조함수 [LoadPicture\(\)](./enusscriptapi_loadpicture.md), [RemovePicture\(\)](./enusscriptapi_removepicture.md)

```lua
-- lua
ChangePicture("window", "picture\\testpage.svg")
```

```js
// javascript
ChangePicture("window", "picture\\testpage.svg");
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    ChangePicture("window","picture\\testpage.svg")
end
```

```js
// JavaScript
function _onmousedown()
{    
    ChangePicture("window","picture\\testpage.svg");
}
```



