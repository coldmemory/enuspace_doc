---
layout: default
title: Close
parent: hdf5 functions
last_modified_date: now
---

# Close

void hdf5.Close\(hdf5file* filehandle\)

#### Parameters

hdf5file* filehandle : HDF5의 파일 핸들을 입력합니다.
(Open, Create 함수를 통하여 생성된 핸들을 입력합니다.)
#### Return Value



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
