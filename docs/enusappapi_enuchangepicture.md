---
layout: default
title: enuChangePicture
parent: Application API
---
# void enuChangePicture\(wchar\_t\* strWindow, wchar\_t\* strPicName\)

void enuChangePicture\(wchar\_t\* strWindow, wchar\_t\* strPicName\)

#### Parameters

* wchar\_t\* strWindow

화면 전환할 윈도우의 이름을 지정합니다.

* wchar\_t\* strPicName

정의된 윈도우에 화면전환하고자하는 픽쳐의 이름을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

enuSpace 편집기에서 윈도우 이름을 정의하지 않으면 윈도우 이름은 기본값 "window"로 정의됩니다.

픽쳐 파일이름은 "picture\filename.svg"형태로 picture 디렉토리를 포함하여야 합니다.

enuChangePicture\(\)함수는 로드된 픽쳐를 보여주거나, 로드되지 않은 픽쳐를 호출하였을 경우 로드를 수행하고 해당 윈도우에 픽쳐 파일을 보여줍니다.

#### Examples

```cpp
enuChangePicture(L"window", "picture\\picture.svg");        // 동기식 호출
```



