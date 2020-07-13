---
layout: default
title: enuAddTrendSeriesByNode
parent: Application API
---
# HNODE enuAddTrendSeriesByNode\(HSVG pSvgHandler, HNODE TrendNode, wchar\_t\* strSeriesID\)

HNODE enuAddTrendSeriesByNode\(HSVG pSvgHandler, HNODE TrendNode, wchar\_t\* strSeriesID\)

#### Parameters

* HSVG pSvgHandler

픽쳐 SVG 핸들을 입력합니다.

* HNODE TrendNode

트랜드 객체의 노드를 입력합니다.

* wchar\_t\* strSeriesID

트랜드 객체에 추가하고자하는 시리즈 ID를 입력합니다.

#### Return Value

Type : HNODE

추가된 시리즈의 노드를 반환합니다.

#### Remarks

트랜드 객체에 시리즈를 추가하는 함수입니다. 반환된 노드가 NULL이 아닌경우에는 정상적으로 추가되어 시리즈의 노드를 반환 받습니다. 반환된 시리즈 노드를 이용하여 시리즈의 속성정보를 변경하여 활용합니다.

#### Examples

```cpp
HVIEW ViewHandle = NULL; 
void CSampleView::OnInitialUpdate() 
{ 
    CView::OnInitialUpdate(); 

    enuCreateProject(); 

    // Load Project
    enuLoadProjectFile(L"Project\\sample.enup"); 

    // Create View
    ViewHandle = enuCreateView(this->m_hWnd); 

    // New Page Create. 
    CString strPicture = L"picture\\KoreaAIP.svg"; 
    HSVG SvgHandle = enuNewSvgPageFile(strPicture.GetBuffer(0)); 

    // ENU View Attach Set Page 
    enuSetSvgPageView(ViewHandle , strPicture.GetBuffer(0)); 
    
    HNODE trend = enuCreateTrend(ViewHandle, L"MYTREND", 0, 0, 200, 150, 0, 0);
    HNODE series = enuAddTrendSeriesByNode(ViewHandle, trend , L"series1");
}
```



