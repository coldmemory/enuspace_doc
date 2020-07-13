---
layout: default
title: enuPlaySoundX
parent: Application API
---
# void enuPlaySoundX\(wchar\_t\* wavfilename\)

void enuPlaySoundX\(wchar\_t\* wavfilename\)

#### Parameters

* wchar\_t\* wavfilename

Wave 파일이름을 입력합니다.

#### Return Value

Type :  NONE

#### Remarks

directx기반의 사운드를 재생합니다.

#### Examples

```cpp
void OnEvent()
    enuPlaySoundX("resource\\alarm.wav");
end
```



