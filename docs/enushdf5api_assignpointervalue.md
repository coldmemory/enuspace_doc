---
layout: default
title: AssignPointerValue
parent: hdf5 functions
last_modified_date: now
---

# AssignPointerValue

void hdf5.AssignPointerValue\(void* target, int type, int offset, variable value\)

#### Parameters

* void* target : 값을 쓰고자 하는 데이터 포인터 핸들을 입력합니다.

* int type : 데이터의 타입을 입력합니다.

* int offset : 포인터의 옵셋정보를 입력합니다. 

* variable value : lua의 가변 변수값을 지정합니다.

#### Return Value

* NONE

#### Remarks

* 본 함수의 잘못된 사용은 프로그램 오류를 유발합니다. 정확한 메모리와 해당 메모리의 옵셋정보를 지정하여야 합니다.

#### Reference

* SCRIPT API : [AssignPointerArrayValue](/enuspace_doc/docs/enushdf5api_assignpointerarrayvalue/)

#### Examples

```lua
function UpdatePanel()
	
	local file = m_filename

	if file ~= nil and file ~= '' then
		local nodename = m_nodename
		local hdf = hdf5.Open(file)
		local dataname = string.format("/ROOT/OUTPUT_FILE/BURNUPDATA[%d]/%s", m_burnup, nodename)
		local hdata = hdf5.GetDataset(hdf, dataname)
	
		local rank = hdf5.GetRank(hdata)
		if (rank == 3) then
			local x_dim = hdf5.GetDimension(hdata, 0)
			local y_dim = hdf5.GetDimension(hdata, 1)
			local z_dim = hdf5.GetDimension(hdata, 2)

			local i
			local j
			local k
			local value

			local l = m_level
			local pointer2
			local datatype2
			local datasize2
			pointer2, datatype2, datasize2 = GetVariablePointer_str("ID_SEL.data")
			for i=0, x_dim-1 do
				for j=0, y_dim-1 do
					value = hdf5.GetValue(hdata, string.format("[%d][%d][%d]", i, j, l))
					hdf5.AssignPointerValue(pointer2, datatype2, y_dim*i+j, value) 
				end
			end
			
		end
		hdf5.Close(hdf)
	end
end

```
