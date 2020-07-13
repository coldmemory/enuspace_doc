---
layout: default
title: enuIsEnableConnectionPin
parent: Application API
---
# bool enuIsEnableConnectionPin\(HVIEW pENUView\)

bool enuIsEnableConnectionPin\(HVIEW pENUView\)

#### Parameters

HVIEW pENUView

뷰 핸들을 입력합니다.

#### Return Value

Type : bool

ConnectionPin의 편집 가능상태 여부를 반환합니다.

#### Remarks

픽쳐, 로직편집 역역에서만 활성화 됩니다.

#### Examples

```cpp
void CenuSpaceView::OnUpdateConnectionPin(CCmdUI *pCmdUI)
{
    if (m_iFileType == DEF_FILE_LOGIC)
        pCmdUI->Enable(true);
    else
        pCmdUI->Enable(false);

    bool bEnable = enuIsEnableConnectionPin(m_pENUView);
    if (bEnable)
        pCmdUI->SetCheck(true);
    else
        pCmdUI->SetCheck(false);
}
```



