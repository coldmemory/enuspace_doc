---
layout: default
title: PlaySoundX
parent: Script API
---
# PlaySoundX\(wave\)

PlaySoundX\(\)

#### Parameters

wave : directx기반의 사운드를 재생합니다.

#### Return Value



#### Remarks

PlaySoundX\(\)함수는 StopSoundX\(\), SetVolumeX\(\)와 함께 사용합니다.



```lua
-- lua
PlaySoundX("resource\\alarm.wav")
```

```js
// javascript
PlaySoundX("resource\\alarm.wav")
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    PlaySoundX("resource\\alarm.wav")
end
```

```js
// JavaScript
function _onmousedown()
{    
    PlaySoundX("resource\\alarm.wav");
}
```



