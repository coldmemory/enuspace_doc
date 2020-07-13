---
layout: default
title: enuSet3DLuaScriptByNode
parent: Application API
---
# void enuSet3DLuaScriptByNode\(HX3D pX3D, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)

void enuSet3DLuaScriptByNode\(HX3D pX3D, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)

#### Parameters

* HX3D pX3D

X3D 픽쳐 핸들을 입력합니다.

* HNODE pNode

Shape 핸들을 입력합니다.

* wchar\_t\* strFunction

등록하고자 하는 함수의 이름을 입력합니다.

* wchar\_t\* strScript

스크립트의 내용을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

객체에 스크립트를 추가한 file format 예시.

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
				<script
					type="text/lua"
				>
						<![CDATA[function _ontaskview()
	rotation_z = rotation_z + 1
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
    HNODE hGeo = enuCreate3DBox(pX3D, L"ID_BOX", 100, 0, 0, 0);   
    HX3D hShape = enuGetShapeFromGeometry(pX3D, hGeo);

    CString script = L"function _ontaskview()\r\n rotation_z = rotation_z + 1 \r\nend"
    enuSet3DLuaScriptByNode(pX3D, hShape, L"_ontaskview", script.GetBuffer(0));
}
```



