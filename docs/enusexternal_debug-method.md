---
layout: default
title: Debug 방법
parent: External Task
---

# External Task Debug 방법

---

외부 태스크를 등록하여 디버깅을 수행하는 방법에 대하여 설명합니다.



#### DLL 프로젝트에서 디버깅

DLL 프로젝트 디버깅을 시작하려면 프로젝트 속성에서 호출 응용 프로그램을 지정해야 합니다.



#### C++ 프로젝트에서 호출 응용 프로그램을 지정하려면

1. **솔루션 탐색기**에서 프로젝트 노드를 마우스 오른쪽 단추로 클릭하고**속성**을 선택합니다.**디버그**탭으로 이동합니다.

2. 창의 맨 위에 있는**구성**필드가**디버그**로 설정되어 있는지 확인합니다.

3. **구성 속성/디버깅**으로 이동합니다.

4. **실행할 디버거**목록에서**로컬 Windows 디버거**또는**원격 Windows 디버거**를 선택합니다.

5. **명령**또는**원격 명령**상자에서 응용 프로그램의 정규화된 경로 이름을 추가합니다.

6. 필요한 프로그램 인수를**명령 인수**상자에 추가합니다.



#### External Task DLL의 프로젝트 속성 설정

Command 속성에 enuSpace 프로그램의 패스정보를 포함한 응용프로그램 이름을 적용합니다.

예시\) C:\Program Files\enuSpace for Jupiter\enuSpace.exe

![](./assets/externaltask/externaltask_debug.png)







