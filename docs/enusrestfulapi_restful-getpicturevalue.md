---
layout: default
title: getpicturevalue
parent: RESTful API
grand_parent: enuSpace Tutorial
---

# **RESTful API - getpicturevalue**

---

특정 픽쳐에서 사용된 변수의 현재 값을 요청

## **Description**

---

enuSpace 서버측에 특정 픽쳐에서 사용된 변수의 현재 값을 요청하는 API

## **Request**

---

HTTP Method : POST

URI : [http://localhost:8080/getpicturevalue?page=sample.svg](http://localhost:8080/getpicturevalue?page=sample.svg)

Query Parameters

```
    page : svg filename
```

Example : ?page=sample.svg

Content-Type : application/json; charset=UTF-8

## **Response**

---

### **Body**

json file format

### **Body Example**

```json
{

    "RESULT": "OK",

    "RESULT_CODE": "RESULT_OK",

    "MESSAGE": "GETPICTURE VALUE COMPLETE",

    "TIME_FORMAT": "SIM",

    "TIME": "2017-04-19 10:46:23.001",

    "VALUES": {  "VARIABLE":"ID_AND.input" , "VALUE":"10"  },{  "VARIABLE":"ID_AND.output" , "VALUE":"10" }

}
```

### **Sample Call**

JavaScript

```js
function getPictureValue(page)
{
    var xmlHttp = new XMLHttpRequest();
    var strUrl = "getpicturevalue" ;
    var strParam= "page="+page;

    xmlHttp.onreadystatechange=function()
    {
        if (xmlHttp.readyState==4 && xmlHttp.status==200)
        {
            var msg = xmlHttp.responseText;
            var arr;
            if(msg != "")
            {
                arr = JSON.parse(msg);
            }
    };

    xmlHttp.open("POST", strUrl, true);    
    xmlHttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded;charset=UTF-8");
    xmlHttp.setRequestHeader("Cache-Control","no-cache, must-revalidate");
    xmlHttp.setRequestHeader("Pragma","no-cache");
    xmlHttp.send(strParam);
}
```



