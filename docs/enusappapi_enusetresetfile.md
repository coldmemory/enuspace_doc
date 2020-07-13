---
layout: default
title: enuSetResetFile
parent: Application API
---
# void enuSetResetFile\(wchar\_t\* strFilename\)

void enuSetResetFile\(wchar\_t\* strFilename\)

#### Parameters

* wchar\_t\* strFilename

로직의 상태정보를 이전에 저장된 reset 파일\(.ic\)을 입력한다.

#### Return Value

Type : NONE

#### Remarks

저장된 Snap파일을 통하여, 상태정보를 복원하는 기능을 수행한다.

#### Examples

```cpp
void CMainFrame::OnModeReset()
{
	wchar_t* pProjectFullName = enuGetProjectFullName();
	CString strProject;
	strProject = pProjectFullName;

	if (strProject.IsEmpty())
	{
		AfxMessageBox(L"프로젝트가 로드되어 있지 않습니다.", MB_TOPMOST | MB_SETFOREGROUND);
		return;
	}

	CDlgReset dlg;
	if (dlg.DoModal() == IDOK)
	{
		enuSetScriptOperationMode(false);							
		enuSetTaskOperationMode(DEF_MODE_EDIT);

		CString strFilename = dlg.GetResetFile() + L".ic";
		enuSetResetFile(strFilename.GetBuffer(0));					
	}
}
```



