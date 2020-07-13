---
layout: default
title: enuSetSelectSpecularColor
parent: Application API
---
# void enuSetSelectSpecularColor\(HVIEW pENUView, wchar\_t\* strColor\)

void enuSetSelectSpecularColor\(HVIEW pENUView, wchar\_t\* strColor\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

* wchar\_t\* strColor

색상값을 입력합니다. \(ex. "RGB\(255,255,255\)" or "\#FFFFFF"

#### Return Value

Type : NONE

#### Remarks

선택된 객체의 specularColor의 속성값을 지정합니다.

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
void CenuSpaceView::On3DSpecularColor()
{
	CMFCRibbonBar* pRibbon = ((CMDIFrameWndEx*) AfxGetMainWnd())->GetRibbonBar(); 
	ASSERT_VALID(pRibbon); 

	CMFCRibbonColorButton* pFillColorBtn = DYNAMIC_DOWNCAST(CMFCRibbonColorButton, pRibbon->FindByID(ID_3D_SPECULARCOLOR));

	if (pFillColorBtn != NULL)
	{
		COLORREF color = pFillColorBtn->GetColor();
		int R = 0, G = 0, B = 0; 

		R = GetRValue(color); 
		G = GetGValue(color);
		B = GetBValue(color); 

		CString strColor;
		strColor.Format(L"%2x%2x%2x", R, G, B);

		enuSetSelectSpecularColor(m_pENUView, strColor.GetBuffer(0));
	}
}
```



