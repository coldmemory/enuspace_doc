---
layout: default
title: requestpage
parent: RESTful API
grand_parent: enuSpace Tutorial
---

# **RESTful API - requestpage**

---

서버에 대한 svg 픽쳐 파일 요청

## **Description**

---

enuSpace 서버측에 화면구성된 svg 파일을 웹 브라우져에서 현시하기 위하여 픽쳐파일을  요청하는 API

## **Request**

---

HTTP Method : POST

URI : [http://localhost:8080/requestpage?page=picture.svg](http://localhost:8080/requestpage?page=picture.svg)

Query Parameters

```
    page : picture file name
```

Example : ?page=picture.svg

Content-Type : text/html; charset=UTF-8

## **Response**

---

### **Body**

```json
svg file contents

or

{“RESULT”:”FAIL”,“RESULT_CODE”:”CODE_INVALID_PARAMETER”,“MESSAGE":”Invalid requestpage parameter”}
```

### **Body Example**

```xml
<?xml version="1.0" encoding="UTF-16"?>
<svg
    stroke="rgb(0,0,0)"
    stroke-opacity="1.00"
    stroke-width="1.00"
    transform="translate(0.00,0.00) rotate(0.00) scale(1.0000, 1.0000)"
    pg-xcenter="0.00"
    pg-ycenter="0.00"
    style="stroke:rgb(127,127,127);stroke-opacity:1.00;stroke-width:2.00;stroke-dasharray:1,1,1;background-color:rgb(61,61,59);"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    width="1920"
    height="1080"
>
    <rect
        id="ID_1ct3IF0"
        stroke="rgb(0,119,189)"
        stroke-opacity="0.00"
        stroke-width="2.00"
        transform="translate(-8.43,-4.31) rotate(0.00) scale(1.0000, 1.0000)"
        pg-xcenter="0.00"
        pg-ycenter="0.00"
        stroke-linecap="butt"
         stroke-linejoin="miter"
         x="0.00"
        y="-4.15"
        width="1942.11"
        height="1100.24"
        rx="0.00"
        ry="0.00"
        fill="url(#ID_1ct3IF0_GRAD)"
        fill-opacity="1.00"
    >
    </rect>
</svg>
```

### **Sample Call**

JavaScript

```js
function requestpage(var picture) 
{
    var xmlHttp = new XMLHttpRequest();
    var strUrl = "requestpage" ;
    var strParam= "page="+picture;  
    xmlHttp.onreadystatechange=function()
    {
        if (xmlHttp.readyState==4 && xmlHttp.status==200)
        {        
            var msg = xmlHttp.responseText;
            var arr = JSON.parse(msg);        
            if (arr.RESULT == "FAIL")
            {
                location = "http://localhost:8080/fail.html";
            }
            else
            {
                // data processing
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



