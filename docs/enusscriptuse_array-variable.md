---
layout: default
title: 배열변수의 활용방법
parent: Script 사용방법
grand_parent: enuSpace Tutorial
---

# 배열변수의 활용방법

---

배열변수를 스크립트에서 사용하는 방법은 다음과 같다.

```lua
function _ontaskview()
	
	--TODO Add your lua script code here
	local i
	local j
	for i=0, subdivision_x-1 do
		for j=0, subdivision_y-1 do
			data[i][j] = data[i][j] + 1
		end
	end
end
```

배열 변수 사용에 있어 주의해야할 점은 data\[i\]\[j\] 변수에 있어 i, j의 변수는 로컬 변수로 할당하여야 한다. 



wrong sample

```lua
function _ontaskview()
	
	--TODO Add your lua script code here
	ID_PIN.data[m_ilevel][j] -- wrong
	
	local i = m_ilevel
	local j = 0
	ID_PIN.data[i][j] -- OK
end
```



