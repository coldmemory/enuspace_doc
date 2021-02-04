---
layout: default
title: Create
parent: hdf5 functions
last_modified_date: now
---

# Create

hdf5file* hdf5.Create\(string filename\)

#### Parameters

string filename : HDF5의 파일명을 입력합니다.
* 이전에 파일이 존재하는 경우, 모든 내용을 지우고 새롭게 생성됩니다.

#### Return Value

hdf5file* filehandle : 생성된 HDF5의 파일 핸들을 반환합니다.

#### Remarks



#### Examples

```lua
function _onload()
	
	local hdfw = hdf5.Create("D:/git//GOGO_NEW12.h5")
	hdf5.SetDataset(hdfw,"/ROOT/data", pointer2, datatype2, "[19][19]")
	hdf5.SetDataset(hdfw,"/ROOT/SUB1/SUB2/data", pointer2, datatype2, "[19][19]")
	hdf5.Close(hdfw)end
end

```
