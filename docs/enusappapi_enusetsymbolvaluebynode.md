---
layout: default
title: enuSetSymbolValueByNode
parent: Application API
---
# void enuSetSymbolValueByNode\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)

void enuSetSymbolValueByNode\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)

#### Parameters

* HSVG pSvgHandler

SVG핸들을 입력합니다.

* HNODE pNode

해당객체의 노드 핸들을 지정합니다.

* wchar\_t\* pStrVariable

USE 객체의 변수를 입력합니다.

* wchar\_t\* pStrValue

Value값을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

USE객체의 속성값을 설정할 경우 사용합니다.

USE 객체의 자식으로 Symbol 객체가 있으며 Symbol 객체의 자식으로 Attribute객체를 포함합니다. 위 함수는 Attribute객체의 속성값을 설정하는 함수입니다.

USE Child -&gt; Symbol Child -&gt; Attribute \(변수\) &lt;- 변수의 값을 설정하기 위한 함수입니다.

USE객체의 Interface 속성값을 설정할 경우에는 enuSetUseInterfaceByNode\(\) 함수 활용.

