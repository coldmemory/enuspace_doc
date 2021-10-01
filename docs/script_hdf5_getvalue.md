---
layout: default
title: GetValue
parent: hdf5 functions
last_modified_date: now
---

# GetValue

value hdf5.GetValue\(hdf5dataset* datahandle, string dimension\)

#### Parameters

hdf5dataset* datahandle : 로드된 데이터 셋의 핸들을 입력합니다.

string dimension : 문자열로 취득하고자하는 배열 정보를 입력합니다. ex) “[2][2]”

#### Return Value

variable value : 각 타입의 형에 맞는 데이터를 반환합니다. 

#### Remarks



#### Examples

```lua
function _onload()
	local h3ddata = hdf5.GetDataset(hdf, "/ROOT/AXIALLY_AVERAGE_POWER_3D")
	local rank = hdf5.GetRank(h3ddata)
	if (rank == 1) then
		local dim = hdf5.GetDimension(h3ddata, rank-1)  -- zero based index
		pointer1, datatype1, datasize1 = hdf5.GetDatasetValue(h3ddata)
		local data_chart
		local add
		local value
		local i
		local array
		for i=0, dim-1 do
			value = hdf5.GetValue(h3ddata, string.format("[%d]", i))
			add = string.format("%f,%d", value, i)
			
			if (i==0)then
				data_chart = add
			else
				data_chart = string.format("%s %s", data_chart, add)
			end
		end
		ID_AXIAL_CHART.Series1.data = data_chart
	end
	hdf5.Close(h3ddata) 
end


```
