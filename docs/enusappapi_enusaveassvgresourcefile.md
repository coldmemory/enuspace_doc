---
layout: default
title: enuSaveAsSvgResourceFile
parent: Application API
---
# bool enuSaveAsSvgResourceFile\(wchar\_t\* strTaget, wchar\_t\* strSource\)

bool enuSaveAsSvgResourceFile\(wchar\_t\* strTaget, wchar\_t\* strSource\)

#### Parameters

* wchar\_t\* strTaget

RESOURCE영역의 저장 SVG 파일이름을 입력합니다.

* wchar\_t\* strSource

RESOURCE영역의 로드된 SVG 파일이름을 입력합니다.

#### Return Value

Type : bool

정상 저장여부를 반환합니다.

#### Remarks

동일한 이름으로 저장하고자 하는 경우에는 , strTarget이름과 strSouce의 이름을 이전의 픽쳐파이름을 입력합니다.

#### Examples

```cpp
enuSaveAsSvgResourceFile(L"style\\style.svg", L"style\\style.svg");
```



