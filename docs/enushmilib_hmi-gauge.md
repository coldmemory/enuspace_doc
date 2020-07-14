---
layout: default
title: Gauge
parent: HMI 라이브러리 만들기
grand_parent: enuSpace Tutorial
---

# SVG와 JavaScript를 이용한 다이나믹 HMI 심볼 제작

---

IoT library : [https://github.com/EXPNUNI/enuSpace-Article/tree/master/library%20package](https://github.com/EXPNUNI/enuSpace-Article/tree/master/library package)

![](./assets/tutorial/hmi_symbol.png)

## 라이브러리 생성

enuSpace를 실행하고 Project Explorer에서 Library하위에서 Hmi 선택후 Add New hmi Library를 선택합니다. 라이브러리 파일이름을 입력후 Create를 수행하면, 새로운 hmi 라이브러리 파일이 생성됩니다.

생성된 파일을 선택후 팝업메뉴를 이용하여 Add Symbol를 통하여 새로운 심볼을 생성합니다. 생성된 심볼을 디자인합니다. 디자인 객체를 이용하여 아래 그림과 같이 디자인을 수행합니다.

![](./assets/hmi-library1/hmi_symbol_edit.png)

각각의 객체의 속성에 id를 설정합니다. 

심볼의 자체에 이벤트 함수를 등록합니다. \_onload\(\)함수에 아래의 코드를 추가합니다. 

```lua
function _onload()
{	
	//TODO Add your javascript code here
	ID_GAUGE.fill = m_color;
}
```

속성 변수창을 이용하여 심볼 변수 추가

double m\_min = 0

double m\_max = 100

double m\_value = 0

string m\_color = "\#ffbf28"

## 동적 디스플레이

다음으로 심볼을 선택하거나 배경을 선택후 이벤트함수 \_ontaskview\(\)함수를 추가합니다. 이때 추가할 스크립트는 JavaScript를 이용하여 추가합니다. JavaScript를 이용하는 경우에는 웹 현시에 있어 동일한 스크립트가 동작되어 수행됩니다.

```js
function _ontaskview()
{	
	//TODO Add your javascript code here
	var datagap = m_max-m_min;
	var data = m_value;

	if (data < m_min)
		data = m_min;
	else if (data >m_max)
		data = m_max;

	var angle = ((360 * (data-m_min)) / (m_max - m_min) - 90);

	// M40,40 L67.80,11.36 A40.00,40.00 0 0,0 40.00,0.00 Z
	// M40,40 L35.42,79.76 A40.00,40.00 0 1,0 40.00,0.00 Z
	var x1 = 80+Math.cos(angle * 3.141592 / 180)*80;
	var y1 = 80+Math.sin(angle * 3.141592 / 180)*80;
	var dir = 0;

	if (angle+90>180)
		dir = 1;

	ID_GAUGE.d = "M80,80 L"+x1.toString()+ ","+y1.toString()+" A80.00,80.00 0 "+ dir.toString()+",0 80.00,0.00 Z";
	ID_LABEL.textContent = m_value.toString();
}
```

위 코드를 간단하게 보면, 출력 데이터의 값이 심볼변수를 설정한 min, max의 범위안에서 처리가 되도록 조건을 걸어줍니다. 다음으로 ID\_GAUGE는 패스객체로서 값에 따른 동적 표현을 위한 포인트정보를 계산하여 d 속성에 할당합니다.

ID\_LABEL의 값 현시를 위한 코드를 추가합니다. 이와같은 방법으로 SVG 그래픽 과 JavaScript 코드를 이용하여 다양한 그래픽 심볼 라이브러리를 생성할 수 있습니다.

## 화면 적용

생성된 라이브러리를 이용하여 픽쳐페이지에 적용합니다. Project Explorer에서 Picture를 선택후 Add New Picture Item 메뉴를 선택하여 픽쳐페이지를 생성합니다.

생성된 픽쳐페이지에 생성한 라이브러리를 마우스를 이용하여 드래그 & 드랍으로 객체를 생성합니다. 

생성된 객체를 선택후, m\_value변수에 상수값을 입력하거나 외부의 변수를 입력합니다. 외부의 변수 입력은 \#ID.variable 형태로 변수의 첫문자는 \#문자로 지정합니다.

 ![](./assets/hmi-library1/hmi_gauge_accept.png)



