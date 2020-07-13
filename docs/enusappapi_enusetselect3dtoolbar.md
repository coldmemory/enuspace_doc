---
layout: default
title: enuSetSelect3DToolBar
parent: Application API
---
# void enuSetSelect3DToolBar\(int iSel\)

void enuSetSelect3DToolBar\(int iSel\)

#### Parameters

* int iSel

3D객체의 생성을 위한 선택 객체타입을 지정합니다.

#### Return Value

Type : NONE

#### Remarks

편집모드시 3D 객체 생성을 위한 선택 객체를 설정합니다. 뷰에 마우스 다운 클릭시 선택 객체를 생성합니다.

```cpp
#define DEF_BOX						21
#define DEF_CONE					22
#define DEF_CYLINDER					23
#define DEF_SPHERE					24
#define DEF_LINESET					25
....
#define DEF_TEXT					32
```

#### Examples

```cpp
void CMainFrame::SetSelect3DToolBar(int iSel, bool bFlag)
{
	m_iSel3DToolbar = iSel;

	if (!bFlag)
		return;

	enuSetSelect3DToolBar(iSel);
}
```



