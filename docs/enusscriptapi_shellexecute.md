---
layout: default
title: ShellExecute
parent: Script API
---
# ShellExecute\(operation, file, param, directory\)

ShellExecute\(\)

#### Parameters

operation : 실행옵션을 입력합니다.

file : 파일이름을 입력합니다.

param : 파라미터를 입력합니다.

directory : 디렉토리를 입력합니다.

#### Return Value

value

#### Remarks

[reference msdn](https://msdn.microsoft.com/query/dev14.query?appId=Dev14IDEF1&l=EN-US&k=k%28SHELLAPI%2FShellExecute%29;k%28ShellExecute%29;k%28DevLang-C%2B%2B%29;k%28TargetOS-Windows%29&rd=true)

```lua
-- lua
ShellExecute("open", "notepad.exe", "note.txt", "")
```

```js
// javascript
-- lua
ShellExecute("open", "notepad.exe", "note.txt", "");
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    ShellExecute("open", "notepad.exe", "note.txt", "")
end
```

```js
// JavaScript
function _onmousedown()
{    
    ShellExecute("open", "notepad.exe", "note.txt", "");
}
```



