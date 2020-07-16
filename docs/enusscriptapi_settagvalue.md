---
layout: default
title: SetTagValue
parent: Script API
---
# SetTagValue\("tagid", value\)

SetTagValue\(\)

#### Parameters

tagid

데이터베이스의 tag id를 지정합니다. 변수명은 문자열로 입력을 수행한다.

value

데이터베이스의 설정하고자하는 값을 지정합니다.

#### Return Value

none

#### Remarks

SetTagValue\(\)함수는 enuSpace 에서는 데이터베이스 변수의 값을 설정하는 함수이다. 또한, 웹에서는 RESTful API [setvalue](./enusrestfulapi_restful-setvalue.md) 함수를 통하여 연계되어 동작을 수행한다.

* [웹 연동 방법](#)

#### Examples

```js
function _ontaskview()
{    
    //TODO Add your javascript code here
    var dd = GetTagValue("@CORE.display[0][0]");
    data[i][j] = dd*80;

    SetTagValue("@Presentation.rotate", 45);
}
```



