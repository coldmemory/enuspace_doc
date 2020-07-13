---
layout: default
title: getvalue
parent: RESTful API
grand_parent: enuSpace Tutorial
---

# **RESTful API - getvalue**

---

특정변수에 대하여 값을 요청

## **Description**

---

enuSpace 서버측에 데이터베이스의 변수값을 요청하는 API

## **Request**

---

HTTP Method : POST

URI : [http://localhost:8080/getvalue?devicekey=043DFEDEFD&variable=A0](http://localhost:8080/getvalue?devicekey=043DFEDEFD&variable=A0)

URI : [http://localhost:8080/getvalue?tagid=@043DFEDEFD.A0](http://localhost:8080/getvalue?tagid=@043DFEDEFD.A0)

URI : [http://localhost:8080/getvalue?page=main.svg&variable=ID\_LOGIC.A0](http://localhost:8080/getvalue?page=main.svg&variable=ID_LOGIC.A0)

Query Parameters

```
    devicekey : device name

    variable : device variable

    or

    tagid : database tagid

    or

    page : picture name

    variable : variable name
```

`Example : ?devicekey=043DFEDEFD&variable=A0`

`Example : ?tagid=@043DFEDEFD.A0`

`Example : ?page=main.svg&variable=ID_LOGIC.A0`

`Content-Type : application/json; charset=UTF-8`

## **Response**

---

### **Body**

json file format

### **Body Example**

```json
{

    "RESULT":"OK",

    "RESULT_CODE":"RESULT_OK",

    "DEVICE_KEY":"043DFEDEFD",

    "VARIABLE":"A0",

    "TAGID":"043DFEDEFD.A0",

    "TYPE":"int",

    "VALUE":"50"

}
```

### **Sample Call**

---

JavaScript

```js
function getvalue()

{
    var devicekey= document.getElementById("devicekey").value;
    var variable = document.getElementById("variable").value;
    var xmlHttp = new XMLHttpRequest();
    var strUrl = "getvalue" ;
    var strParam= "devicekey="+devicekey + "&" + "variable="+ variable;  

    xmlHttp.onreadystatechange=function()
    {
        if (xmlHttp.readyState==4 && xmlHttp.status==200)
        {        
            var msg = xmlHttp.responseText;
            var arr = JSON.parse(msg);        
            if (arr.RESULT == "OK")
            {
                alert(arr.VALUE);
            }
            else
            {
                if (arr.RESULT_CODE == "CODE_VARIABLE_NOUT_FOUND" )
                {
                    alert(" 등록된 디바이스의 변수를  검색하지 못하였습니다.");
                }
                if (arr.RESULT_CODE == "CODE_UNKNOWN_DATATYPE" )
                {
                    alert("알수없는 데이터 타입니다..");
                }                
            }
        }
     };

    xmlHttp.open("POST",strUrl,true);    
    xmlHttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded;charset=UTF-8");
    xmlHttp.setRequestHeader("Cache-Control","no-cache, must-revalidate");
    xmlHttp.setRequestHeader("Pragma","no-cache");
    xmlHttp.send(strParam);    

}
```



