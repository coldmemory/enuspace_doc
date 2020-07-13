---
layout: default
title: ExecuteString
parent: Script API
---
# ExecuteString\(string, parent\)

ExecuteString\(\)

#### Parameters

string : 실행하고자 하는 문자열을 입력합니다. \(ex "ID_TEXT.UpdageLabel\(\)", or "ID\_TEXT.width = 100"\)_

parent : 호출시 적용되는 노드를 지정합니다. \(PARENT or empty\)

#### Return Value

none

#### Remarks

문자열을 이용하여 함수를 호출하거나, 특정변수의 값을 설정합니다.

PARENT 옵션은 최상단 루트 노드기준으로 실행 또는 자신의 부모노드에서 실행여부를 설정합니다.

* "PARENT"입력시 객체의 상위노드를 기준으로 실행합니다. 
* 공백을 입력하였을 경우에는 최상단 SVG노드 기준으로 실행합니다.
* "SVG" 입력시에는 특정 SVG 파일에 대하여 최상단 SVG노드 기준으로 실행합니다.



```lua
-- lua
ExecuteString("ID_RECT.width=10", "PARENT")    -- varaible set

ExecuteString("ID_RECT._onload()", "PARENT")    -- function call
```

```js
// javascript
ExecuteString("ID_RECT.width=10", "PARENT");    // varaible set

ExecuteString("ID_RECT._onload()", "PARENT");    // function call
```

SVG 옵션 

```lua
ExecuteString("_onload()", "SVG", "picture\\picture.svg")
```

```js
ExecuteString("_onload()", 'SVG', "picture\\picture.svg");
```

#### Examples

```lua
-- lua
function _onmousedown()
    ExecuteString("ID_RECT.width=10", "PARENT")    -- varaible set
end
```

```js
// JavaScript
function _onmousedown()
{    
    ExecuteString("ID_RECT.width=10", "PARENT");    // varaible set
}
```



