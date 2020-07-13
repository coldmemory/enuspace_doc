---
layout: default
title: enuGetAttributeByNode
parent: Application API
---
# void enuGetAttributeByNode\(HSVG pSvgHandler, HNODE pObject, wchar\_t\* pStrVariable, VariableStruct\* pData\)

void enuGetAttributeByNode\(HSVG pSvgHandler, HNODE pObject, wchar\_t\* pStrVariable, VariableStruct\* pData\)

#### Parameters

* HSVG pSvgHandler

2d svg 픽쳐 핸들을 입력합니다.

* HNODE pObject

속성값을 설정할 노드 핸들을 입력합니다.

* wchar\_t\* pStrVariable

속성값을 입력합니다.

* VariableStruct\* pData

반환받고자 하는 구조체의 주소값을 지정합니다.

```cpp
struct VariableStruct
{
    wchar_t name[DEF_NAME_LEN];
    int     type;
    void*   pValue;
    wchar_t strValue[DEF_MAXTEXT_LEN];
    arrayInfo array;

public :VariableStruct()
        {
            wcscpy_s(name, L"");            
            type = DEF_UNKNOWN;
            pValue = NULL;
            wcscpy_s(strValue, L"N/A");
        }
};
```

#### Return Value

Type : VariableStruct\* pData

구조체의 정보에 해당 객체의 노드 정보를 반환받습니다.

#### Remarks

2D 노드에 대하여 해당 노드의 정보를 반환받습니다.

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

    // object create
    HNODE hnode = enuCreateRect(SvgHandle, L"MyObject", 0, 0, 100, 100, 0, 0);
    
    VariableStruct width_info;

    enuGetAttributeByNode(SvgHandle, hnode, L"width", &width_info);
    if (width_info.pValue)
    {
        if (width_info.type == DEF_FLOAT)
        {
            float fValue = *(float*)width_info.pValue;
        }
    }
}
```



