---
layout: default
title: enuGetVariablePointer
parent: Application API
---
# void enuGetVariablePointer\(HSVG pSvgHandler, wchar\_t\* pStrVariable, VariableStruct\* pData\)

void enuGetVariablePointer\(HSVG pSvgHandler, wchar\_t\* pStrVariable, VariableStruct\* pData\)

#### Parameters

Type : HSVG

페이지 핸들을 전달합니다.

#### Return Value

Type : wchar\_t\* strVariable

픽쳐파일 내부의 변수를 지정합니다.

Type : VariableStruct\* pData

변수의 정보를 반환받고자하는 구조체의 주소값을 지정합니다.

#### Remarks

변수구조체를 생성하고, 주소값을 전달하면 해당 변수의 메모리 주소, 타입 정보를 반환받습니다.



#### Examples

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
			wcscpy_s(name, L"");			// [ver.56] add : 초기화 추가.
			type = DEF_UNKNOWN;
			pValue = NULL;
			wcscpy_s(strValue, L"N/A");
		}
};

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

    // get picture handle
    HSVG hsvg = enuGetSvgHandler(ViewHandle )

    // set variable value
    enuSetVariableValue(hsvg, L"@OCEAN.I_BU", strValue.GetBuffer(0))
    
    VariableStruct data;
    enuGetVariablePointer(hsvg, L"@OCEAN.data", &data);
    
    // 주소값이 NULL이 아닌경우, 정상적으로 반환.
    if (data.pValue)    
    {
        if (data.type == DEF_DOUBLE)
        {
            // 메모리 주소값에 값 할당.
            *((double*)data.pValue) = 100.0f;
        }
    }
}
```



