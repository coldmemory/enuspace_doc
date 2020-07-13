---
layout: default
title: enuIsEnablePaste
parent: Application API
---
# bool enuIsEnablePaste\(\)

bool enuIsEnablePaste\(\)

#### Parameters

NONE

#### Return Value

Type : bool

붙여넣기 기능 가능여부를 반환합니다.

#### Remarks

복사기능이 수행후 붙여넣기 기능이 활성화 됩니다.

#### Examples

```cpp
void CenuSpaceView::OnUpdateEditPaste(CCmdUI* pCmdUI)
{
	// [ver.65] mod
	bool bClipBoard = false;
	if (OpenClipboard() == true)
	{
		if (IsClipboardFormatAvailable(CF_DIB) == TRUE)
		{
			bClipBoard = true;
		}
		else if (IsClipboardFormatAvailable(CF_TEXT) == TRUE)
		{
			bClipBoard = true;
		}
		CloseClipboard();
	}

	if (m_i2D3DView == DEF_VIEW_2D)
	{
		bool bEnable = enuIsEnablePaste();
		if (bClipBoard || bEnable)
			pCmdUI->Enable(true);
		else
			pCmdUI->Enable(false);
	}
	else if (m_i2D3DView == DEF_VIEW_2D)
	{
		pCmdUI->Enable(false);
	}
}
```



