---
layout: default
title: Set3DCameraRotation
parent: Script API
last_modified_date: now
---
# Set3DCameraRotation\("window"\, rotation_x, rotation_y, rotation_z)

Set3DCameraRotation\("window"\, rotation_x, rotation_y, rotation_z)

#### Parameters

window

윈도우의 id를 설정합니다.

rotation_x

카메라의 x축 회전값을 설정합니다.

rotation_y

카메라의 y축 회전값을 설정합니다.

rotation_z

카메라의 z축 회전값을 설정합니다.

#### Return Value

none

#### Remarks

Set3DCameraRotation() 함수는 카메라의 회전값을 변경합니다.

#### Examples

```lua
-- lua
function _ontaskview()
	
	if (g_3d_animation) then
		g_rotation_z = g_rotation_z + 1
		Set3DCameraRotation("win3d",  g_rotation_x, g_rotation_y, g_rotation_z)
	end
end
```



