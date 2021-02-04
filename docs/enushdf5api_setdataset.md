---
layout: default
title: SetDataset
parent: hdf5 functions
last_modified_date: now
---

# SetDataset

int hdf5.SetDataset\(hdf5file* filehandle, string datapath, void* data, int type, int size\)

#### Parameters

hdf5file* filehandle: 오픈된 HDF5 파일 핸들을 입력합니다.
string datapath : 저장하고자 하는 패스 및 데이터셋 이름을 입력합니다.
void* data : 값을 쓰고자 하는 데이터 포인터 핸들을 입력합니다.
int type : 데이터의 타입을 입력합니다.
int size : 테이터의 사이즈를 입력합니다.

#### Return Value

int status : 함수의 성공 여부를 반환합니다. 

#### Remarks



#### Examples

```lua
function _onload()
	
	local hdfw = hdf5.Create("D:/git//GOGO_NEW12.h5")
	hdf5.SetDataset(hdfw,"/ROOT/CORE4/Core", pointer2, datatype2, "[19][19]")
	hdf5.Close(hdfw)

end

```
