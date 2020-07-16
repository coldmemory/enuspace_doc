---
layout: default
title: GetTagValue
parent: Script API
---
# GetTagValue\("tagid"\)

GetTagValue\(\)

#### Parameters

tagid

데이터베이스의 tag id를 지정합니다. 변수를 지정할경우 문자열로 입력을 수행한다.

#### Return Value

value

요청한 값을 반환한다.

#### Remarks

GetTagValue\(\)함수는 enuSpace 에서는 데이터베이스 변수의 값을 가져올때 수행하는 함수이다. 또한, 웹에서는 RESTful API [getvalue](./enusrestfulapi_restful-getvalue.md) 함수를 통하여 연계되어 동작을 수행한다.

* [웹 연동 방법](/tutorial/web-interface.html)

#### Examples

```js
function _ontaskview()
{    
    //TODO Add your javascript code here
    var dd = GetTagValue("@CORE.display[0][0]");
    data[i][j] = dd*80;

    ID_TEXT.textContent = GetTagValue("@Presentation.rotate").toString();
}
```



