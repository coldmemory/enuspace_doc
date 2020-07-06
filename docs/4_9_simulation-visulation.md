---
layout: default
title: Simulation & Visualization
parent: enuSpace Tutorial
nav_order: 9
---

# **enuSpace 시뮬레이션 기능 및 Data Visualization 사용방법**

---

본 문서는 enuSpace for mars version 기반으로 작성되었습니다.



enuSpace 학생용 버젼 다운로드 :[http://enuspace.tistory.com/entry/enuSpace-for-Mars-2017](http://enuspace.tistory.com/entry/enuSpace-for-Mars-2017)

enuSpace for mars에서 시뮬레이션 또는 task를 개발함에 있어 2가지 형태의 모델로 구성될 수 있습니다. enuSpace for mars의 ontask함수를 활용한 방법과 외부의 task의 모듈을 연동하는 방법입니다.

**Lesson5 sample :**[![](http://t1.daumcdn.net/tistory_admin/blogs/image/extension/zip.gif?_version_=5edd9eee8cdd891e2125a28405975fd20eb6ee50)lesson5.zip](http://enuspace.tistory.com/attachment/cfile9.uf@260B884B590016CA2BED05.zip)

1. 로직 라이브러리를 이용한 flowbased programming 방법.

2. 외부 모델을 이용한 연동 방법.

**동영상 미리보기 **[**https://youtu.be/V9Tw4aVTfYo**](https://youtu.be/V9Tw4aVTfYo)

## **New Project**

---

새로운 프로젝트를 생성하기 위해서 Home-&gt;New-&gt;New Project메뉴를 이용하여 새로운 프로젝트를 생성합니다.

**  **![](/assets/simulation-visulation/8 newproject0.png)**      
**

## **Simulation Time Setup**

---

새로운 프로젝트 생성을 완료하였다면, 리본메뉴 Data/Communication-&gt;System Configuration메뉴를 선택하여 System Configuration 대화창의 속성을 설정합니다. 시뮬레이션용으로 설정하기 위해서는 Time의 속성중 Simulation Time을 설정합니다. Simulation Time을 설정하게 되면 enuSpace에서 기동되는 시작시간의 정보는 0초부터 동작을 수행합니다.

System Time옵션에서 Simulation Time옵션으로 변경 수행시 프로젝트에 기존에 누적된 히스토리 데이터베이스가 모두 제거되어 초기화 됩니다. 프로젝트 로드시에도 기존의 히스토리 데이터베이스를 초기화 합니다.

참고로 System Time의 설정은 현재시간\(UTC\)을 기준으로 모든 데이터가 생성되고  히스토레 데이터에 누적됩니다.

**  **![](/assets/simulation-visulation/8 newproject1.png)**      
**

## **Simulation Scheduling**

---

enuSpace for mars의 task\(\)함수를 사용하는 경우에는 flowbased programming을 통하여 동작을 수행합니다. 내부 task\(\)함수는 스케쥴링 속성값에 따라서 주기적인 연산을 호출하도록 구성되어 있습니다. 속성 설정하기 위해서 Project Explorer창 Task하위 logic\_svg 아이템을 선택합니다. logic\_svg 속성창 중 Cycle \(Hz\) 속성은 1초에 1, 2, 3, 4, 6, 8, 12, 24회 호출 주기에 대한 설정입니다. Task In/Out의 속성은 선택한 Task에 대하여 연산을 수행할 것인지, 제외할것인지를 설정합니다.

![](/assets/simulation-visulation/8 newproject2.png)

시뮬레이션 모델을 제작하다보면 task\(\)함수에서 delta T값을 이용하는 경우가 있습니다. 전역변수 dt값을 이용하여 코드를 구현합니다.

```lua
function _ontask()
    --TODO Add your lua script code here
    local deltaT =dt
    --bla bla ~~
end
```

---

## **외부 모델 연계 API**

---

시뮬레이션 모델 개발시 기존의 코드를 재활용하거나 외부의 모델과의 인터페이스가 필요한 경우가 있습니다. enuSpace는 외부 모델과 연동하기 위한 인터페이스 모듈을 제공합니다. 외부 모델과 연계시 dynamic link library\(dll\)을 이용합니다.

외부 연동 인터페이스 모듈의 dll의 주요 함수는 아래와 같습니다.

```cpp
extern "C" __declspec(dllexport) bool OnInit();
extern "C" __declspec(dllexport) bool OnLoad();
extern "C" __declspec(dllexport) bool OnUnload();
extern "C" __declspec(dllexport) bool OnTask();
```

각 함수는 아래와 같은 조건에서 호출됩니다.

OnInit\(\) : 첫 기동시 호출되는 초기화 함수

OnLoad\(\) : dll 로드수행시 호출되는 함수

OnUnload\(\) : dll 언로드 수행시 호출되는 함수

OnTask\(\) : 스케쥴링 주기에 따라서 호출되는 함수

OnTask\(\)함수 구현부에는 시뮬레이션을 수행하고자 하는 알고리즘을 추가합니다. 작성된 코드와 enuSpace와 연동하기 위해서 인터페이스용 콜백함수 4개를 제공합니다.

```cpp
extern "C" __declspec(dllexport) void SetCallBack_SetValue(void fcbSetValue(wchar_t*, double));
extern "C" __declspec(dllexport) void SetCallBack_GetValue(DBDataStruct* fcbGetValue(wchar_t*));
extern "C" __declspec(dllexport) void SetCallBack_SetArrayValue(void fcbSetArrayValue(wchar_t*, void*, int, int));
extern "C" __declspec(dllexport) void SetCallBack_GetArrayValue(DBDataStruct* fcbGetArrayValue(wchar_t*));
```

특정 데이터베이스의 Tag값을 읽고 쓰기 위한 함수 포인터입니다. 본 함수는 dll로드 수행시 함수의 포인터로 전달됩니다. 전달된 함수 포인터 이용하여 값을 읽거나 쓰기를 수행합니다.

구현부를 보시면 아래와 같습니다.

```cpp
void (*g_fcbSetValue)(wchar_t*, double) = NULL;
DBDataStruct* (*g_fcbGetValue)(wchar_t*) = NULL;
void(*g_fcbSetArrayValue)(wchar_t*, void*, int, int) = NULL;
DBDataStruct* (*g_fcbGetArrayValue)(wchar_t*) = NULL;

extern "C" __declspec(dllexport) void SetCallBack_SetValue(void fcbSetValue(wchar_t*, double)) { g_fcbSetValue = fcbSetValue; }
extern "C" __declspec(dllexport) void SetCallBack_GetValue(DBDataStruct* fcbGetValue(wchar_t*)) { g_fcbGetValue = fcbGetValue; }
extern "C" __declspec(dllexport) void SetCallBack_SetArrayValue(void fcbSetArrayValue(wchar_t*, void*, int, int)) { g_fcbSetArrayValue = fcbSetArrayValue; }
extern "C" __declspec(dllexport) void SetCallBack_GetArrayValue(DBDataStruct* fcbGetArrayValue(wchar_t*)) { g_fcbGetArrayValue = fcbGetArrayValue; }
```

위 코드는 기 제공되는 코드의 예시입니다.

```cpp
CMap<CString, LPCWSTR, DBDataStruct*, DBDataStruct*> g_DBMapList;
void SetArrayValue(CString strVariable, void* pSrc, int iType, int iSize)
{
    if (g_fcbSetArrayValue)
        g_fcbSetArrayValue(strVariable.GetBuffer(0), pSrc, iType, iSize);
}
DBDataStruct* GetArrayValue(CString strVariable)
{
    if (g_fcbGetArrayValue)
        return g_fcbGetArrayValue(strVariable.GetBuffer(0));
    return NULL;
}
void SetValue(CString strVariable, double fValue)
{
    double fReturn = 0;
    DBDataStruct* pData = NULL;
    g_DBMapList.Lookup(strVariable, pData);
    if (g_fcbSetValue && pData == NULL)
    {
        pData = g_fcbGetValue(strVariable.GetBuffer(0));
        g_DBMapList.SetAt(strVariable, pData);
    }
    if (pData && pData->pValue)
    {
        switch (pData->itype)
        {
        case DEF_INT:
            *(int*)pData->pValue = (int)fValue;
            break;
        case DEF_FLOAT:
            *(float*)pData->pValue = (float)fValue;
            break;
        case DEF_DOUBLE:
            *(double*)pData->pValue = fValue;
            break;
        case DEF_BOOL:
            if (fValue == 1)
                *(bool*)pData->pValue = true;
            else
                *(bool*)pData->pValue = false;
            break;
        case DEF_WCHAR:
            break;
        default:
            break;
        }
    }
}
double GetValue(CString strVariable)
{
    double fReturn = 0;
    DBDataStruct* pData = NULL;
    g_DBMapList.Lookup(strVariable, pData);
    if (g_fcbGetValue && pData == NULL)
    {
        pData = g_fcbGetValue(strVariable.GetBuffer(0));
        if (pData)
            g_DBMapList.SetAt(strVariable, pData);
    }
    if (pData && pData->pValue)
    {
        switch (pData->itype)
        {
        case DEF_INT:
            fReturn = *(int*)pData->pValue;
            break;
        case DEF_FLOAT:
            fReturn = *(float*)pData->pValue;
            break;
        case DEF_DOUBLE:
            fReturn = *(double*)pData->pValue;
            break;
        case DEF_BOOL:
            if (*(bool*)pData->pValue == TRUE)
                fReturn = 1;
            else
                fReturn = 0;
            break;
        default:
            break;
        }
    }
    return fReturn;
}
```

실제 인터페이스는 값을 읽기 쓰기위한 코드와 모델 연산로직 코드를 추가함으로서 외부 모델을 연계할 수 있습니다.

**모델 예\)**

**모델의 실행 코드와 인터페이스 코드 예시**

```cpp
double display[16][16];
float initValue = 1.0f;

extern "C" __declspec(dllexport) bool OnTask()
{
    initValue = initValue + 0.1;
    for (int x = 0; x < 16; x++)
    {
        for (int y = 0; y < 16; y++)
        {
            display[x][y] = 1.0 + sin(double((x * 16) + (y * 16)) / 3.141592 / 5 + initValue);
        }
    }
    SetArrayValue(L"@CORE.display[0][0]", display, DEF_DOUBLE, 16 * 16);
    return true;
}
```

sin파를 생성하여 데이터 인터페이스를 수행하는 코드를 작성하였습니다. 위와 같이 코드를 추가하고 컴파일을 수행하여 CoreTask.dll을 생성합니다. 모델 생성이 완료하였다면 데이터베이스와 연동하기 위한 tag id를 enuSpace 프로젝트에 추가를 수행합니다. SetArrayValue\(\)함수는 배열 정보를 enuSpace에서 추가한 tag의\(@CORE.display\[0\]\[0\]\) 값에 연산 결과를 전달하는 과정입니다.

SetArrayValue\(\) 함수의 파라미터 정보를 보면 변수명, 원본 데이터의 메모리 주소, 복사하고자하는 데이터 타입, 사이즈값입니다. 만약 단일 변수에 추가하고자 하는 경우에는 SetValue\(\)함수를 이용합니다. 경우에 따라서 위의 예시에서 제공하는 SetValue\(\)함수 등은 확장 및 변경하여 구현할 수 있습니다.

## **enuSpace for mars 데이터베이스 TAG 추가**

---

enuSpace의 리본메뉴 Data/Communication-&gt;DB Show 버튼을 클릭합니다. 다음과 같이 DB Table의 정보가 나타나고 DB+ 버튼을 클릭하여 모델간의 인터페이스를 위한 TAG 변수를 추가합니다. 추가되는 최종 TAG ID는 @문자가 앞에 추가됩니다. @문자는 데이터베이스 TAG 변수와 전역변수와의 구분자로도 활용됩니다. 데이터베이스 TAG ID를 이용하여 스크립트에서 활용합니다.

![](/assets/simulation-visulation/8 newproject3.png)

정상적으로 데이터베이스 TAG가 추가완료 후 앞에서 제작한 외부 TASK\(CoreTask.dll\)를 enuSpace 프로젝트에 추가합니다. Project Explorer의 Task항목을 선택하고 팝업메뉴 Add Task를 선택하여 Task Module의 콤보박스에 CoreTask.dll을 선택합니다. 프로젝트 디렉토리 lesson5//Task//CoreTask에 앞에서 생성한 CoreTask.dll 파일이 존재하는 경우 자동으로 콤보박스에서 선택이 가능하도록 제공이 됩니다.

![](/assets/simulation-visulation/8 newproject4.png)

디렉토리의 구조 및 외부 TASK의 위치는 아래 그림과 같습니다.

![](/assets/simulation-visulation/8 newproject5.png)

TASK가 정상 등록이 되었다면, TASK를 기동하기 위해서 리본메뉴 Home-&gt;Script Operation의 Run 버튼을 클릭합니다. 연산이 정상적으로 처리되고 있는지를 확인하기 위해서 리본메뉴의 리본메뉴의 Data/Communication-&gt;DB Show메뉴를 선택하여 데이터베이스의 실시간 값을 확인합니다.![](/assets/simulation-visulation/8 newproject9.png)

아래 그림과 같이 차트 버튼을 클릭하여 팝업 Trend를 이용하여 데이터값을 확인할 수 있습니다. 차트사용 방법은 별도의 강좌에서 설명하도록 하겠습니다.

![](/assets/simulation-visulation/8 newproject10.png)

## **3D data visualization**

---

앞에서 제작한 배열변수의 값을 3차원 디스플레이에 디스플레이 하기 위해서 픽쳐파일 core\_display.x3d 파일을 추가합니다. 추가된 x3d 파일을 선택후 Terrain객체를 추가합니다. Terrain 객체의 속성중 subdivision\_x, subdivision\_y의 값을 데이터베이스 TAG의 배열정보 16, 16으로 설정합니다. subdivision의 값을 설정함에 따라 내부의 double형 데이터 변수 data\[16\]\[16\]가 생성됩니다.![](/assets/simulation-visulation/8 newproject12.png)

추가된 Terrain 객체에 javascript 또는 lua script를 이용하여 데이터베이스 tag의 값을 그래픽 객체의 디스플레이 객체에 전달하여 실시간 데이터를 디스플레이 하기 위해서 아래 예시 코드와 같이 memcpy\(\) 함수를 이용합니다. memcpy\(\) 함수를 이용하지 않고 개별적인 인터페이스는

data\[0\]\[0\] = @CORE.display\[0\]\[0\];

data\[0\]\[1\] = @CORE.display\[0\]\[1\]; ... 와 같이 코드를 작성할 수 있습니다.

\* memcpy함수 사용시 변수의 타입과 변수 사이즈 입력에 주의하여야 한다. 잘못된 인자의 사용으로 인한 메모리 릭 또는 비정상 종료가 발생할 수 있습니다.

ex\) lua script

```lua
function _ontaskview()
    --TODO Add your lua script code here
    memcpy(&data[0][0],&@CORE.display[0][0],16*16)
end
```

ex\) javascript

```js
function _ontaskview()
{
    //TODO Add your javascript code here
    memcpy(&data[0][0],&@CORE.display[0][0],16*16);
}
```

![](/assets/simulation-visulation/8 newproject13.png)

## **2D data visualization**

---

앞 강좌에서 기초객체의 속성값을 이용하여 2D 그래픽에 가시화하는 방법에 소개하였습니다. 간략히 살펴보면 추가된 객체를 선택하고 ontaskview의 함수를 추가합니다. enuSpace는 javascript와 lua script를 지원하며 각각의 예시는 아래와 같습니다.

```js
function _ontaskview()
{
    //TODO Add your javascript code here
    textContent = @CORE.display[0][0];
}
```

```lua
function _ontaskview()
    --TODO Add your lua script code here
    text = string.format("%f", @CORE.display[0][0])
end
```

데이터베이스의 tag 값을 가져오기 위해서는 데이터베이스 tag id를 이용합니다. 데이터베이스 변수는 첫문자에 @문자를 포함합니다.

![](/assets/simulation-visulation/8 newproject14.png)

데이터베이스의 값을 가져와 Text 객체의 값으로 할당하는 예시 화면.

사각형의 객체를 가져와 연산 결과를 높이값으로 표현하기 위해서 아래와 같이 코드를 추가합니다.

```js
function _ontaskview()
{
    //TODO Add your javascript code here
    height = @CORE.display[0][15]*50;
}
```

![](/assets/simulation-visulation/8 newproject15.png)

## **시뮬레이션 상태값 저장 및 복원 \(Snap, Reset\) 기능**

---

enuSpace 시뮬레이션 기능은 현재 설정된 상태값을 저장하고 저장된 상태값에 대한 복원 기능을 제공합니다. 상단의 리본메뉴 Home-&gt;Condition의 Snap 버튼과 Reset 버튼을 이용합니다.

