---
layout: default
title: enuGetAttribute3DByNode
parent: Application API
---
# void enuGetAttribute3DByNode\(HX3D pX3DHandler, HNODE pObject, wchar\_t\* pStrVariable, VariableStruct\* pData\)

void enuGetAttribute3DByNode\(HX3D pX3DHandler, HNODE pObject, wchar\_t\* pStrVariable, VariableStruct\* pData\)

#### Parameters

* HX3D pX3DHandler

X3D 픽쳐 핸들러를 지정합니다.

* HNODE pObject

3D 객체 NODE 핸들을 지정합니다.

* wchar\_t\* pStrVariable

속성변수명을 지정합니다.

* VariableStruct\* pData

반환받고자 하는 구조체의 주소값을 지정합니다.

```cpp
struct VariableStruct
{
    wchar_t name[DEF_NAME_LEN];
    int     type;
    void*   pValue;
    wchar_t strValue[DEF_MAXTEXT_LEN];
    arrayInfo array;

public :VariableStruct()
        {
            wcscpy_s(name, L"");            
            type = DEF_UNKNOWN;
            pValue = NULL;
            wcscpy_s(strValue, L"N/A");
        }
};
```

#### Return Value

Type : VariableStruct\* pData

구조체의 정보에 해당 객체의 노드 정보를 반환받습니다.

#### Remarks

3D 노드에 대하여 해당 노드의 정보를 반환받습니다.

```css
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
    HNODE hGeo = enuCreate3DBox(pX3D,"MyBox", 100, 0, 0, 0);       

    VariableStruct size_info;

    enuGetAttribute3DByNode(pX3D, hGeo, L"size", &size_info);
    if (size_info.pValue)
    {
        if (size_info.type == DEF_FLOAT)
        {
            float size[3];
            size[0] = *((float*)size_info.pValue + 0);
            size[1] = *((float*)size_info.pValue + 1);
            size[2] = *((float*)size_info.pValue + 2);
        }
    }
}
```



