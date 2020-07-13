---
layout: default
title: enuGetTaskProperty
parent: Application API
---
# TaskStruct\* enuGetTaskProperty\(wchar\_t\* pStrTaskID\)

TaskStruct\* enuGetTaskProperty\(wchar\_t\* pStrTaskID\)

#### Parameters

* wchar\_t\* pStrTaskID

TASK의 ID를 입력합니다.

#### Return Value

Type : TaskStruct\*

Task의 구조체 정보를 반환합니다.

#### Remarks

```cpp
struct TaskStruct
{
	HINSTANCE hDLL;
	int iMode;				// RUN,FREEZE,INIT,STEP
	CString strTaskID;
	CString strTaskModule;
	int iCycle;
	int iActive;				// 0 : Inactive, 1 : Active 설정값.

	bool bCalculate;
	int iOverTime;
	double dt;				

	bool bTASKWait;			
	HANDLE hTASKWaitEvent;		
	HANDLE hTASKRunEvent;		

	FuncPtr_OnEditComponent fn_OnEditComponent;
	FuncPtr_OnShowComponent fn_OnShowComponent;

	FuncPtr_OnInit fn_OnInit;
	FuncPtr_OnLoad fn_OnLoad;
	FuncPtr_OnUnload fn_OnUnload;
	FuncPtr_OnTask fn_OnTask;
	FuncPtr_OnModeChange fn_OnModeChange;
	FuncPtr_ExecuteFunction fn_ExecuteFunction;

	HANDLE hTaskThread;
	bool bTaskThread;
	HANDLE hTaskCloseEvent;
	HANDLE hTaskEvent;

	int iTaskType;									
	FuncPtr_IsEnableTransfer fn_IsEnableTransfer;	// TaskTyp이 TASK_TYPE_COMPONENT인경우, 연결선이 연결가능한지를 체크하는 함수.
	FuncPtr_ShowHelp fn_ShowHelp;			// TASK에 Help에 대한 호출 함수

	public: TaskStruct()
	{
		hDLL = NULL;
		iMode = 0;
		iCycle = 100;
		iActive = DEF_TASK_IN;
	
		bCalculate = true;
		iOverTime = 0;
	
		fn_OnEditComponent = NULL;		
		fn_OnShowComponent = NULL;		

		fn_OnInit = NULL;
		fn_OnLoad = NULL;
		fn_OnUnload = NULL;
		fn_OnTask = NULL;
		fn_OnModeChange = NULL;
		fn_ExecuteFunction = NULL;
	
		hTaskCloseEvent = NULL;
		hTaskThread = NULL;
		bTaskThread = false;
		hTaskEvent = NULL;

		dt = 1.0f / double(iCycle);		
		bTASKWait = false;				
		hTASKWaitEvent = NULL;			
		hTASKRunEvent = NULL;			

		iTaskType = TASK_TYPE_PROCESS;	
		fn_IsEnableTransfer = NULL;	
		fn_ShowHelp = NULL;		
	}
};

```

#### Examples

```cpp
TaskStruct* pTaskStruct = enuGetTaskProperty(strTaskID.GetBuffer(0));

if (pTaskStruct)
{
	// TO DO JOB
}
```



