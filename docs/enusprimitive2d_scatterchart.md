---
layout: default
title: scatterchart
parent: 기초객체(2D)
grand_parent: enuSpace Tutorial
---

# scatterchart



---

scatterchart 객체에 대하여 설명합니다. enuSpace는 OpenGl엔진을 이용합니다.

## Properties

아래의 테이블의 속성정보는 스크립트상에서 연계되는 속성 이름과 데이터 타입정보 입니다.

| Property | Type | Description | Value |
| :--- | :--- | :--- | :--- |
| diffuseColor | string | 객체의 color 속성 | "rgb\(0,0,0\)", "\#000000" |
| emissiveColor | string | 객체의 발광 color 속성 | "rgb\(0,0,0\)", "\#000000" |
| specularColor | string | 객체의 highlight color 속성 | "rgb\(0,0,0\)", "\#000000" |
| ambientlntensity | float | 객체의 라인 투명도 속성 | 0~1 |
| shininess | float | 객체표면의 광택의 강도 | 0~1 |
| transparency | float | 객체의 투명도 속성 | value |
| translation\_x | double | 객체의 X축 위치 | value |
| translation\_y | double | 객체의 Y축 위치 | value |
| translation\_z | double | 객체의 Z축 위치 | value |
| rotation\_x | float | 객체의 X축 회전값 | value |
| rotation\_y | float | 객체의 Y축 회전값 | value |
| rotation\_z | float | 객체의 Z축 회전값 | value |
| scale\_x | float | 객체의 X 확대율 | value |
| scale\_y | float | 객체의 Y 확대율 | value |
| scale\_z | float | 객체의 Z 확대울 | value |
| center\_x | float | 객체의 X축 중앙점 | value |
| center\_y | float | 객체의 Y축 중앙점 | value |
| center\_z | float | 객체의 Z축 중앙점 | value |
| solid | bool | 면 채우기 | true, false |
| size\_x | float | 객체의 x축 크기 | value |
| size\_y | float | 객체의 y축 크기 | value |
| height | float | 객체의 z축 크기 | value |
| minData\_x | float | x축 최소 값 | value |
| minData\_y | float | y축 최소 값 | value |
| minData\_z | float | z축 최소 값 | value |
| maxData\_x | float | x축 최대 값 | value |
| maxData\_y | float | y축 최대 값 | value |
| maxData\_z | float | z축 최대 값 | value |
| dataArray\_size | int | data의 총 갯수를 결정하는 속성 | value |
| symbolType | string | 심볼의 타입 | symbol\_rect, symbol\_point, symbol\_textnshape, symbol\_image |
| symbolSize\_x | float | 심볼의 x크기 | value |
| symbolSize\_y | float | 심볼의 y크기 | value |
| subLabelType | string |  | value |
| label\_num | string | color값의 갯수에 따라 층을 나누고, 해당하는 층의 color값을 결정한다 | rgb\(10,50,120\);rgb\(15,75,165\);....... |

## Script Example

스크립트는 lua스크립트와 javascript를 이용하여 적용할 수 있습니다.

객체의 속성을 설정하는 방법에는 직접 객체의 변수에 접근하여 적용하는 방법이 있습니다. 직접 변수에 접근하고자 할 경우에는 위 테이블의 속성이름을 통하여 접근을 수행합니다.

스크립트를 X3D노드에서 추가하였을 경우에는 해당객체의 ID와 속성을 통하여 스크립트를 작성합니다.

### lua Script

lua Script \(객체내부의 ontaskview 함수에서의 구현한 예시\)

```lua
function _ontaskview()

    data[0][0] = 10    -- 객체 내부에서 속성 변경시 직접 변경 할 수 있음
    data[0][1] = 90
    data[0][2] = 40
    data[0][3] = 0
    data[0][4] = 30
    data[0][5] = 0
    data[1][0] = 20
    data[1][1] = 90
    data[1][2] = 80
    data[1][3] = 60
    data[1][4] = 30
    data[1][5] = 50
    data[2][0] = 20
    data[2][1] = 40
    data[2][2] = 90
    data[2][3] = 80
    data[2][4] = 70
    data[2][5] = 100
end
```

lua Script \(x3d의 ontaskview 함수에서의 구현한 예시\)

