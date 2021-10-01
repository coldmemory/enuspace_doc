---
layout: default
title: ExecuteProgram
parent: Script API
last_modified_date: now
---
# ExecuteProgram\(program, param\)

ExecuteProgram\(\)

#### Parameters

program : 실행하고자하는 프로그램의 이름을 입력합니다. 

param : 실행프로그램의 파라미터를 입력합니다.

#### Return Value

none

#### Remarks

외부 프로그램을 실행하는경우에 본 스크립트 함수를 활용합니다.

만약 상대패스로 입력해야 할 경우, [RelativePath\(\)](https://expnuni.github.io/enuspace_doc/docs/enusscriptapi_RelativePath/)함수를 통해 프로젝트 패스 기준으로 상대패스를 절대패스로 만듭니다.
```lua
-- lua
ExecuteProgram("notepad.exe" "note.txt")
```

```js
// javascript
ExecuteProgram("notepad.exe" "note.txt");
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()

    -- 절대패스 입력할 경우 예시
    ExecuteProgram("D:\\Development\\notepad.exe", "note.txt")

    -- 상대패스로 입력할 경우 예시
    -- 프로젝트 패스를 기준으로 상대패스 입력
    ExecuteProgram("..\\notepad.exe", "note.txt")

    --RelativePath를 통해 절대 패스를 만들어 입력할 경우
    local path = RelativePath("..\\note.txt")
    ExecuteProgram("..\\notepad.exe", path)




end

```

```js
// JavaScript
function _onmousedown()
{    
    // 절대패스 입력할 경우 예시
    ExecuteProgram("D:\\Development\\notepad.exe", "ote.txt");

    // 상대패스로 입력할 경우 예시
    // 프로젝트 패스를 기준으로 상대패스 입력
    ExecuteProgram("..\\notepad.exe", "note.txt");

    //RelativePath를 통해 절대 패스를 만들어 입력할 경우
    var path = RelativePath("..\\note.txt");
    ExecuteProgram("..\\notepad.exe", path);

}
```





