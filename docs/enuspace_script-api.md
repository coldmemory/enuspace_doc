---
layout: default
title: Script API
has_children: true
nav_order: h
---


## Script Interface

| 함수원형 | 설명 | 스크립트\(![](./assets/javascript.png), ![](./assets/lua.png)\) |
| :--- | :--- | :---: |
| [ GetValue\(\)](./enusscriptapi_getvalue.md) | 객체의 속성값, 변수값을 리턴합니다. | javascript\(web\), lua |
| [ SetValue\(\)](./enusscriptapi_setvalue.md) | 객체의 속성값, 변수값을 설정합니다. | javascript\(web\), lua |
| [GetTagValue\(\)](./ScriptAPI/GetTagValue.md) | 데이터베이스 태그값을 가져옵니다. | javascript\(web\) |
| [SetTagValue\(\)](./ScriptAPI/SetTagValue.md) | 데이터베이스 태그값 설정합니다. | javascript\(web\) |
| [GetValuePackage\(\)](./ScriptAPI/GetValue_Package.md) | 배열정보의 값을 가져옵니다. | javascript\(web\) |
| [ FileFind\(\)](./enusscriptapi_filefind.md) | 파일을 검색합니다. | lua |
| [ PrintMessage\(\)](./enusscriptapi_printmessage.md) | 디버그 출력창에 메세지를 출력합니다. | javascript, lua |
| [ printf\(\)](./enusscriptapi_printf.md) | 디버그 출력창에 메세지를 출력합니다. | lua |
| [ CreateLine\(\)](./enusscriptapi_createline.md) | 라인객체를 생성합니다. | javascript, lua |
| [ CreatePolyline\(\)](./enusscriptapi_createpolyline.md) | 폴리라인 객체를 생성합니다. | javascript, lua |
| [ CreatePolygon\(\)](./enusscriptapi_createpolygon.md) | 폴리곤 객체를 생성합니다. | javascript, lua |
| [ CreateCircle\(\)](./enusscriptapi_createcircle.md) | 원 객체를 생성합니다. | javascript, lua |
| [ CreateEllipse\(\)](./enusscriptapi_createellipse.md) | 타원 객체를 생성합니다. | javascript, lua |
| [ CreateRect\(\)](./enusscriptapi_createrect.md) | 사각형 객체를 생성합니다. | javascript, lua |
| [ CreateText\(\)](./enusscriptapi_createtext.md) | 텍스트 객체를 생성합니다. | javascript, lua |
| [ CreateImage\(\)](./enusscriptapi_createimage.md) | 이미지 객체를 생성합니다. | javascript, lua |
| [ CreateTrend\(\)](./enusscriptapi_createtrend.md) | 트랜드 객체를 생성합니다. | javascript, lua |
| [ CreatePath\(\)](./enusscriptapi_createpath.md) | 패스 객체를 생성합니다. | javascript, lua |
| [ CreateUse\(\)](./enusscriptapi_createuse.md) | use 객체를 생성합니다. | javascript, lua |
| [ SetAttribute\(\)](./enusscriptapi_setattribute.md) | 객체의 속성값을 설정합니다. | javascript, lua |
| [ ExecuteProgram\(\)](./enusscriptapi_executeprogram.md) | 외부 프로그램을 실행합니다. | javascript, lua |
| [ ExecuteString\(\)](./enusscriptapi_executestring.md) | 함수 문자열을 실행합니다. | javascript, lua |
| [ ChangePicture\(\)](./enusscriptapi_changepicture.md) | 화면 전환을 수행합니다. | javascript, lua |
| [ LoadPicture\(\)](./enusscriptapi_loadpicture.md) | 픽쳐파일을 로드합니다. | javascript, lua |
| [ RemovePicture\(\)](./enusscriptapi_removepicture.md) | 로드된 픽쳐파일을 제거합니다. | javascript, lua |
| [ GetWindowSize\(\)](./enusscriptapi_getwindowsize.md) | 윈도우의 사이즈 정보를 가져옵니다. | javascript, lua |
| [ GetImageSize\(\)](./enusscriptapi_getimagesize.md) | 이미지의 사이즈 정보를 가져옵니다. | javascript, lua |
| [ ExecFunctionSync\(\)](./enusscriptapi_execfunctionsync.md) | 동기식으로 함수를 실행합니다. | javascript, lua |
| [ ExecFunctionAsync\(\)](./enusscriptapi_execfunctionasync.md) | 비동기식으로 함수를 실행합니다. | javascript, lua |
| [ GetLocalCursorPos\(\)](./enusscriptapi_getlocalcursorpos.md) | 윈도우 기준의 마우스 좌표를 가져옵니다. | javascript, lua |
| GetLocalCursorPosX\(\) | 마우스의 X좌표를 가져옵니다. | javascript |
| GetLocalCursorPosY\(\) | 마우스의 Y좌표를 가져옵니다. | javascript |
| [ GetWorldCursorPos\(\)](./enusscriptapi_getworldcursorpos.md) | 데스크탑 기준의 마우스 좌표를 가져옵니다. | javascript, lua |
| GetWorldCursorPosX\(\) | 마우스의 X좌표를 가져옵니다. | javascript |
| GetWorldCursorPosY\(\) | 마우스의 Y좌표를  가져옵니다. | javascript |
| [ GetZoomScale\(\)](./enusscriptapi_getzoomscale.md) | 화면 스케일 정보를 가져옵니다. | javascript, lua |
| [ SetZoomScale\(\)](./enusscriptapi_setzoomscale.md) | 화면 스케일 정보를 설정합니다. | javascript, lua |
| [ SetMoveCanvas\(\)](./enusscriptapi_setmovecanvas.md) | 켄버스의 이동합니다. | javascript, lua |
| [ GetMoveCanvas\(\)](./enusscriptapi_getmovecanvas.md) | 켄버스의 이동정보를 가져옵니다. | javascript, lua |
| [ OpenWindow\(\)](./enusscriptapi_openwindow.md) | 윈도우 창을 엽니다. | javascript, lua |
| [ CloseWindow\(\)](./enusscriptapi_closewindow.md) | 윈도우 창을 닫습니다. | javascript, lua |
| [ MoveWindow\(\)](./enusscriptapi_movewindow.md) | 윈도우 창을 이동합니다. | javascript, lua |
| [ GetMouseWheelDelta\(\)](./enusscriptapi_getmousewheeldelta.md) | 마우스 휠 델타값을 가져옵니다. | javascript, lua |
| [ ShellExecute\(\)](./enusscriptapi_shellexecute.md) | 쉘 프로램을 실행합니다. | javascript, lua |
| [ PlaySound\(\)](./enusscriptapi_playsound.md) | 사운드를 재생합니다. | javascript, lua |
| [ PlaySoundX\(\)](./enusscriptapi_playsoundx.md) | 사운드를 재생합니다. | javascript, lua |
| [ StopSoundX\(\)](./enusscriptapi_stopsoundx.md) | 사운드를 정지합니다. | javascript, lua |
| [ SetVolumeX\(\)](./enusscriptapi_setvolumex.md) | 볼륨을 조절합니다. | javascript, lua |
| [ Create3DBox\(\)](./enusscriptapi_create3dbox.md) | 3차원 박스객체를 생성합니다. | javascript, lua |
| [ Create3DText\(\)](./enusscriptapi_create3dtext.md) | 3차원 텍스트 객체를 생성합니다. | javascript, lua |
| [ Create3DInline\(\)](./enusscriptapi_create3dinline.md) | 3차원 인라인 객체를 생성합니다. | javascript, lua |
| [ Create3DCone\(\)](./enusscriptapi_create3dcone.md) | 3차원 콘 객체를 생성합니다. | javascript, lua |
| [ Create3DSphere\(\)](./enusscriptapi_create3dsphere.md) | 3차원 스피어 객체를 생성합니다. | javascript, lua |
| [ Create3DCylinder\(\)](./enusscriptapi_create3dcylinder.md) | 3차원 실린더 객체를 생성합니다. | javascript, lua |
| [ Create3DFaceSet\(\)](./enusscriptapi_create3dfaceset.md) | 3차원 면조합객체를 생성합니다. | javascript, lua |
| [ Create3DLineSet\(\)](./enusscriptapi_create3dlineset.md) | 3차원 라인조합객체를 생성합니다. | javascript, lua |
| [ Create3DTerrain\(\)](./enusscriptapi_create3dterrain.md) | 3차원 Terrain객체를 생성합니다. | javascript, lua |
| [ SetAttribute3D\(\)](./enusscriptapi_setattribute3d.md) | 3차원 객체의 속성값을 지정합니다. | javascript, lua |
| [ RegisterLuaScriptById\(\)](./enusscriptapi_registerluascriptbyid.md) | 루아 스크립트를 등록합니다. | javascript, lua |
| [ RegisterJavaScriptById\(\)](./enusscriptapi_registerjavascriptbyid.md) | 자바스크립트를 등록합니다. | javascript, lua |
| [ SetArrayValue\(\)](./enusscriptapi_setarrayvalue.md) | 배열값을 설정합니다. | javascript, lua |
| [ GetArrayValue\(\)](./enusscriptapi_getarrayvalue.md) | 배열값을 가져옵니다. | javascript, lua |
| [ memcpy\(\)](./enusscriptapi_memcpy.md) | 메모리 값을 복사합니다. | javascript, lua |
| [ IsExistGlobalVariable\(\)](./enusscriptapi_isexistglobalvariable.md) | 전역변수 존재 유무를 확인합니다. | javascript, lua |
| [ CreateGlobalVariable\(\)](./enusscriptapi_createglobalvariable.md) | 전역변수를 생성합니다. | javascript, lua |
| [ SetReShapeArrayValue\(\)](./enusscriptapi_setreshapearrayvalue.md) | 배열 사이즈와 값을 변경합니다. | javascript, lua |
| [ SetScriptOperationMode\(\)](./enusscriptapi_setscriptoperationmode.md) | 스크립트 동작을 제어합니다. | javascript, lua |
| [SetTaskOperationMode\(\)](./ScriptAPI\SetTaskOperationMode.md) | 태스크를 제어합니다. | javascript, lua |
| [GetTaskOperationMode\(\)](./ScriptAPI/GetTaskOperationMode.md) | 태스크 상태값을 반환합니다. | javascript, lua |
| [ExecuteTaskFunction\(\)](./ScriptAPI\ExecuteTaskFunction.md) | 외부 태스크의 함수를 호출합니다. | javascript, lua |
| [ GetTime\(\)](./enusscriptapi_gettime.md) | 시간값을 리턴합니다. | javascript, lua |
| [ GetDateTimeString\(\)](./enusscriptapi_getdatetimestring.md) | 시간값을 문자열로 반환합니다. | javascript, lua |



