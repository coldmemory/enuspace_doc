---
layout: default
title: enuGetMaterialFromAppearance
parent: Application API
---
# HNODE enuGetMaterialFromAppearance\(HX3D pX3DHandler, HNODE node\)

HNODE enuGetMaterialFromAppearance\(HX3D pX3DHandler, HNODE node\)

#### Parameters {#parameters}

* HX3D pX3DHandler

X3D 핸들을 입력합니다.

* HNODE node

X3D Applearance 핸들을 입력합니다.

#### Return Value {#return-value}

Type : HNODE

해당 Appearance에 해당하는 Material노드를 반환합니다.

#### Remarks {#remarks}

3D 객체 Appearance노드로 부터 Material노드를 반환합니다.

아래 X3D 내용은 객체를 생성시 노드의 구성정보.

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
                id="ID_1elRo8"
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
                <Box
                    size="10.000000,10.000000,10.000000"
                >
                </Box>
            </Shape>
        </Transform>
    </Scene>
</x3d>
```

#### Examples {#examples}

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

    // Create 3D Cylinder.
    HNODE hGeo = enuCreate3DCylinder(pX3D,"MyCylinder", 100, 100, 10, 0, 0, 0);        

    HX3D hShape = enuGetShapeFromGeometry(pX3D, hGeo);
    HX3D hApp = enuGetAppearanceFromShape(pX3D, hShape);

    HX3D hSeGeo = enuGetGeometryFromShape(pX3D, hShape);        // hSeGeo and hGeo equal.
    HX3D hMat = enuGetMaterialFromGeometry(pX3D, hGeo);  
    HX3D hSeMat = enuGetMaterialFromAppearance(pX3D, hApp);     // hSeMat and hMat equal.
    HX3D hTrans =enuGetTransformFromGeometry(pX3D, hGeo);

    enu3DSetAttributeByNode(pX3D, hMat, L"transparency", L"0.5");
}
```



