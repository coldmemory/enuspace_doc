---
layout: default
title: enuGetLogicList
parent: Application API
---
# void\* enuGetLogicList\(\)

void\* enuGetLogicList\(\)

#### Parameters {#parameters}

NONE

#### Return Value {#return-value}

Type : void\*

CPtrList의 포인터를 반환합니다. 포인터의 정보는 LogicFileStruct 구조체 정보를 포함하고 있습니다.

#### Remarks {#remarks}

LOGIC영역의 파일리스트를 반환하는 함수입니다.

```cpp
struct LogicFileStruct
{
	wchar_t name[DEF_NAME_LEN];			// href
	wchar_t value[DEF_MAXTEXT_LEN];		// logic_library.svg
	bool bTask;					// TASK용 로직 심볼여부의 속성
	wchar_t taskname[DEF_MAXTEXT_LEN];		// TASK라이브러리 이름 설정

	CSvgHandler LogicHandler;			// LogicStruct의 구조체 정보를 담고있음.

	public:LogicFileStruct()				
	{
		wcscpy_s(name, L"");
		wcscpy_s(value, L"");
		bTask = false;
		wcscpy_s(taskname, L"logic");		// 기본값으로 logic으로 설정. (예약어) 외부라이브러리는 logic을 사용불가.
	}
};
```

#### Examples {#examples}

```cpp
CPtrList* pList = (CPtrList*)enuGetLogicList();

POSITION pos = pList->GetHeadPosition();
LogicFileStruct* pData = NULL;
while (pos)
{
    pData = (LogicFileStruct *) pList->GetAt(pos);

    wchar_t strData[DEF_MAXTEXT_LEN];
    wcscpy_s(strData, pData->value);        // logic_library.svg

    (LogicFileStruct *)pList->GetNext(pos);
}
```



