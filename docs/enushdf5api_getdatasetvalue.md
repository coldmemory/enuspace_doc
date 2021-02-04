---
layout: default
title: GetDatasetValue
parent: hdf5 functions
last_modified_date: now
---

# GetDatasetValue

void*, int, int hdf5.GetDatasetValue\(hdf5dataset* datahandle\)

#### Parameters

hdf5dataset* datahandle : 로드된 데이터 셋의 핸들을 입력합니다.

#### Return Value

void* datapointer : 데이터의 포인터를 반환합니다.

int type : 데이터의 타입정보를 반환합니다.

int size : 데이터의 사이즈를 반환합니다.


#### Remarks



#### Examples

```lua
function _onload()
	
	local hdf = hdf5.Open("D:/git/ GOGO.h5")
	local hdata = hdf5.GetDataset(hdf, "/ROOT/POWER_DISTRIBUTION")

	local pointer1
	local datatype1
	local datasize1
	pointer1, datatype1, datasize1 = hdf5.GetDatasetValue(hdata)

	local pointer2
	local datatype2
	local datasize2
	pointer2, datatype2, datasize2 = GetVariablePointer(ID_CORE.data)
	
	if (datatype1 == datatype2 and datasize1 == datasize2) then
		hdf5.AssignValue(pointer2, pointer1, datatype2, datasize2)
	end

	hdf5.Close(hdf)
end

```
