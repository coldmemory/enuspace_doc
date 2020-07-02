# void enuSetAutoScale\(HVIEW pENUView, int x, int y, int cx, int cy\)

void enuSetAutoScale\(HVIEW pENUView, int x, int y, int cx, int cy\)

#### Parameters

* HVIEW pENUView

뷰 핸들을 입력합니다.

* int x

뷰의 x 포지션 값을 입력합니다.

* int y

뷰의 y 포지션 값을 입력합니다..

* int cx

뷰의 cx  폭 값을 입력합니다..

* int cy

뷰의 cy 높이 값을 입력합니다.

#### Return Value

Type :

#### Remarks

뷰의 사이즈 변경시, 자동으로 뷰의 스케일을 조정하여 픽처의 사이즈를 설정된 윈도우에 맞추어 디스플레이 합니다.

#### Examples

```cpp
void CSampleView::OnSize(UINT nType, int cx, int cy)
{
	CView::OnSize(nType, cx, cy);

	if (m_pView)
	{
		RECT rect;
		GetClientRect(&rect);

		enuSetMoveCanvas(m_pView, 0, 0);
		enuSetWindowPos(m_pView, rect.left, rect.top, rect.right, rect.bottom);
		enuSetAutoScale(m_pView, rect.left, rect.top, rect.right, rect.bottom);
	}
}

```

#### 



