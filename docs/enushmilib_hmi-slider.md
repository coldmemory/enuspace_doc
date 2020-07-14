---
layout: default
title: Slider
parent: HMI 라이브러리 만들기
grand_parent: enuSpace Tutorial
---

# SVG와 JavaScript를 이용한 다이나믹 HMI 심볼 제작

---

### Slider SVG + JavaScript

version : enuSpace for saturn 2020

![](./assets/tutorial/slider.png)

시간정보를 이용한 슬라이더 샘플.

```svg
<?xml version="1.0" encoding="UTF-16"?>
<svg id="ID_1gH6sG34" stroke="rgb(0,119,189)" stroke-opacity="1" stroke-width="1" transform="translate(0,0) rotate(0) scale(1, 1)" pg-xcenter="0" pg-ycenter="0" style="stroke:rgb(127,127,127);stroke-opacity:1.00;stroke-width:2.00;stroke-dasharray:1,1,1;"
    enuspace-version="4.0.0.0"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    width="1920"
    height="1080"
>
    <defs id="ID_1gH2av1">
        <symbol id="SENSOR_BARCONTROL" type="node" stroke="rgb(0,0,0)" stroke-opacity="1" stroke-width="1" transform="translate(0,0) rotate(0) scale(1, 1)" pg-xcenter="0" pg-ycenter="0" onload="_onload()">
            <rect id="ID_1gH4EX0" stroke="rgb(126,126,126)" stroke-opacity="1" stroke-width="2" transform="translate(7.78358,5.82069) rotate(0) scale(1, 1)" pg-xcenter="0" pg-ycenter="0" stroke-linecap="butt" stroke-linejoin="miter" x="-7" y="-4.7811" width="662.909" height="85.4868" rx="10" ry="10" fill="rgb(65,65,65)" fill-opacity="1"></rect>
            <script id="ID_1cQWtJ" type="text/javascript">
<![CDATA[function _onload()
{    
    var dateString = "";  
    var endDate = new Date(m_max*1000 - 11644473600000 - 32400000);
    dateString += ("0" + endDate.getHours()).substr(-2) + ":";          
    dateString += ("0" + endDate.getMinutes()).substr(-2) + ":";         
    dateString += ("0" + endDate.getSeconds()).substr(-2) + ".";         
    dateString += endDate.getMilliseconds();     
    ID_LABEL_MAX.textContent =  dateString;

    dateString = "";  
    var newDate = new Date(m_min*1000 - 11644473600000 - 32400000);
    dateString += ("0" + newDate.getHours()).substr(-2) + ":";          
    dateString += ("0" + newDate.getMinutes()).substr(-2) + ":";         
    dateString += ("0" + newDate.getSeconds()).substr(-2) + ".";         
    dateString += newDate.getMilliseconds() ;     
    ID_LABEL_MIN.textContent =  dateString;

    Update();
}

function Update()
{    
    var dateString = "";  
    var valDate = new Date(m_posvalue*1000 - 11644473600000 - 32400000);
    dateString += ("0" + valDate.getHours()).substr(-2) + ":";           
    dateString += ("0" + valDate.getMinutes()).substr(-2) + ":";         
    dateString += ("0" + valDate.getSeconds()).substr(-2) + ".";         
    dateString += valDate.getMilliseconds() ;     
    ID_LABEL_VALUE.textContent =  dateString;

    var pos = (ID_BAR.width * (m_posvalue-m_min)) / (m_max - m_min);
    ID_POINT.translate_x = ID_BAR.translate_x +  pos;
    ID_PROGRESS.width = pos;
}

function SetRange(min, max)
{    
    //TODO Add your javascript code here
    m_min = min;
    m_max = max;
    _onload();
}


function SetPos(value)
{    
    //TODO Add your javascript code here
    m_posvalue = value;
    Update();
}]]>
            </script>
            <rect id="ID_BAR" stroke="rgb(0,174,238)" stroke-opacity="1" stroke-width="1" transform="translate(26.48,42) rotate(0) scale(1, 1)" pg-xcenter="0" pg-ycenter="0" stroke-linecap="butt" stroke-linejoin="miter" x="3.05176e-05" y="0" width="605.464" height="10" rx="5" ry="5" fill="rgb(0,174,238)" fill-opacity="1"></rect>
            <text id="ID_LABEL_MIN" stroke="rgb(255,191,40)" stroke-opacity="1" stroke-width="1" transform="translate(26.74,78.26) rotate(0) scale(1, 1)" pg-xcenter="0" pg-ycenter="0" stroke-linecap="butt" stroke-linejoin="miter" x="0.00" y="0.00" dx="0.00" dy="0.00" font-family="Arial" font-size="14.5" font-weight="bold" font-style="normal" text-anchor="start" baseline-shift="0" baseline-height="-16.673584" fill="rgb(0,0,0)" fill-opacity="1.00" pg-line-count="1" pg-oneline-height="16.673584" text-decoration="none">
00:00:00.0
            </text>
            <text id="ID_LABEL_MAX" stroke="rgb(255,191,40)" stroke-opacity="1" stroke-width="1" transform="translate(633.185,76.72) rotate(0) scale(1, 1)" pg-xcenter="0" pg-ycenter="0" stroke-linecap="butt" stroke-linejoin="miter" x="0.00" y="0.00" dx="0.00" dy="0.00" font-family="Arial" font-size="14.5" font-weight="bold" font-style="normal" text-anchor="end" baseline-shift="0" baseline-height="-16.673584" fill="rgb(0,0,0)" fill-opacity="1.00" pg-line-count="1" pg-oneline-height="16.673584" text-decoration="none">
00:01:40.0
            </text>
            <text id="ID_LABEL_VALUE" stroke="rgb(0,175,84)" stroke-opacity="1" stroke-width="1" transform="translate(26.43,31.0164) rotate(0) scale(1, 1)" pg-xcenter="0" pg-ycenter="0" stroke-linecap="butt" stroke-linejoin="miter" x="0.00" y="0.00" dx="0.00" dy="0.00" font-family="Arial" font-size="19.1" font-weight="bold" font-style="normal" text-anchor="start" baseline-shift="0" baseline-height="-21.963135" fill="rgb(0,0,0)" fill-opacity="1.00" pg-line-count="1" pg-oneline-height="21.963135" text-decoration="none">
00:00:30.0
            </text>
            <pg-attribute type="float" variable="m_min" initial="0"></pg-attribute>
            <pg-attribute type="float" variable="m_max" initial="100"></pg-attribute>
            <pg-attribute type="bool" variable="m_bMouseDown" initial="FALSE"></pg-attribute>
            <pg-attribute type="float" variable="m_posvalue" initial="30"></pg-attribute>
            <pg-attribute type="int" variable="m_mousedownx" initial="0"></pg-attribute>
            <pg-attribute type="int" variable="m_mousedowny" initial="0"></pg-attribute>
            <pg-attribute type="float" variable="m_oldvalue" initial="0"></pg-attribute>
            <rect id="ID_PROGRESS" stroke="rgb(255,20,24)" stroke-opacity="1" stroke-width="1" transform="translate(26.48,42) rotate(0) scale(1, 1)" pg-xcenter="0" pg-ycenter="0" stroke-linecap="butt" stroke-linejoin="miter" x="0" y="0" width="181.639" height="10" rx="5" ry="5" fill="rgb(255,191,40)" fill-opacity="1"></rect>
            <circle id="ID_POINT" stroke="rgb(0,36,95)" stroke-opacity="1" stroke-width="1" transform="translate(208.119,47) rotate(0) scale(1, 1)" pg-xcenter="-5.13" pg-ycenter="-6.16" stroke-linecap="butt" stroke-linejoin="miter" onmousedown="_onmousedown()" onmouseup="_onmouseup()" onmousemove="_onmousemove()" cx="0.00" cy="0.00" rx="10.00" ry="10.00" r="10.00" fill="rgb(0,111,189)" fill-opacity="1.00">
                <script id="ID_1gH3Bc" type="text/javascript">
<![CDATA[function _onmousemove()
{    
    //TODO Add your javascript code here
    if (m_bMouseDown)
    {
        var curx = GetCursorPosX();            

        var gap = curx - m_mousedownx;
        var zoom = GetZoomScale("window") ;
        var newgap = gap / zoom;

        var rate =  newgap/ID_BAR.width;
        var databand = m_max - m_min;
        var value = databand*rate;
        m_posvalue = value + m_oldvalue;

        if (m_posvalue > m_max) 
            m_posvalue = m_max;
        if (m_posvalue < m_min) 
            m_posvalue = m_min;

        var output = Math.floor(m_posvalue);
        var dateString = "";  
        var valDate = new Date(m_posvalue*1000 - 11644473600000 - 32400000);
        dateString += ("0" + valDate.getHours()).substr(-2) + ":";           
        dateString += ("0" + valDate.getMinutes()).substr(-2) + ":";        
        dateString += ("0" + valDate.getSeconds()).substr(-2) + ".";      
        dateString += valDate.getMilliseconds();     
        ID_LABEL_VALUE.textContent =  dateString;

        var pos = (ID_BAR.width * (m_posvalue-m_min)) / (m_max - m_min);

        translate_x = ID_BAR.translate_x +  pos;
        ID_PROGRESS.width = pos;
    }
}
function _onmouseup()
{    
    //TODO Add your javascript code here
        m_bMouseDown= false;
    fill = "rgb(0,119,189)";
}
function _onmousedown()
{    
    //TODO Add your javascript code here
        m_bMouseDown= true;
    fill = "rgb(255,191,40)";
    m_mousedownx = GetCursorPosX();
    m_oldvalue = m_posvalue;
}]]>
                </script>
            </circle>
        </symbol>
    </defs>
</svg>
```

