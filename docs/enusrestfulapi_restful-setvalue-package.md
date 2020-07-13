---
layout: default
title: setvalue_package
parent: RESTful API
grand_parent: enuSpace Tutorial
---

# **RESTful API - setvalue\_package**

---

특정변수 리스트에 대하여 값 설정 요청

## **Description**

---

enuSpace 서버측에 데이터베이스의 변수 리스트의 값을 설정 요청하는 API

## **Request**

---

HTTP Method : POST

URI : [http://localhost:8080/setvaue\_package?tagid\_list={“@043DFEDEFD](http://localhost:8080/setvaue_package?tagid_list={“@043DFEDEFD). A0”:”10”, “@043DFEDEFD. A1”:”20”}

Query Parameters

```
    tagid\_list : tagid list
```

Example : ?tagid\_list={“@043DFEDEFD. A0”:”10”, “@043DFEDEFD. A1”:”20”}

Content-Type : application/json; charset=UTF-8

## **Response**

---

### **Body**

json file format

### **Body Example**

```json
{

    "RESULT":"OK",

    "RESULT_CODE":"RESULT_OK",

    "MESSAGE":""

}
```

### **Sample Call**

JavaScript

```js
function setvalue_package()
{
    var tag_id1= document.getElementById("tagid1").value;
    var setvalue1 = document.getElementById("setvalue1").value;
    var tag_id2= document.getElementById("tagid2").value;
    var setvalue2 = document.getElementById("setvalue2").value;
    var xmlHttp = new XMLHttpRequest();
    var strUrl = "setvalue_package" ;
    var text = "{\"" +  tag_id1 +  "\":\""  + setvalue1 + "\",\""  +  tag_id2 +  "\":\""  + setvalue2 + "\"}";
    var strParam= "tagid_list="+text;  
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
        }
     };    

    xmlHttp.open("POST",strUrl,true);    
    xmlHttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded;charset=UTF-8");
    xmlHttp.setRequestHeader("Cache-Control","no-cache, must-revalidate");
    xmlHttp.setRequestHeader("Pragma","no-cache");
    xmlHttp.send(strParam);    
}
```



