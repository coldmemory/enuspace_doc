---
layout: default
title: enuSelConnectionPin
parent: Application API
---
# bool enuSelConnectionPin\(HVIEW pENUView, wchar\_t\* strPicture, wchar\_t\* strSymbol\)

bool enuSelConnectionPin\(HVIEW pENUView, wchar\_t\* strPicture, wchar\_t\* strSymbol\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

* wchar\_t\* strPicture

L"" 공백처리합니다. 더이상 사용하지 않습니다.

* wchar\_t\* strSymbol

L"" 공백처리합니다. 더이상 사용하지 않습니다.

#### Return Value

Type : bool

#### Remarks

PIN객체 추가 모드 상태로 설정합니다. PIN객체 설정후 뷰에 마우스 다운시 PIN객체가 생성됩니다.

#### Examples

```cpp
void CenuSpaceView::OnSelConnectionPin()
{
	if (m_pENUView)
		enuSelConnectionPin(m_pENUView, L"", L"");
}
```



