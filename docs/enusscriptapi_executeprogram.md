---
layout: default
title: ExecuteProgram
parent: Script API
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



```lua
-- lua
ExecuteProgram(L"notepad.exe" "note.txt")
```

```js
// javascript
ExecuteProgram(L"notepad.exe" "note.txt");
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    ExecuteProgram(L"notepad.exe" "note.txt")
end
```

```js
// JavaScript
function _onmousedown()
{    
    ExecuteProgram(L"notepad.exe" "note.txt");
}
```



