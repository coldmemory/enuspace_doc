---
layout: default
title: GetDataset
parent: hdf5 functions
last_modified_date: now
---

# GetDataset

hdf5dataset*, type, size hdf5.GetDataset\(hdf5file* filehandle, string datapath\)

#### Parameters

hdf5file* filehandle : HDF5의 파일 핸들을 입력합니다.

string datapath : 로드하고자하는 data의 패스정보를 제공합니다.

#### Return Value

hdf5dataset* datahandle : 오픈된 HDF5의 파일 핸들을 반환합니다.

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
