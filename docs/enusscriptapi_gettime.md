---
layout: default
title: GetTime
parent: Script API
---
#### GetTime\(\)

GetTime\(\)

#### Parameters

none

#### Return Value

enuSpace의 시간값을 반환합니다.

#### Remarks

enuSpace 설정된 Simulation Time 또는 System Time에 해당하는 값을 반환합니다.

참조함수 [GetDateTimeString\(\)](./enusscriptapi_getdatetimestring.md)

```lua
-- lua
GetTime()
```

```js
// javascript
GetTime();
```

#### 

#### Examples

```lua
-- lua
function _ontaskview()

    --TODO Add your lua script code here
    text = string.format("%d", GetTime())
end
```

```js
// JavaScript
function _ontaskview()
{    
    //TODO Add your javascript code here
    textContent = GetTime().toString();
}
```

#### lua에서 time값을 이용하여 시간 현시 방법

sample1 , 참고 lua date and time : [https://www.lua.org/pil/22.1.html](https://www.lua.org/pil/22.1.html)

```lua
function _ontaskview()

    --TODO Add your lua script code here
    local time = math.floor(GetTime()/10000000)
    text = os.date("%x %X", time)        -- time의 value값이 0인 경우
end
```

result msg : 01/01/70 09:00:00

#### javascript에서 time 값을 이용하여 시간 현시방법

##### sample1

```js
function _ontaskview()
{    
    //TODO Add your javascript code here
    var time = GetTime();
    textContent = new Date ( time / 10000 - 11644473600000 );
}
```

result msg : Mon Jan 01 1601 09:02:34 GMT+0900 \(대한민국 표준시\)

##### sample2

```js
function _ontaskview()
{    
    //TODO Add your javascript code here
    var time = GetTime();
    textContent = new Date(time/10000 - 11644473600000).toISOString();
}
```

result msg : 1601-01-01T00:02:34.283Z

