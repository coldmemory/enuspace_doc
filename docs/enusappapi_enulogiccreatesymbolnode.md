---
layout: default
title: enuLogicCreateSymbolNode
parent: Application API
---
# bool enuLogicCreateSymbolNode\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)

bool enuLogicCreateSymbolNode\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)

#### Parameters

* wchar\_t\* pStrFilename

LOGIC영역에서의 SVG 파일이름을 입력합니다.

* wchar\_t\* pStrSymbol

추가하고자하는 심볼의 이름을 입력합니다.

#### Return Value

Type : bool

로직 심볼의 생성여부를 반환합니다.

#### Remarks

#### Examples

```cpp
bool CMainFrame::CreateLogicNode(CString strLogicFile)
{
	CString strFilename = strLgoicFile;
	if (!IsAbsolutePath(strLgoicFile))
		strLgoicFile = L"library\\logic\\" + strLgoicFile;

	CDlgName dlg;
	dlg.SetLabelText(L"Node Name :");
	if (dlg.DoModal() == IDOK)
	{
		CString strName = dlg.GetNameText();
		enuLogicCreateSymbolNode(strLgoicFile.GetBuffer(0), strName.GetBuffer(0));

		// TO DO JOB
		
		return true;
	}
	return false;
}
```



