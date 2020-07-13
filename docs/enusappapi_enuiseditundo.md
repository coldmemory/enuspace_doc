---
layout: default
title: enuIsEditUndo
parent: Application API
---
# bool enuIsEditUndo\(HVIEW pENUView\)

bool enuIsEditUndo\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

#### Return Value

Type : bool

편집 모드에서의 Undo기능이 활성화 여부를 반환합니다.

#### Remarks

편집 수행에 따른 Undo기능이 활성화 여부를 반환합니다.

#### Examples

```cpp
bool bEnableUndo = enuIsEditUndo(ViewHandle);
```



