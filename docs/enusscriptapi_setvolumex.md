---
layout: default
title: SetVolumeX
parent: Script API
---
# SetVolumeX\(volume\)

SetVolumeX\(\)

#### Parameters

volume : 볼륨값을 입력합니다.

#### Return Value

none

#### Remarks

[PlaySoundX\(\)](./enusscriptapi_playsoundx.md), [StopSoundX\(\)](./enusscriptapi_stopsoundx.md)함수와 함께 사용됩니다.

```lua
-- lua
SetVolumeX(75)
```

```js
// javascript
SetVolumeX(75);
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    SetVolumeX(75)
end
```

```js
// JavaScript
function _onmousedown()
{    
    SetVolumeX(75);
}
```



