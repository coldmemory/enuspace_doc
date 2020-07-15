---
layout: default
title: Script API
has_children: true
nav_order: h
---


## Script Interface

| 함수원형 | 설명 | 스크립트\(![](/assets/javascript.png), ![](/assets/lua.png)\) |
| :--- | :--- | :---: |
| [ GetValue\(\)](./enusscriptapi_GetValue.md) | 객체의 속성값, 변수값을 리턴합니다. | javascript\(web\), lua |
| [ SetValue\(\)](./enusscriptapi_SetValue.md) | 객체의 속성값, 변수값을 설정합니다. | javascript\(web\), lua |
| [GetTagValue\(\)](/ScriptAPI/GetTagValue.md) | 데이터베이스 태그값을 가져옵니다. | javascript\(web\) |
| [SetTagValue\(\)](/ScriptAPI/SetTagValue.md) | 데이터베이스 태그값 설정합니다. | javascript\(web\) |
| [GetValuePackage\(\)](/ScriptAPI/GetValue_Package.md) | 배열정보의 값을 가져옵니다. | javascript\(web\) |
| [ FileFind\(\)](./enusscriptapi_FileFind.md) | 파일을 검색합니다. | lua |
| [ PrintMessage\(\)](./enusscriptapi_PrintMessage.md) | 디버그 출력창에 메세지를 출력합니다. | javascript, lua |
| [ printf\(\)](./enusscriptapi_printf.md) | 디버그 출력창에 메세지를 출력합니다. | lua |
| [ CreateLine\(\)](./enusscriptapi_CreateLine.md) | 라인객체를 생성합니다. | javascript, lua |
| [ CreatePolyline\(\)](./enusscriptapi_CreatePolyline.md) | 폴리라인 객체를 생성합니다. | javascript, lua |
| [ CreatePolygon\(\)](./enusscriptapi_CreatePolygon.md) | 폴리곤 객체를 생성합니다. | javascript, lua |
| [ CreateCircle\(\)](./enusscriptapi_CreateCircle.md) | 원 객체를 생성합니다. | javascript, lua |
| [ CreateEllipse\(\)](./enusscriptapi_CreateEllipse.md) | 타원 객체를 생성합니다. | javascript, lua |
| [ CreateRect\(\)](./enusscriptapi_CreateRect.md) | 사각형 객체를 생성합니다. | javascript, lua |
| [ CreateText\(\)](./enusscriptapi_CreateText.md) | 텍스트 객체를 생성합니다. | javascript, lua |
| [ CreateImage\(\)](./enusscriptapi_CreateImage.md) | 이미지 객체를 생성합니다. | javascript, lua |
| [ CreateTrend\(\)](./enusscriptapi_CreateTrend.md) | 트랜드 객체를 생성합니다. | javascript, lua |
| [ CreatePath\(\)](./enusscriptapi_CreatePath.md) | 패스 객체를 생성합니다. | javascript, lua |
| [ CreateUse\(\)](./enusscriptapi_CreateUse.md) | use 객체를 생성합니다. | javascript, lua |
| [ SetAttribute\(\)](./enusscriptapi_SetAttribute.md) | 객체의 속성값을 설정합니다. | javascript, lua |
| [ ExecuteProgram\(\)](./enusscriptapi_ExecuteProgram.md) | 외부 프로그램을 실행합니다. | javascript, lua |
| [ ExecuteString\(\)](./enusscriptapi_ExecuteString.md) | 함수 문자열을 실행합니다. | javascript, lua |
| [ ChangePicture\(\)](./enusscriptapi_ChangePicture.md) | 화면 전환을 수행합니다. | javascript, lua |
| [ LoadPicture\(\)](./enusscriptapi_LoadPicture.md) | 픽쳐파일을 로드합니다. | javascript, lua |
| [ RemovePicture\(\)](./enusscriptapi_RemovePicture.md) | 로드된 픽쳐파일을 제거합니다. | javascript, lua |
| [ GetWindowSize\(\)](./enusscriptapi_GetWindowSize.md) | 윈도우의 사이즈 정보를 가져옵니다. | javascript, lua |
| [ GetImageSize\(\)](./enusscriptapi_GetImageSize.md) | 이미지의 사이즈 정보를 가져옵니다. | javascript, lua |
| [ ExecFunctionSync\(\)](./enusscriptapi_ExecFunctionSync.md) | 동기식으로 함수를 실행합니다. | javascript, lua |
| [ ExecFunctionAsync\(\)](./enusscriptapi_ExecFunctionAsync.md) | 비동기식으로 함수를 실행합니다. | javascript, lua |
| [ GetLocalCursorPos\(\)](./enusscriptapi_GetLocalCursorPos.md) | 윈도우 기준의 마우스 좌표를 가져옵니다. | javascript, lua |
| GetLocalCursorPosX\(\) | 마우스의 X좌표를 가져옵니다. | javascript |
| GetLocalCursorPosY\(\) | 마우스의 Y좌표를 가져옵니다. | javascript |
| [ GetWorldCursorPos\(\)](./enusscriptapi_GetWorldCursorPos.md) | 데스크탑 기준의 마우스 좌표를 가져옵니다. | javascript, lua |
| GetWorldCursorPosX\(\) | 마우스의 X좌표를 가져옵니다. | javascript |
| GetWorldCursorPosY\(\) | 마우스의 Y좌표를  가져옵니다. | javascript |
| [ GetZoomScale\(\)](./enusscriptapi_GetZoomScale.md) | 화면 스케일 정보를 가져옵니다. | javascript, lua |
| [ SetZoomScale\(\)](./enusscriptapi_SetZoomScale.md) | 화면 스케일 정보를 설정합니다. | javascript, lua |
| [ SetMoveCanvas\(\)](./enusscriptapi_SetMoveCanvas.md) | 켄버스의 이동합니다. | javascript, lua |
| [ GetMoveCanvas\(\)](./enusscriptapi_GetMoveCanvas.md) | 켄버스의 이동정보를 가져옵니다. | javascript, lua |
| [ OpenWindow\(\)](./enusscriptapi_OpenWindow.md) | 윈도우 창을 엽니다. | javascript, lua |
| [ CloseWindow\(\)](./enusscriptapi_CloseWindow.md) | 윈도우 창을 닫습니다. | javascript, lua |
| [ MoveWindow\(\)](./enusscriptapi_MoveWindow.md) | 윈도우 창을 이동합니다. | javascript, lua |
| [ GetMouseWheelDelta\(\)](./enusscriptapi_GetMouseWheelDelta.md) | 마우스 휠 델타값을 가져옵니다. | javascript, lua |
| [ ShellExecute\(\)](./enusscriptapi_ShellExecute.md) | 쉘 프로램을 실행합니다. | javascript, lua |
| [ PlaySound\(\)](./enusscriptapi_PlaySound.md) | 사운드를 재생합니다. | javascript, lua |
| [ PlaySoundX\(\)](./enusscriptapi_PlaySoundX.md) | 사운드를 재생합니다. | javascript, lua |
| [ StopSoundX\(\)](./enusscriptapi_StopSoundX.md) | 사운드를 정지합니다. | javascript, lua |
| [ SetVolumeX\(\)](./enusscriptapi_SetVolumeX.md) | 볼륨을 조절합니다. | javascript, lua |
| [ Create3DBox\(\)](./enusscriptapi_Create3DBox.md) | 3차원 박스객체를 생성합니다. | javascript, lua |
| [ Create3DText\(\)](./enusscriptapi_Create3DText.md) | 3차원 텍스트 객체를 생성합니다. | javascript, lua |
| [ Create3DInline\(\)](./enusscriptapi_Create3DInline.md) | 3차원 인라인 객체를 생성합니다. | javascript, lua |
| [ Create3DCone\(\)](./enusscriptapi_Create3DCone.md) | 3차원 콘 객체를 생성합니다. | javascript, lua |
| [ Create3DSphere\(\)](./enusscriptapi_Create3DSphere.md) | 3차원 스피어 객체를 생성합니다. | javascript, lua |
| [ Create3DCylinder\(\)](./enusscriptapi_Create3DCylinder.md) | 3차원 실린더 객체를 생성합니다. | javascript, lua |
| [ Create3DFaceSet\(\)](./enusscriptapi_Create3DFaceSet.md) | 3차원 면조합객체를 생성합니다. | javascript, lua |
| [ Create3DLineSet\(\)](./enusscriptapi_Create3DLineSet.md) | 3차원 라인조합객체를 생성합니다. | javascript, lua |
| [ Create3DTerrain\(\)](./enusscriptapi_Create3DTerrain.md) | 3차원 Terrain객체를 생성합니다. | javascript, lua |
| [ SetAttribute3D\(\)](./enusscriptapi_SetAttribute3D.md) | 3차원 객체의 속성값을 지정합니다. | javascript, lua |
| [ RegisterLuaScriptById\(\)](./enusscriptapi_RegisterLuaScriptById.md) | 루아 스크립트를 등록합니다. | javascript, lua |
| [ RegisterJavaScriptById\(\)](./enusscriptapi_RegisterJavaScriptById.md) | 자바스크립트를 등록합니다. | javascript, lua |
| [ SetArrayValue\(\)](./enusscriptapi_SetArrayValue.md) | 배열값을 설정합니다. | javascript, lua |
| [ GetArrayValue\(\)](./enusscriptapi_GetArrayValue.md) | 배열값을 가져옵니다. | javascript, lua |
| [ memcpy\(\)](./enusscriptapi_memcpy.md) | 메모리 값을 복사합니다. | javascript, lua |
| [ IsExistGlobalVariable\(\)](./enusscriptapi_IsExistGlobalVariable.md) | 전역변수 존재 유무를 확인합니다. | javascript, lua |
| [ CreateGlobalVariable\(\)](./enusscriptapi_CreateGlobalVariable.md) | 전역변수를 생성합니다. | javascript, lua |
| [ SetReShapeArrayValue\(\)](./enusscriptapi_SetReShapeArrayValue.md) | 배열 사이즈와 값을 변경합니다. | javascript, lua |
| [ SetScriptOperationMode\(\)](./enusscriptapi_SetScriptOperationMode.md) | 스크립트 동작을 제어합니다. | javascript, lua |
| [SetTaskOperationMode\(\)](/ScriptAPI\SetTaskOperationMode.md) | 태스크를 제어합니다. | javascript, lua |
| [GetTaskOperationMode\(\)](/ScriptAPI/GetTaskOperationMode.md) | 태스크 상태값을 반환합니다. | javascript, lua |
| [ExecuteTaskFunction\(\)](/ScriptAPI\ExecuteTaskFunction.md) | 외부 태스크의 함수를 호출합니다. | javascript, lua |
| [ GetTime\(\)](./enusscriptapi_GetTime.md) | 시간값을 리턴합니다. | javascript, lua |
| [ GetDateTimeString\(\)](./enusscriptapi_GetDateTimeString.md) | 시간값을 문자열로 반환합니다. | javascript, lua |



