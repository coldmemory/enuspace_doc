---
layout: default
title: enuResourceCreateStyle
parent: Application API
---
# bool enuResourceCreateStyle\(wchar\_t\* pStrFilename, wchar\_t\* pStrStyle\)

bool enuResourceCreateStyle\(wchar\_t\* pStrFilename, wchar\_t\* pStrStyle\)

#### Parameters

* wchar\_t\* pStrFilename

RESOURCE영역의 SVG파일을 입력합니다.

* wchar\_t\* pStrStyle

추가하고자 하는 스타일을 입력합니다.

#### Return Value

Type : bool

스타일추가의 정상여부를 반환합니다.

#### Remarks

#### Examples

```cpp
bool CMainFrame::CreateStyle(CString strStyleFile)
{
	CString strFilename = strStyleFile;
	if (!IsAbsolutePath(strStyleFile))
		strStyleFile = L"style\\" + strStyleFile;

	CDlgName dlg;
	dlg.SetLabelText(L"Style Name :");
	if (dlg.DoModal() == IDOK)
	{
		CString strName = dlg.GetNameText();
		enuResourceCreateStyle(strStyleFile.GetBuffer(0), strName.GetBuffer(0));

		return true;
	}
	return false;
}
```



