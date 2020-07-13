---
layout: default
title: enuGetResourceList
parent: Application API
---
# void\* enuGetResourceList\(\)

void\* enuGetResourceList\(\)

#### Parameters

NONE

#### Return Value

Type : void\*

CPtrList의 포인터를 반환합니다. 포인터의 정보는 ResourceFileStruct 구조체 정보를 포함하고 있습니다.

#### Remarks

RESOURCE영역의 파일리스트를 반환하는 함수입니다.

```cpp
struct ResourceFileStruct
{
	wchar_t name[DEF_NAME_LEN];				// href
	wchar_t value[DEF_MAXTEXT_LEN];			// font-resource.enur

	CSvgHandler ResourceHandler;
};
```

#### Examples

```cpp
CPtrList* pList = (CPtrList*)enuGetResourceList();

pos = pList->GetHeadPosition();
ResourceFileStruct* pResData = NULL;
while (pos)
{
	pResData = (ResourceFileStruct  *)pList->GetAt(pos);

	// TO DO JOB
	if (enuGetModifyResource(pResData->value))
	{
		
	}

	(ResourceFileStruct *)pList->GetNext(pos);
}
```



