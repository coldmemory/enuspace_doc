---
layout: default
title: SetValue
parent: Script API
---
# SetValue\(variable, value\)

SetValue\(\)

#### Parameters

variable : 변수명을 입력합니다.

value : 변수명에 해당하는 값을 입력합니다.

#### Return Value

none

#### Remarks

특정객체의 속성값을 설정하고나, 변수의 값을 설정할때 사용한다.

일반적으로 ID\_RECT.width = 0와 같은 표현식으로 사용하여도 된다.

* enuSpace 스튜디어오에서 파일 저장시 웹동작을 위한 변환 파일이 생성된다. 변환시 본 함수의 첫번째 파라미터는 문자열로 변경되어 웹 랜더러를 통한 인터페이스를 수행한다. SetValue\(ID\_RECT.width, 10\);  ---&gt; SetValue\("ID\_RECT.width", 10\);   
* 웹을 통하여 아래의 javascript 함수가 동작을 수행하는 경우에,  RESTful [setvalue\(\)](./enusrestfulapi_restful-setvalue.md) API를 통하여 연계되어 동작을 수행한다.  

```lua
-- lua

SetValue(ID_RECT.width, 10)
```

```js
// javascript

SetValue(ID_RECT.width, 10);    
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    SetValue(ID_RECT.width, 10)
end

function _onmousedown()
    SetValue(ID_RECT.width, ID_RECT2.width)
end
```

```js
// JavaScript
function _onmousedown()
{    
    SetValue(ID_RECT.width, 10);
}

function _onmousedown()
{    
    SetValue(ID_RECT.width, ID_RECT2.width);
}
```



