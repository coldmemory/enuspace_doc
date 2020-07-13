---
layout: default
title: enuIsSelectFontBold
parent: Application API
---
# bool enuIsSelectFontBold\(HVIEW pENUView\)

bool enuIsSelectFontBold\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

#### Return Value

Type : bool

선택 텍스트 객체의 볼드 설정여부를 반환합니다.

#### Remarks

선택된 객체가 텍스트가 아닌경우에는 false를 반환합니다.

#### Examples

```cpp
void CenuSpaceView::OnUpdateFontBold(CCmdUI* pCmdUI)
{
	bool bEnable = enuIsSelectFontBold(m_pENUView);
	pCmdUI->SetCheck(bEnable);
}
```



