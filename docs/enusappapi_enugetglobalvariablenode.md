---
layout: default
title: enuGetGlobalVariableNode
parent: Application API
---
# HNODE enuGetGlobalVariableNode\(wchar\_t\* pStrVariable\)

HNODE enuGetGlobalVariableNode\(wchar\_t\* pStrVariable\)

#### Parameters

* wchar\_t\* pStrVariable

전역변수명을 입력합니다.

#### Return Value

Type : HNODE

전역변수의 핸들을 반환합니다.

#### Remarks

Global영역에서 전역변수의 노드를 반환하는 함수입니다.

```xml
<?xml version="1.0" encoding="UTF-16"?>
<svg
	id="ID_1enaBg"
	stroke="rgb(0,119,189)"
	stroke-opacity="1.00"
	stroke-width="1.00"
	transform="translate(0.00,0.00) rotate(0.00) scale(1.0000, 1.0000)"
	pg-xcenter="0.00"
	pg-ycenter="0.00"
	enuspace-version="3.0.2.0"
	xmlns="http://www.w3.org/2000/svg"
	xmlns:xlink="http://www.w3.org/1999/xlink"
	pg-classname="global"
>
	<defs
		id="ID_1enaBg0"
	>
		<pg-struct
			id="ID_1enbGj"
			type="DataIO"
			desc=""
		>
			<pg-attribute
				id="ID_1enbGj0"
				type="double"
				variable="Input"
				initial="0.000000"
				desc="input variable"
			>
			</pg-attribute>
			<pg-attribute
				id="ID_1enbGj1"
				type="double"
				variable="Output"
				initial="0.000000"
				desc="output variable"
			>
			</pg-attribute>
		</pg-struct>
	</defs>
	<pg-attribute
		id="ID_1enbbg"
		type="DataIO"
		variable="g_IO1"
		initial="g_IO1.Input=0.000000 g_IO1.Output=0.000000 "
		desc=""
	>
	</pg-attribute>
	<pg-attribute
		id="ID_1enbdp"
		type="DataIO"
		variable="g_IO2"
		initial="g_IO2.Input=0.000000 g_IO2.Output=0.000000 "
		desc=""
	>
	</pg-attribute>
</svg>
```

#### Examples

```cpp
HNODE enuGetGlobalVariableNode(L"g_IO1");
```



