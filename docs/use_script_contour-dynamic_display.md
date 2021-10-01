---
layout: default
title: Contour객체 동적 가시화 방법
parent: Script 사용방법
grand_parent: enuSpace Tutorial
last_modified_date: now
---

# Contour객체 동적 가시화 방법

---

Contour 객체를 스크립트에서 subdivision-x, subdivsion-y 값을 동적으로 변경후, Contour 객체의 가시화 메모리에 적재하는 방법에 대하여 설명한다.

---
아래의 코드는 2차원 데이터 [19][19] 배열의 정보값을 Contour 객체에 동적할당하여 가시화 하는 코드이다.

hdf5 파일로부터 2차원 데이터를 가져와 2차원 데이터의 rank 정보를 확인후 Contour객체의 subdivision-x, subdivison-y의 값을 설정한다. 
이때 SetAttribute() 함수를 통하여 subdivision-x의 값을 변경처리한다. 

(correct)
```lua
SetAttribute("ID_CORE.subdivision-x", string.format("%d", hdf5.GetDimension(hdata, 0) ))
SetAttribute("ID_CORE.subdivision-y", string.format("%d", hdf5.GetDimension(hdata, 1) ))
```

아래의 코드와 같이 직접 속성값에 할당하는 경우에는 스크립트가 컴파일 시점에 할당된 메모리에 값을 변경하게 된다. 

(wrong)  
```lua
ID_CORE.subdibision_x = hdf5.GetDimension(hdata, 0) 
ID_CORE.subdibision_y = hdf5.GetDimension(hdata, 1) 
```

SetAttribute() 함수를 이용하면, 해당 문자열에 대하여 명령어 처리 및 해당 명령어 따른 동적 메모리 할당을 수행하게 된다.

다음으로 Contour객체의 data 메모리값을 취득한다. 
Contour객체의 data 메모리 정보를 반환받기 위해서 GetVariablePointer_str() 함수를 이용한다. 앞에서 SetAttribute() 함수를 통하여 변경된 동적 메모리 정보를 반환받기 위해서 GetVariablePointer_str() 함수를 이용한다. 

만약 동적 할당이 아닌 컴파일 시점에 할당된 메모리값을 이용한다면, GetVariablePointer() 함수를 이용할 수 있다.


```lua
  pointer2, datatype2, datasize2 = GetVariablePointer(ID_CORE.data)   -- 동적 처리시 사용
  pointer2, datatype2, datasize2 = GetVariablePointer_str("ID_CORE.data")  -- 정적 처리시 사용
```


#### Lua Script (예시)

```lua
function _onload()
	----------------------------------------------------------------------------	
	local hdf = hdf5.Open("D:/GOGO.h5")
	local hdata = hdf5.GetDataset(hdf, "/ROOT/NORMALIZED_POWER_DISTRIBUTION")

	local pointer1
	local datatype1
	local datasize1
	pointer1, datatype1, datasize1 = hdf5.GetDatasetValue(hdata)

	local rank = hdf5.GetRank(hdata)
	if (rank == 2) then
		SetAttribute("ID_CORE.subdivision-x", string.format("%d", hdf5.GetDimension(hdata, 0) ))
		SetAttribute("ID_CORE.subdivision-y", string.format("%d", hdf5.GetDimension(hdata, 1) ))
	end

	local pointer2
	local datatype2
	local datasize2
	pointer2, datatype2, datasize2 = GetVariablePointer_str("ID_CORE.data")

	if (datatype1 == datatype2 and datasize1 == datasize2) then
		hdf5.AssignValue(pointer2, pointer1, datatype2, datasize2)
		PrintMessage("OK")
	end
end
```
