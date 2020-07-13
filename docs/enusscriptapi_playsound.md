---
layout: default
title: PlaySound
parent: Script API
---
# PlaySound\(wave\)

PlaySound\(\)

#### Parameters

wave : wave 파일을 입력합니다.

#### Return Value

none

#### Remarks

비동기식으로 wave 파일을 재생합니다.

```lua
-- lua
PlaySound("resource\\alarm.wav")
```

```js
// javascript
PlaySound("resource\\alarm.wav");
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    PlaySound("resource\\alarm.wav")
end
```

```js
// JavaScript
function _onmousedown()
{    
    PlaySound("resource\\alarm.wav");
}
```



