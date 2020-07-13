---
layout: default
title: enuIsEditRedo
parent: Application API
---
# bool enuIsEditRedo\(HVIEW pENUView\)

bool enuIsEditRedo\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

#### Return Value

Type : bool

편집 모드에서의 Redo기능이 활성화 여부를 반환합니다.

#### Remarks

편집 모드에서의 Undo 수행에 따른 Redo기능이 활성화 여부를 반환합니다.

#### Examples

```cpp
bool bEnableRedo = enuIsEditRedo(ViewHandle);
```



