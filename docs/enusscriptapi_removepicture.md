---
layout: default
title: RemovePicture
parent: Script API
---
# RemovePicture\(picture\)

RemovePicture\(\)

#### Parameters

picture : 메모리에 로드된 픽쳐를 제거합니다.

#### Return Value

none

#### Remarks

RemovePicture\(\)함수는 [LoadPicture\(\)](./enusscriptapi_loadpicture.md), [ChangePicture\(\)](./enusscriptapi_changepicture.md)함수의 조합으로 활용됩니다.

메모리에 불필요한 픽쳐파일을 수동으로 Remove를 수행합니다. 필요시 LoadPicture\(\), ChangePicture\(\)함수를 통하여 메모리에 로드하여 디스플레이합니다.

```lua
-- lua
RemovePicture("picture\\sample.svg")
```

```js
// javascript
RemovePicture("picture\\sample.svg");
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    RemovePicture("picture\\sample.svg")
end
```

```js
// JavaScript
function _onmousedown()
{    
    RemovePicture("picture\\sample.svg");
}
```



