---
layout: default
title: enuRegisterJavaScriptByNode
parent: Application API
---
# void enuRegisterJavaScriptByNode\(wchar\_t\* strPagename, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)

void enuRegisterJavaScriptByNode\(wchar\_t\* strPagename, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)

#### Parameters

* wchar\_t\* strPagename

픽쳐의 파일이름을 입력합니다.

* HNODE pNode

객체의 핸들을 입력합니다.

* wchar\_t\* strFunction

추가하고자하는 함수의 이름을 입력합니다.

* wchar\_t\* strScript

스크립트의 내용을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

객체의 핸들정보를 이용하여 스크립트를 등록합니다.

#### Examples

```cpp
void OnAddScript()
{    
    CString strPicture = L"picture\\picture.svg";
    HSVG hsvg = enuGetSvgPageClass(strPicture.GetBuffer(0));
    if (hsvg)
    {
        HNODE hnode = enuGetObjectById(hsvg, L"ID_RECT");
        if (hnode)
        {
            CString script = L"function BlickFunction()\r\n{PrintMessage(\"call...\")\r\n}"        // javascript function

            enuRegisterJavaScriptByNode(L"picture\\picture.svg", hnode, L"BlickFunction", script.GetBuffer(0));
            enuExecuteFunction(L"ID_RECT.BlickFunction()");    
        }   
    }
}
```



