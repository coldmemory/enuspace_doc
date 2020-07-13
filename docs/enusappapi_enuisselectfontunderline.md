---
layout: default
title: enuIsSelectFontUnderline
parent: Application API
---
# bool enuIsSelectFontUnderline\(HVIEW pENUView\)

bool enuIsSelectFontUnderline\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

#### Return Value

Type : bool

선택 텍스트 객체의 Underline설정여부를 반환합니다.

#### Remarks

선택된 객체가 텍스트가 아닌경우에는 false를 반환합니다.

#### Examples

```cpp
void CenuSpaceView::OnUpdateFontUnderline(CCmdUI* pCmdUI)
{
    bool bEnable = enuIsSelectFontUnderline(m_pENUView);
    pCmdUI->SetCheck(bEnable);
}
```



