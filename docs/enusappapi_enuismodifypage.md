---
layout: default
title: enuIsModifyPage
parent: Application API
---
# bool enuIsModifyPage\(HVIEW pENUView\)

bool enuIsModifyPage\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

#### Return Value

Type : bool

픽쳐파일의 수정여부를 반환합니다.

#### Remarks

픽쳐파일의 수정 상태정보를 확인할 경우 사용합니다.

#### Examples

```cpp
void CenuSpaceView::OnUpdateEditModify(CCmdUI *pCmdUI)
{
    if (m_pENUView)
    {
        bool bModify = enuIsModifyPage(m_pENUView);

        pCmdUI->Enable(bModify);
    }
}
```



