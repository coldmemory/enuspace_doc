---
layout: default
title: enuGetCoordinateFromIndexedFaceSet
parent: Application API
---
# HNODE enuGetCoordinateFromIndexedFaceSet\(HX3D pX3DHandler, HNODE node\)

HNODE enuGetCoordinateFromIndexedFaceSet\(HX3D pX3DHandler, HNODE node\)

#### Parameters

* HX3D pX3DHandler

3D X3D 핸들을 입력합니다.

* HNODE node

IndexedFaceSet 객체의 노드를 입력합니다.

#### Return Value

Type : HNODE

Coordinate 노드를 반환합니다.

#### Remarks

```xml
<?xml version="1.0" encoding="UTF-16" ?>
<x3d
>
    <Scene
    >
        <Transform
            rotation="0.000000,0.000000,0.000000"
            scaleOrientation="0.000000,0.000000,1.000000,0.000000"
        >
            <Shape
                id="ID_1enaCm"
            >
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
                <IndexedFaceSet
                    coordIndex="0 1 2 -1 3 4 5 -1 6 7 8 -1 9 10 11 -1 12 13 14 -1 15 16 17 -1 18 19 20 -1"
                >
                    <Coordinate
                        point="-10 -5 0 -9 -5 1 -8 -5 2 -7 -5 3 -6 -5 8 -5 -5 2 -4 -5 9 -3 -5 1 -2 -5 5 -1 -5 7 0 0 5 1 5 3 2 5 3 3 5 6 4 5 1 5 5 10 6 5 6 7 5 9 8 5 2 9 5 7 10 5 2"
                    >
                    </Coordinate>
                </IndexedFaceSet>
            </Shape>
        </Transform>
    </Scene>
</x3d>
```

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

    // Create 3D FaceSet
    CString points = L"-10 -5 0 -9 -5 1 -8 -5 2 -7 -5 3 -6 -5 8 -5 -5 2 -4 -5 9 -3 -5 1 -2 -5 5 -1 -5 7 0 0 5 1 5 3 2 5 3 3 5 6 4 5 1 5 5 10 6 5 6 7 5 9 8 5 2 9 5 7 10 5 2";
    CString vectors = L"0 1 2 -1 3 4 5 -1 6 7 8 -1 9 10 11 -1 12 13 14 -1 15 16 17 -1 18 19 20 -1";
    HNODE node = enuCreate3DFaceSet(pX3D,"MyObject", points.GetBuffer(0), vectors.GetBuffer(0), 0, 0, 0);       

    HNODE node_cord = enuGetCoordinateFromIndexedFaceSet(pX3D, node);

    VariableStruct point_info;
    enuGetAttribute3DByNode(pX3D, hGeo, L"point", &point_info);
    if (point_info.pValue)
    {
        if (point_info.type == DEF_STRING)
        {
            CString strPoint = *(CString*)point_info.pValue;

            // strPoint Value : "-10 -5 0 -9 -5 1 -8 -5 2 -7 -5 3 -6 -5 8 -5 -5 2 -4 -5 9 -3 -5 1 -2 -5 5 -1 -5 7 0 0 5 1 5 3 2 5 3 3 5 6 4 5 1 5 5 10 6 5 6 7 5 9 8 5 2 9 5 7 10 5 2";
        }
    }
}
```



