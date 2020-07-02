## Script Interface

| 함수원형 | 설명 | 스크립트\(![](/assets/javascript.png), ![](/assets/lua.png)\) |
| :--- | :--- | :---: |
| [ GetValue\(\)](//ScriptAPI/GetValue.html) | 객체의 속성값, 변수값을 리턴합니다. | javascript\(web\), lua |
| [ SetValue\(\)](//ScriptAPI/SetValue.html) | 객체의 속성값, 변수값을 설정합니다. | javascript\(web\), lua |
| [GetTagValue\(\)](/ScriptAPI/GetTagValue.html) | 데이터베이스 태그값을 가져옵니다. | javascript\(web\) |
| [SetTagValue\(\)](/ScriptAPI/SetTagValue.html) | 데이터베이스 태그값 설정합니다. | javascript\(web\) |
| [GetValuePackage\(\)](/ScriptAPI/GetValue_Package.html) | 배열정보의 값을 가져옵니다. | javascript\(web\) |
| [ FileFind\(\)](//ScriptAPI/FileFind.html) | 파일을 검색합니다. | lua |
| [ PrintMessage\(\)](//ScriptAPI/PrintMessage.html) | 디버그 출력창에 메세지를 출력합니다. | javascript, lua |
| [ printf\(\)](//ScriptAPI/printf.html) | 디버그 출력창에 메세지를 출력합니다. | lua |
| [ CreateLine\(\)](//ScriptAPI/CreateLine.html) | 라인객체를 생성합니다. | javascript, lua |
| [ CreatePolyline\(\)](//ScriptAPI/CreatePolyline.html) | 폴리라인 객체를 생성합니다. | javascript, lua |
| [ CreatePolygon\(\)](//ScriptAPI/CreatePolygon.html) | 폴리곤 객체를 생성합니다. | javascript, lua |
| [ CreateCircle\(\)](//ScriptAPI/CreateCircle.html) | 원 객체를 생성합니다. | javascript, lua |
| [ CreateEllipse\(\)](//ScriptAPI/CreateEllipse.html) | 타원 객체를 생성합니다. | javascript, lua |
| [ CreateRect\(\)](//ScriptAPI/CreateRect.html) | 사각형 객체를 생성합니다. | javascript, lua |
| [ CreateText\(\)](//ScriptAPI/CreateText.html) | 텍스트 객체를 생성합니다. | javascript, lua |
| [ CreateImage\(\)](//ScriptAPI/CreateImage.html) | 이미지 객체를 생성합니다. | javascript, lua |
| [ CreateTrend\(\)](//ScriptAPI/CreateTrend.html) | 트랜드 객체를 생성합니다. | javascript, lua |
| [ CreatePath\(\)](//ScriptAPI/CreatePath.html) | 패스 객체를 생성합니다. | javascript, lua |
| [ CreateUse\(\)](//ScriptAPI/CreateUse.html) | use 객체를 생성합니다. | javascript, lua |
| [ SetAttribute\(\)](//ScriptAPI/SetAttribute.html) | 객체의 속성값을 설정합니다. | javascript, lua |
| [ ExecuteProgram\(\)](//ScriptAPI/ExecuteProgram.html) | 외부 프로그램을 실행합니다. | javascript, lua |
| [ ExecuteString\(\)](//ScriptAPI/ExecuteString.html) | 함수 문자열을 실행합니다. | javascript, lua |
| [ ChangePicture\(\)](//ScriptAPI/ChangePicture.html) | 화면 전환을 수행합니다. | javascript, lua |
| [ LoadPicture\(\)](//ScriptAPI/LoadPicture.html) | 픽쳐파일을 로드합니다. | javascript, lua |
| [ RemovePicture\(\)](//ScriptAPI/RemovePicture.html) | 로드된 픽쳐파일을 제거합니다. | javascript, lua |
| [ GetWindowSize\(\)](//ScriptAPI/GetWindowSize.html) | 윈도우의 사이즈 정보를 가져옵니다. | javascript, lua |
| [ GetImageSize\(\)](//ScriptAPI/GetImageSize.html) | 이미지의 사이즈 정보를 가져옵니다. | javascript, lua |
| [ ExecFunctionSync\(\)](//ScriptAPI/ExecFunctionSync.html) | 동기식으로 함수를 실행합니다. | javascript, lua |
| [ ExecFunctionAsync\(\)](//ScriptAPI/ExecFunctionAsync.html) | 비동기식으로 함수를 실행합니다. | javascript, lua |
| [ GetLocalCursorPos\(\)](//ScriptAPI/GetLocalCursorPos.html) | 윈도우 기준의 마우스 좌표를 가져옵니다. | javascript, lua |
| GetLocalCursorPosX\(\) | 마우스의 X좌표를 가져옵니다. | javascript |
| GetLocalCursorPosY\(\) | 마우스의 Y좌표를 가져옵니다. | javascript |
| [ GetWorldCursorPos\(\)](//ScriptAPI/GetWorldCursorPos.html) | 데스크탑 기준의 마우스 좌표를 가져옵니다. | javascript, lua |
| GetWorldCursorPosX\(\) | 마우스의 X좌표를 가져옵니다. | javascript |
| GetWorldCursorPosY\(\) | 마우스의 Y좌표를  가져옵니다. | javascript |
| [ GetZoomScale\(\)](//ScriptAPI/GetZoomScale.html) | 화면 스케일 정보를 가져옵니다. | javascript, lua |
| [ SetZoomScale\(\)](//ScriptAPI/SetZoomScale.html) | 화면 스케일 정보를 설정합니다. | javascript, lua |
| [ SetMoveCanvas\(\)](//ScriptAPI/SetMoveCanvas.html) | 켄버스의 이동합니다. | javascript, lua |
| [ GetMoveCanvas\(\)](//ScriptAPI/GetMoveCanvas.html) | 켄버스의 이동정보를 가져옵니다. | javascript, lua |
| [ OpenWindow\(\)](//ScriptAPI/OpenWindow.html) | 윈도우 창을 엽니다. | javascript, lua |
| [ CloseWindow\(\)](//ScriptAPI/CloseWindow.html) | 윈도우 창을 닫습니다. | javascript, lua |
| [ MoveWindow\(\)](//ScriptAPI/MoveWindow.html) | 윈도우 창을 이동합니다. | javascript, lua |
| [ GetMouseWheelDelta\(\)](//ScriptAPI/GetMouseWheelDelta.html) | 마우스 휠 델타값을 가져옵니다. | javascript, lua |
| [ ShellExecute\(\)](//ScriptAPI/ShellExecute.html) | 쉘 프로램을 실행합니다. | javascript, lua |
| [ PlaySound\(\)](//ScriptAPI/PlaySound.html) | 사운드를 재생합니다. | javascript, lua |
| [ PlaySoundX\(\)](//ScriptAPI/PlaySoundX.html) | 사운드를 재생합니다. | javascript, lua |
| [ StopSoundX\(\)](//ScriptAPI/StopSoundX.html) | 사운드를 정지합니다. | javascript, lua |
| [ SetVolumeX\(\)](//ScriptAPI/SetVolumeX.html) | 볼륨을 조절합니다. | javascript, lua |
| [ Create3DBox\(\)](//ScriptAPI/Create3DBox.html) | 3차원 박스객체를 생성합니다. | javascript, lua |
| [ Create3DText\(\)](//ScriptAPI/Create3DText.html) | 3차원 텍스트 객체를 생성합니다. | javascript, lua |
| [ Create3DInline\(\)](//ScriptAPI/Create3DInline.html) | 3차원 인라인 객체를 생성합니다. | javascript, lua |
| [ Create3DCone\(\)](//ScriptAPI/Create3DCone.html) | 3차원 콘 객체를 생성합니다. | javascript, lua |
| [ Create3DSphere\(\)](//ScriptAPI/Create3DSphere.html) | 3차원 스피어 객체를 생성합니다. | javascript, lua |
| [ Create3DCylinder\(\)](//ScriptAPI/Create3DCylinder.html) | 3차원 실린더 객체를 생성합니다. | javascript, lua |
| [ Create3DFaceSet\(\)](//ScriptAPI/Create3DFaceSet.html) | 3차원 면조합객체를 생성합니다. | javascript, lua |
| [ Create3DLineSet\(\)](//ScriptAPI/Create3DLineSet.html) | 3차원 라인조합객체를 생성합니다. | javascript, lua |
| [ Create3DTerrain\(\)](//ScriptAPI/Create3DTerrain.html) | 3차원 Terrain객체를 생성합니다. | javascript, lua |
| [ SetAttribute3D\(\)](//ScriptAPI/SetAttribute3D.html) | 3차원 객체의 속성값을 지정합니다. | javascript, lua |
| [ RegisterLuaScriptById\(\)](//ScriptAPI/RegisterLuaScriptById.html) | 루아 스크립트를 등록합니다. | javascript, lua |
| [ RegisterJavaScriptById\(\)](//ScriptAPI/RegisterJavaScriptById.html) | 자바스크립트를 등록합니다. | javascript, lua |
| [ SetArrayValue\(\)](//ScriptAPI/SetArrayValue.html) | 배열값을 설정합니다. | javascript, lua |
| [ GetArrayValue\(\)](//ScriptAPI/GetArrayValue.html) | 배열값을 가져옵니다. | javascript, lua |
| [ memcpy\(\)](//ScriptAPI/memcpy.html) | 메모리 값을 복사합니다. | javascript, lua |
| [ IsExistGlobalVariable\(\)](//ScriptAPI/IsExistGlobalVariable.html) | 전역변수 존재 유무를 확인합니다. | javascript, lua |
| [ CreateGlobalVariable\(\)](//ScriptAPI/CreateGlobalVariable.html) | 전역변수를 생성합니다. | javascript, lua |
| [ SetReShapeArrayValue\(\)](//ScriptAPI/SetReShapeArrayValue.html) | 배열 사이즈와 값을 변경합니다. | javascript, lua |
| [ SetScriptOperationMode\(\)](//ScriptAPI/SetScriptOperationMode.html) | 스크립트 동작을 제어합니다. | javascript, lua |
| [SetTaskOperationMode\(\)](/ScriptAPI\SetTaskOperationMode.html) | 태스크를 제어합니다. | javascript, lua |
| [GetTaskOperationMode\(\)](/ScriptAPI/GetTaskOperationMode.html) | 태스크 상태값을 반환합니다. | javascript, lua |
| [ExecuteTaskFunction\(\)](/ScriptAPI\ExecuteTaskFunction.html) | 외부 태스크의 함수를 호출합니다. | javascript, lua |
| [ GetTime\(\)](//ScriptAPI/GetTime.html) | 시간값을 리턴합니다. | javascript, lua |
| [ GetDateTimeString\(\)](//ScriptAPI/GetDateTimeString.html) | 시간값을 문자열로 반환합니다. | javascript, lua |


