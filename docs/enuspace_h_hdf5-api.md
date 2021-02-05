---
layout: default
title: hdf5 functions
has_children: true
nav_order: h
last_modified_date: now
---

## enuSpace

## hdf5 functions

---

본 문서는 enuSpace for uranus(v5) version 기반으로 작성되었습니다.

enuSpace for uranus(v5) 버젼에서는 hdf5 데이터베이스 함수를 제공합니다.

hdf5.Open()
* hdf5 파일을 오픈합니다.

hdf5.Create()
* hdf5 파일을 생성합니다.

hdf5.Close()
* hdf5 파일을 닫습니다.

hdf5.GetDataset()
* 데이터셋을 불러옵니다.

hdf5.GetDatasetValue()
* 데이터셋의 데이터 주소, 타입, 사이즈를 가져옵니다.

hdf5.AssignValue()
* 메모리의 값을 전달합니다.

hdf5.GetRank()
* 데이터셋의 랭크정보를 가져옵니다.

hdf5.GetDimension()
* 특정 랭크의 배열 정보를 가져옵니다.

hdf5.GetValue()
* 데이터셋의 값을 가져옵니다.

hdf5.SetDataset()
* 데이터셋의 값을 저장합니다.



```lua
function _onload()
	----------------------------------------------------------------------------	
	local hdf = hdf5.Open("D:/git/GOGO.h5")
	local hdata = hdf5.GetDataset(hdf, "/ROOT/OUTPUT_FILE/BURNUPDATA[10]/NORMALIZED_POWER_DISTRIBUTION")

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

	----------------------------------------------------------------------------
	local h3ddata = hdf5.GetDataset(hdf, "/ROOT/OUTPUT_FILE/BURNUPDATA[20]/POWER_1D")
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

	local hmax = hdf5.GetDataset(hdf, "/ROOT/INPUT_FILE/CARD_CR/CR_MAX_NUM")
	local maxvalue = hdf5.GetValue(hmax, "")

	hdf5.Close(hdf)
	------------------------------------------------------------------------------
	local hdfw = hdf5.Create("D:/git/GOGO_NEW12.h5")
	hdf5.SetDataset(hdfw,"/ROOT/CORE", pointer2, datatype2, "[19][19]")
	hdf5.SetDataset(hdfw,"/ROOT/CORE2", pointer2, datatype2, "[19][19]")
	hdf5.Close(hdfw)

end

```




