---
layout: default
title: enuSetSelectGroup
parent: Application API
---
# void enuSetSelectGroup\(HVIEW pENUView\)

void enuSetSelectGroup\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

선택 객체에 대하여 Group을 수행합니다.

```xml
<?xml version="1.0" encoding="UTF-16"?>
<svg
	id="ID_1enfXB"
	stroke="rgb(0,119,189)"
	stroke-opacity="1.00"
	stroke-width="1.00"
	transform="translate(0.00,0.00) rotate(0.00) scale(1.0000, 1.0000)"
	pg-xcenter="0.00"
	pg-ycenter="0.00"
	style="stroke:rgb(127,127,127);stroke-opacity:1.00;stroke-width:2.00;stroke-dasharray:1,1,1;"
	enuspace-version="3.0.2.0"
	xmlns="http://www.w3.org/2000/svg"
	xmlns:xlink="http://www.w3.org/1999/xlink"
	pg-create-time="2018-2-19 7:6:45.663"
	width="1920"
	height="1080"
>
	<rect
		id="ID_RECT"
		stroke="rgb(0,119,189)"
		stroke-opacity="1.00"
		stroke-width="2.00"
		transform="translate(235.00,137.00) rotate(0.00) scale(1.0000, 1.0000)"
		pg-xcenter="0.00"
		pg-ycenter="0.00"
		stroke-linecap="butt"
 		stroke-linejoin="miter"
 		x="0.00"
		y="0.00"
		width="80.00"
		height="73.00"
		rx="0.00"
		ry="0.00"
		fill="rgb(0,174,238)"
		fill-opacity="1.00"
	>
	</rect>
	<circle
		id="ID_CIRCLE"
		stroke="rgb(0,119,189)"
		stroke-opacity="1.00"
		stroke-width="2.00"
		transform="translate(417.00,215.00) rotate(0.00) scale(1.0000, 1.0000)"
		pg-xcenter="0.00"
		pg-ycenter="0.00"
		stroke-linecap="butt"
 		stroke-linejoin="miter"
 		cx="0.00"
		cy="0.00"
		rx="52.00"
		ry="52.00"
		r="52.00"
		fill="rgb(0,174,238)"
		fill-opacity="1.00"
	>
	</circle>
</svg>

```

```xml
<?xml version="1.0" encoding="UTF-16"?>
<svg
	id="ID_1enfXB"
	stroke="rgb(0,119,189)"
	stroke-opacity="1.00"
	stroke-width="1.00"
	transform="translate(0.00,0.00) rotate(0.00) scale(1.0000, 1.0000)"
	pg-xcenter="0.00"
	pg-ycenter="0.00"
	style="stroke:rgb(127,127,127);stroke-opacity:1.00;stroke-width:2.00;stroke-dasharray:1,1,1;"
	enuspace-version="3.0.2.0"
	xmlns="http://www.w3.org/2000/svg"
	xmlns:xlink="http://www.w3.org/1999/xlink"
	pg-create-time="2018-2-19 7:6:45.663"
	width="1920"
	height="1080"
>
	<g
		id="ID_1enmz71"
		stroke="rgb(0,119,189)"
		stroke-opacity="1.00"
		stroke-width="1.00"
		transform="translate(0.00,0.00) rotate(0.00) scale(1.0000, 1.0000)"
		pg-xcenter="0.00"
		pg-ycenter="0.00"
	>
		<rect
			id="ID_RECT"
			stroke="rgb(0,119,189)"
			stroke-opacity="1.00"
			stroke-width="2.00"
			transform="translate(235.00,137.00) rotate(0.00) scale(1.0000, 1.0000)"
			pg-xcenter="0.00"
			pg-ycenter="0.00"
			stroke-linecap="butt"
 			stroke-linejoin="miter"
 			x="0.00"
			y="0.00"
			width="80.00"
			height="73.00"
			rx="0.00"
			ry="0.00"
			fill="rgb(0,174,238)"
			fill-opacity="1.00"
		>
		</rect>
		<circle
			id="ID_CIRCLE"
			stroke="rgb(0,119,189)"
			stroke-opacity="1.00"
			stroke-width="2.00"
			transform="translate(417.00,215.00) rotate(0.00) scale(1.0000, 1.0000)"
			pg-xcenter="0.00"
			pg-ycenter="0.00"
			stroke-linecap="butt"
 			stroke-linejoin="miter"
 			cx="0.00"
			cy="0.00"
			rx="52.00"
			ry="52.00"
			r="52.00"
			fill="rgb(0,174,238)"
			fill-opacity="1.00"
		>
		</circle>
	</g>
</svg>
```

#### Examples

```cpp
void CenuSpaceView::OnGroup()
{
	enuSetSelectGroup(m_pENUView);
}
```



