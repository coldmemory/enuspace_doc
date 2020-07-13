---
layout: default
title: enuDuplicateLogicSymbol
parent: Application API
---
# HNODE enuDuplicateLogicSymbol\(wchar\_t\* strPicture, wchar\_t\* strSymbol\)

HNODE enuDuplicateLogicSymbol\(wchar\_t\* strPicture, wchar\_t\* strSymbol\)

#### Parameters

* wchar\_t\* strPicture

Logic 영역의 픽쳐이름을 입력합니다. \(ex "library\logic\logic\_symbol.svg"\)

* wchar\_t\* strSymbol

Logic 영역의 심볼을 복재하고자 하는 이름을 입력합니다.

#### Return Value

Type : HNODE

복재된 Symbol노드를 반환합니다.

#### Remarks

Logic 영역의 정의된 심볼을 복재하여 추가된 심볼의 노드를 반환하는 함수입니다.

#### Examples

```cpp
enuDuplicateLogicSymbol(L"library\\logic\\logic_symbol.svg", "ID_AND");
```



