---
layout: default
title: GetValuePackage
parent: Script API
---
# GetValuePackage\(variable\)

GetValuePackage\(\)

#### Parameters

variable

배열 변수의 값을 취득하고자하는 변수의 이름을 입력한다. 배열정보는 미포함 \(예 "@CORE.display\[16\]\[16\]" 변수인 경우, "@CORE.display" 변수명만 기입\)

#### Return Value

value

요청한 배열 값을 반환한다.

#### Remarks

GetValue\_Package\(\)함수는 enuSpace 에서는 데이터베이스 배열변수의 값을 가져올때 수행하는 함수이다. 또한, 웹에서는 RESTful API [getvalue\_package](./enusrestfulapi_restful-getvalue-package.md) 함수를 통하여 연계되어 동작을 수행한다.

* enuSpace 스튜디어오에서 파일 저장시 웹동작을 위한 변환 파일이 생성된다. 변환시 본 함수의 첫번째 파라미터는 문자열로 변경되어 웹 랜더러를 통한 인터페이스를 수행한다. GetValuePackage\(@CORE.display\);  ---&gt; GetValuePackage\("@CORE.display"\);

* [웹 연동 방법](/tutorial/web-interface.html)

#### Examples

Terrain 객체의 subdivision의 개수를 16, 16으로 설정하였을 경우, data는 \[16\]\[16\]배열로 구성된다. 데이터베이스 Tag의 변수 @CORE.display\[16\]\[16\]으로 정의된 값을 data\[16\]\[16\]에 전달하여 Terrain객체를 가시화 한다.

```js
// JavaScript
function _onmousedown()
{    
    ID_TERRAIN.data = GetValuePackage(@CORE.display);
}
```



