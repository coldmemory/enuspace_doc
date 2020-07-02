# **enuSpace를 이용한 HMI 라이브러리 생성 및 적용 방법 \(2/2\)**

---

본 강좌에서는 다이나틱 데이터 디스플레이를 HMI Panel 라이브러리 제작하는 과정을 포함하고 있습니다.

[enuSpace를 이용한 HMI 라이브러리 생성 및 적용 방법\(1/2\)](//tutorial/hmi-library1.html)

강좌샘플 : [![](http://t1.daumcdn.net/tistory_admin/blogs/image/extension/zip.gif?_version_=5edd9eee8cdd891e2125a28405975fd20eb6ee50)lesson2.zip](http://enuspace.tistory.com/attachment/cfile3.uf@220E2C4458F997E7232C7F.zip)



enuSpace를 이용한 HMI 라이브러리 생성 및 적용 방법\(1/2\)절에 이어서 심볼의 사이즈 조정인자와 심볼의 색상, 라벨의 색상값을 설정할 수 있는 인터페이스를 추가합니다.

![](/assets/hmi_library2/5 newproject0.png)

Project Explorer에서 LABEL\_VALUE를 선택후 Properties창에서 Variable Window를 선택합니다. 다음과 같이 4개의 변수를 추가합니다.

![](/assets/hmi_library2/5 newproject1.png)

`double m_width;                // 라이브러리 폭 조정인자`

`double m_height;               // 라이브러리 높이 조정인자`

`wchar m_backcolor;             // 라이브러리 패널 색상 조정인자`

`wchar m_labelcolor;            // 라이브러리 라벨 색상 조정인자`

라이브러리에 추가된 멤버변수는 onload\(\) 함수를 통하여 연계를 수행합니다. onload\(\) 함수는 객체가 초기에 로드시 호출되며, 멤버변수의 속성을 변경 수행시 호출되는 함수입니다.

![](/assets/hmi_library2/5 newproject2.png)

추가된  코드 내용을 보면 아래와 같습니다.

```lua
function _onload()
{
    //TODO Add your javascript code here
    ID_PANEL.width = ID_PANEL.translate_x + m_width;
    ID_PANEL.height = ID_PANEL.translate_y + m_height;
    ID_PANEL.fill = m_backcolor;
    ID_LABEL.stroke = m_labelcolor;
    ID_LABEL.translate_x = ID_PANEL.width/2;
    ID_LABEL.translate_y = ID_PANEL.height - ID_PANEL.height/5;
}
```

ID\_PANEL의 폭값은 ID\_PANEL의 위치 이동값과 사용자가 업데이트한 또는 초기화된 값의 합으로 설정되며, 높이 또한 동일한 연산을 통하여 ID\_PANEL의 사이즈롤 조정합니다.

또한, 패널의 내부 색상값은 멤버변수 m\_backcolor값과 라벨의 폰트 색상은 m\_labelcolor의 값을 이용하여 연계됩니다.

패널의 사이즈 조정시 라벨의 위치값도 조정을 해주어야 합니다. 라벨의 속성중 text\_anchor의 값은 middle로 설정되어 있기 때문에 폭의 중간값으로 설정하고 높이는 패널 높이의 4/5위치에 배치시켰다.

코드를 Compile 버튼을 클릭후 이전장에서 추가한 Project Explorer의 Picture의 sample.svg 파일을 오픈한다. 오픈을 수행하면 이전에 생성된 객체의 속성을 유지하고 있기 때문에 재로딩을 수행한다. 단축키 F5 버튼을 누르면 픽쳐페이지를 재로딩을 수행합니다. 수정한 라이브러리의 속성이 나타납니다.

![](/assets/hmi_library2/5 newproject3.png)

sample.svg 픽쳐에 여러개의 LABEL\_VALUE객체를 추가하여 각 객체의 멤버변수의 값을 조정하여 테스트를 합니다. 색상값을 입력할 경우 rgb\(20,20,20\) 형태로 입력합니다.

![](/assets/hmi_library2/5 newproject4.png)

라이브러리의 속성값 변경에 따른 디스플레이

LABEL\_VALUE 라이브러리에 패널의 외곽선 색상, 폰트의 사이즈에 대한 인터페이스도 추가하여 완성도 높은  라이브러리를 작성해 보세요.

