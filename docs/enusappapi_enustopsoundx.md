---
layout: default
title: enuStopSoundX
parent: Application API
---
# void enuStopSoundX\(wchar\_t\* wavfilename\)

void enuStopSoundX\(wchar\_t\* wavfilename\)

#### Parameters

* wchar\_t\* wavfilename

Wave 파일이름을 입력합니다.

#### Return Value

Type :  NONE

#### Remarks

directx기반의 사운드를 정지합니다.

#### Examples

```cpp
void OnEvent()
    enuStopSoundX("resource\\alarm.wav");
end
```



