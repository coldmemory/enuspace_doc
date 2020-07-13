---
layout: default
title: C to Fortran Interface
parent: Component Task(saturn ver.4)
grand_parent: External Task
---

# External Task - Component Task \(C to Fortran Interface\)

##### \(enuSpace for saturn\)

---

본 문서는 External Task를 Component 기반으로 제작하는 방법에 있어 C++과 Fortran의 구조체 변수를 이용한 연동 방에 대하여 설명합니다.

reference sample : [https://github.com/EXPNUNI/enuSpace-Article/tree/master/enuSpace%20for%20Saturn/component\_task\_fortran\_x64](https://github.com/EXPNUNI/enuSpace-Article/tree/master/enuSpace for Saturn/component_task_fortran_x64)

Component의 입출력 정보에 대하여 구조체로 C++ 해더에 선언을 수행합니다.

구조체 선언

```cpp
#pragma once

#include "..\model\model\GlobalHeader.h"
#include <string>
#include <vector>
#include <afxcoll.h>
#include "EnuObj.h"

#ifndef _MODEL_HEADER__
#define _MODEL_HEADER__

extern CPtrArray *enuObject;
extern double g_DT;

#pragma pack(push, 1) 

struct component1 : EnuObject
{
    int iCount;
    double fValue;
    double fArray[5][10];
    component1()
    {
        iCount = 0;
        fValue = 0;
    }
    void Simulation(void);
};
struct component2 : EnuObject
{
    int input;
    int output;
    component2()
    {
        input = 0;
        output = 0;
    }
    void Simulation(void);
};
#pragma pack(pop) 

///////////////////////////////////////////////////////////////////////////
void InitModel();
void TaskModel();
///////////////////////////////////////////////////////////////////////////


#endif
```

구조체 선언시 EnuObject를 부모로 부터 상속 받습니다.

선언된 구조체를 이용하여 enuSpace와 연동하기 위한 C++ 코드는 아래와 같습니다.

```cpp
// CoreTask.cpp : Defines the initialization routines for the DLL.
//

#include "stdafx.h"
#include "CoreTask.h"

#include "..\model.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

// CCoreTaskApp

BEGIN_MESSAGE_MAP(CCoreTaskApp, CWinApp)
END_MESSAGE_MAP()


// CCoreTaskApp construction

CCoreTaskApp::CCoreTaskApp()
{
    // TODO: add construction code here,
    // Place all significant initialization in InitInstance
}

// The one and only CCoreTaskApp object

CCoreTaskApp theApp;


// CCoreTaskApp initialization

CString g_strDllPath;
HANDLE g_hConsole = NULL;
CPtrArray *enuObject;
double g_DT;

BOOL CCoreTaskApp::InitInstance()
{
    CWinApp::InitInstance();

    HINSTANCE hInstance = AfxGetInstanceHandle();
    wchar_t szPath[MAX_PATH];
    GetModuleFileName(hInstance, szPath, MAX_PATH);

    wchar_t drive[MAX_PATH];               // 드라이브 명
    wchar_t dir[MAX_PATH];                 // 디렉토리 경로
    wchar_t fname[MAX_PATH];               // 파일명
    wchar_t ext[MAX_PATH];                 // 확장자 명

    _wsplitpath_s(szPath, drive, dir, fname, ext);
    g_strDllPath.Format(L"%s%s", drive, dir);

    if (AllocConsole())
    {
        freopen("CONIN$", "rb", stdin);
        freopen("CONOUT$", "wb", stdout);
        freopen("CONOUT$", "wb", stderr);

        g_hConsole = ::GetStdHandle(STD_OUTPUT_HANDLE);
        SetConsoleTitle(L"Fortran");
    }

    return TRUE;
}

int CCoreTaskApp::ExitInstance()
{
    ::FreeConsole();
    return CWinApp::ExitInstance();
}
///////////////////////////////////////////////////////////////////////////////////////////
void PrintMessage(CString strMessage, CString strID = L"");
CString MBToWC(char * str);

///////////////////////////////////////////////////////////////////////////////////////////
extern "C"
{
    void _Message(char* pMessage);

    void TASK_MAIN_COM1(component1* pStruct);
    void TASK_MAIN_COM2(component2* pStruct);
    void TASK_INIT();
    void TASK_LOAD();
    void TASK_UNLOAD();
};
//////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////
// enuSpace interface function pointer.
void(*g_fcbSetValue)(wchar_t*, double) = NULL;
VariableStruct(*g_fcbGetValue)(wchar_t*) = NULL;
void(*g_fcbSetArrayValue)(wchar_t*, void*, int, int) = NULL;
void(*g_fcbSetReShapeArrayValue)(wchar_t*, void*, int, int) = NULL;
void(*g_fcbSetPinInterfaceVariable)(wchar_t*, void*, int, int) = NULL;
VariableStruct(*g_fcbGetArrayValue)(wchar_t*) = NULL;
void(*g_fcbPrintMessage)(wchar_t*, wchar_t*) = NULL;
//////////////////////////////////////////////////////////////////////////////////////////////
// enuSpace interface functions.
extern "C" __declspec(dllexport) void SetCallBack_SetValue(void fcbSetValue(wchar_t*, double));
extern "C" __declspec(dllexport) void SetCallBack_GetValue(VariableStruct fcbGetValue(wchar_t*));
extern "C" __declspec(dllexport) void SetCallBack_SetArrayValue(void fcbSetArrayValue(wchar_t*, void*, int, int));
extern "C" __declspec(dllexport) void SetCallBack_GetArrayValue(VariableStruct fcbGetArrayValue(wchar_t*));
extern "C" __declspec(dllexport) void SetCallBack_SetReShapeArrayValue(void fcbSetReShapeArrayValue(wchar_t*, void*, int, int));
extern "C" __declspec(dllexport) void SetCallBack_SetPinInterfaceVariable(void fcbSetPinInterfaceVariable(wchar_t*, void*, int, int));
extern "C" __declspec(dllexport) void SetCallBack_PrintMessage(void fcbPrintMessage(wchar_t*, wchar_t*));

extern "C" __declspec(dllexport) int GetTaskType();
extern "C" __declspec(dllexport) bool IsEnableTransfer(wchar_t* pMyType,wchar_t* pFromType, wchar_t* pToType);
extern "C" __declspec(dllexport) bool IsTaskStopWhenModify();

extern "C" __declspec(dllexport) bool OnInit();
extern "C" __declspec(dllexport) bool OnLoad();
extern "C" __declspec(dllexport) bool OnUnload();
extern "C" __declspec(dllexport) bool OnTask(__int64 time);
extern "C" __declspec(dllexport) void OnModeChange(int iMode);
extern "C" __declspec(dllexport) void ExecuteFunction(wchar_t* pStrFunction);

extern "C" __declspec(dllexport) void OnEditComponent(wchar_t* pStrSymbolName, wchar_t* pStrID);
extern "C" __declspec(dllexport) void OnShowComponent(wchar_t* pStrSymbolName, wchar_t* pStrID);
extern "C" __declspec(dllexport) bool OnShowHelp(wchar_t* pStrSymbolName);

extern "C" __declspec(dllexport) void OnSetObjectArray(CPtrArray* Object);
//////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////
extern "C" __declspec(dllexport) void SetCallBack_SetValue(void fcbSetValue(wchar_t*, double))
{
    g_fcbSetValue = fcbSetValue;
}

extern "C" __declspec(dllexport) void SetCallBack_GetValue(VariableStruct fcbGetValue(wchar_t*))
{
    g_fcbGetValue = fcbGetValue;
}

extern "C" __declspec(dllexport) void SetCallBack_SetArrayValue(void fcbSetArrayValue(wchar_t*, void*, int, int))
{
    g_fcbSetArrayValue = fcbSetArrayValue;
}

extern "C" __declspec(dllexport) void SetCallBack_GetArrayValue(VariableStruct fcbGetArrayValue(wchar_t*))
{
    g_fcbGetArrayValue = fcbGetArrayValue;
}

extern "C" __declspec(dllexport) void SetCallBack_SetReShapeArrayValue(void fcbSetReShapeArrayValue(wchar_t*, void*, int, int))
{
    g_fcbSetReShapeArrayValue = fcbSetReShapeArrayValue;
}

extern "C" __declspec(dllexport) void SetCallBack_SetPinInterfaceVariable(void fcbSetPinInterfaceVariable(wchar_t*, void*, int, int))
{
    g_fcbSetPinInterfaceVariable = fcbSetPinInterfaceVariable;
}

extern "C" __declspec(dllexport) void SetCallBack_PrintMessage(void fcbPrintMessage(wchar_t*, wchar_t*))
{
    g_fcbPrintMessage = fcbPrintMessage;
}

extern "C" __declspec(dllexport) void OnSetObjectArray(CPtrArray* Object)
{
    if (Object)    enuObject = Object;
}

extern "C" __declspec(dllexport) bool OnLoad()
{
    TASK_LOAD();
    return true;
}

extern "C" __declspec(dllexport) bool OnInit()
{
    try
    {
        if (g_fcbGetValue)
        {
            VariableStruct data;
            data = g_fcbGetValue(L"dt.model");
            if (data.type == DEF_DOUBLE)
                g_DT = *(double*)data.pValue;
        }
        // InitModel();
        TASK_INIT();
        return true;
    }
    catch (...)
    {

    }
    return false;
}

extern "C" __declspec(dllexport) bool OnTask(__int64 time)
{
    try
    {
        if (g_fcbGetValue)
        {
            VariableStruct data;
            data = g_fcbGetValue(L"dt.model");
            if (data.type == DEF_DOUBLE)
                g_DT = *(double*)data.pValue;
        }

        // TaskModel();            // C++ 함수 호출.

        for (int index = 0; index < enuObject->GetSize(); ++index)
        {
            EnuObject *pobj = (EnuObject *)(enuObject->GetAt(index));

            if (wcscmp(pobj->type, L"component1") == 0)
                TASK_MAIN_COM1((component1*)pobj);    // fortran 함수 호출.
            else if (wcscmp(pobj->type, L"component2") == 0)
                TASK_MAIN_COM2((component2*)pobj);    // fortran 함수 호출.
        }

        return true;
    }
    catch (...)
    {

    }
    return false;
}

extern "C" __declspec(dllexport) bool OnUnload()
{
    TASK_UNLOAD();
    return true;
}

extern "C" __declspec(dllexport) void OnEditComponent(wchar_t* pStrSymbolName, wchar_t* pStrID)
{

}

extern "C" __declspec(dllexport) void OnShowComponent(wchar_t* pStrSymbolName, wchar_t* pStrID)
{

}

extern "C" __declspec(dllexport) void OnModeChange(int iMode)
{

}

extern "C" __declspec(dllexport) void ExecuteFunction(wchar_t* pStrFunction)
{

}

extern "C" __declspec(dllexport) bool OnShowHelp(wchar_t* pStrSymbolName)
{
    return true;
}

extern "C" __declspec(dllexport) int GetTaskType()
{
    return TASK_TYPE_OBJECTARRAY;
}

extern "C" __declspec(dllexport) bool IsEnableTransfer(wchar_t* pMyType,wchar_t* pFromType, wchar_t* pToType)
{
    return true;
}

extern "C" __declspec(dllexport) bool IsTaskStopWhenModify()
{
    return true;
}
////////////////////////////////////////////////////////////////////////////
void PrintMessage(CString strMessage, CString strID)
{
    if (g_fcbPrintMessage)
    {
        strMessage = L"model->" + strMessage;
        g_fcbPrintMessage(strMessage.GetBuffer(0), strID.GetBuffer(0));
    }
}

CString MBToWC(char * str)
{
    wchar_t* strResult = new wchar_t[strlen(str) + 1];
    MultiByteToWideChar(CP_ACP, 0, str, (int)strlen(str) + 1, strResult, (int)strlen(str) + 1);
    CString strReturn;
    strReturn = strResult;
    delete[] strResult;
    return strReturn;
}

void _Message(char* pMessage)
{
    PrintMessage(MBToWC(pMessage));
}
```

태스크의 타입을 지정하는 함수 GetTaskType\(\)에서 리턴값을 TASK\_TYPE\_OBJECTARRAY로 반환을 수행하면, enuSpace 프로그램은  OnSetObjectArray\(\)함수를 통하여 CPtrArray를 통하여 객체의 리스트 정보를 제공합니다.

OnTask\(\)함는 시뮬레이션 실행시 매 주기 호출되는 함수 입니다.

```cpp
extern "C" __declspec(dllexport) bool OnTask(__int64 time)
{
    try
    {
        if (g_fcbGetValue)
        {
            VariableStruct data;
            data = g_fcbGetValue(L"dt.model");
            if (data.type == DEF_DOUBLE)
                g_DT = *(double*)data.pValue;
        }

        // TaskModel();            // C++ 함수 호출.

        for (int index = 0; index < enuObject->GetSize(); ++index)
        {
            EnuObject *pobj = (EnuObject *)(enuObject->GetAt(index));

            if (wcscmp(pobj->type, L"component1") == 0)
                TASK_MAIN_COM1((component1*)pobj);    // fortran 함수 호출.
            else if (wcscmp(pobj->type, L"component2") == 0)
                TASK_MAIN_COM2((component2*)pobj);    // fortran 함수 호출.
        }

        return true;
    }
    catch (...)
    {

    }
    return false;
}
```

전체 오븍젝트의 개수에 대하여 각 타입에 따라서 개별 처리를 수행합니다. enuSpace는 오브젝트의 컴포넌트의 타입에 따라서 type정보를 제공합니다. 자신의 타입에 맞는 형으로 변환하여 컴포넌트의 메인 함수를 호출합니다.

#### Fortran 연동

fortran 코드와 연동하기 위해서 extern 함수를 선언합니다.

```cpp
///////////////////////////////////////////////////////////////////////////////////////////
extern "C"
{
    void _Message(char* pMessage);

    void TASK_MAIN_COM1(component1* pStruct);
    void TASK_MAIN_COM2(component2* pStruct);
    void TASK_INIT();
    void TASK_LOAD();
    void TASK_UNLOAD();
};
//////////////////////////////////////////////////////////////////////////////////////////////
```

Fortran Code

```fortran
MODULE Interface_to_C_Func

   INTERFACE

      SUBROUTINE Message(string) BIND(C, NAME="_Message")
         USE, INTRINSIC :: ISO_C_BINDING, ONLY : C_INT, C_CHAR, C_PTR, C_DOUBLE
         !.. Return value

         !.. Argument list
         CHARACTER(KIND=C_CHAR)     :: string(*)     
      END SUBROUTINE Message 

   END INTERFACE

END MODULE Interface_to_C_Func

MODULE IO_DATA
    USE, INTRINSIC :: ISO_C_BINDING
    IMPLICIT NONE

    TYPE :: COMPONENT1
          SEQUENCE
          REAL(C_DOUBLE) :: DUMMY(18)   ! EnuObject Dummy
          INTEGER(C_INT) :: ICOUNT
          REAL(C_DOUBLE) :: FVALUE
          REAL(C_DOUBLE) :: FARRAY(10,5)
    END TYPE COMPONENT1

    TYPE :: COMPONENT2
          SEQUENCE
          REAL(C_DOUBLE) :: DUMMY(18)   ! EnuObject Dummy
          INTEGER(C_INT) :: INPUT
          INTEGER(C_INT) :: OUTPUT
    END TYPE COMPONENT2

END MODULE IO_DATA


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    SUBROUTINE TASK_MAIN_COM1(INPUT) BIND(C,NAME='TASK_MAIN_COM1')

        USE Interface_to_C_Func
        USE IO_DATA

        TYPE(COMPONENT1) INPUT

        INPUT.ICOUNT = INPUT.ICOUNT + 1
        INPUT.FVALUE = INPUT.FVALUE + 0.1
        INPUT.FARRAY(1,1) = INPUT.FARRAY(1,1) + 0.1

        CALL Message('Call Main Proc-Component1')      

        RETURN
    END

    SUBROUTINE TASK_MAIN_COM2(INPUT) BIND(C,NAME='TASK_MAIN_COM2')

        USE Interface_to_C_Func
        USE IO_DATA

        TYPE(COMPONENT2) INPUT

        INPUT.INPUT = INPUT.INPUT + 1
        INPUT.OUTPUT = INPUT.INPUT

        CALL Message('Call Main Proc-Component2')      

        RETURN
    END    

    SUBROUTINE TASK_INIT
        ! CALL INIT_PROC()
        RETURN
   END  

    SUBROUTINE TASK_LOAD
        ! CALL LOAD_PROC()
        RETURN
    END      

    SUBROUTINE TASK_UNLOAD
        ! CALL UNLOAD_PROC()
        RETURN
    END
```

C++ 코드에서 호출한 TASK\_MAIN\_COM1\(\(component1\*\)pobj\) 함수에서 구조체의 주소값을 전달을 수행한다.

Fortran 코드에서 동일한 구조체를 선언하고, 선언된 구조체를 입력으로 받는다.

Fortran에서 구조체 선언 \(C++에서 선언된 동일한 메모리 사이즈를 이용하여 적용\)

```fortran
MODULE IO_DATA
    USE, INTRINSIC :: ISO_C_BINDING
    IMPLICIT NONE

    TYPE :: COMPONENT1
          SEQUENCE
          REAL(C_DOUBLE) :: DUMMY(18)   ! EnuObject Dummy
          INTEGER(C_INT) :: ICOUNT
          REAL(C_DOUBLE) :: FVALUE
          REAL(C_DOUBLE) :: FARRAY(10,5)
    END TYPE COMPONENT1

    TYPE :: COMPONENT2
          SEQUENCE
          REAL(C_DOUBLE) :: DUMMY(18)   ! EnuObject Dummy
          INTEGER(C_INT) :: INPUT
          INTEGER(C_INT) :: OUTPUT
    END TYPE COMPONENT2

END MODULE IO_DATA
```

REAL\(C\_DOUBLE\) :: DUMMY\(18\)   ! EnuObject Dummy 선언은 EnuObject로 부터 상속받은 구간에 대하여 더미 영역으로 할당한 내용이다.

입력받은 구조체의 정보를 이용하여 계산을 수행한다.

계산된 결과는 enuSpace의 심볼테이블 다이얼로그를 통하여 확인 및 값을 변경할 수 있다.

