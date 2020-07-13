---
layout: default
title: enuLogicGetSymbolType
parent: Application API
---
# wchar\_t\* enuLogicGetSymbolType\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)

wchar\_t\* enuLogicGetSymbolType\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)

#### Parameters

* wchar\_t\* pStrFilename

LOGIC영역에서의 SVG 파일을 입력합니다.

* wchar\_t\* pStrSymbol

심볼의 이름을 입력합니다.

#### Return Value

Type : wchar\_t\*

심볼의 Type정보를 반환합니다.

#### Remarks

#### Examples

```cpp
bool CMainFrame::LogicSymbolEdit()
{
	wchar_t* pStrType = enuLogicGetSymbolType(L"library\\logic\\logic_symbol.svg", L"ADDER");
	if (pStrType)
	{
		if (wcscmp(pStrType, L"node") == 0)
		{
			OpenLogicFile(strPicture, strSymbol);
			return true;
		}
		else
		{
			CString strMessage;
			strMessage.Format(L"%s - 알수없는 심볼의 타입 정보입니다", pStrType);
			AfxMessageBox(strMessage);
			return false;
		}
	}
	return false;
}
```



