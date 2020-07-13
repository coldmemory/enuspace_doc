---
layout: default
title: gethistoricaldata
parent: RESTful API
grand_parent: enuSpace Tutorial
---

# **RESTful API - gethistoricaldata**

---

특정변수의 히스토리 데이터에 대하여 값을 요청

## **Description**

---

enuSpace 서버측에 데이터베이스의 변수 히스토리 값을 요청하는 API

## **Request**

---

HTTP Method : POST

URI : [http://localhost:8080/gethistoricaldata?tagid=@043DFEDEFD](http://localhost:8080/gethistoricaldata?tagid=@043DFEDEFD). A0&duration=300&endtime=0

Query Parameters

```
    tagid : database tagid

    duration : duration time

    endtime = 0      // 0-&gt;current time
```

Example : ?tagid=@043DFEDEFD. A0&duration=300&endtime=0

Content-Type : application/json; charset=UTF-8

## **Response**

---

### **Body**

json file format

TIME\_FORMAT : "SIM" or "SYS" -&gt; SIM : Simulation Time, SYS : System Time

### **Body Example**

```json
{

    "RESULT": "OK",

    "RESULT_CODE": "RESULT_OK",

    "MESSAGE": "GETHISTORICAL DATA COMPLETE",

    "TIME_FORMAT": "SIM",

    "TAGID": "@043DFEDEFD. A0",

     "VALUES": {  "TIME":"2017-04-19 10:46:23.001" , "VALUE":"84"  },{  "TIME":"2017-04-19 10:46:21.959" , "VALUE":"77"  }

}
```

### **Sample Call**

JavaScript

```js
function gethistoricaldata(tagid, duration, endtime, datalist)
{
    var xmlHttp = new XMLHttpRequest();
    var strUrl = "gethistoricaldata" ;
    var strParam= "tagid="+tagid+"&"+"duration="+duration+"&"+"endtime="+endtime;
    xmlHttp.open("POST", strUrl, false);    
    xmlHttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded;charset=UTF-8");
    xmlHttp.setRequestHeader("Cache-Control","no-cache, must-revalidate");
    xmlHttp.setRequestHeader("Pragma","no-cache");
    xmlHttp.send(strParam);    
    var msg = xmlHttp.responseText;
    var arr = JSON.parse(msg);
    if (arr.RESULT == "OK")
    {
        var values = arr.VALUES;
        if(values.length > 0)
        {
            if(arr.TIME_FORMAT == "SIM")
            {
                for(var i in values)
                {
                    var recive_time = new Date(values[i].TIME).valueOf();
                    var sub_time = new Date("1601-01-01 00:00:00.000").valueOf();
                    var x = recive_time - sub_time;
                    var y = parseFloat(Number(values[i].VALUE));
                    var point_data = new data_point(x, y);
                    datalist.unshift(point_data);
                }
            }
            else if(arr.TIME_FORMAT == "SYS")
            {
                for(var i in values)
                {
                    var x = new Date(values[i].TIME).valueOf();
                    var y = parseFloat(Number(values[i].VALUE));
                    var point_data = new data_point(x, y);
                    datalist.unshift(point_data);
                }
            }
        }
    }
    else
    {
        console.log("gethistoricaldata: 받아오기 에러");
    }
}
```



