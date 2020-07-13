---
layout: default
title: enuSetModifyUseHref
parent: Application API
---
# void enuSetModifyUseHref\(wchar\_t\* strSrcId, wchar\_t\* strNewId\)

void enuSetModifyUseHref\(wchar\_t\* strSrcId, wchar\_t\* strNewId\)

#### Parameters

* wchar\_t\* strSrcId

적용된 USE객체의 href를 입력합니다.

* wchar\_t\* strNewId

변경할 USE객체의 href를 입력합니다.

#### Return Value

Type : void

#### Remarks

심볼객체의 id 변경시, 기존 추가된 USE객체의 모든 href의 속성 변경 수행시 위 함수를 호출하여 모든 USE객체의 href의 값을 변경한다.

```xml
<?xml version="1.0" encoding="UTF-16"?>
<svg
	id="ID_1encCj"
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
	pg-create-time="2018-2-19 3:33:25.1"
	width="1920"
	height="1080"
>
	<defs
		id="ID_1encCj1"
	>
		<symbol
			id="NODE"
			type="node"
			stroke="rgb(0,119,189)"
			stroke-opacity="1.00"
			stroke-width="1.00"
			transform="translate(0.00,0.00) rotate(0.00) scale(1.0000, 1.0000)"
			pg-xcenter="0.00"
			pg-ycenter="0.00"
		>
			<script
				id="ID_1encDi"
				type="text/lua"
			>
					<![CDATA[function _ontask()
	output = input
end]]>
			</script>
			<pg-pin
				id="ID_1encD2"
				name="input"
				desc=""
				pin-type="input"
				color="rgb(255,255,255)"
				var-type="int"
				unit=""
				default-value="0"
			>
				<circle
					id="ID_1encD21"
					stroke="rgb(200,0,0)"
					stroke-opacity="1.00"
					stroke-width="1.00"
					transform="translate(9.00,11.00) rotate(0.00) scale(1.0000, 1.0000)"
					pg-xcenter="0.00"
					pg-ycenter="0.00"
					stroke-dasharray="1,1,1"
 					cx="0.00"
					cy="0.00"
					rx="0.00"
					ry="0.00"
					r="5.00"
					fill="rgb(0,176,80)"
					fill-opacity="1.00"
				>
				</circle>
			</pg-pin>
			<pg-pin
				id="ID_1encDG"
				name="output"
				desc=""
				pin-type="input"
				color="rgb(255,255,255)"
				var-type="int"
				unit=""
				default-value="0"
			>
				<circle
					id="ID_1encDG1"
					stroke="rgb(200,0,0)"
					stroke-opacity="1.00"
					stroke-width="1.00"
					transform="translate(47.18,12.21) rotate(0.00) scale(1.0000, 1.0000)"
					pg-xcenter="0.00"
					pg-ycenter="0.00"
					stroke-dasharray="1,1,1"
 					cx="0.00"
					cy="0.00"
					rx="0.00"
					ry="0.00"
					r="5.00"
					fill="rgb(0,176,80)"
					fill-opacity="1.00"
				>
				</circle>
			</pg-pin>
		</symbol>
	</defs>
</svg>

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
	<use
		id="ID_1enlR20"
		type="logic"
		stroke="rgb(0,119,189)"
		stroke-opacity="1.00"
		stroke-width="1.00"
		transform="translate(514.00,197.00) rotate(0.00) scale(1.0000, 1.0000)"
		pg-xcenter="0.00"
		pg-ycenter="0.00"
		xlink:href="#NODE"
		x="0.00"
		y="0.00"
	>
		<pg-set-pin variable="#input" shape="" var-type="int" value="0"/>
		<pg-set-pin variable="#output" shape="" var-type="int" value="0"/>
	</use>
</svg>


```

#### Examples

```cpp
void ChangeSymbolName()
{
    enuSetModifyUseHref(L"#NODE", L"#NODE_NEW");
}
```



