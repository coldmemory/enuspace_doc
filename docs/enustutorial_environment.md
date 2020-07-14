---
layout: default
title: 개발환경 및 구조
parent: enuSpace Tutorial
nav_order: a
---

Revision 2019.02.22 - enuSpace for saturn\(ver4.0\)

# **enuSpace 개발 환경 및 구조**

---

## enuSpace ?

---

enuSpace는 HMI/SCADA/DCS/IOT분야에서 활용되는 다기능 통합 개발자 솔루션입니다. 그래픽 편집 및 런타임 뷰어 기능을 포함하고 있으며, 동적 데이터 가시화 도구를 제공합니다. 객체 지향 프로그래밍\(Object Oriented Programming:OOP\) 개념을 도입한 사용자 정의 라이브러리를 생성하여 그래픽 컴포넌트로 적용 가능합니다.

enuSpace는 동적 디스플레이와 시뮬레이션 도구가 통합되어 로직 및 알고리즘 라이브러리 블럭을 이용하여 데이터 연결선만으로 플로우베이스 프로그래밍\(Flowbased Programming\)이 가능합니다. 연산결과는 동적 디스플레이 객체를 통하여 표현합니다.

enuSpace는 소프트웨어 개발자 도구\(Software Development Kit :SDK\)를 제공하며, SDK 그래픽 기능을 활용하여 빠르고 수려한 윈도우 그래픽 프로그램을 개발할 수 있습니다.

운영환경 : Windows 7, Windows 10 64bit \(Recommand\)

![](./assets/environment/1 basic1.png)

### 1. Ribbon menu

Ribbon menu는 사용자가 화면을 제작을 위한 메뉴와 운영에 필요한 메뉴가 구성되어 있습니다.

### 2. Project Explorer

Project Explorer는 현재 열려진 프로젝트의 모든 정보를 제공합니다.

### 3. Debug output

각종 출력 메세지를 통하여 프로젝트의 디버깅을 수행합니다.

### 4. Graphic window

Project Explorer의 픽쳐 아이템에 대한 그래픽 정보를 제공합니다. 화면을 편집및 수정을 위한 인터페이스를 제공합니다.

그래픽 편집기에서 기본적으로 그리드 간격으로 마우스 이동을 제공합니다. Ctrl 키 누른 후, 객체 조정시 미세 조정을 수행할 수 있습니다.

### 5. Properties Window

각 객체의 속성에 대한 정보를 제공하며, 각 속성 아이템에 대하여 속성 변경처리를 수행합니다. 속성창은 객체의 속성, 객체의 이벤트, 객체의 변수에 대하여 설정할수 있는 인터페이스를 제공합니다.

![](./assets/environment/1 basic2.png)

\* 객체의 이벤트에 사용되는 스크립트 언어는 Lua, Javascript language를 지원하며 객체의 속성을 변경하고자 할 경우에는 속성창의 이름을 이용하여 동적으로 스크립트에서 제어할 수 있습니다. fill-opacity와 같이 -가 포함된 문자는 fill\_opacity의 변수로 접근합니다.

* #### Logic Library Window

로직 라이브러리의 리스트를 보여줍니다. 로직 라이브러리를 선택 Graphic window에 마우스를 이용한 Drag & Drop을 이용하여 객체를 추가합니다.

* #### HMI Library Window

HMI 라이브러리의 리스트를 보여줍니다. HMI 라이브러리를 선택 Graphic window에 마우스를 이용한 Drag & Drop을 이용하여 객체를 추가합니다.

