---
layout: default
title: enuSpace Download
nav_order: b
last_modified_date: now
---

# Release Note

### ![](./assets/neptune_icon.png)enuSpace for neptune \(2022\)

We are working.
* Fixed : 3d - Memory leak patch when removing 3D objects through API.
* Improved : Improved 3d scatter chart function. (line option)
* New : Script api added - RelativePath function added.
* Improved : 3d view - Fixed object selection not being displayed in runtime mode
* Fixed : 3d view - Patch a bug that occurs when executing the text billboard option.
* Fixed : Trend object label-format added. (engineering unit).
* New : Added trend log scale.  
* Improved : Flownetwork task module updated.
* Improved : Added execution function for relative path input parameter when executing program.
* Improved : Added transparent coordinate setting function to contour object.
* Improved : ExternalFunction multi module support.
* Improved : Improved this contour object property dialog.
* Improved : Contour object x-axis, y-axis text label display.
* Fixed : Error in assigning address of string variable in SetArrayValue function.
* Fixed : Fixed line object arrow drawing.

---

**Release date : 2021.07.07, Version : 6.0.0.0**

64bit Version : [enuSpace for neptune 6.0.0.0 x64 Download \(student\)](http://www.enu-tech.co.kr/student_release/enuspace_setup_6.0.0.0_x64_st.exe)

New feature
* Improved :Add time information to the debug output window
* New : javascript and lua api added - [DeleteObject](/enuspace_doc/docs/enusscriptapi_deleteobject/) added. 
* Improved : Shape Outline ribbon menu (line weight, line dashes) added.
* New : enuSpace Runtime viewer - Project file relative path input module.
* New : Loading the project-based WebExtension.dll module.
* Improved : DXFHandler SOLID object patched. Error exception handling.
* Improved : DXFHandler User-based property setting window provided.
* Fixed : Special character processing when saving SetAttribute object variable.
* New : Add color fill and gradient color functions when expressing a series of trend objects.
* New : Added interface to link with functions of external modules.

---

### ![](./assets/uranus_icon.png)enuSpace for uranus \(2021\)

---

**Release date : 2021.02.15, Version : 5.0.2.0**

64bit Version : [enuSpace for uranus 5.0.2.0 x64 Download \(student\)](http://www.enu-tech.co.kr/student_release/enuspace_setup_5.0.2.0_x64_st.exe)

New feature
* New : APP api added - enuUpdateScriptByNode API added.
* Improved : dll recognition function referenced in task dll.
* Improved : task api added - SetValueByString function added.
* New : APP api added -  enuSetComponentHighlightOption API added.
* New : APP api added -  enuSetComponentSymbolTableOption API added.
* New : APP api added -  enuUpdateDatabase API added.
* New : APP api added -  enuInsertDatabase API added.
* New : APP api added -  enuDeleteDatabase API added.
* Improved : text object interface variable update module patched.
* Improved : logic task - flow based calculation module patched.
* New : javascript and lua api added - UpdateDatabase API added.
* New : javascript and lua api added - InsertDatabase API added.
* New : javascript and lua api added - DeleteDatabase API added.
* Improved : Editbox text cursor position error patch.
* New : Addition of color setting function outside canvas
* New : APP api added - enuSetTagValue API added.
* New : lua script api added - hdf5 moudle API added.
* New : javascript and lua api added - GetVariabplePointer API added.
* New : javascript and lua api added - GetVariabplePointer_str API added.
* Imporved : javascript and lua api - SetAttribute function patched.
* New : sqlite db interface module - ExecBegin, ExecCommit function added.
* Improved : Additional management module function added for trend object scheduler update object.
* New : trend object attribute added - "symbol-step" attribute added.
* Improved : Switching from Runtimeview class to drawing logic RTM delivery method.
* Improved : Add HMI, LOC, PIC separator when registering script.
* Improved : external tast pin and link interface module patched.

---

**Release date : 2020.08.07, Version : 5.0.1.0**

32bit Version : [enuSpace for uranus 5.0.1.0 x32 Download \(student\)](http://www.enu-tech.co.kr/student_release/enuspace_setup_5.0.1.0_x32_st.exe)

64bit Version : [enuSpace for uranus 5.0.1.0 x64 Download \(student\)](http://www.enu-tech.co.kr/student_release/enuspace_setup_5.0.1.0_x64_st.exe)

New feature

* Updated : V8 version 7.5.288.31
* Updated : CAD DXF file parsing.
* New : API added : void enuTrendReset\(HNODE TrendNode\)
* Improved : Terrain object attribute added\(draw direction, grid interpolation\)
* Improved : Trend object Text Label function added\(SetAttribute\(L"text-label", "a;b;c;d"\)\)
* Bugfixed : Fixed Terrain object abnormal coordinate display
* Bugfixed : Enable Trend Chart Object Recent Value Display Option
* Bugfixed : Fixed bug when obtaining terrain object data
* Bugfixed : Fixed an error when executing a script at the 3D root node

---

**Release date : 2020.03.01, Version : 5.0.0.0**

64bit Version : [enuSpace for uranus 5.0.0.0 x64 Download \(student\)](http://www.enu-tech.co.kr/student_release/enuspace_setup_5.0.0.0_x64_st.exe)

New feature

* New : CAD DXF file  import function
* New : API added : enuSetCanvasColorBySvg\(HSVG pSvg, byte iR, byte iG, byte iB\)
* New : API added : enuSetCanvasOutsideColorBySvg\(HSVG pSvg, byte iR, byte iG, byte iB\)
* New : API added : enuCreateG\(HSVG pSvgHandler, wchar\_t\* strID\)
* New : API added : enuCreateGAsync\(HSVG pSvgHandler, wchar\_t\* strID\)
* Improved : SQLite, Maria DB interface updated.

---

### ![](/assets/enuspace_saturn.png)enuSpace for saturn \(2020\)

---

**Release date : 2020.02.06, Version : 4.0.6.0**

64bit Version : [enuSpace for saturn 4.0.6.0 x64 Download \(student\)](http://www.enu-tech.co.kr/student_release/enuspace_setup_4.0.6.0_x64_st.exe)

New feature

* Drawing logic optimization : 3D contour
* New : 3D Object billboard function
* fixed : minimum value was not normally displayed when configuring the elevation color with HSL instead of RGB.
* fixed : rotation\_z property display error
* fixed : did not run Malfunction in the scenario base test
* fixed : Malfunction Insert function sometimes did not work
* fixed : which the SetValue type command did not work in the scenario base test.

---

**Release date : 2020.01.07, Version : 4.0.5.0**

64bit Version : [enuSpace for saturn 4.0.5.0 x64 Download \(student\)](http://www.enu-tech.co.kr/student_release/enuspace_setup_4.0.5.0_x64_st.exe)

New feature

* Task model scheduling and control the task model for simulation.
* Improved : wchar\_t array variable script interface.
* New : Support multi window for 3D rendering.
* New : copy parameter / paste parameter function added.
* Improved : 3d surface polygon smooth option.
* Fixed : Symbol table "more" display bug fixed.
* Improved : 2D window auto scale function. 
* Fixed : 2D window copy, paste, cut, delete function key disabled in runtime view.
* New : Add properties to 2D contour objects. Set transparency if the minimum value of elevation and the data value are minimum
* New : 2d contour, 3d contour circlePosition parameter added.
* New : enuTrendSeriesAppendData, enuTrendSeriesClearData Application API added.

---

**Release date : 2019.09.09, Version : 4.0.4.0**

64bit Version : [enuSpace for saturn 4.0.4.0 x64 Download \(student\)](http://www.enu-tech.co.kr/student_release/enuspace_setup_4.0.4.0_x64_st.exe)

New feature

* New : Added hdf5 based snap and reset function
* New : Add database extension module \(extensions maria db and sqlite modules\)
* Improved : Improved display of large array variables\(symbol table\)
* Fixed : Color Parsing Module Improvements for RGBA
* Improved : Add wchar\_t variable and add variable interface function

---

**Release date : 2019.06.05, Version : 4.0.3.0**

64bit Version : [enuSpace for saturn 4.0.3.0 x64 Download \(student\)](http://www.enu-tech.co.kr/student_release/enuspace_setup_4.0.3.0_x64_st.exe)

* New :  grid movement when editing graphics
* Improved : Instructor station display update
* Improved : Watcher and symbol table add function
* Improved : output window and add error code
* Improved : drawing speed of 3D objects
* Improved : Adding multiple functions to the Trend Contour
* Fixed : Runtime view scale and resizing bug
* Fixed : Trend Contour function bug

---

**Release date : 2019.02.15, Version : 4.0.2.0 **

64bit Version : [enuSpace for saturn 4.0.2.0 x64 Download \(student\)](http://www.enu-tech.co.kr/student_release/enuspace_setup_4.0.2.0_x64_st.exe)

* New : Variable access to nodes and links in 3d objects.
* Fixed : Edit function bug fixes in Datasheet dialog.
* Fixed : Instructor Panel Dialog abnormal error patch, When Removing Trend Dialog.
* Improved : User-defined layout dialog UI change of Contour object.
* Improved : Applied Java Script V8 Engine new version\(v7.3\).
* Fixed : If the window scale setting is not 100%, fix the mouse mouse position error.

---

**Release date : 2019.01.21, Version : 4.0.1.0 **

64bit Version : [enuSpace for saturn 4.0.1.0 x64 Download \(student\)](http://www.enu-tech.co.kr/student_release/enuspace_setup_4.0.1.0_x64_st.exe)

* New : Create struct memory and interface component object for simulation.
* New : Transfer line interface functions.
* New : New data visualization component \(circle contour\).
* New : Instructor module.
* New : enuGetParentNode\(\), enuGetPrevNode\(\),  enuGetNextNode\(\), enuGetFirstchildNode\(\) API add.
* New : enuCreateEditbox\(\) API add.
* Fixed : Symbol Table multi dimension data display bug fix.

---

**Release date : 2018.11.07, Version : 4.0.0.0 **

64bit Version : [enuSpace for saturn 4.0.0.0 x64 Download \(student\)](http://www.enu-tech.co.kr/student_release/enuspace_setup_4.0.0.0_x64_st.exe)

* New : Structure Creation and Interfaces
* New : Node and Link interfaces.
* New : Change the memory structure for a task

### ![](/assets/enuspace_jupiter.png)**enuSpace for jupiter\(2019\)**

---

Add features

* Artificial intelligence platform \(tensorflow module\) plugin support.
* Big data analysis.
* Algebra functions.

---

**Release date : 2018.05.10, Version : 3.0.7.0 \(beta\)**

64bit Version : [enuSpace for jupiter 3.0.7.0 x64 Download \(student\)](http://www.enu-tech.co.kr/student_release/enuspace_setup_3.0.7.0_x64.exe)

* Improved : Project Explorer user interface changed.
* Add : enuSaveAsX3DPageFile\(\) Application API add.
* Add : enuUpdateViewSymbol\(\) API add. 

---

**Release date : 2018.04.18, Version : 3.0.6.0 \(beta\)**

64bit Version : [enuSpace for jupiter 3.0.6.0 x64 Download \(student\)](http://www.enu-tech.co.kr/student_release/enuspace_setup_3.0.6.0_x64.exe)

* Fixed : Project loading procedure changed for delta time.
* Improved : Runtime view - popup dialog support \([OpenWindow\(\)](/ScriptAPI/OpenWindow.html)\).
* Improved : [ExecuteString](/ScriptAPI/ExecuteString.html)\(\) Script function extention.
* Fixed : Plot chart close event crash patch.
* Improved : global lua script, javascript loading procedure changed.
* New : [GetTaskOperationMode\(\)](/ScriptAPI/GetTaskOperationMode.html) Script API add.
* New : [GetValuePackage\(\)](/ScriptAPI/GetValue_Package.html) Script API add \(for web\).
* New : Added fuction to modify database tags.
* Improved : Add debug detail output information to script field.
* Improved : Defining and extending functions for runtime mode. [enuSetRuntimeMode\(\)](https://expnuni.github.io/enuspace_doc/docs/enusappapi_enusetruntimemode/)
* New : GetTime\(\), GetDateTimeString\(\) Script API add.
* Improved : OnTask\(\). Add time information to function parameters
* New : enuGetPageClass\(\) Application API add.
* New : enuSetPageProperty\(\) Application API add.
* New : enuSetLogicProperty\(\) Application API add.
* New : enuSetHmiProperty\(\) Application API add.
* New : enuSetGlobalProperty\(\) Application API add.
* New : enuSetResourceProperty\(\) Application API add.
* New : enuGetDefsSymbolById\(\) Application API add.

---

**Release date : 2018.03.29, Version : 3.0.5.1 \(beta\)**

64bit Version : [enuSpace for jupiter 3.0.5.1 x64 Download \(student\)](http://www.enu-tech.co.kr/student_release/enuspace_setup_3.0.5.1_x64.exe)

* Improved : File Exception Handling on Project Loading.
* Fixed : Tensorflow arraysize, Script Parsing arraysize check.
* Improved : Improved debugging output display speed up.
* Fixed :  Fixed the locking when the project was finished in the simulation execution state.
* Fixed : Output window copy function patch.
* Imporved : Added function to save and load array information when snap, reset event.
* Improved : Add function to perform temporary file removal.
* New : Task delta time get method. \('dt.{TaskName}'\)

---

**Release date : 2018.03.21, Version : 3.0.4.0 \(beta\)**

64bit Version : [enuSpace for jupiter 3.0.4.0 x64 Download \(student\)](http://www.enu-tech.co.kr/student_release/enuspace_setup_3.0.4.0_x64.exe)

* New : In the equation editor added save and load file function.
* New : [enuGet3DObjectById\(\)](/ApplicationAPI/enuGet3DObjectById.html) API add.
* New : External Task model interface output format extended.
* New : External Task SetPinInterfaceVariable\(\) API add.
* New : Added script re-registration function after calling external task init function.

---

**Release date : 2018.03.12, Version : 3.0.3.0 \(beta\)**

64bit Version : [enuSpace for jupiter 3.0.3.0 x64 Download \(student\)](http://www.enu-tech.co.kr/student_release/enuspace_setup_3.0.3.0_x64.exe)

* New : [Statistics](/statistics/statistics-api.html) function.
* New : Plot and Table caption title, Table row column display.
* New : [enuRemoveTask\(\)](/ApplicationAPI/enuRemoveTask.html) API add.
* Fixed : Perform toolbar update when performing external task removal event.
* Fixed : Pop-up trend array variable history display function patched.

---

**Release date : 2018.02.22, Version : 3.0.2.0 \(beta\)**

64bit Version : [enuSpace for jupiter 3.0.2.0 x64 Download \(student\)](http://www.enu-tech.co.kr/student_release/enuspace_setup_3.0.2.0_x64.exe)

* New : Math Algebra function support.
* New : Various Plot chart support. \(Plot, Histogram, Stem, Area\)
* New : Plugin Manager.
* New : Plugin enuSpace-Tensorflow
* New : Plugin enuSpace-SQLite

### ![](/assets/mars_logo.png)**enuSpace for mars \(2017\)**

---

**enuSpace for mars overview**

* Task model scheduling and control the task model.
* Design symbol and drawing pictures for simulation and monitoring.
* Advanced GUI Programming. \(Flowbased Programming\)
* Extended file format. \(Scalable Vector Graphics + Lua or Javascript Language\)
* Versatile software tool to develop and display dynamic graphical user interfaces.
* Graphic Component. \(Easy to development User Application Program\)
* Making Dynamic Symbols & Logic Symbols.
* Web server and extension module support.

IoT\(Internet of Things\) devices management and control.

**enuSpace for mars\(student version\) is free for personal users.**

**Installation Guide : **[**http://enuspace.tistory.com/entry/enuSpace-Installation-Guide-IoT-Platform**](http://enuspace.tistory.com/entry/enuSpace-Installation-Guide-IoT-Platform)

---

##### **Release date : 2017.06.15, Version : 2.0.6.86**

**32bit **[**Version : enuSpace for mars 2.0.6.86 x86 Download \(student\)**](http://www.enu-tech.co.kr/release/enuspace_setup_2.0.6.86_x86.exe)

**64bit **[**Version : enuSpace for mars 2.0.6.86 x64 Download \(student\)**](http://www.enu-tech.co.kr/release/enuspace_setup_2.0.6.86_x64.exe)

* New : 64bit version release
* Fixed : pin struct property modify
* Fixed : trend bug fix & property modify
* Fixed : pg-Attribute object bug fix

---

##### **Release date : 2017.05.16, Version : 2.0.6.85**

[Version : enuSpace for mars 2.0.6.85 x86 Download \(student\)](http://www.enu-tech.co.kr/release/enuspace_setup_2.0.6.85.exe)

* New : Web render gradient offset interface.
* New : Clipboard interface module patch.

---

##### **Release date : 2017.04.28, Version : 2.0.6.84**

[Version : enuSpace for mars 2.0.6.84 Download \(student\)](http://www.enu-tech.co.kr/release/enuspace_setup_2.0.6.84.exe)

* New : 웹 랜더러 팝업 테이블을 Set Value 연동 추가.
* New : enuSpace global 함수 웹 랜더러 javascript 연동 추가.
* New : RESTful API 확장 \(SetValue, GetValue\).

---

##### **Release date : 2017.04.26, Version : 2.0.6.83**

[Version : enuSpace for mars 2.0.6.83 Download \(student\)](http://www.enu-tech.co.kr/release/enuspace_setup_2.0.6.83.exe)

* Improved : 3D data visualization GUI 인터페이스 패치
* Improved : Array database tag 인터페이스 패치.

---

##### **Release date : 2017.04.24, Version : 2.0.6.82**

[Version : enuSpace for mars 2.0.6.82 Download \(student\)](http://www.enu-tech.co.kr/release/enuspace_setup_2.0.6.82.exe)

* Improved : Trend 버퍼 제거 설정 패치
* Improved : javascript global function 인터페이스 패치.

---

##### **Release date : 2017.04.14, Version : 2.0.6.81**

[Version : enuSpace for mars 2.0.6.81 Download \(student\)](http://www.enu-tech.co.kr/release/enuspace_setup_2.0.6.81.exe)

* Improved : Trend Series드로잉 최적화.
* Improved : 3D 스크립트 실행 및 리본 메뉴활성화 패치.

---

##### **Release date : 2017.04.11, Version : 2.0.6.80**

[**Version : enuSpace for mars 2.0.6.80 Download \(student\)**](http://www.enu-tech.co.kr/release/enuspace_setup_2.0.6.80.exe)

[Windows 10 Core App : enuSpace\_IoT \(enuSpace\_IoT\_1.0.3.0\_x86\_x64\_arm.appxbundle\) Download](http://www.enu-tech.co.kr/release/enuSpace_IoT_1.0.3.0_x86_x64_arm.appxbundle)

* New : 자바 스크립트 엔진 V8 추가.
* New : Web Server가 기본 탑재되어, HMI 화면이 웹 브라우져에서 다이나믹 재생 기능 추가.
* New : 강력한 분산 서버 및 모델 프로세싱이 가능한 스케쥴링 기능 추가.
* New : 데이터베이스 및 히스토리 데이터베이스 기능 추가.
* New : IoT 디바이스 인터페이스 RASTful API 기능 제공.

^^

### ![](/assets/enuspace_moon.png)**enuSpace for Moon\(2016\) **

---

##### **Release date : 2016.08.03, Version : **[**1.0.3.0 D**](http://www.enu-tech.co.kr/release/enuspace_setup_1.0.3.0.exe)[**ownload**](http://www.enu-tech.co.kr/release/enuspace_setup_1.0.3.0.exe)

* Fixed : path 객체 Picking 기능 버그 개선
* Fixed : enuSpace SDK enuCreateImage 함수 버그 개선
* Improved : new Picture 생성시 파일이름 공백 및 탭 처리 변경
* Improved : 심볼 ID를  변경하였을 경우, 뷰의 타이틀 변경문제 개선
* Improved : 편집모드시 다중 테이블 제거 기능 개선.
* New : 프로젝트 속성 설정 저장 로직 추가.

```xml
<pg-serverclient operator="server" connect="true"/>
```

* New : C++ API 기능 추가

```cpp
void enuSelectObjectListClear(HVIEW pENUView);
void enuAddSelectObjectByNode(HVIEW pENUView, HNODE hNode);
bool enuIsCommuncationReady();
wchar_t* enuGetServerIP();
wchar_t* enuGetServerPort();
bool enuIsServerSide();
bool enuIsAutoConnect()
wchar_t* enuSetProjectName(wchar_t* projectname);
bool enuSetSystemIP(wchar_t* system, wchar_t* ip);
bool enuSetSystemPort(wchar_t* system, wchar_t* port);
bool enuSetServerSide(bool bflag);
bool enuSetAutoConnect(bool bflag);
```

---

##### **Release date : 2016.02.17, Version : **[**1.0.2.0 D**](http://www.enu-tech.co.kr/release/enuspace_setup_1.0.2.0.exe)[**ownload**](http://www.enu-tech.co.kr/release/enuspace_setup_1.0.2.0.exe)

* New : Line, Polyline Arrow 기능 추가
* New : Logic Symbol Transfer Line 방향 정보 표시 기능 추가
* New : C++ API 기능 추가

```cpp
  enuSetWindowColor();
  enuSetMouseWheelCallBack();
  enuSetMouseMoveCallBack();
  enuSetMButtonUpCallBack();
  enuSetRButtonUpCallBack();
  enuSetRButtonDownCallBack();
  enuSetLButtonUpCallBack();
  enuSetLButtonDownCallBack();
```

* Fixed : Use object에 사용된 rect 객체의 회전 오류 개선

---

##### **Release date : 2016.01.12, Version :**[**1.0.1.0 **](http://www.enu-tech.co.kr/release/enuspace_setup_1.0.1.0.exe)[**Download**](http://www.enu-tech.co.kr/release/enuspace_setup_1.0.1.0.exe)

* New :  SCADA HMI Solution.
* New :  Graphics Component \(SDK support\).
* New :  Advanced GUI Editor.
* New :  Symbol Edit Interface \(User Component\).
* New :  Extended file format \(SVG\).
* New : Logic & Symbol Merged editor and viewer.
* New : Global Variable Register.
* New : Distributed Control System.
* New : Server / Client System.



