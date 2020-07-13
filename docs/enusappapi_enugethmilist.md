---
layout: default
title: enuGetHmiList
parent: Application API
---
# void\* enuGetHmiList\(\)

void\* enuGetHmiList\(\)

#### Parameters {#parameters}

NONE

#### Return Value {#return-value}

Type : void\*

CPtrList의 포인터를 반환합니다. 포인터의 정보는 HmiFileStruct 구조체 정보를 포함하고 있습니다.

#### Remarks {#remarks}

HMI 영역의 파일리스트를 반환하는 함수입니다.

```cpp
struct HmiFileStruct
{
    wchar_t name[DEF_NAME_LEN];                // href
    wchar_t value[DEF_MAXTEXT_LEN];            // hmi_library.svg

    CSvgHandler HmiHandler;
};
```

#### Examples {#examples}

```cpp
CPtrList* pList = (CPtrList*)enuGetHmiList();

POSITION pos = pList->GetHeadPosition();
HmiFileStruct* pData = NULL;
while (pos)
{
    pData = (HmiFileStruct  *) pList->GetAt(pos);

    wchar_t strData[DEF_MAXTEXT_LEN];
    wcscpy_s(strData, pData->value);        // hmi_library.svg

    (HmiFileStruct *)pList->GetNext(pos);
}
```



