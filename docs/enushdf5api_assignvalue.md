---
layout: default
title: AssignValue
parent: hdf5 functions
last_modified_date: now
---

# Open

void hdf5.AssignValue\(void* target, void* source, int type, int size\)

#### Parameters

void* target : 값을 쓰고자 하는 데이터 포인터 핸들을 입력합니다.
void* source : 값을 전달하고자 하는 데이터 포인터 핸들을 입력합니다.
int datatype : 데이터의 타입을 입력합니다.
int datasize : 테이터의 사이즈를 입력합니다.

#### Return Value



#### Remarks



#### Examples

```lua
function _onload()

	local hdf = hdf5.Open("D:/git/GOGO.h5")
	local hdata = hdf5.GetDataset(hdf, "/ROOT/NORMALIZED_POWER_DISTRIBUTION")

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
end

```
