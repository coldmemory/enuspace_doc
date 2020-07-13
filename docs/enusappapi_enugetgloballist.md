---
layout: default
title: enuGetGlobalList
parent: Application API
---
# void\* enuGetGlobalList\(\)

void\* enuGetGlobalList\(\)

#### Parameters

NONE

#### Return Value

Type : void\*

CPtrList의 포인터를 반환합니다. 포인터의 정보는 GlobalFileStruct 구조체 정보를 포함하고 있습니다.

#### Remarks

```cpp
struct GlobalFileStruct
{
	wchar_t name[DEF_NAME_LEN];				// href
	wchar_t value[DEF_MAXTEXT_LEN];			// global.svg

	CSvgHandler GlobalHandler;
};
```

#### Examples

```cpp
CPtrList* pList = (CPtrList*)enuGetGlobalList();

pos = pList->GetHeadPosition();
GlobalFileStruct* pGloData = NULL;
while (pos)
{
	pGloData = (GlobalFileStruct  *) pList->GetAt(pos);
	if (enuGetModifyGlobal(pGloData->value))
	{
		strFileName.Format(L"%s", pGloData->GlobalHandler.GetSvgFileName());		
		AfxMessageBox(strFileName);
	}
	(GlobalFileStruct *)pList->GetNext(pos);			
}
```



