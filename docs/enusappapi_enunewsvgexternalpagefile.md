---
layout: default
title: enuNewSvgExternalPageFile
parent: Application API
---
# HSVG enuNewSvgExternalPageFile\(wchar\_t\* pFileName\)

HSVG enuNewSvgExternalPageFile\(wchar\_t\* pFileName\)

#### Parameters

* wchar\_t\* pFileName

External용 SVG 파일명을 입력합니다.

#### Return Value

Type : bool 

External용 SVG 파일 정상 생성 유무를 반환합니다.

#### Remarks

External용 SVG 픽쳐 파일은 프로젝트 저장시 포함되지 않으며, 프로그램 동작중에 생성하여 픽쳐를 현시합니다. 대표적인 예로 PopupTrend의 픽쳐생성 및 제거등이 있습니다. 

제거시에는 enuDeleteSvgExternalPageFile\(\) 함수를 통하여 이용합니다.

#### Examples

```cpp
HVIEW ViewHandle = NULL; 
CreateExternalPage()
{
    HSVG SvgHandle = enuNewSvgExternalPageFile(L"Exteran_Page1");
    ViewHandle = enuCreateView(this->m_hWnd);
    enuSetSvgView(ViewHandle , SvgHandle); 
}

DeleteExternalPage()
{
    enuDeleteSvgExternalPageFile(L"Exteran_Page1");
}
```



