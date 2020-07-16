---
layout: default
title: GetValue
parent: Script API
---
# GetValue\(variable\)

GetValue\(\)

#### Parameters

variable

객체의 속성값, 변수의 값을 가져오고자하는 이름을 입력한다.

#### Return Value

value

요청한 값을 반환한다.

#### Remarks

아래의 코드는 동일한 결과를 출력한다. 명시적으로 GetValue\(\)함수를 활용하여 값을 취득할 수 있으며, 객체의 ID와 속성정보를 이용하여 값을 취득할 수 있다.

* enuSpace 스튜디어오에서 파일 저장시 웹동작을 위한 변환 파일이 생성된다. 변환시 본 함수의 첫번째 파라미터는 문자열로 변경되어 웹 랜더러를 통한 인터페이스를 수행한다. GetValue\(ID\_RECT.width\);  ---&gt; GetValue\("ID\_RECT.width"\);

* 웹을 통하여 아래의 javascript 함수가 동작을 수행하는 경우에는,  RESTful [getvalue\(\)](./enusrestfulapi_restful-getvalue.md) API를 통하여 연계되어 동작을 수행한다.

```lua
-- lua 

ID_TEXT.text = string.format("%f", GetValue(ID_RECT.width))
ID_TEXT.text = string.format("%f", ID_RECT.width)
```

```js
// javascript

ID_TEXT.textContent = GetValue(ID_RECT.width).toString();
ID_TEXT.textContent = ID_RECT.width.toString();
```

#### 

#### Examples

```lua
-- lua
function _onmousedown()
    ID_TEXT.text = string.format("%f", GetValue(ID_RECT.width))
end
```

```js
// JavaScript
function _onmousedown()
{    
    ID_TEXT.textContent = GetValue(ID_RECT.width).toString();
}
```

#### 



