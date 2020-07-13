---
layout: default
title: enuExportWebStyleSvg
parent: Application API
---
# bool enuExportWebStyleSvg\(wchar\_t\* strTaget, wchar\_t\* strSource\)

bool enuExportWebStyleSvg\(wchar\_t\* strTaget, wchar\_t\* strSource\)

#### Parameters

* wchar\_t\* strTaget

웹 기반의 파일 포맺으로 변경될 파일이름을 입력합니다.

* wchar\_t\* strSource

픽쳐 파일의 이름을 입력합니다.

#### Return Value

Type : bool

웹 기반의 파일 포맺으로 정상 저장 유무를 반환합니다.

#### Remarks

웹 기반의 파일 포맺으로 픽쳐파일을 저장합니다. 저장된 픽쳐 파일은 웹으로 현시됩니다.

#### Examples

```cpp
enuExportWebStyleSvg(L"web\\picture1.svg", L"picture\\picture1.svg");
```



