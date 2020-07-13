---
layout: default
title: enuSetLogicComponent
parent: Application API
---
# bool enuSetLogicComponent\(HVIEW pENUView, wchar\_t\* pStrFileName, wchar\_t\* pStrSymbol\)

bool enuSetLogicComponent\(HVIEW pENUView, wchar\_t\* pStrFileName, wchar\_t\* pStrSymbol\)

#### Parameters

* HVIEW pENUView

뷰 핸들을 입력합니다.

* wchar\_t\* pStrFileName

HMI영역의 SVG 파일 이름을 입력합니다.

* wchar\_t\* pStrSymbol

SVG 파일에 정의된 심볼 이름을 입력합니다.

#### Return Value

Type : bool

정상 설정 여부를 반환합니다.

#### Remarks

컴퍼넌트 뷰에 심볼을 디스플레이하기 위한 함수입니다.

#### Examples

```cpp
void SetComponentView()
{
    HVIEW pView = enuCreateView(this->m_hWnd);
    enuSetComponentMode(pView, true);

    if (enuSetLogicComponent(pView, L"library\\logic\\logic_symbol.vg", L"ADDER"))
    {
        // TO DO JOB
    }    
}
```



