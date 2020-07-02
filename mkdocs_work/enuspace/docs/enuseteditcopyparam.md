# void enuSetEditCopyParam\(HVIEW pENUView\)

void enuSetEditCopyParam\(HVIEW pENUView\)

#### Parameters

* HVIEW pENUView

뷰의 핸들을 입력합니다.

#### Return Value

Type : NONE

#### Remarks

Copy Parameter 명령을 수행합니다. 선택 객체에 대하여 복사 루틴을 수행합니다. enuSetEditPasteParam\(\)함수를 통하여 파라미터 붙여넣기를 수행합니다.

#### Examples

```cpp
void CenuSpaceView::OnEditCopy()
{
    enuSetEditCopyParam(m_pENUView);
}
```



