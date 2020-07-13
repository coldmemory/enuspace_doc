---
layout: default
title: enuSetConfiguration
parent: Application API
---
# bool enuSetConfiguration\(wchar\_t\* pAttribute, wchar\_t\* pValue\)

bool enuSetConfiguration\(wchar\_t\* pAttribute, wchar\_t\* pValue\)

#### Parameters

* wchar\_t\* pAttribute

Configuration 속성이름을 입력합니다.

* wchar\_t\* pValue

해당 속성의 값을 입력합니다.

#### Return Value

Type : bool

Configuration 정보가 정상적으로 설정 유무를 반환합니다.

#### Remarks

기 설정된 속성 설정을 업데이트 하거나, 신규 속성을 추가하는 경우에 활용합니다.

#### Examples

```cpp
void SetConfiguration()
{
    enuSetConfiguration(L"WebServerIP", L"127.0.0.1");
}
```



