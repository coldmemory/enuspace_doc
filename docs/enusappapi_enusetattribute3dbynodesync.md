---
layout: default
title: enuSetAttribute3DByNodeSync
parent: Application API
---
# bool enuSetAttribute3DByNodeSync\(HX3D pX3DHandler, HNODE pObject, wchar\_t\* pStrVariable, wchar\_t\* pStrValue, bool bHistory, bool bScript\)

bool enuSetAttribute3DByNodeSync\(HX3D pX3DHandler, HNODE pObject, wchar\_t\* pStrVariable, wchar\_t\* pStrValue, bool bool bHistory, bool bScript\)

#### Parameters

* HX3D pX3DHandler

X3D핸들을 입력합니다.

* HNODE pObject

3D 객체 핸들을 입력합니다.

* wchar\_t\* pStrVariable

설정하고자하는 속성 변수를 입력합니다.

* wchar\_t\* pStrValue

변수의 값을 입력합니다.

* bool bHistory=false

Undo를 위한 히스토리 저장여부를 설정합니다.

* bool bScript=false

해당객체의 스크립트를 재등록여부를 설정합니다. \(ID의 속성값을 변경하였을 경우, 스크립트를 재등록하여야 합니다.\)

#### Return Value

Type : bool

정상적인 속성 변경여부를 반환합니다.

#### Remarks

```xml
<?xml version="1.0" encoding="UTF-16" ?>
<x3d
>
    <Scene
    >
        <Transform
            rotation="0.000000,0.000000,113.000000"
            scaleOrientation="0.000000,0.000000,1.000000,0.000000"
        >
            <Shape
                id="ID_BOX"
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

    // Create 3D Box.
    HNODE hGeo= enuCreate3DBox(pX3D,L"MyBox", 100, 0, 0, 0);   

    enuSetAttribute3D(pX3D , L"ID_BOX.size_x", L"100");
    enuSetAttribute3D(pX3D , L"ID_BOX.rotation_z", L"45");
    enuSetAttribute3D(pX3D , L"ID_BOX.transparency", L"0.5");

    HX3D hMat = enuGetMaterialFromGeometry(pX3D, hGeo);
    HX3D hTrans =enuGetTransformFromGeometry(pX3D, hGeo); 

    enuSetAttribute3DByNode(pX3D, hGeo, L"size_x", L"100");                // 비동기식 함수 호출
    enuSetAttribute3DByNode(pX3D, hTrans, L"rotation_z", L"45");           // 비동기식 함수 호출
    enuSetAttribute3DByNode(pX3D, hMat, L"transparency", L"0.5");          // 비동기식 함수 호출

    enuSetAttribute3DByNodeSync(pX3D, hGeo, L"size_x", L"100", false, false);        // 동기식 함수 호출
    enuSetAttribute3DByNodeSync(pX3D, hTrans, L"rotation_z", L"45"false, false);     // 동기식 함수 호출
    enuSetAttribute3DByNodeSync(pX3D, hMat, L"transparency", L"0.5"false, false);    // 동기식 함수 호출

}
```

#### 



