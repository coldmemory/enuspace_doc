---
layout: default
title: Script API
has_children: true
nav_order: j
last_modified_date: now
---


## Script Interface

| 함수원형 | 설명 | 스크립트\(![](./assets/javascript.png), ![](./assets/lua.png)\) |
| :--- | :--- | :---: |
| [ GetValue\(\)](./script_api_getvalue.md) | 객체의 속성값, 변수값을 리턴합니다. | javascript\(web\), lua |
| [ SetValue\(\)](./script_api_setvalue.md) | 객체의 속성값, 변수값을 설정합니다. | javascript\(web\), lua |
| [GetTagValue\(\)](./script_api/GetTagValue.md) | 데이터베이스 태그값을 가져옵니다. | javascript\(web\) |
| [SetTagValue\(\)](./script_api/SetTagValue.md) | 데이터베이스 태그값 설정합니다. | javascript\(web\) |
| [GetValuePackage\(\)](./script_api/GetValue_Package.md) | 배열정보의 값을 가져옵니다. | javascript\(web\) |
| [ FileFind\(\)](./script_api_filefind.md) | 파일을 검색합니다. | lua |
| [ PrintMessage\(\)](./script_api_printmessage.md) | 디버그 출력창에 메세지를 출력합니다. | javascript, lua |
| [ printf\(\)](./script_api_printf.md) | 디버그 출력창에 메세지를 출력합니다. | lua |
| [ CreateLine\(\)](./script_api_createline.md) | 라인객체를 생성합니다. | javascript, lua |
| [ CreatePolyline\(\)](./script_api_createpolyline.md) | 폴리라인 객체를 생성합니다. | javascript, lua |
| [ CreatePolygon\(\)](./script_api_createpolygon.md) | 폴리곤 객체를 생성합니다. | javascript, lua |
| [ CreateCircle\(\)](./script_api_createcircle.md) | 원 객체를 생성합니다. | javascript, lua |
| [ CreateEllipse\(\)](./script_api_createellipse.md) | 타원 객체를 생성합니다. | javascript, lua |
| [ CreateRect\(\)](./script_api_createrect.md) | 사각형 객체를 생성합니다. | javascript, lua |
| [ CreateText\(\)](./script_api_createtext.md) | 텍스트 객체를 생성합니다. | javascript, lua |
| [ CreateImage\(\)](./script_api_createimage.md) | 이미지 객체를 생성합니다. | javascript, lua |
| [ CreateTrend\(\)](./script_api_createtrend.md) | 트랜드 객체를 생성합니다. | javascript, lua |
| [ CreatePath\(\)](./script_api_createpath.md) | 패스 객체를 생성합니다. | javascript, lua |
| [ CreateUse\(\)](./script_api_createuse.md) | use 객체를 생성합니다. | javascript, lua |
| [ SetAttribute\(\)](./script_api_setattribute.md) | 객체의 속성값을 설정합니다. | javascript, lua |
| [ ExecuteProgram\(\)](./script_api_executeprogram.md) | 외부 프로그램을 실행합니다. | javascript, lua |
| [ ExecuteString\(\)](./script_api_executestring.md) | 함수 문자열을 실행합니다. | javascript, lua |
| [ ChangePicture\(\)](./script_api_changepicture.md) | 화면 전환을 수행합니다. | javascript, lua |
| [ LoadPicture\(\)](./script_api_loadpicture.md) | 픽쳐파일을 로드합니다. | javascript, lua |
| [ RemovePicture\(\)](./script_api_removepicture.md) | 로드된 픽쳐파일을 제거합니다. | javascript, lua |
| [ GetWindowSize\(\)](./script_api_getwindowsize.md) | 윈도우의 사이즈 정보를 가져옵니다. | javascript, lua |
| [ GetImageSize\(\)](./script_api_getimagesize.md) | 이미지의 사이즈 정보를 가져옵니다. | javascript, lua |
| [ ExecFunctionSync\(\)](./script_api_execfunctionsync.md) | 동기식으로 함수를 실행합니다. | javascript, lua |
| [ ExecFunctionAsync\(\)](./script_api_execfunctionasync.md) | 비동기식으로 함수를 실행합니다. | javascript, lua |
| [ GetLocalCursorPos\(\)](./script_api_getlocalcursorpos.md) | 윈도우 기준의 마우스 좌표를 가져옵니다. | javascript, lua |
| GetLocalCursorPosX\(\) | 마우스의 X좌표를 가져옵니다. | javascript |
| GetLocalCursorPosY\(\) | 마우스의 Y좌표를 가져옵니다. | javascript |
| [ GetWorldCursorPos\(\)](./script_api_getworldcursorpos.md) | 데스크탑 기준의 마우스 좌표를 가져옵니다. | javascript, lua |
| GetWorldCursorPosX\(\) | 마우스의 X좌표를 가져옵니다. | javascript |
| GetWorldCursorPosY\(\) | 마우스의 Y좌표를  가져옵니다. | javascript |
| [ GetZoomScale\(\)](./script_api_getzoomscale.md) | 화면 스케일 정보를 가져옵니다. | javascript, lua |
| [ SetZoomScale\(\)](./script_api_setzoomscale.md) | 화면 스케일 정보를 설정합니다. | javascript, lua |
| [ SetMoveCanvas\(\)](./script_api_setmovecanvas.md) | 켄버스의 이동합니다. | javascript, lua |
| [ GetMoveCanvas\(\)](./script_api_getmovecanvas.md) | 켄버스의 이동정보를 가져옵니다. | javascript, lua |
| [ OpenWindow\(\)](./script_api_openwindow.md) | 윈도우 창을 엽니다. | javascript, lua |
| [ CloseWindow\(\)](./script_api_closewindow.md) | 윈도우 창을 닫습니다. | javascript, lua |
| [ MoveWindow\(\)](./script_api_movewindow.md) | 윈도우 창을 이동합니다. | javascript, lua |
| [ GetMouseWheelDelta\(\)](./script_api_getmousewheeldelta.md) | 마우스 휠 델타값을 가져옵니다. | javascript, lua |
| [ ShellExecute\(\)](./script_api_shellexecute.md) | 쉘 프로램을 실행합니다. | javascript, lua |
| [ PlaySound\(\)](./script_api_playsound.md) | 사운드를 재생합니다. | javascript, lua |
| [ PlaySoundX\(\)](./script_api_playsoundx.md) | 사운드를 재생합니다. | javascript, lua |
| [ StopSoundX\(\)](./script_api_stopsoundx.md) | 사운드를 정지합니다. | javascript, lua |
| [ SetVolumeX\(\)](./script_api_setvolumex.md) | 볼륨을 조절합니다. | javascript, lua |
| [ Create3DBox\(\)](./script_api_create3dbox.md) | 3차원 박스객체를 생성합니다. | javascript, lua |
| [ Create3DText\(\)](./script_api_create3dtext.md) | 3차원 텍스트 객체를 생성합니다. | javascript, lua |
| [ Create3DInline\(\)](./script_api_create3dinline.md) | 3차원 인라인 객체를 생성합니다. | javascript, lua |
| [ Create3DCone\(\)](./script_api_create3dcone.md) | 3차원 콘 객체를 생성합니다. | javascript, lua |
| [ Create3DSphere\(\)](./script_api_create3dsphere.md) | 3차원 스피어 객체를 생성합니다. | javascript, lua |
| [ Create3DCylinder\(\)](./script_api_create3dcylinder.md) | 3차원 실린더 객체를 생성합니다. | javascript, lua |
| [ Create3DFaceSet\(\)](./script_api_create3dfaceset.md) | 3차원 면조합객체를 생성합니다. | javascript, lua |
| [ Create3DLineSet\(\)](./script_api_create3dlineset.md) | 3차원 라인조합객체를 생성합니다. | javascript, lua |
| [ Create3DTerrain\(\)](./script_api_create3dterrain.md) | 3차원 Terrain객체를 생성합니다. | javascript, lua |
| [ SetAttribute3D\(\)](./script_api_setattribute3d.md) | 3차원 객체의 속성값을 지정합니다. | javascript, lua |
| [ RegisterLuaScriptById\(\)](./script_api_registerluascriptbyid.md) | 루아 스크립트를 등록합니다. | javascript, lua |
| [ RegisterJavaScriptById\(\)](./script_api_registerjavascriptbyid.md) | 자바스크립트를 등록합니다. | javascript, lua |
| [ SetArrayValue\(\)](./script_api_setarrayvalue.md) | 배열값을 설정합니다. | javascript, lua |
| [ GetArrayValue\(\)](./script_api_getarrayvalue.md) | 배열값을 가져옵니다. | javascript, lua |
| [ memcpy\(\)](./script_api_memcpy.md) | 메모리 값을 복사합니다. | javascript, lua |
| [ IsExistGlobalVariable\(\)](./script_api_isexistglobalvariable.md) | 전역변수 존재 유무를 확인합니다. | javascript, lua |
| [ CreateGlobalVariable\(\)](./script_api_createglobalvariable.md) | 전역변수를 생성합니다. | javascript, lua |
| [ SetReShapeArrayValue\(\)](./script_api_setreshapearrayvalue.md) | 배열 사이즈와 값을 변경합니다. | javascript, lua |
| [ SetScriptOperationMode\(\)](./script_api_setscriptoperationmode.md) | 스크립트 동작을 제어합니다. | javascript, lua |
| [SetTaskOperationMode\(\)](./script_api\SetTaskOperationMode.md) | 태스크를 제어합니다. | javascript, lua |
| [GetTaskOperationMode\(\)](./script_api/GetTaskOperationMode.md) | 태스크 상태값을 반환합니다. | javascript, lua |
| [ExecuteTaskFunction\(\)](./script_api\ExecuteTaskFunction.md) | 외부 태스크의 함수를 호출합니다. | javascript, lua |
| [ GetTime\(\)](./script_api_gettime.md) | 시간값을 리턴합니다. | javascript, lua |
| [ GetDateTimeString\(\)](./script_api_getdatetimestring.md) | 시간값을 문자열로 반환합니다. | javascript, lua |



