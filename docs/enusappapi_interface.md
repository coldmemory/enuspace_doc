---
layout: default
title: enuSetUseAttribute_interface
parent: Application API
---
# void enuSetUseAttribute\_interface\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strValue\)

void enuSetUseAttribute\_interface\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strValue\)

#### Parameters

* HSVG pSvgHandler

SVG 핸들을 입력합니다.

* HNODE pNode

USE객체의 노드 핸들을 입력합니다.

* wchar\_t\* strValue

Interface의 값을 지정합니다. \(true or false\)

#### Return Value

Type : NONE

#### Remarks

USE객체는 외부의 심볼 또는 USE객체에 대하여 interface를 수행할 수 있다. 인터페이스를 설정하게되면 해당 인터페이스 id값을 지정하여 인터페이스객체로 연계한다.

#### Examples

```cpp
enuSetUseAttribute_interface(hsvg, node_use, L"true");
enuSetUseAttribute_interface_id(hsvg, node_use, L"#ID_USE1");
```



