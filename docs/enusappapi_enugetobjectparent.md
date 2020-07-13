---
layout: default
title: enuGetObjectParent
parent: Application API
---
enuSpace for saturn\(ver.4\)

# HNODE enuGetObjectParent\(HNODE pNode\)

HNODE enuGetObjectParent\(HNODE pNode\)

#### Parameters

* HNODE pNode

객체를 입력합니다.

#### Return Value

Type : HNODE

해당하는 객체의 상위 객체를 반환받습니다. 해당하는 객체가 없는경우 NULL값을 반환합니다.

#### Remarks

```xml
<?xml version="1.0" encoding="UTF-16"?>
<svg id="RootNode" stroke="rgb(0,119,189)" stroke-opacity="1" stroke-width="1" transform="translate(0,0) rotate(0) scale(1, 1)" pg-xcenter="0" pg-ycenter="0" style="stroke:rgb(127,127,127);stroke-opacity:1.00;stroke-width:2.00;stroke-dasharray:1,1,1;"
    enuspace-version="4.0.0.0"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    width="1920"
    height="1080"
>
    <defs id="Node">
        <symbol id="Node01" type="node" stroke="rgb(0,0,0)" stroke-opacity="1" stroke-width="1" transform="translate(0,0) rotate(0) scale(1, 1)" pg-xcenter="0" pg-ycenter="0">
            <rect id="1_1" stroke="rgb(255,255,255)" stroke-opacity="1" stroke-width="1" transform="translate(-32,-96) rotate(0) scale(1, 1)" pg-xcenter="0" pg-ycenter="0" x="0" y="0" width="31" height="31" rx="0" ry="0" fill="rgb(89,89,89)" fill-opacity="1" use-text="true" text="" font-family="Arial" font-size=" 0.1" font-style="normal" text-color="rgb(0,0,0)" text-opacity="1.00" horizontal_align="center" vertical_align="middle"></rect>
            <rect id="1_2" stroke="rgb(255,255,255)" stroke-opacity="1" stroke-width="1" transform="translate(-32,-96) rotate(0) scale(1, 1)" pg-xcenter="0" pg-ycenter="0" x="0" y="0" width="31" height="31" rx="0" ry="0" fill="rgb(89,89,89)" fill-opacity="1" use-text="true" text="" font-family="Arial" font-size=" 0.1" font-style="normal" text-color="rgb(0,0,0)" text-opacity="1.00" horizontal_align="center" vertical_align="middle"></rect>
        </symbol>
        <symbol id="Node02" type="node" stroke="rgb(0,119,189)" stroke-opacity="1" stroke-width="1" transform="translate(0,0) rotate(0) scale(1, 1)" pg-xcenter="0" pg-ycenter="0">
            <rect id="2_1" stroke="rgb(255,255,255)" stroke-opacity="1" stroke-width="1" transform="translate(-32,-96) rotate(0) scale(1, 1)" pg-xcenter="0" pg-ycenter="0" x="0" y="0" width="31" height="31" rx="0" ry="0" fill="rgb(89,89,89)" fill-opacity="1" use-text="true" text="" font-family="Arial" font-size=" 0.1" font-style="normal" text-color="rgb(0,0,0)" text-opacity="1.00" horizontal_align="center" vertical_align="middle"></rect>
            <rect id="2_2" stroke="rgb(255,255,255)" stroke-opacity="1" stroke-width="1" transform="translate(-32,-96) rotate(0) scale(1, 1)" pg-xcenter="0" pg-ycenter="0" x="0" y="0" width="31" height="31" rx="0" ry="0" fill="rgb(89,89,89)" fill-opacity="1" use-text="true" text="" font-family="Arial" font-size=" 0.1" font-style="normal" text-color="rgb(0,0,0)" text-opacity="1.00" horizontal_align="center" vertical_align="middle"></rect>
        </symbol>
    </defs>
</svg>
```

#### Examples

```cpp
HSVG hsvg = enuGetHmiClass(L"library\\hmi\\hmi_symbol.svg");
if (hsvg)
{
    HNODE hmyNode = enuGetObjectById(hsvg, L"2_2");
    if (hmyNode)
    {
        HNODE hNode = enuGetObjectParent(hmyNode); // Node02 객체 반환

        while (hNode)
        {
            // To do your job.

            hNode = enuGetObjectPrev(hNode);
        }
    }
}
```



