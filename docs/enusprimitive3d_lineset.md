---
layout: default
title: lineset
parent: 기초객체(3D)
grand_parent: enuSpace Tutorial
---

# lineset

![](./assets/3d/lineset.png)

---

선 객체에 대하여 설명합니다. enuSpace는 OpenGl엔진을 이용합니다.

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
| vertexCount | int | 정점의 갯수 | value |
| point | string | 라인의 포인트를 나열하는 속성\(ex: x y z x y z\) | string |

## Script Example

스크립트는 lua스크립트와 javascript를 이용하여 적용할 수 있습니다.

객체의 속성을 설정하는 방법에는 직접 객체의 변수에 접근하여 적용하는 방법이 있습니다. 직접 변수에 접근하고자 할 경우에는 위 테이블의 속성이름을 통하여 접근을 수행합니다.

스크립트를 X3D노드에서 추가하였을 경우에는 해당객체의 ID와 속성을 통하여 스크립트를 작성합니다.

### lua Script

lua Script \(객체내부의 ontaskview 함수에서의 구현한 예시\)

```lua
function _ontaskview()
    translation_x = 50   -- 객체 내부에서 속성 변경시 직접 변경 할 수 있음
end
```

lua Script \(x3d의 ontaskview 함수에서의 구현한 예시\)

```lua
function _ontaskview()
    ID_LINESET.translation_x = 50    -- 객체 내부에서 속성 변경시 직접 변경 할 수 있음
end
```

### javascript

javascript를 이용하여 적용하였을 경우, 웹 랜더러를 이용하여 동적 웹 가시화가 가능합니다.

javascript \(객체내부의 ontaskview함수에서의 구현한 예시\)

```js
function _ontaskview()
{
    translation_x = 50;    //객체 내부에서 속성 변경시 직접 변경 할 수 있음
}
```

## enuSpace의 속성 윈도우

enuSpace 스튜디오를 통하여 객체의 편집 및 속성정보를 확인할 수 있습니다.

![](./assets/3d/lineset_prop.png)

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
            scale="3.000000,3.000000,3.000000"
            scaleOrientation="0.000000,0.000000,1.000000,0.000000"
        >
            <Shape
                id="ID_LINESET"
            >
                <script
                    type="text/lua"
                >
                        <![CDATA[function _ontaskview()

    translation_x = 50

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
                <LineSet
                    vertexCount="0"
                >
                    <Coordinate
                        point="-10 -5 0 -9 -5 1 -8 -5 2 -7 -5 3 -6 -5 8 -5 -5 2 -4 -5 9 -3 -5 1 -2 -5 5 -1 -5 7 0 0 5 1 5 3 2 5 3 3 5 6 4 5 1 5 5 10 6 5 6 7 5 9 8 5 2 9 5 7 10 5 2"
                    >
                    </Coordinate>
                </LineSet>
            </Shape>
        </Transform>
    </Scene>
</x3d>
```



