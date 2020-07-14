---
layout: default
title: enuRegisterFunction
parent: Application API
---
# bool enuRegisterFunction\(wchar\_t\* strFunction, int \(\*pfunc\)\(lua\_State\* L\)\)

bool enuRegisterFunction\(wchar\_t\* strFunction, int \(\*pfunc\)\(lua\_State\* L\)\);

#### 

#### Parameters

Type : wchar\_t\* strFunctionName

스크립트에서 사용할 함수 이름을 지정한다.

Type : lua\_state\* functionPointer

스크립트에서 호출되는 함수포인터값을 지정한다.



#### Return Value

Type : bool

외부 함수 등록 여부를 제공한다. 

#### 

#### Remarks

본 함수는 enuCreateProject\(\) 함수 다음에 호출되어 등록하여야 한다. 정상적으로 외부함수가 등록되었다면, enuLoadProject\(\)함수를 통하여 외부함수가 프로젝트에 적용된다. 



#### Examples

```cpp
#include <SvgDefine.h>
#include <enuLibrary.h>

int AddFunction(lua_State *L)
{
	const char* str;
	str = luaL_checkstring(L,1);
	CString strPageName(str);

	str = luaL_checkstring(L,2);
	CString strScriptName(str);

	int iInput1 = luaL_checknumber(L,3);
	int iInput2 = luaL_checknumber(L,4);
	int iReturn = iInput1 + iInput2;
	lua_pushnumber(L, iReturn);

	return 1;
}

BOOL CSampleDlg::OnInitDialog()
{
	HPROJECT m_SpadeProject = enuCreateProject();
	
	enuRegisterFunction(L"AddFunction", AddFunction);

	enuLoadProjectFile(L"Sample\\Sample.enup");
	enuSetRuntimeMode(true);
	enuShowRuntimeView(NULL);

	return TRUE; 
}
```

위와 같이 응용프로그램을 개발하였을 경우, enuSpace 뷰 화면에서 AddFunction\(\)함수를 호출하여 활용할 수 있다. 

```lua
function onmousedown()
    local add = Addfunction(5,6)
end
```

#### 

#### Tutorial



**응용프로그램에서 lua 스크립트 함수 호출하기**

응용 프로그램에서 enuSpace 뷰에 추가된 함수를 호출 하기 위해서, 아래 그림과 같이 예시를 생성한다.

![](./enuspace_doc/docs/assets/enuRegisterFunction_step1.png)  
1. HMI 심볼 객체를 생성한다. \(심볼 객체 생성 방법 참조\) 생성될 심볼은 사용자의 함수를 추가하여 작성한다.

2. HMI 시볼 객체를 그래픽 Picture 화면에 추가한 후 Use 객체의 ID를 지정한다. \(ID\_PUMP\) 설정된 프로젝트를 저장한다. 

3. 저장된 프로젝트를 이용하여 응용 프로그램에서 Use 객체의 함수를 호출하여 속성 값을 변경한다.



위 Example 코드는 샘플 프로젝트 파일을 이용하여 프로젝트를 로드 수행한 후 특정 객체의 함수를 호출 하는 예시이다.

```cpp
#include <SvgDefine.h>
#include <enuLibrary.h>

BOOL CSampleDlg::OnInitDialog()
{
	HPROJECT m_Project = enuCreateProject();
	enuLoadProjectFile(L"d:\\Sample\\Sample.enup");

	enuSetRuntimeMode(true);
	enuShowRuntimeView(NULL);

	HSVG pSvgHandler = enuGetPageClass(L"Picture\\SamplePicture.svg");

	if (pSvgHandler)
	{
		enuExecuteFunction(pSvgHandler, L"ID_PUMP.SetProperty(false, false, 0, 2, \"LABEL\", true, true, true, true)");
	} 

	return TRUE; 
}
```

**enuExecuteFunction\(\)**

본 함수는SVG핸들러를 이용하여 함수를 호출하는API이다.



**enuExecuteFunctionByNode\(\)**

본 함수는SVG핸들과 객체 핸들을 이용하여 함수를 호출하는API이다.

![](./enuspace_doc/docs/assets/enuRegisterFunction_step2.png)



**lua 스크립트에서 응용프로그램 함수 호출하기**

내부 스크립트에서 응용 프로그램에서 생성한 함수를 호출하기 위한 방법에 대하여 알아본다. 내부 스크립트에서 응용 프로그램의 함수를 호출하기 위해서는 응용 프로그램은 다음과 같은 절차를 통하여 함수를 등록 및 적용한다. 



1. 결과값을 디스플레이 하기 위한 Text객체를 추가한다. 추가된 Text의 객체의 아이디를 ID\_TEXT로 지정한다.

2. 사각형 객체를 추가하고 마우스다운 이벤트 스크립트 창을 호출한다. 

3. 스크립트 창에 스크립트를 작성한다.

4. 외부함수에 입력 파라미터를 작성하고 컴파일 버튼을 누른다. 

주\) 컴파일 시 아래와 같은 info 정보가 나타난다. 

info ID\_1ZJYsp0::onmousedown AddFunction Recognized internal variable in this function.

Compile OK : Page Name:samplepicture, Object Name:ID\_1ZJYsp0, Function Name:onmousedown

![](./enuspace_doc/docs/assets/enuRegisterFunction_step3.png)  
샘플 프로젝트를 작성하였다면 위 Sample코드와 같이 함수를 등록하는 코드를 작성한다.

```cpp
#include <SvgDefine.h>
#include <enuLibrary.h>

int AddFunction(lua_State *L)
{
	const char* str;
	str = luaL_checkstring(L,1);
	CString strPageName(str);

	str = luaL_checkstring(L,2);
	CString strScriptName(str);

	int iInput1 = luaL_checknumber(L,3);
	int iInput2 = luaL_checknumber(L,4);
	int iReturn = iInput1 + iInput2;
	lua_pushnumber(L, iReturn);

	return 1;
}

BOOL CSampleDlg::OnInitDialog()
{
	HPROJECT m_SpadeProject = enuCreateProject();
	
	enuRegisterFunction(L"AddFunction", AddFunction);

	enuLoadProjectFile(L"Sample\\Sample.enup");
	enuSetRuntimeMode(true);
	enuShowRuntimeView(NULL);

	return TRUE; 
}
```

**enuRegisterFunction\(\)**

본 함수는 함수를 등록하기 위한API함수이며,사용하기 위해서는 루아 라이브러리를 링크하여야 한다.



아래 그림은Visual Studio에 루아 라이브러리를 등록하는 방법을 나타낸 것이다

![](./enuspace_doc/docs/assets/enuRegisterFunction_step4.png)  


아래 그림은 lua 스크립트에서 외부 응용프로그램의 함수를 호출하여 연산된 결과를 나타낸다.

![](./enuspace_doc/docs/assets/enuRegisterFunction_step5.png)

