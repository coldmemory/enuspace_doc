---
layout: default
title: enuSetUseInterface
parent: Application API
---
# void enuSetUseInterface\(HSVG pSvgHandler, wchar\_t\* strVariable, wchar\_t\* strValue\)

void enuSetUseInterface\(HSVG pSvgHandler, wchar\_t\* strVariable, wchar\_t\* strValue\)

#### Parameters

* HSVG pSvgHandler

SVG 핸들을 입력합니다.

* wchar\_t\* strVariable

USE객체의 인터페이스 변수를 지정합니다.

* wchar\_t\* strValue

USE객체의 변수값을 지정합니다.

#### Return Value

Type : void

#### Remarks

USE객체의 Attribute에 해당하는 SetAttribute의 속성값을 지정합니다.

```xml
<?xml version="1.0" encoding="UTF-16"?>
<svg
    id="ID_1enc0p"
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
    width="1920"
    height="1080"
>
    <defs
        id="ID_1enc0p1"
    >
        <symbol
            id="SYMBOL1"
            type="node"
            stroke="rgb(0,119,189)"
            stroke-opacity="1.00"
            stroke-width="1.00"
            transform="translate(0.00,0.00) rotate(0.00) scale(1.0000, 1.0000)"
            pg-xcenter="0.00"
            pg-ycenter="0.00"
        >
            <rect
                id="ID_1enc0z0"
                stroke="rgb(0,119,189)"
                stroke-opacity="1.00"
                stroke-width="2.00"
                transform="translate(2.00,-1.00) rotate(0.00) scale(1.0000, 1.0000)"
                pg-xcenter="0.00"
                pg-ycenter="0.00"
                stroke-linecap="butt"
                 stroke-linejoin="miter"
                 x="0.00"
                y="0.00"
                width="82.00"
                height="55.00"
                rx="0.00"
                ry="0.00"
                fill="rgb(0,174,238)"
                fill-opacity="1.00"
            >
            </rect>
            <pg-attribute
                id="ID_1enoLa"
                type="int"
                variable="m_value"
                initial="0"
                desc=""
            >
            </pg-attribute>
        </symbol>
    </defs>
</svg>
```

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
    width="1920"
    height="1080"
>
    <use
        id="ID_USE"
        type="logic"
        stroke="rgb(0,119,189)"
        stroke-opacity="1.00"
        stroke-width="1.00"
        transform="translate(220.00,123.00) rotate(0.00) scale(1.0000, 1.0000)"
        pg-xcenter="0.00"
        pg-ycenter="0.00"
        xlink:href="#NODE"
        x="0.00"
        y="0.00"
    >
        <pg-set-pin variable="#input" shape="" var-type="int" value="10"/>
        <pg-set-pin variable="#output" shape="" var-type="int" value="10"/>
    </use>
    <use
        id="ID_1enoMr0"
        type="hmi"
        stroke="rgb(0,119,189)"
        stroke-opacity="1.00"
        stroke-width="1.00"
        transform="translate(214.00,229.00) rotate(0.00) scale(1.0000, 1.0000)"
        pg-xcenter="0.00"
        pg-ycenter="0.00"
        xlink:href="#SYMBOL1"
        x="0.00"
        y="0.00"
    >
        <pg-set-attribute
            id="ID_1enoMr4"
            variable="#m_value"
            value="#ID_USE.input"
        >
        </pg-set-attribute>
    </use>
</svg>
```

#### 

#### Examples

```cpp
enuSetUseInterface(hsvg, L"ID_OBJECT.#m_value", L"#ID_USE.input");
```



