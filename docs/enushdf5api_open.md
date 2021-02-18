---
layout: default
title: Open
parent: hdf5 functions
last_modified_date: now
---

# Open

hdf5file* hdf5.Open\(string filename\)

#### Parameters

string filename : HDF5의 파일명을 입력합니다.

#### Return Value

hdf5file* filehandle : 오픈된 HDF5의 파일 핸들을 반환합니다.

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
		hdf5.AssignPointerArrayValue(pointer2, pointer1, datatype2, datasize2)
	end
end

```
