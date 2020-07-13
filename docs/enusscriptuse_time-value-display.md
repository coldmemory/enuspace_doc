---
layout: default
title: 시간정보 출력방법
parent: Script 사용방법
grand_parent: enuSpace Tutorial
---

# 시간정보 출력방법

---

#### Lua Script

```lua
--enuSpace의 Script API GetTime()함수를 이용한 simulation time(작업시간)을 텍스트 객체에 출력하는 방법(텍스트 객체의 이벤트안에서 적용)
local time = math.floor(GetTime()/10000000)
text = os.date("%x %X", time)                        -- 01/01/70 09:46:18

------------------------------------------------------------------------------------------------------------------------
--enuSpace의 Script API GetDateTimeString()함수를 이용한 simulation time(작업시간)을 텍스트 객체에 출력하는 방법(텍스트 객체의 이벤트안에서 적용)

--text = GetDateTimeString("number")                 -- 6678080000
--text = GetDateTimeString("yyyy-mm-dd")             -- 1601-01-01
--text = GetDateTimeString("yyyy-mm")                -- 1601-01
--text = GetDateTimeString("yyyy")                   -- 1601
--text = GetDateTimeString("yy-mm-dd")               -- 01-01-01
--text = GetDateTimeString("yy-mm")                  -- 01-01
--text = GetDateTimeString("yy")                     -- 01
--text = GetDateTimeString("hh:mm:ss.ms")            -- 00:01:02:279
--text = GetDateTimeString("hh:mm:ss")               -- 00:01:58
  text = GetDateTimeString("yyyy-mm-dd hh:mm:ss.ms") -- 1601-01-01 00:03:35.455
--text = GetDateTimeString("yyyy-mm-dd hh:mm:ss")    -- 1601-01-01 00:05:17
--text = GetDateTimeString("yy-mm-dd hh:mm:ss.ms")   -- 01-01-01 00:06:21.28
--text = GetDateTimeString("yy-mm-dd hh:mm:ss")      -- 01-01-01 00:08:42

--text = GetDateTimeString()                         -- 1601-01-01 01:07:02.715

------------------------------------------------------------------------------------------------------------------------
-- OS의 로컬 시간을 가져와서 텍스트 객체에 출력하는 방법
text = os.date("%y년 %m월 %d일 %H시 %M분 %S초")    -- 로컬시간 년,월,일,시,분,초 값 반환
```

#### JavaScript

```js
//enuSpace의 Script API GetTime()함수를 이용한 simulation time(작업시간)을 텍스트 객체에 출력하는 방법(텍스트 객체의 이벤트안에서 적용)
var time = GetTime();
textContent = new Date ( time / 10000 - 11644473600000 );               //Mon Jan 01 1601 09:01:11 GMT+0900 (대한민국 표준시)

//var time = GetTime();
//textContent = new Date(time/10000 - 11644473600000).toISOString();    //1601-01-01T00:01:18.761Z

------------------------------------------------------------------------------------------------------------------------
//enuSpace의 Script API GetDateTimeString()함수를 이용한 simulation time(작업시간)을 텍스트 객체에 출력하는 방법(텍스트 객체의 이벤트안에서 적용)

//textContent = GetDateTimeString("number");                     // 8729310000
//textContent = GetDateTimeString("yyyy-mm-dd");                 // 1601-01-01
//textContent = GetDateTimeString("yyyy-mm");                    // 1601-01
//textContent = GetDateTimeString("yyyy");                       // 1601
//textContent = GetDateTimeString("yy-mm-dd");                   // 01-01-01
//textContent = GetDateTimeString("yy-mm");                      // 01-01
//textContent = GetDateTimeString("yy");                         // 01
//textContent = GetDateTimeString("hh:mm:ss.ms");                // 00:01:02:279
//textContent = GetDateTimeString("hh:mm:ss");                   // 00:01:58
  textContent = GetDateTimeString("yyyy-mm-dd hh:mm:ss.ms");     // 1601-01-01 00:03:35.455
//textContent = GetDateTimeString("yyyy-mm-dd hh:mm:ss");        // 1601-01-01 00:05:17
//textContent = GetDateTimeString("yy-mm-dd hh:mm:ss.ms");       // 01-01-01 00:06:21.28
//textContent = GetDateTimeString("yy-mm-dd hh:mm:ss");          // 01-01-01 00:08:42

//textContent = GetDateTimeString();                             // 1601-01-01 01:04:55.328

------------------------------------------------------------------------------------------------------------------------
// OS의 로컬 시간을 가져와서 텍스트 객체에출력하는 방법
//https://msdn.microsoft.com/ko-kr/library/cd9w2te4(v=vs.94).aspx 참조
var dateString = "Today's date is: ";               // String 변수 초기화
var newDate = new Date();                           // Date 객체 생성

dateString += newDate.getFullYear() + "년 ";        // 로컬 시간을 사용하여 연도 값을 반환
dateString += (newDate.getMonth() + 1) + "월 ";     // 로컬 시간을 사용하여 월 값을 반환
dateString += newDate.getDate() + "일 ";            // 로컬 시간을 사용하여 일(주 기준) 값을 반환
dateString += newDate.getHours() + "시 ";           // 로컬 시간을 사용하여 시간 값을 반환
dateString += newDate.getMinutes() + "분 ";         // 로컬 시간을 사용하여 분 값을 반환
dateString += newDate.getSeconds() + "초 ";         // 로컬 시간을 사용하여 초 값을 반환
dateString += newDate.getMilliseconds() + "ms";     // 로컬 시간을 사용하여 밀리초 값을 반환

textContent = dateString;                           // Today's date is: 2018년 4월 17일 16시 4분 53초 307ms로 출력
```



