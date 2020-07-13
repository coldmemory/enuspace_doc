---
layout: default
title: enuSetSelectAlign
parent: Application API
---
# void enuSetSelectAlign\(HVIEW pENUView, int iType\)

void enuSetSelectAlign\(HVIEW pENUView, int iType\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

* int iType

정렬의 타입정보를 입력합니다.

#### Return Value

Type : NONE

#### Remarks

다중 선택 객체의 정렬 기능을 제공합니다.

#### Examples

```cpp
void CenuSpaceView::OnAlignLeft()
{
    enuSetSelectAlign(m_pENUView, DEF_ALIGN_LEFT);
}
void CenuSpaceView::OnAlignCenter()
{
    enuSetSelectAlign(m_pENUView, DEF_ALIGN_CENTER);
}
void CenuSpaceView::OnAlignRight()
{
    enuSetSelectAlign(m_pENUView, DEF_ALIGN_RIGHT);
}
void CenuSpaceView::OnAlignTop()
{
    enuSetSelectAlign(m_pENUView, DEF_ALIGN_TOP);
}
void CenuSpaceView::OnAlignMiddle()
{
    enuSetSelectAlign(m_pENUView, DEF_ALIGN_MIDDLE);
}
void CenuSpaceView::OnAlignBottom()
{
    enuSetSelectAlign(m_pENUView, DEF_ALIGN_BOTTOM);
}
void CenuSpaceView::OnAlignDisHor()
{
    enuSetSelectAlign(m_pENUView, DEF_ALIGN_DISHOR);
}
void CenuSpaceView::OnAlignDisVer()
{
    enuSetSelectAlign(m_pENUView, DEF_ALIGN_DISVER);
}
```