### Slider SVG + Lua Script

version : enuSpace for saturn 2020

```svg
<?xml version="1.0" encoding="UTF-16"?>
<svg id="ID_1gHKeT1065" stroke="rgb(0,119,189)" stroke-opacity="1" stroke-width="1" transform="translate(0,0) rotate(0) scale(1, 1)" pg-xcenter="0" pg-ycenter="0" style="stroke:rgb(127,127,127);stroke-opacity:1.00;stroke-width:2.00;stroke-dasharray:1,1,1;"
	enuspace-version="4.0.0.0"
	xmlns="http://www.w3.org/2000/svg"
	xmlns:xlink="http://www.w3.org/1999/xlink"
	width="1920"
	height="1080"
>
	<defs id="ID_1gH2av1">
		<symbol id="SENSOR_BARCONTROL_L" type="node" stroke="rgb(0,0,0)" stroke-opacity="1" stroke-width="1" transform="translate(0,0) rotate(0) scale(1, 1)" pg-xcenter="0" pg-ycenter="0" onload="_onload()">
			<script id="ID_1gHKhF" type="text/lua">
<![CDATA[function _onload()

	local hour
	local minute
	local second

	hour = math.floor(m_min / 3600)
	minute = math.floor((m_min % 3600)/60)
	second = m_min%60
	ID_LABEL_MIN.text = string.format("%02d:%02d:%02d", hour, minute, second)

	hour = math.floor(m_max / 3600)
	minute = math.floor((m_max % 3600)/60)
	second = m_max%60
	ID_LABEL_MAX.text = string.format("%02d:%02d:%02d", hour, minute, second)

end
function Update()

	local hour
	local minute
	local second

	hour = math.floor(m_posvalue / 3600)
	minute = math.floor((m_posvalue % 3600)/60)
	second = m_posvalue%60
	ID_LABEL_VALUE.text = string.format("%02d:%02d:%02d", hour, minute, second)
	
	local pos = (ID_BAR.width * (m_posvalue-m_min)) / (m_max - m_min)
	ID_POINT.translate_x = ID_BAR.translate_x +  pos
	ID_PROGRESS.width = pos	
end
function SetPos(value)
	m_posvalue = value
	Update()
end
function SetRange(min, max)
	
	m_min = min
	m_max = max
	_onload()

end]]>
			</script>
			<rect id="ID_1gH4EX0" stroke="rgb(126,126,126)" stroke-opacity="1" stroke-width="2" transform="translate(7.78358,5.82069) rotate(0) scale(1, 1)" pg-xcenter="0" pg-ycenter="0" stroke-linecap="butt" stroke-linejoin="miter" x="-7" y="-4.7811" width="662.909" height="85.4868" rx="10" ry="10" fill="rgb(65,65,65)" fill-opacity="1"></rect>
			<rect id="ID_BAR" stroke="rgb(0,174,238)" stroke-opacity="1" stroke-width="1" transform="translate(26.48,42) rotate(0) scale(1, 1)" pg-xcenter="0" pg-ycenter="0" stroke-linecap="butt" stroke-linejoin="miter" x="3.05176e-05" y="0" width="605.464" height="10" rx="5" ry="5" fill="rgb(0,174,238)" fill-opacity="1"></rect>
			<text id="ID_LABEL_MIN" stroke="rgb(255,191,40)" stroke-opacity="1" stroke-width="1" transform="translate(26.74,78.26) rotate(0) scale(1, 1)" pg-xcenter="0" pg-ycenter="0" stroke-linecap="butt" stroke-linejoin="miter" x="0.00" y="0.00" dx="0.00" dy="0.00" font-family="Arial" font-size="14.5" font-weight="bold" font-style="normal" text-anchor="start" baseline-shift="0" baseline-height="-16.673584" fill="rgb(0,0,0)" fill-opacity="1.00" pg-line-count="1" pg-oneline-height="16.673584" text-decoration="none">
00:00:00
			</text>
			<text id="ID_LABEL_MAX" stroke="rgb(255,191,40)" stroke-opacity="1" stroke-width="1" transform="translate(633.185,76.72) rotate(0) scale(1, 1)" pg-xcenter="0" pg-ycenter="0" stroke-linecap="butt" stroke-linejoin="miter" x="0.00" y="0.00" dx="0.00" dy="0.00" font-family="Arial" font-size="14.5" font-weight="bold" font-style="normal" text-anchor="end" baseline-shift="0" baseline-height="-16.673584" fill="rgb(0,0,0)" fill-opacity="1.00" pg-line-count="1" pg-oneline-height="16.673584" text-decoration="none">
00:01:40
			</text>
			<text id="ID_LABEL_VALUE" stroke="rgb(0,175,84)" stroke-opacity="1" stroke-width="1" transform="translate(26.43,31.0164) rotate(0) scale(1, 1)" pg-xcenter="0" pg-ycenter="0" stroke-linecap="butt" stroke-linejoin="miter" x="0.00" y="0.00" dx="0.00" dy="0.00" font-family="Arial" font-size="19.1" font-weight="bold" font-style="normal" text-anchor="start" baseline-shift="0" baseline-height="-21.963135" fill="rgb(0,0,0)" fill-opacity="1.00" pg-line-count="1" pg-oneline-height="21.963135" text-decoration="none">
00:00:30.0
			</text>
			<pg-attribute type="float" variable="m_min" initial="0"></pg-attribute>
			<pg-attribute type="float" variable="m_max" initial="100"></pg-attribute>
			<pg-attribute type="bool" variable="m_bMouseDown" initial="FALSE"></pg-attribute>
			<pg-attribute type="float" variable="m_posvalue" initial="30"></pg-attribute>
			<pg-attribute type="int" variable="m_mousedownx" initial="0"></pg-attribute>
			<pg-attribute type="int" variable="m_mousedowny" initial="0"></pg-attribute>
			<pg-attribute type="float" variable="m_oldvalue" initial="0"></pg-attribute>
			<rect id="ID_PROGRESS" stroke="rgb(255,20,24)" stroke-opacity="1" stroke-width="1" transform="translate(26.48,42) rotate(0) scale(1, 1)" pg-xcenter="0" pg-ycenter="0" stroke-linecap="butt" stroke-linejoin="miter" x="0" y="0" width="181.639" height="10" rx="5" ry="5" fill="rgb(255,191,40)" fill-opacity="1"></rect>
			<circle id="ID_POINT" stroke="rgb(0,36,95)" stroke-opacity="1" stroke-width="1" transform="translate(208.119,47) rotate(0) scale(1, 1)" pg-xcenter="-5.13" pg-ycenter="-6.16" stroke-linecap="butt" stroke-linejoin="miter" onmousedown="_onmousedown()" onmouseup="_onmouseup()" onmousemove="_onmousemove()" cx="0.00" cy="0.00" rx="10.00" ry="10.00" r="10.00" fill="rgb(0,111,189)" fill-opacity="1.00">
				<script id="ID_1gHL0B" type="text/lua">
<![CDATA[function _onmousedown()
	
	m_bMouseDown= true

	local posx
	local posy
	posx, posy = GetCursorPos()
	m_mousedownx = posx
	m_mousedowny = posy

	fill = "rgb(255,191,40)"
	m_oldvalue = m_posvalue

end
function _onmouseup()
	
	m_bMouseDown= false
	fill = "rgb(0,119,189)"

end
function _onmousemove()
	
	--TODO Add your lua script code here
	if (m_bMouseDown) then
		local curx
		local cury
		curx, cury = GetCursorPos()			

		local gap = curx - m_mousedownx
		local zoom = GetZoomScale("window")
		local newgap = gap / zoom

		local rate =  newgap/ID_BAR.width
		local databand = m_max - m_min
		local value = databand*rate
		m_posvalue = value + m_oldvalue

		if (m_posvalue > m_max) then
			m_posvalue = m_max
		end
		if (m_posvalue < m_min) then
			m_posvalue = m_min
		end

		local output = math.floor(m_posvalue)
		local hour
		local minute
		local second
	
		hour = math.floor(output / 3600)
		minute = math.floor((output % 3600)/60)
		second = output%60
		ID_LABEL_VALUE.text = string.format("%02d:%02d:%02d", hour, minute, second)
	
		local pos = (ID_BAR.width * (m_posvalue-m_min)) / (m_max - m_min)

		translate_x = ID_BAR.translate_x +  pos
		ID_PROGRESS.width = pos
	end
end]]>
				</script>
			</circle>
		</symbol>
	</defs>
</svg>
```



