---
layout: default
title: enuSetSnapFile
parent: Application API
---
# void enuSetSnapFile\(wchar\_t\* strFilename\)

void enuSetSnapFile\(wchar\_t\* strFilename\)

#### Parameters

* wchar\_t\* strFilename

로직의 상태값을 저장할 파일명을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

로직의 상태값을 저장하고, enuSetResetFile\(\)함수를 통하여 리셋을 수행합니다.

#### Examples

```cpp
void CMainFrame::OnModeSnap()
{
	wchar_t* pProjectFullName = enuGetProjectFullName();
	CString strProject;
	strProject = pProjectFullName;

	if (strProject.IsEmpty())
	{
		AfxMessageBox(L"프로젝트가 로드되어 있지 않습니다.", MB_TOPMOST | MB_SETFOREGROUND);
		return;
	}

	CDlgSnap dlg;
	if (dlg.DoModal() == IDOK)
	{
		enuSetScriptOperationMode(false);							// [ver.42] Add
		enuSetTaskOperationMode(DEF_MODE_EDIT);

		CString strFilename = dlg.GetSnapFile() + L".ic";
		enuSetSnapFile(strFilename.GetBuffer(0));
	}
}
```



