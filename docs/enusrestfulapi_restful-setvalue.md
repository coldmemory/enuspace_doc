---
layout: default
title: setvalue
parent: RESTful API
grand_parent: enuSpace Tutorial
---

# **RESTful API - setvalue**

---

특정변수에 대하여 값을 설정 요청

## **Description**

---

enuSpace 서버측에 데이터베이스의 변수값을 설정 요청하는 API

## **Request**

---

HTTP Method : POST

URI : [http://localhost:8080/setvalue?devicekey=043DFEDEFD&variable=A0&value=10](http://localhost:8080/setvalue?devicekey=043DFEDEFD&variable=A0&value=10)

URI : [http://localhost:8080/setvalue?tagid=@043DFEDEFD.A0&value=10](http://localhost:8080/setvalue?tagid=@043DFEDEFD.A0&value=10)

URI : [http://localhost:8080/setvalue?page=main.svg&variable=ID\_ARD.A0&value=10](http://localhost:8080/setvalue?page=main.svg&variable=ID_ARD.A0&value=10)

Query Parameters

```
    devicekey : device name

    variable : device variable

    value : set value

    or

    tagid : database tagid

    value : set value

    or

    page : picture file name

    variable : variable name

    value : set value
```

`Example : ?devicekey=043DFEDEFD&variable=A0&value=10`

`Example : ?tagid=@043DFEDEFD.A0&value=10`

`Example : ?page=main.svg&variable=ID_ARD.A0&value=10`

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

    "VALUE":"10"

}
```

### **Sample Call**

---

JavaScript

```js
function setvalue()

{
    var devicekey= document.getElementById("devicekey").value;
    var variable = document.getElementById("variable").value;
    var setvalue = document.getElementById("setvalue").value;
    var xmlHttp = new XMLHttpRequest();
    var strUrl = "setvalue" ;
    var strParam= "devicekey="+devicekey + "&" + "variable="+ variable + "&" + "value="+ setvalue;  
    xmlHttp.onreadystatechange=function()
    {
        if (xmlHttp.readyState==4 && xmlHttp.status==200)
        {        
            var msg = xmlHttp.responseText;
            var arr = JSON.parse(msg);        
            if (arr.RESULT == "OK")
            {
                location = "http://192.168.10.21:8080/main.html";
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



