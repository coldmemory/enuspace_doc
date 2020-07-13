---
layout: default
title: enuGet3DObjectById
parent: Application API
---
# HNODE enuGet3DObjectById\(HX3D pX3DHandler, wchar\_t\* objectid\)

HNODE enuGet3DObjectById\(HX3D pX3DHandler, wchar\_t\* objectid\)

#### Parameters

* HX3D pX3DHandler

3d 픽쳐 핸들을 입력합니다.

* wchar\_t\* objectid

객체의 ID를 지정합니다.

#### Return Value

Type : 객체의 핸들을 반환합니다. 해당하는 객체가 없는 경우에는 NULL을 반환합니다.

#### Remarks

객체의 ID로부터 3D객체의 핸들을 반환받습니다.

#### Examples

```cpp
HVIEW ViewHandle = NULL; 
void CSampleView::OnInitialUpdate() 
{ 
    CView::OnInitialUpdate(); 

    enuCreateProject();

    // Load Project
    enuLoadProjectFile(L"Project\\sample.enup");

    // Create View
    ViewHandle = enuCreate3DView(this->m_hWnd);

    // ENU View Attach Set Page
    enuSetX3dPageView(ViewHandle , L"picture\\core_3d.x3d");

    // Get X3D picture handle
    HX3D pX3D = enuGetX3DHandler(ViewHandle);

    static VariableStruct data_3d;
    HNODE shape = enuGet3DObjectById(hX3D, L"ID_PIN_CONTOUR");
    HX3D Geo = enuGetGeometryFromShape(hX3D, shape);
    enuGetAttribute3DByNode(hX3D, Geo, L"data", &data_3d);

    if (data_3d.pValue)
    {
        // data_3d.array..size; // 배열정보 확인. 
        double data[240][240][11];

        // data 변수값 설정
        data[0][0][0] = 1;

        // 값 전달.
        if (data_3d.type == DEF_DOUBLE)
        {
            memcpy(data_3d.pValue, data, sizeof(double)*240*240*11);
        }
    }    
}
```

#### SVG 예시

```xml
<?xml version="1.0" encoding="UTF-16" ?>
<x3d
>
    <Scene
    >
        <Transform
            rotation="0.000000,0.000000,0.000000"
            scaleOrientation="0.000000,0.000000,1.000000,0.000000"
            translation="-125.000000,-125.000000,-250.000000"
        >
            <Shape
                id="ID_PIN_CONTOUR"
            >
                <script
                    type="text/lua"
                >
                        <![CDATA[]]>
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
                <Contour3D
                    size="250.000000,250.000000"
                    height="500.000000"
                    subdivision="240.000000,240.000000,11.000000"
                    minElevation="0.000000"
                    maxElevation="1.700000"
                    colorElevation="rgb(0,0,147);rgb(0,0,175);rgb(0,0,207);rgb(0,0,235);rgb(0,12,255);rgb(0,40,255);rgb(0,64,255);rgb(0,96,255);rgb(0,124,255);rgb(0,151,255);rgb(0,183,255);rgb(0,211,255);rgb(0,239,255);rgb(16,255,239);rgb(46,255,209);rgb(76,255,179);rgb(104,255,151);rgb(131,255,124);rgb(155,255,96);rgb(187,255,68);rgb(219,255,36);rgb(246,255,9);rgb(255,235,0);rgb(255,203,0);rgb(255,175,0);rgb(255,147,0);rgb(255,119,0);rgb(255,88,0);rgb(255,60,0);rgb(255,32,0);rgb(255,2,0);rgb(227,0,0);rgb(199,0,0);rgb(169,0,0);rgb(139,0,0)"
                    grid_visible="hidden"
                    outline_visible="hidden"
                    xyaxis_visible="hidden"
                    zaxis_visible="hidden"
                    value_visible="hidden"
                    hidden_points="0:79,0:15,z 0:47,15:31,z 0:31,31:47,z 0:15,47:79,z 159:239,0:15,z 191:239,15:31,z 207:239,31:47,z 223:239,47:79,z 0:79,223:239,z 0:47,207:223,z 0:31,191:207,z 0:15,159:191,z 159:239,223:239,z 191:239,207:223,z 207:239,191:207,z 223:239,159:191,z 0:119,0:119,5:10  0:119,0:239,7:10"
                >
                </Contour3D>
            </Shape>
        </Transform>
    </Scene>
</x3d>
```



