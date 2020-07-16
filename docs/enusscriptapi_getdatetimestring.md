---
layout: default
title: GetDateTimeString
parent: Script API
---
# GetDateTimeString\(timetype\)

GetDateTimeString\(\)

#### Parameters

none or timetype

timetype

```
"yyyy-mm-dd"
"yyyy-mm"
"yyyy"
"yy-mm-dd"
"yy-mm"
"yy"
"hh:mm:ss.ms"
"hh:mm:ss"
"yyyy-mm-dd hh:mm:ss.ms"
"yyyy-mm-dd hh:mm:ss"
"yy-mm-dd hh:mm:ss.ms"
"yy-mm-dd hh:mm:ss"
```

#### Return Value

enuSpace의 시간값을 문자열로 반환합니다.

#### Remarks

\_\_int64 iTime 을 이용하여 FILETIME으로 적용되며, 적용된 FILETIME은 SYSTEMTIME으로 변환되어 문자열로 반환되어 디스플레이 된다.

FILETIME 구조체 : [https://msdn.microsoft.com/ko-kr/library/x3399a54.aspx](https://msdn.microsoft.com/ko-kr/library/x3399a54.aspx)

SYSTEMTIME 구조체 : [https://msdn.microsoft.com/ko-kr/library/windows/desktop/ms724950\(v=vs.85\).aspx](https://msdn.microsoft.com/ko-kr/library/windows/desktop/ms724950%28v=vs.85%29.aspx)

참조 : [GetTime\(\)](./enusscriptapi_gettime.md)

```cpp
__int64 iTime
FILETIME toTime;
toTime.dwLowDateTime = iTime;
toTime.dwHighDateTime = iTime >> 32;

SYSTEMTIME SystemTime;
FileTimeToSystemTime(&toTime, &SystemTime);
CString strLabel;
strLabel.Format(L"System Time : %04d-%02d-%02d %02d:%02d:%02d.%03d", SystemTime.wYear, SystemTime.wMonth, SystemTime.wDay, SystemTime.wHour, SystemTime.wMinute, SystemTime.wSecond, SystemTime.wMilliseconds);
```

입력 파라미터를 입력하지 않은경우에는 1601.01.01 00:00:10 형태로 디스플레이 되며, 특정 타입으로 지정하였을 경우 지정된 타입의 시간값으로 현시된다.

```lua
-- lua
GetDateTimeString("hh:mm:ss.ms")
```

```js
// javascript
GetDateTimeString("hh:mm:ss.ms");
```

#### 

#### Examples

```lua
-- lua
function _ontaskview()

    --TODO Add your lua script code here
    text = GetDateTimeString("hh:mm:ss.ms")
end
```

result display : 00:02:34.283

```js
// JavaScript
function _ontaskview()
{    
    //TODO Add your javascript code here
    textContent = GetDateTimeString("yyyy-mm-dd hh:mm:ss");
}
```

result display : 1601-01-01 00:02:34

