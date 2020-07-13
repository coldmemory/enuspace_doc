---
layout: default
title: enuSetFindObjectCallBack
parent: Application API
---
# void enuSetFindObjectCallBack\(void fcbFindMessage\(HNODE, int, wchar\_t\*, wchar\_t\*\), wchar\_t\* pStrSearch, bool bMatchCase, bool bWholeWord\)

void enuSetFindObjectCallBack\(void fcbFindMessage\(HNODE, int, wchar\_t\*, wchar\_t\*\), wchar\_t\* pStrSearch, bool bMatchCase, bool bWholeWord\)

#### Parameters

* void fcbFindMessage\(HNODE, int, wchar\_t\*, wchar\_t\*\)

객체 검색후 전달받을 콜백함수를 지정합니다.

* wchar\_t\* pStrSearch

검색 문자열을 입력합니다.

* bool bMatchCase

대소문자 구분 조건을 입력합니다. \(true시 대소문자를 구분하지 않습니다. false시 대소문자를 구분합니다.\)

* bool bWholeWord

전체 문자열 일치조건을 입력합니다. \(true시 전체단어 일치조건입니다.\)

#### Return Value

Type : NONE

#### Remarks

#### Examples

```cpp
void FindMessageCallBack(HNODE pNode, int iFileType, wchar_t* pStrPageName, wchar_t* pStrSymbol)
{
    if (g_pDlgFind)
    {
        g_pDlgFind->AddSearchList(pNode, iFileType, pStrPageName, pStrSymbol);
    }
}

void CDlgFind::AddSearchList(HNODE pNODE, int iFileType, wchar_t* pStrPageName, wchar_t* pStrSymbol)
{
    int iCount = m_listOutput.GetItemCount();

    if (iFileType == DEF_FILE_PICTURE)
        m_listOutput.InsertItem(iCount, L"Picture");
    else if (iFileType == DEF_FILE_LOGIC)
        m_listOutput.InsertItem(iCount, L"Logic Symbol");
    else if (iFileType == DEF_FILE_HMI)
        m_listOutput.InsertItem(iCount, L"HMI Symbol");
    else if (iFileType == DEF_FILE_GLOBAL)
        m_listOutput.InsertItem(iCount, L"Global");
    else if (iFileType == DEF_FILE_RESOURCE)
        m_listOutput.InsertItem(iCount, L"Resource");
    else
    {
        AfxMessageBox(L"Missed file Type");
        return;
    }

    m_listOutput.SetItemText(iCount, 1, pStrPageName);

    CSvgNodeBase* pNode = (CSvgNodeBase*)pNODE;
    ///////////////////////////////////////////////////////////////////////////////////////
    if (pNode->Get_pg_type() == DEF_NODE_PG_ATTRIBUTE)
    {
        CSvgNodePgAttribute* pAttribute = (CSvgNodePgAttribute*)pNode;
        m_listOutput.SetItemText(iCount, 2, pAttribute->Get_type());
    }
    else
        m_listOutput.SetItemText(iCount, 2, pNode->Get_pg_nodename());
    ///////////////////////////////////////////////////////////////////////////////////////

    ///////////////////////////////////////////////////////////////////////////////////////
    if (pNode->Get_pg_type() == DEF_NODE_PG_ATTRIBUTE)
    {
        CSvgNodePgAttribute* pAttribute = (CSvgNodePgAttribute*)pNode;
        m_listOutput.SetItemText(iCount, 3, pAttribute->Get_variable());
    }
    else if (pNode->Get_pg_type() == DEF_NODE_PG_STRUCT)
    {
        CSvgNodePgStruct* pStruct = (CSvgNodePgStruct*)pNode;
        m_listOutput.SetItemText(iCount, 3, pStruct->Get_type());
    }
    else if (pNode->Get_pg_type() == DEF_NODE_STYLE_ITEM)
    {
        CSvgNodeResource* pRes = (CSvgNodeResource* )pNode;
        CString strText;
        strText.Format(L"%s.%s", pRes->Get_res_class(), pRes->Get_res_name());
        m_listOutput.SetItemText(iCount, 3, strText);
    }
    else
        m_listOutput.SetItemText(iCount, 3, pNode->Get_id());
    ///////////////////////////////////////////////////////////////////////////////////////

    m_listOutput.SetItemText(iCount, 4, pStrSymbol);

    if (pNode->Get_pg_type() == DEF_NODE_TEXT)
    {
        CSvgNodeText* pText = (CSvgNodeText*)pNode;
        CString strText = pText->Get_text();            // [v3.11]
        m_listOutput.SetItemText(iCount, 5, strText);            
    }        

    if (m_bFindEvent && iCount == 0)
    {
        SelectItem(iCount);
        m_bFindEvent = false;
    }
}

void FindEvent()
{
    enuSetFindObjectCallBack(FindMessageCallBack, L"ID_", false, false);
}
```