```lua
function _ontaskview()
    ID_CONTOUR.data[0][0] = 10 -- 객체 내부에서 속성 변경시 직접 변경 할 수 있음
    ID_CONTOUR.data[0][1] = 90
    ID_CONTOUR.data[0][2] = 40
    ID_CONTOUR.data[0][3] = 0
    ID_CONTOUR.data[0][4] = 30
    ID_CONTOUR.data[0][5] = 0
    ID_CONTOUR.data[1][0] = 20
    ID_CONTOUR.data[1][1] = 90
    ID_CONTOUR.data[1][2] = 80
    ID_CONTOUR.data[1][3] = 60
    ID_CONTOUR.data[1][4] = 30
    ID_CONTOUR.data[1][5] = 50
    ID_CONTOUR.data[2][0] = 20
    ID_CONTOUR.data[2][1] = 40
    ID_CONTOUR.data[2][2] = 90
    ID_CONTOUR.data[2][3] = 80
    ID_CONTOUR.data[2][4] = 70
    ID_CONTOUR.data[2][5] = 100

end
```

### javascript

javascript를 이용하여 적용하였을 경우, 웹 랜더러를 이용하여 동적 웹 가시화가 가능합니다.

javascript \(객체내부의 ontaskview함수에서의 구현한 예시\)

```js
function _ontaskview()
{
    data[0][0] = 10;    //객체 내부에서 속성 변경시 직접 변경 할 수 있음
    data[0][1] = 90;
    data[0][2] = 40;
    data[0][3] = 0;
    data[0][4] = 30;
    data[0][5] = 0;
    data[1][0] = 20;
    data[1][1] = 90;
    data[1][2] = 80;
    data[1][3] = 60;
    data[1][4] = 30;
    data[1][5] = 50;
    data[2][0] = 20;
    data[2][1] = 40;
    data[2][2] = 90;
    data[2][3] = 80;
    data[2][4] = 70;
    data[2][5] = 100;

}
```

## enuSpace의 속성 윈도우

enuSpace 스튜디오를 통하여 객체의 편집 및 속성정보를 확인할 수 있습니다.

![](./assets/3d/terrain_prop.png)

## X3D Tag 예시

객체의 내부에 추가된 스크립트와 x3d루트에 추가된 스크립트는 아래 스크립트 예시와 같이 적용됩니다.

```xml
<?xml version="1.0" encoding="UTF-16" ?>
<x3d
>
    <Scene
    >
        <Transform
            rotation="0.000000,0.000000,0.000000"
            scaleOrientation="0.000000,0.000000,1.000000,0.000000"
            translation="-50.000000,-50.000000,0.000000"
        >
            <Shape
                id="ID_TERRAIN"
            >
                <script
                    type="text/lua"
                >
                        <![CDATA[function _ontaskview()

    data[0][0] = 10
    data[0][1] = 90
    data[0][2] = 40
    data[0][3] = 0
    data[0][4] = 30
    data[0][5] = 0
    data[1][0] = 20
    data[1][1] = 90
    data[1][2] = 80
    data[1][3] = 60
    data[1][4] = 30
    data[1][5] = 50
    data[2][0] = 20
    data[2][1] = 40
    data[2][2] = 90
    data[2][3] = 80
    data[2][4] = 70
    data[2][5] = 100    
end]]>
                </script>
                <Appearance
                >
                    <Material
                        ambientIntensity="0.200000"
                        shininess="0.200000"
                        transparency="1.000000"
                        diffuseColor="0.800000,0.800000,0.800000"
                        emissiveColor="0.000000,0.000000,0.000000"
                        specularColor="0.000000,0.000000,0.000000"
                    >
                    </Material>
                </Appearance>
                <Terrain
            size="100.000000,100.000000"
            subdivision="3.000000,6.000000"
            height="50.000000"
            minElevation="0.000000"
            maxElevation="100.000000"
            elevationType="color+height"
            colorElevation="rgb(10,50,120);rgb(15,75,165);rgb(30,110,200);rgb(60,160,240);rgb(80,180,250);rgb(130,210,255);rgb(160,240,255);rgb(200,250,255);rgb(230,255,255);rgb(255,250,220);rgb(255,232,120);rgb(255,192,60);rgb(255,160,0);rgb(255,96,0);rgb(255,50,0);rgb(225,20,0);rgb(192,0,0);rgb(165,0,0)"
            terrainType="contour"
            grid_visible="visible"
            outline_visible="visible"
            xyaxis_visible="visible"
            zaxis_visible="visible"
            value_visible="hidden"
            >
        </Terrain>
            </Shape>
        </Transform>
    </Scene>
</x3d>
```



