---
layout: default
title: getvalue_package
parent: RESTful API
grand_parent: enuSpace Tutorial
---

# **RESTful API - getvalue\_package**

---

특정 DB변수의 리스트에 대하여 값을 요청

## **Description**

---

enuSpace 서버측에 데이터베이스의 변수 리스트의 값을 요청하는 API

## **Request**

---

HTTP Method : POST

URI : [http://localhost:8080/getvaue\_package?tagid\_list=@CORE.display,@TEST.case1](http://localhost:8080/getvaue_package?tagid_list=@CORE.display,@TEST.case1)

Query Parameters

```
tagid_list : tagid1,tagid2
```

Example : ?tagid\_list=@CORE.display,@TEST.case1

Content-Type : application/json; charset=UTF-8

## **Response**

---

### **Body**

json file format

### **Body Example**

#### RESULT OK

```json
{  
     "RESULT":"OK" ,
     "RESULT_CODE":"RESULT_OK" ,
     "MESSAGE":"GETVALUE COMPLETE" ,
     "VALUES":
     [
          {
               "VALUE":"1.973848;1.317413;0.923313;1.808636;" ,
               "TAGID":"@CORE.display" ,
               "VARTYPE":"DOUBLE" ,
               "ARRAYSIZE":"4" ,
               "DIMENSION":"[2][2]"
          }
          {
               "VALUE":"2.000000;" ,
               "TAGID":"@TEST.case1[1]" ,
               "VARTYPE":"DOUBLE" ,
               "ARRAYSIZE":"2" ,
               "DIMENSION":"[2]"
          }
     ]
}
```

#### VARIABLE NOT FOUND

```json
{
    "RESULT":"FAIL" ,
    "RESULT_CODE":"CODE_VARIABLE_NOT_FOUND" ,
    "MESSAGE":"VARIABLE NOT FOUND" ,
    "VALUES":[]
}
```

#### **Sample Call**

---

JavaScript

```js
function GetValuePackage(id_list)
{
    var xmlHttp = new XMLHttpRequest();
    var strUrl = "getvalue_package" ;
    var strParam= "tagid_list="+id_list;

    xmlHttp.open("POST", strUrl, false);
    xmlHttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded;charset=UTF-8");
    xmlHttp.setRequestHeader("Cache-Control","no-cache, must-revalidate");
    xmlHttp.setRequestHeader("Pragma","no-cache");

    var msg = xmlHttp.responseText;
    var arr;
    if(msg != "")
    {
        arr = JSON.parse(msg);
    }

    if(arr != undefined)
    {
        if(arr.RESULT_CODE == "RESULT_OK")
        {
            for(var i = 0; i < arr.VALUES.length;i++)
            {
                if(arr.VALUES[i].TAGID.indexOf("[") == -1)
                {
                    console.log(arr.VALUES[i].TAGID);
                    console.log(arr.VALUES[i].VALUE);
                    console.log(arr.VALUES[i].VARTYPE);
                    console.log(arr.VALUES[i].ARRAYSIZE);
                    console.log(arr.VALUES[i].DIMENSION);
                }
                else
                {
                    console.log(arr.VALUES[i].TAGID);
                    console.log(arr.VALUES[i].VARTYPE);
                    console.log(arr.VALUES[i].ARRAYSIZE);
                    console.log(arr.VALUES[i].DIMENSION);
                    switch(arr.VALUES[i].VARTYPE)
                    {
                        case "INT":
                            console.log(parseInt(arr.VALUES[i].VALUE));
                            break;
                        case "FLOAT":
                        case "DOUBLE":
                            console.log(parseFloat(arr.VALUES[i].VALUE));
                            break;
                        case "STRING":
                            console.log(arr.VALUES[i].VALUE);
                            break;
                        case "BOOL":
                            console.log(Boolean(arr.VALUES[i].VALUE));
                            break;
                    }
                }
            }
        }
        else
        {
            if(arr.RESULT_CODE == "CODE_INVALID_ID")
            {
                console.log("getValue_Package: 찾는 ID가 없습니다.");
            }
        }
    }
}
```



