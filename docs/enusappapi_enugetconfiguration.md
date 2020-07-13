---
layout: default
title: enuGetConfiguration
parent: Application API
---
# wchar\_t\* enuGetConfiguration\(wchar\_t\* pAttribute\)

wchar\_t\* enuGetConfiguration\(wchar\_t\* pAttribute\)

#### Parameters

* wchar\_t\* pAttribute

Configuration의 정의값을 지정합니다.

#### Return Value

Type : wchar\_t\*

속성값을 반환합니다.

#### Remarks

| Attribute | Value |
| :--- | :--- |
| WebServerIP | 127.0.0.1 |
| WebServerUse | true |
|  |  |
| WebServerStartup | false |
|  |  |
| enuServerIP | 0.0.0.0 |
|  |  |
| enuServerUse | false |
|  |  |
| enuServerStartup | false |
|  |  |
| TimeMode | Simulation Time |
|  |  |
| WebServerPort | 8080 |

#### Examples

```cpp
CString strWebUse = enuGetConfiguration(L"WebServerUse");
```



