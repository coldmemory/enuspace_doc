---
layout: default
title: Application API
has_children: true
nav_order: i
---



## Project Interface

[ bool enuLoadProjectFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuLoadProjectFile.md)  
 [ HPROJECT enuCreateProject\(\)](./enusappapi_enuCreateProject.md)  
 [ void enuDestoryProject\(HPROJECT pProject\)](./enusappapi_enuDestoryProject.md)  
 [ bool enuSetActiveProject\(HPROJECT pHANDLE\)](./enusappapi_enuSetActiveProject.md)  
 [ HPROJECT enuGetActiveProject\(\)](./enusappapi_enuGetActiveProject.md)  
 [ void enuSetWidgetProject\(\)](./enusappapi_enuSetWidgetProject.md)  
 [ bool enuSaveProjectFile\(\)](./enusappapi_enuSaveProjectFile.md)  
 [ bool enuCloseProjectFile\(\)](./enusappapi_enuCloseProjectFile.md)  
 [ wchar\_t\* enuGetProjectName\(\)](./enusappapi_enuGetProjectName.md)  
 [ wchar\_t\* enuGetProjectFullName\(\)](./enusappapi_enuGetProjectFullName.md)  
 [ wchar\_t\* enuGetProjectPath\(\)](./enusappapi_enuGetProjectPath.md)  
 [ wchar\_t\* enuGetProjectType\(\)](./enusappapi_enuGetProjectType.md)  
 [ void enuSetProjectName\(wchar\_t\* projectname\)](./enusappapi_enuSetProjectName.md)  
 [ void enuSetModifyProject\(bool bFlag\)](./enusappapi_enuSetModifyProject.md)  
 [ bool enuGetModifyProject\(\)](./enusappapi_enuGetModifyProject.md)

## Operation Interface

## Script Operation Interface

[ void enuSetScriptOperationMode\(bool bFlag\)](./enusappapi_enuSetScriptOperationMode.md)  
 [ bool enuGetScriptOperationMode\(\)](./enusappapi_enuGetScriptOperationMode.md)  
 [ void enuSetHMIScriptUpdateTime\(int iMiliSecond\)](./enusappapi_enuSetHMIScriptUpdateTime.md)

## Edit Operation Interface

[ void enuSetEditOperationMode\(HVIEW pENUView, bool bFlag\)](./enusappapi_enuSetEditOperationMode.md)  
 [ bool enuGetEditOperationMode\(HVIEW pENUVie\)](./enusappapi_enuGetEditOperationMode.md)

## Mouse Interface

[ void enuSetLButtonDownCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](./enusappapi_enuSetLButtonDownCallBack.md)  
 [ void enuSetLButtonUpCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](./enusappapi_enuSetLButtonUpCallBack.md)  
 [ void enuSetRButtonDownCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](./enusappapi_enuSetRButtonDownCallBack.md)  
 [ void enuSetRButtonUpCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](./enusappapi_enuSetRButtonUpCallBack.md)  
 [ void enuSetMButtonDownCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](./enusappapi_enuSetMButtonDownCallBack.md)  
 [ void enuSetMButtonUpCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](./enusappapi_enuSetMButtonUpCallBack.md)  
 [ void enuSetMouseMoveCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](./enusappapi_enuSetMouseMoveCallBack.md)  
 [ void enuSetMouseWheelCallBack\(HVIEW pENUView, void functioncb\(float, float, float\) \)](./enusappapi_enuSetMouseWheelCallBack.md)  
 [ void enuSetLButtonDblClkCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](./enusappapi_enuSetLButtonDblClkCallBack.md)  
 [ void enuOnMouseWheel\(HVIEW pENUView, UINT nFlags, short zDelta, CPoint pt\)](./enusappapi_enuOnMouseWheel.md)  
 [ POINTF enuGetLocalPosition\(HVIEW pENUView, POINT point\)](./enusappapi_enuGetLocalPosition.md)  
 [ POINT enuGetCursorPos\(\)](./enusappapi_enuGetCursorPos.md)  
 [ void enuSetDefaultWheelControl\(HVIEW pENUView, bool bDefault\)](./enusappapi_enuSetDefaultWheelControl.md)

## View Interface

[ void enuActivateView\(HVIEW pENUView\)](./enusappapi_enuActivateView.md)  
 [ void enuDeactivateView\(HVIEW pENUView\)](./enusappapi_enuDeactivateView.md)  
 [ void enuSetRenderObjectPreReset\(HVIEW pENUView\)](./enusappapi_enuSetRenderObjectPreReset.md)  
 [ void enuSetRenderObjectReset\(HVIEW pENUView\)](./enusappapi_enuSetRenderObjectReset.md)

## File IO Interface

[ HSVG enuLoadSvgPageFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuLoadSvgPageFile.md)  
 [ HSVG enuLoadSvgHmiFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuLoadSvgHmiFile.md)  
 [ HSVG enuLoadSvgLogicFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuLoadSvgLogicFile.md)  
 [ HSVG enuLoadSvgResourceFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuLoadSvgResourceFile.md)  
 [ HSVG enuLoadSvgGlobalFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuLoadSvgGlobalFile.md)  
 [ HSVG enuNewSvgPageFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuNewSvgPageFile.md)  
 [ HSVG enuNewSvgHmiFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuNewSvgHmiFile.md)  
 [ HSVG enuNewSvgLogicFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuNewSvgLogicFile.md)  
 [ HSVG enuNewSvgGlobalFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuNewSvgGlobalFile.md)  
 [ HSVG enuNewSvgResourceFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuNewSvgResourceFile.md)  
 [ bool enuSaveAsSvgPageFile\(wchar\_t\* strTaget, wchar\_t\* strSource\)](./enusappapi_enuSaveAsSvgPageFile.md)  
 [ bool enuSaveAsSvgHmiFile\(wchar\_t\* strTaget, wchar\_t\* strSource\)](./enusappapi_enuSaveAsSvgHmiFile.md)  
 [ bool enuSaveAsSvgLogicFile\(wchar\_t\* strTaget, wchar\_t\* strSource\)](./enusappapi_enuSaveAsSvgLogicFile.md)  
 [ bool enuSaveAsSvgGlobalFile\(wchar\_t\* strTaget, wchar\_t\* strSource\)](./enusappapi_enuSaveAsSvgGlobalFile.md)  
 [ bool enuSaveAsSvgResourceFile\(wchar\_t\* strTaget, wchar\_t\* strSource\)](./enusappapi_enuSaveAsSvgResourceFile.md)  
 [ bool enuSaveSvgFile\(HSVG pSvgHandler, wchar\_t\* strFileName= L""\)](./enusappapi_enuSaveSvgFile.md)  
 [ bool enuDeleteSvgPageFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuDeleteSvgPageFile.md)  
 [ bool enuDeleteSvgHmiFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuDeleteSvgHmiFile.md)  
 [ bool enuDeleteSvgLogicFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuDeleteSvgLogicFile.md)  
 [ bool enuDeleteSvgResourceFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuDeleteSvgResourceFile.md)  
 [ bool enuDeleteSvgGlobalFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuDeleteSvgGlobalFile.md)  
 [ bool enuExportWebStyleSvg\(wchar\_t\* strTaget, wchar\_t\* strSource\)](./enusappapi_enuExportWebStyleSvg.md)  
 [ void enuSetAutoSaveMode\(bool bAuto\)](./enusappapi_enuSetAutoSaveMode.md)

## File handle Interface
[ HSVG enuGetPageClass\(wchar\_t\* pStrFileName\)](./enusappapi_enuGetPageClass.md)  
 [ HSVG enuGetSvgPageClass\(wchar\_t\* pStrFileName\)](./enusappapi_enuGetSvgPageClass.md)  
 [ HSVG enuGetLogicClass\(wchar\_t\* pStrFileName\)](./enusappapi_enuGetLogicClass.md)  
 [ HSVG enuGetHmiClass\(wchar\_t\* pStrFileName\)](./enusappapi_enuGetHmiClass.md)  
 [ HSVG enuGetGlobalClass\(wchar\_t\* pStrFileName\)](./enusappapi_enuGetGlobalClass.md)  
 [ HSVG enuGetResourceClass\(wchar\_t\* pStrFileName\)](./enusappapi_enuGetResourceClass.md)  
 [ void\* enuGetPageList\(\)](./enusappapi_enuGetPageList.md)  
 [ void\* enuGetHmiList\(\)](./enusappapi_enuGetHmiList.md)  
 [ void\* enuGetLogicList\(\)](./enusappapi_enuGetLogicList.md)  
 [ void\* enuGetGlobalList\(\)](./enusappapi_enuGetGlobalList.md)  
 [ void\* enuGetResourceList\(\)](./enusappapi_enuGetResourceList.md)  
 [ bool enuGetModifyPage\(wchar\_t\* pStrFilename\)](./enusappapi_enuGetModifyPage.md)  
 [ bool enuGetModifyHmi\(wchar\_t\* pStrFilename\)](./enusappapi_enuGetModifyHmi.md)  
 [ bool enuGetModifyLogic\(wchar\_t\* pStrFilename\)](./enusappapi_enuGetModifyLogic.md)  
 [ bool enuGetModifyGlobal\(wchar\_t\* pStrFilename\)](./enusappapi_enuGetModifyGlobal.md)  
 [ bool enuGetModifyResource\(wchar\_t\* pStrFilename\)](./enusappapi_enuGetModifyResource.md)
 [ bool enuSetPageProperty\(void\_t\* pPage, wchar\_t\* pAttribute, wchar\_t\* pValue\)](./enusappapi_enuSetPageProperty.md)
 [ bool enuSetLogicProperty\(HSVG pSvg, wchar\_t\* pAttribute, wchar\_t\* pValue\)](./enusappapi_enuSetLogicProperty.md)
 [ bool enuSetHmiProperty\(HSVG pSvg, wchar\_t\* pAttribute, wchar\_t\* pValue\)](./enusappapi_enuSetHmiProperty.md)
 [ bool enuSetGlobalProperty\(HSVG pSvg, wchar\_t\* pAttribute, wchar\_t\* pValue\)](./enusappapi_enuSetGlobalProperty.md) 
 [ bool enuSetResourceProperty\(HSVG pSvg, wchar\_t\* pAttribute, wchar\_t\* pValue\)](./enusappapi_enuSetResourceProperty.md)  
## Library Interface

[ bool enuLogicCreateSymbolNode\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)](./enusappapi_enuLogicCreateSymbolNode.md)  
 [ bool enuLogicCreateSymbolLink\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)](./enusappapi_enuLogicCreateSymbolLink.md)  
 [ bool enuHmiCreateSymbol\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)](./enusappapi_enuHmiCreateSymbol.md)  
 [ bool enuResourceCreateStyle\(wchar\_t\* pStrFilename, wchar\_t\* pStrStyle\)](./enusappapi_enuResourceCreateStyle.md)  
 [ bool enuDeleteLogicSymbol\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)](./enusappapi_enuDeleteLogicSymbol.md)  
 [ bool enuDeleteHmiSymbol\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)](./enusappapi_enuDeleteHmiSymbol.md)  
 [ wchar\_t\* enuLogicGetSymbolType\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)](./enusappapi_enuLogicGetSymbolType.md)  
 [ void\* enuGetHmiSymbolList\(wchar\_t\* pStrFilename\)](./enusappapi_enuGetHmiSymbolList.md)  
 [ void\* enuGetLogicSymbolList\(wchar\_t\* pStrFilename\)](./enusappapi_enuGetLogicSymbolList.md)

## Global Interface

[ bool enuAddGlobalStruct\(wchar\_t\* pStrFileName, wchar\_t\* pStrStructName, CPtrList\* pItem\)](./enusappapi_enuAddGlobalStruct.md)  
 [ void\* enuGetGlobalPgStructList\(wchar\_t\* pStrFileName\)](./enusappapi_enuGetGlobalPgStructList.md)  
 [ void\* enuGetGlobalVariableList\(wchar\_t\* pStrFileName\)](./enusappapi_enuGetGlobalVariableList.md)  
 [ void\* enuGetGlobalPgAttributeList\(wchar\_t\* pStrFileName, wchar\_t\* pStrStructName\)](./enusappapi_enuGetGlobalPgAttributeList.md)  
 [ HNODE enuGetGlobalVariableNode\(wchar\_t\* pStrVariable\)](./enusappapi_enuGetGlobalVariableNode.md)  
 [ bool enuAddGlobalVariable\(wchar\_t\* pStrFileName, wchar\_t\* pStrType, wchar\_t\* strVariable, wchar\_t\* strInitValue=L"", wchar\_t\* strDescription=L""\)](./enusappapi_enuAddGlobalVariable.md)  
 [ bool enuDeleteGlobalVariable\(wchar\_t\* pStrFileName, wchar\_t\* strVariable\)](./enusappapi_enuDeleteGlobalVariable.md)  
 [ bool enuModifyGlobalVariable\(wchar\_t\* pStrFileName, wchar\_t\* strVariable, wchar\_t\* strNewType, wchar\_t\* strNewVariable, wchar\_t\* strNewDescription\)](./enusappapi_enuModifyGlobalVariable.md)  
 [ bool enuDeleteGlobalStruct\(wchar\_t\* pStrFileName, wchar\_t\* strStruct\)](./enusappapi_enuDeleteGlobalStruct.md)  
 [ bool enuModifyGlobalStruct\(wchar\_t\* pStrFileName, wchar\_t\* strStruct, wchar\_t\* strNewStruct, CPtrList\* pItem\)](./enusappapi_enuModifyGlobalStruct.md)  
 [ void enuReloadPicture\(HVIEW pENUView\)](./enusappapi_enuReloadPicture.md)  
 [ bool enuIsModifyPage\(HVIEW pENUView\)](./enusappapi_enuIsModifyPage.md)

## Window Interface

[ void enuSetZoomScale\(HVIEW pENUView, float fPercent\)](./enusappapi_enuSetZoomScale.md)  
 [ float enuGetZoomScale\(HVIEW pENUView\)](./enusappapi_enuGetZoomScale.md)  
 [ float enuGetCanvasWidth\(HVIEW pENUView\)](./enusappapi_enuGetCanvasWidth.md)  
 [ float enuGetCanvasHeight\(HVIEW pENUView\)](./enusappapi_enuGetCanvasHeight.md)  
 [ void enuSetCanvasSize\(HVIEW pENUView, float cx, float cy\)](./enusappapi_enuSetCanvasSize.md)  
 [ void enuSetMoveCanvas\(HVIEW pENUView, float transx, float transy\)](./enusappapi_enuSetMoveCanvas.md)  
 [ void enuGetMoveCanvas\(HVIEW pENUView, float\* transx, float\* transy\)](./enusappapi_enuGetMoveCanvas.md)  
 [ void enuSetCanvasColor\(HVIEW pENUView, byte iR, byte iG, byte iB\)](./enusappapi_enuSetCanvasColor.md)  
 [ void enuSetWindowColor\(HVIEW pENUView, byte iR, byte iG, byte iB\)](./enusappapi_enuSetWindowColor.md)  
 [ bool enuSelConnectionPin\(HVIEW pENUView, wchar\_t\* strPicture, wchar\_t\* strSymbol\)](./enusappapi_enuSelConnectionPin.md)  
 [ bool enuIsEnableConnectionPin\(HVIEW pENUView\)](./enusappapi_enuIsEnableConnectionPin.md)

## Symbol Interface

[ float enuGetSymbolWidth\(HVIEW pENUView, wchar\_t\* strSymbol\)](./enusappapi_enuGetSymbolWidth.md)  
 [ float enuGetSymbolHeight\(HVIEW pENUView, wchar\_t\* strSymbol\)](./enusappapi_enuGetSymbolHeight.md)  
 [ void enuSetSymbolSize\(HVIEW pENUView,  wchar\_t\* strSymbol, float fWidth, float fHeight\)](./enusappapi_enuSetSymbolSize.md)

## Edit Interface

[ void enuSetSelectToolBar\(int iSel\)](./enusappapi_enuSetSelectToolBar.md)  
 [ void enuSetCallBackSelectToolBar\(void fcbSelectToolBar\(int\)\)](./enusappapi_enuSetCallBackSelectToolBar.md)  
 [ void enuSetCallBackSelectEvent\(void fcbSelectObject\(CPtrList\*, void\*\)\)](./enusappapi_enuSetCallBackSelectEvent.md)  
 [ void enuSetCallBackDebugMessage\(void fcbDebugMessage\(wchar\_t\*\)\)](./enusappapi_enuSetCallBackDebugMessage.md)  
 [ bool enuIsEnablePaste\(\)](./enusappapi_enuIsEnablePaste.md)  
 [ bool enuIsSelectObject\(HVIEW pENUView\)](./enusappapi_enuIsEnablePaste.md)  
 [ void enuSetSelectFontname\(HVIEW pENUView,  wchar\_t\* strFontName\)](./enusappapi_enuSetSelectFontname.md)  
 [ void enuSetSelectFontsize\(HVIEW pENUView,  float fSize\)](./enusappapi_enuSetSelectFontsize.md)  
 [ void enuSetSelectFontcolor\(HVIEW pENUView,  wchar\_t\* strFontColor\)](./enusappapi_enuSetSelectFontcolor.md)  
 [ void enuSetSelectFontIncrease\(HVIEW pENUView\)](./enusappapi_enuSetSelectFontIncrease.md)  
 [ void enuSetSelectFontDecrease\(HVIEW pENUView\)](./enusappapi_enuSetSelectFontDecrease.md)  
 [ void enuSetSelectFontBold\(HVIEW pENUView, bool bFlag\)](./enusappapi_enuSetSelectFontBold.md)  
 [ void enuSetSelectFontItalic\(HVIEW pENUView, bool bFlag\)](./enusappapi_enuSetSelectFontItalic.md)  
 [ void enuSetSelectFontUnderline\(HVIEW pENUView, bool bFlag\)](./enusappapi_enuSetSelectFontUnderline.md)  
 [ void enuSetSelectFontStrikethough\(HVIEW pENUView, bool bFlag\)](./enusappapi_enuSetSelectFontStrikethough.md)  
 [ void enuSetSelectFontSubscript\(HVIEW pENUView, bool bFlag\)](./enusappapi_enuSetSelectFontSubscript.md)  
 [ void enuSetSelectFontSuperscript\(HVIEW pENUView, bool bFlag\)](./enusappapi_enuSetSelectFontSuperscript.md)  
 [ void enuSetSelectFontHilight\(HVIEW pENUView, bool bFlag\)](./enusappapi_enuSetSelectFontHilight.md)  
 [ bool enuIsSelectFontBold\(HVIEW pENUView\)](./enusappapi_enuIsSelectFontBold.md)  
 [ bool enuIsSelectFontItalic\(HVIEW pENUView\)](./enusappapi_enuIsSelectFontItalic.md)  
 [ bool enuIsSelectFontUnderline\(HVIEW pENUView\)](./enusappapi_enuIsSelectFontUnderline.md)  
 [ bool enuIsSelectFontStrikethough\(HVIEW pENUView\)](./enusappapi_enuIsSelectFontStrikethough.md)  
 [ bool enuIsSelectFontSubscript\(HVIEW pENUView\)](./enusappapi_enuIsSelectFontSubscript.md)  
 [ bool enuIsSelectFontSuperscript\(HVIEW pENUView\)](./enusappapi_enuIsSelectFontSuperscript.md)  
 [ void enuSetSelectFillcolor\(HVIEW pENUView,  wchar\_t\* strColor\)](./enusappapi_enuSetSelectFillcolor.md)  
 [ void enuSetSelectFillOpacity\(HVIEW pENUView, wchar\_t\* strOpacity\)](./enusappapi_enuSetSelectFillOpacity.md)  
 [ void enuSetSelectLinecolor\(HVIEW pENUView,  wchar\_t\* strColor\)](./enusappapi_enuSetSelectLinecolor.md)  
 [ void enuSetSelectLineOpacity\(HVIEW pENUView, wchar\_t\* strOpacity\)](./enusappapi_enuSetSelectLineOpacity.md)  
 [ void enuSetSelectLineWidth\(HVIEW pENUView, float fWidth\)](./enusappapi_enuSetSelectLineWidth.md)  
 [ void enuSetSelectLineDashes\(HVIEW pENUView, wchar\_t\* strDashes\)](./enusappapi_enuSetSelectLineDashes.md)  
 [ void enuSetSelectAlign\(HVIEW pENUView, int iType\)](./enusappapi_enuSetSelectAlign.md)  
 [ void enuSetSelectRotation\(HVIEW pENUView, float fAngle\)](./enusappapi_enuSetSelectRotation.md)  
 [ void enuSetSelectFlip\(HVIEW pENUView, int iType\)](./enusappapi_enuSetSelectFlip.md)  
 [ HNODE enuGetSelectSingleObject\(HVIEW pENUView\)](./enusappapi_enuGetSelectSingleObject.md)  
 [ void enuSetSelectAll\(HVIEW pENUView\)](./enusappapi_enuSetSelectAll.md)  
 [ bool enuSetSelectObject\(HVIEW pENUView, wchar\_t\* strSelectID\)](./enusappapi_enuSetSelectObject.md)  
 [ void enuSetFindObjectCallBack\(void fcbFindMessage\(HNODE, int, wchar\_t\*, wchar\_t\*\), wchar\_t\* pStrSearch, bool bMatchCase, bool bWholeWord\)](./enusappapi_enuSetFindObjectCallBack.md)  
 [ wchar\_t\* enuGetPrevPageName\(wchar\_t\* pStrFileName\)](./enusappapi_enuGetPrevPageName.md)  
 [ wchar\_t\* enuGetNextPageName\(wchar\_t\* pStrFileName\)](./enusappapi_enuGetNextPageName.md)  
 [ void enuSetSelectZOrder\(HVIEW pENUView, int iType\)](./enusappapi_enuSetSelectZOrder.md)  
 [ void enuSetSelectGroup\(HVIEW pENUView\)](./enusappapi_enuSetSelectGroup.md)  
 [ void enuSetSelectUnGroup\(HVIEW pENUView\)](./enusappapi_enuSetSelectUnGroup.md)  
 [ void enuMoveObjectUp\(HVIEW pENUView\)](./enusappapi_enuMoveObjectUp.md)  
 [ void enuMoveObjectDown\(HVIEW pENUView\)](./enusappapi_enuMoveObjectDown.md)  
 [ void enuMoveObjectLeft\(HVIEW pENUView\)](./enusappapi_enuMoveObjectLeft.md)  
 [ void enuMoveObjectRight\(HVIEW pENUView\)](./enusappapi_enuMoveObjectRight.md)  
 [ void enuSetEditCopy\(HVIEW pENUView\)](./enusappapi_enuSetEditCopy.md)  
 [ void enuSetEditCut\(HVIEW pENUView\)](./enusappapi_enuSetEditCut.md)  
 [ void enuSetEditPaste\(HVIEW pENUView\)](./enusappapi_enuSetEditPaste.md)  
 [ void enuSetEditLock\(HVIEW pENUView\)](./enusappapi_enuSetEditLock.md)  
 [ void enuSetEditUnLock\(HVIEW pENUView\)](./enusappapi_enuSetEditUnLock.md)  
 [ void enuSetEditUndo\(HVIEW pENUView\)](./enusappapi_enuSetEditUndo.md)  
 [ void enuSetEditRedo\(HVIEW pENUView\)](./enusappapi_enuSetEditRedo.md)  
 [ bool enuIsEditUndo\(HVIEW pENUView\)](./enusappapi_enuIsEditUndo.md)  
 [ bool enuIsEditRedo\(HVIEW pENUView\)](./enusappapi_enuIsEditRedo.md)

## Runtime Interface

[ void enuSetCallBackAddTable\( void fcbAddTable\(HNODE\) \)](./enusappapi_enuSetCallBackAddTable.md)  
 [ HSVG enuNewSvgExternalPageFile\(wchar\_t\* pFileName\)](./enusappapi_enuNewSvgExternalPageFile.md)  
 [ HSVG enuLoadSvgExternalPageFile\(wchar\_t\* pFileName\)](./enusappapi_enuLoadSvgExternalPageFile.md)  
 [ bool enuDeleteSvgExternalPageFile\(wchar\_t\* pFileName\)](./enusappapi_enuDeleteSvgExternalPageFile.md)  
 [ bool enuSetSvgExternalPageView\(HVIEW pENUView, HSVG pSvg\)](./enusappapi_enuSetSvgExternalPageView.md)  
 [ bool enuShowRuntimeView\(HWND hWnd\)](./enusappapi_enuShowRuntimeView.md)  
 [ void enuDestoryRuntimeView\(\)](./enusappapi_enuDestoryRuntimeView.md)  
 [ bool enuIsRuntimeView\(\)](./enusappapi_enuIsRuntimeView.md)  
 [ void enuChangePicture\(wchar\_t\* strWindow, wchar\_t\* strPicName\)](./enusappapi_enuChangePicture.md)  
 [ void enuChangePictureAsync\(wchar\_t\* strWindow, wchar\_t\* strPicName\)](./enusappapi_enuChangePictureAsync.md)  
 [ void enuSaveImageToFile\(HVIEW pENUView, wchar\_t\* strFileName, wchar\_t\* strFileType\)](./enusappapi_enuSaveImageToFile.md)  
 [ void enuSetModifyUseHref\(wchar\_t\* strSrcId, wchar\_t\* strNewId\)](./enusappapi_enuSetModifyUseHref.md)  
 [ bool enuGetWindowSize\(wchar\_t\* strWindowID, RECT\* rect\)](./enusappapi_enuGetWindowSize.md)  
 [ bool enuSetWindowSize\(wchar\_t\* strWindowID, int x, int y, int width, int height\)](./enusappapi_enuSetWindowSize.md)  
 [ bool enuRegisterFunction\(wchar\_t\* strFunction, int \(\*pfunc\)\(lua\_State\* L\)\)](./enusappapi_enuRegisterFunction.md)  
 [ HVIEW enuGetWindowView\(wchar\_t\* strWindowID\)](./enusappapi_enuGetWindowView.md)

## View Interface

[ HVIEW enuCreateView\(HWND hWnd\)](./enusappapi_enuCreateView.md)  
 [ void enuDestoryView\(HVIEW pENUView\)](./enusappapi_enuDestoryView.md)  
 [ void enuSetViewID\(HVIEW pENUView, wchar\_t\* strID\)](./enusappapi_enuSetViewID.md)  
 [ void enuSetComponentMode\(HVIEW pView, bool bOper\)](./enusappapi_enuSetComponentMode.md)  
 [ void enuUpdateScreen\(HVIEW pENUView\)](./enusappapi_enuUpdateScreen.md)  
 [ void enuInvalidateView\(HVIEW pENUView\)](./enusappapi_enuInvalidateView.md)  
 [ bool enuSetLogicComponent\(HVIEW pENUView, wchar\_t\* pStrFileName, wchar\_t\* pStrSymbol\)](./enusappapi_enuSetLogicComponent.md)  
 [ bool enuSetHmiComponent\(HVIEW pENUView, wchar\_t\* pStrFileName, wchar\_t\* pStrSymbol\)](./enusappapi_enuSetHmiComponent.md) 
 [ bool enuSetSvgView\(HVIEW pENUView, HSVG\_t\* pSvg\)](./enusappapi_enuSetSvgView.md)  
 [ bool enuSetSvgPageView\(HVIEW pENUView, wchar\_t\* pStrFileName\)](./enusappapi_enuSetSvgPageView.md)  
 [ bool enuSetSvgHmiView\(HVIEW pENUView, wchar\_t\* pStrFileName\)](./enusappapi_enuSetSvgHmiView.md)  
 [ bool enuSetSvgLogicView\(HVIEW pENUView, wchar\_t\* pStrFileName\)](./enusappapi_enuSetSvgLogicView.md)  
 [ HSVG enuGetSvgHandler\(HVIEW pENUView\)](./enusappapi_enuGetSvgHandler.md)  
 [ void enuSetWindowPos\(HVIEW pENUView, int x, int y, int cx, int cy\)](./enusappapi_enuSetWindowPos.md)  
 [ void enuSetWindowCenter\(HVIEW pENUView\)](./enusappapi_enuSetWindowCenter.md)

## Object Interface

[ void enuSetSymbolValue\(HSVG pSvgHandler, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](./enusappapi_enuSetSymbolValue.md)  
 [ void enuSetSymbolValueByNode\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](./enusappapi_enuSetSymbolValueByNode.md)  
 [ void enuSetGlobalValue\(HSVG pSvgHandler, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](./enusappapi_enuSetGlobalValue.md)  
 [ void enuDeleteObjectByName\(HSVG pSvgHandler, wchar\_t\* pStrVariable\)](./enusappapi_enuDeleteObjectByName.md)  
 [ void enuDeleteObjectByNode\(HSVG pSvgHandler, HNODE pTarget\)](./enusappapi_enuDeleteObjectByNode.md)  
 [ void enuDeleteUseObjectByHref\(HSVG pSvgHandler, wchar\_t\* pStrHref\)](./enusappapi_enuDeleteUseObjectByHref.md)  
 [ void enuDeleteAllObject\(HSVG pSvgHandler\)](./enusappapi_enuDeleteAllObject.md)  
 [ void enuSetAttribute\(HSVG pSvgHandler, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](./enusappapi_enuSetAttribute.md)  
 [ void enuSetAttributeByNode\(HSVG pSvgHandler, HNODE pObject, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](./enusappapi_enuSetAttributeByNode.md)  
 [ bool enuSetAttributeByNodeSync\(HSVG pSvgHandler, HNODE pObject, wchar\_t\* pStrVariable, wchar\_t\* pStrValue, bool bHistory=false, bool bScript=false\)](./enusappapi_enuSetAttributeByNodeSync.md)  
 [ void enuGetAttributeByNode\(HSVG pSvgHandler, HNODE pObject, wchar\_t\* pStrVariable, VariableStruct\* pData\)](./enusappapi_enuGetAttributeByNode.md)  
 [ HNODE enuAddTrendSeriesByNode\(HSVG pSvgHandler, HNODE TrendNode, wchar\_t\* strSeriesID\)](./enusappapi_enuAddTrendSeriesByNode.md)  
 [ void enuSetUseInterfaceByNode\(HSVG pSvgHandler, HNODE pUse, wchar\_t\* strVariable, wchar\_t\* strValue\)](./enusappapi_enuSetUseInterfaceByNode.md)  
 [ void enuSetUseInterface\(HSVG pSvgHandler, wchar\_t\* strVariable, wchar\_t\* strValue\)](./enusappapi_enuSetUseInterface.md)  
 [ HNODE enuGetObjectById\(HSVG pSvgHandler, wchar\_t\* objectid\)](./enusappapi_enuGetObjectById.md)  
 [ HNODE enuGetDefsSymbolById\(HSVG pSvgHandler, wchar\_t\* objectid\)](./enusappapi_enuGetDefsSymbolById.md) 
 [ HNODE enuCreateLine\(HSVG pSvgHandler, wchar\_t\* strID, float x1, float y1, float x2, float y2, float transx, float transy\)](./enusappapi_enuCreateLine.md)  
 [ HNODE enuCreatePolyline\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy\)](./enusappapi_enuCreatePolyline.md)  
 [ HNODE enuCreatePolygon\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy\)](./enusappapi_enuCreatePolygon.md)  
 [ HNODE enuCreateCircle\(HSVG pSvgHandler, wchar\_t\* strID, float r, float cx, float cy, float transx, float transy\)](./enusappapi_enuCreateCircle.md)  
 [ HNODE enuCreateEllipse\(HSVG pSvgHandler, wchar\_t\* strID, float rx, float ry, float cx, float cy, float transx, float transy\)](./enusappapi_enuCreateEllipse.md)  
 [ HNODE enuCreateRect\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, float transx, float transy\)](./enusappapi_enuCreateRect.md)  
 [ HNODE enuCreateText\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float dx, float dy, wchar\_t\* text, float transx, float transy\)](./enusappapi_enuCreateText.md)  
 [ HNODE enuCreateImage\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, wchar\_t\* xlink\_href, float transx, float transy\)](./enusappapi_enuCreateImage.md)  
 [ HNODE enuCreateTrend\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, float transx, float transy\)](./enusappapi_enuCreateTrend.md)  
 [ HNODE enuCreatePath\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* pStrValue, float transx, float transy\)](./enusappapi_enuCreatePath.md)  
 [ HNODE enuCreateUse\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, wchar\_t\* xlink\_href, wchar\_t\* strType, float transx = 0, float transy = 0\)](./enusappapi_enuCreateUse.md)  
 [ void enuCreateLineAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x1, float y1, float x2, float y2, float transx, float transy\)](./enusappapi_enuCreateLineAsync.md)  
 [ void enuCreatePolylineAsync\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy\)](./enusappapi_enuCreatePolylineAsync.md)  
 [ void enuCreatePolygonAsync\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy\)](./enusappapi_enuCreatePolygonAsync.md)  
 [ void enuCreateCircleAsync\(HSVG pSvgHandler, wchar\_t\* strID, float r, float cx, float cy, float transx, float transy\)](./enusappapi_enuCreateCircleAsync.md)  
 [ void enuCreateEllipseAsync\(HSVG pSvgHandler, wchar\_t\* strID, float rx, float ry, float cx, float cy, float transx, float transy\)](./enusappapi_enuCreateEllipseAsync.md)  
 [ void enuCreateRectAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, float transx, float transy\)](./enusappapi_enuCreateRectAsync.md)  
 [ void enuCreateTextAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float dx, float dy, wchar\_t\* text, float transx, float transy\)](./enusappapi_enuCreateTextAsync.md)  
 [ void enuCreateImageAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, wchar\_t\* xlink\_href, float transx, float transy\)](./enusappapi_enuCreateImageAsync.md)  
 [ void enuCreateTrendAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, float transx, float transy\)](./enusappapi_enuCreateTrendAsync.md)  
 [ void enuCreatePathAsync\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* pStrValue, float transx, float transy\)](./enusappapi_enuCreatePathAsync.md)  
 [ void enuCreateUseAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, wchar\_t\* xlink\_href, wchar\_t\* strType, float transx, float transy\)](./enusappapi_enuCreateUseAsync.md)  
 [ void enuSetEditDelete\(HVIEW pENUView\)](./enusappapi_enuSetEditDelete.md)  
 [ void enuSetEditDeleteAsync\(HVIEW pENUView\)](./enusappapi_enuSetEditDeleteAsync.md)  
 [ void enuExecuteString\(wchar\_t\* pStrPageName, wchar\_t\* pStrEvent\)](./enusappapi_enuExecuteString.md)  
 [ void enuSetVariableValue\(HSVG pSvgHandler, wchar\_t\* strVariable, wchar\_t\* strValue\)](./enusappapi_enuSetVariableValue.md)  
 [ HNODE enuCreateUseAtView\(HVIEW pENUView, float transx, float transy, wchar\_t\* xlink\_href, wchar\_t\* strType\)](./enusappapi_enuCreateUseAtView.md)  
 [ HNODE enuCreateImageAtView\(HVIEW pENUView, wchar\_t\* strID, float x, float y, float width, float height, wchar\_t\* xlink\_href, float transx, float transy\)](./enusappapi_enuCreateImageAtView.md)  
 [ HNODE enuDuplicateLogicSymbol\(wchar\_t\* strPicture, wchar\_t\* strSymbol\)](./enusappapi_enuDuplicateLogicSymbol.md)  
 [ HNODE enuDuplicateHmiSymbol\(wchar\_t\* strPicture, wchar\_t\* strSymbol\)](./enusappapi_enuDuplicateHmiSymbol.md)  
 [ void enuSetUseAttribute\_interface\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strValue\)](./enusappapi_enuSetUseAttribute_interface.md)  
 [ void enuSetUseAttribute\_interface\_id\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strValue\)](./enusappapi_enuSetUseAttribute_interface_id.md)  
 [ void enuGetVariablePointer\(HSVG pSvgHandler, wchar\_t\* pStrVariable, VariableStruct\* pData\)](./enusappapi_enuGetVariablePointer.md)  
 [ void enuSetReShapeArrayValue\(wchar\_t\* pVariable, void\* fValue, int iType, int iSize\)](./enusappapi_enuSetReShapeArrayValue.md)  
 [ bool enuSetModifySymbolAccept\(wchar\_t\* strPicture, wchar\_t\* strSymbol, int iFileType\)](./enusappapi_enuSetModifySymbolAccept.md)

## Script Interface

[ void enuExecuteFunction\(HSVG pSvgHandler, wchar\_t\* strFunction\)](./enusappapi_enuExecuteFunction.md)  
 [ void enuExecuteFunctionByNode\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strFunction\)](./enusappapi_enuExecuteFunctionByNode.md)  
 [ void enuSetLuaScriptByNode\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)](./enusappapi_enuSetLuaScriptByNode.md)  
 [ void enuSetJavaScriptByNode\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)](./enusappapi_enuSetJavaScriptByNode.md)  
 [ bool enuRegisterLuaScript\(wchar\_t\* pStrScript\)](./enusappapi_enuRegisterLuaScript.md)  
 [ wchar\_t\* enuExecuteLuaScript\(wchar\_t\* pStrExecute\)](./enusappapi_enuExecuteLuaScript.md)  
 [ bool enuRegisterJavaScript\(wchar\_t\* pStrScript\)](./enusappapi_enuRegisterJavaScript.md)  
 [ wchar\_t\* enuExecuteJavaScript\(wchar\_t\* pStrExecute\)](./enusappapi_enuExecuteJavaScript.md)  
 [ void enuRegisterLuaScriptById\(wchar\_t\* strPagename, wchar\_t\* strID, wchar\_t\* strFunction, wchar\_t\* strScript\)](./enusappapi_enuRegisterLuaScriptById.md)  
 [ void enuRegisterJavaScriptById\(wchar\_t\* strPagename, wchar\_t\* strID, wchar\_t\* strFunction, wchar\_t\* strScript\)](./enusappapi_enuRegisterJavaScriptById.md)  
 [ void enuRegisterLuaScriptByNode\(wchar\_t\* strPagename, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)](./enusappapi_enuRegisterLuaScriptByNode.md)  
 [ void enuRegisterJavaScriptByNode\(wchar\_t\* strPagename, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)](./enusappapi_enuRegisterJavaScriptByNode.md)

## Widget Interface

[ HVIEW enuCreateWidget\(HWND hWnd\)](./enusappapi_enuCreateWidget.md)  
 [ void enuDestoryWidget\(HVIEW pView\)](./enusappapi_enuDestoryWidget.md)  
 [ bool enuSetWidgetSize\(HVIEW pENUView, int x, int y, int width, int height\)](./enusappapi_enuSetWidgetSize.md)  
 [ HNODE enuCreateUseWidget\(HVIEW pENUView, float transx, float transy, wchar\_t\* xlink\_href, wchar\_t\* strType\)](./enusappapi_enuCreateUseWidget.md)  
 [ HNODE enuCreateImageWidget\(HVIEW pENUView, wchar\_t\* xlink\_href\)](./enusappapi_enuCreateImageWidget.md)  
 [ HNODE enuCreateTrendWidget\(HVIEW pENUView, float x, float y, float width, float height, float transx, float transy, float angle\)](./enusappapi_enuCreateTrendWidget.md)  
 [ void enuWidgetFunctionByNode\(HVIEW pENUView, HNODE pNode, wchar\_t\* strFunction\)](./enusappapi_enuWidgetFunctionByNode.md)

## Runtime Interface

[ void enuShowDebugMessage\(bool bShow\)](./enusappapi_enuShowDebugMessage.md)  
 [ void enuSetRuntimeMode\(bool bRunTime\)](./enusappapi_enuSetRuntimeMode.md)  
 [ void enuOpenWindow\(wchar\_t\* strWindow, float posX, float posY, wchar\_t\* strHref\)](./enusappapi_enuOpenWindow.md)  
 [ void enuCloseWindow\(wchar\_t\* strWindow\)](./enusappapi_enuCloseWindow.md)  
 [ void enuMoveWindow\(wchar\_t\* strWindow, float posX, float posY\)](./enusappapi_enuMoveWindow.md)  
 [ void enuSetRuntimeView\(HVIEW pENUView, bool bRuntime\)](./enusappapi_enuSetRuntimeView.md)  
 [ void\* enuCreatePopupTrend\(int iType, wchar\_t\* strVariables, int x = 0, int y = 0, int width = 0, int height = 0\)](./enusappapi_enuCreatePopupTrend.md)  
 [ void enuDestoryPopupTrend\(void\* pTrend\)](./enusappapi_enuDestoryPopupTrend.md)

## DataBase Interface

[ void enuSetDBGeneration\(\)](./enusappapi_enuSetDBGeneration.md)  
 [ void enuShowTagList\(\)](./enusappapi_enuShowTagList.md)  
 [ void enuShowDeviceList\(\)](./enusappapi_enuShowDeviceList.md)  
 [ void enuSelectObjectListClear\(HVIEW pENUView\)](./enusappapi_enuSelectObjectListClear.md)  
 [ void enuAddSelectObjectByNode\(HVIEW pENUView, HNODE hNode\)](./enusappapi_enuAddSelectObjectByNode.md)

## Configuration Interface

[ wchar\_t\* enuGetConfiguration\(wchar\_t\* pAttribute\)](./enusappapi_enuGetConfiguration.md)  
 [ bool enuSetConfiguration\(wchar\_t\* pAttribute, wchar\_t\* pValue\)](./enusappapi_enuSetConfiguration.md)  
 [ void enuShowUserList\(\)](./enusappapi_enuShowUserList.md)

## Communication Interface

[ bool enuIsWebServerStart\(\)](./enusappapi_enuIsWebServerStart.md)  
 [ bool enuIsEnuServerStart\(\)](./enusappapi_enuIsEnuServerStart.md)  
 [ void enuWebServerStart\(\)](./enusappapi_enuWebServerStart.md)  
 [ void enuWebServerStop\(\)](./enusappapi_enuWebServerStop.md)  
 [ void enuLinkServerStart\(\)](./enusappapi_enuLinkServerStart.md)  
 [ void enuLinkServerStop\(\)](./enusappapi_enuLinkServerStop.md)  
 [ void enuSendNetData\(wchar\_t\* system, char\* data, int length\)](./enusappapi_enuSendNetData.md)  
 [ void enuRecvNetData\(void functioncb\(wchar\_t\* system, char\* buffer, int length\)\)](./enusappapi_enuRecvNetData.md)

## Media Interface

[ void enuPlaySoundX\(wchar\_t\* wavfilename\)](./enusappapi_enuPlaySoundX.md)  
 [ void enuStopSoundX\(wchar\_t\* wavfilename\)](./enusappapi_enuStopSoundX.md)  
 [ void enuSetVolumeX\(int iVolume\)](./enusappapi_enuSetVolumeX.md)

## Task Operation Interface

[ void enuSetTaskOperationMode\(int iMode, int iStep\)](./enusappapi_enuSetTaskOperationMode.md)  
 [ bool enuAddTask\(wchar\_t\* pStrTaskID, wchar\_t\* pStrTaskModule, wchar\_t\* pStrCycle\)](./enusappapi_enuAddTask.md)  
 [ bool enuRemoveTask\(wchar\_t\* pStrTaskID)](./enusappapi_enuRemoveTask.md)   
 [ wchar\_t\* enuGetTaskList\(\)](./enusappapi_enuGetTaskList.md)  
 [ TaskStruct\* enuGetTaskProperty\(wchar\_t\* pStrTaskID\)](./enusappapi_enuGetTaskProperty.md)  
 [ bool enuSetTaskProperty\(wchar\_t\* pStrTaskID, wchar\_t\* pStrProp, wchar\_t\* pStrValue\)](./enusappapi_enuSetTaskProperty.md)  
 [ void enuSetSnapFile\(wchar\_t\* strFilename\)](./enusappapi_enuSetSnapFile.md)  
 [ void enuSetResetFile\(wchar\_t\* strFilename\)](./enusappapi_enuSetResetFile.md)  
 [ \_\_int64 enuGetCurrentTime\(\)](./enusappapi_enuGetCurrentTime.md)

## 3D Interface

## View Interface

[ HVIEW enuCreate3DView\(HWND hWnd\)](./enusappapi_enuCreate3DView.md)  
 [ bool enuSetX3dPageView\(HVIEW pENUView, wchar\_t\* pStrFileName\)](./enusappapi_enuSetX3dPageView.md)  
 [ HX3D enuGetX3DHandler\(HVIEW pENUView\)](./enusappapi_enuGetX3DHandler.md)

## File IO Interface

[ HX3D enuNewX3DPageFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuNewX3DPageFile.md)  
 [ HSVG enuLoadX3DPageFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuLoadX3DPageFile.md)  
 [ bool enuSaveX3DFile\(HX3D pX3DHandler, wchar\_t\* strFileName = L""\)](./enusappapi_enuSaveX3DFile.md)  
 [ bool enuDeleteX3dPageFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuDeleteX3dPageFile.md)

## File handle Interface

[ HX3D enuGetX3dPageClass\(wchar\_t\* pStrFileName\)](./enusappapi_enuGetX3dPageClass.md)

## Edit Interface

[ void enuSetCallBackSelectEvent3D\(void fcbSelectObject\(CPtrList\*, void\*\)\)](./enusappapi_enuSetCallBackSelectEvent3D.md)  
 [ void enuSetSelectDiffuseColor\(HVIEW pENUView, wchar\_t\* strColor\)](./enusappapi_enuSetSelectDiffuseColor.md)  
 [ void enuSetSelectEmissiveColor\(HVIEW pENUView, wchar\_t\* strColor\)](./enusappapi_enuSetSelectEmissiveColor.md)  
 [ void enuSetSelectSpecularColor\(HVIEW pENUView, wchar\_t\* strColor\)](./enusappapi_enuSetSelectSpecularColor.md)  
 [ void enuSetSelect3DToolBar\(int iSel\)](./enusappapi_enuSetSelect3DToolBar.md)  
 [ void enuSetCallBackSelect3DToolBar\(void fcbSelectToolBar\(int\)\)](./enusappapi_enuSetCallBackSelect3DToolBar.md)

## Window Interface

[ void enuSetMove3DCanvas\(HVIEW pENUView, float transx, float transy, float transz\)](./enusappapi_enuSetMove3DCanvas.md)

## Object Interface

[ HNODE enuCreate3DSphere\(HX3D pX3DHandler, wchar\_t\* strID, float radius, float slices, float transx, float transy, float transz\)](./enusappapi_enuCreate3DSphere.md)  
 [ HNODE enuCreate3DCone\(HX3D pX3DHandler, wchar\_t\* strID, float bottomRadius, float height, float slices, float transx, float transy, float transz\)](./enusappapi_enuCreate3DCone.md)  
 [ HNODE enuCreate3DBox\(HX3D pX3DHandler, wchar\_t\* strID, float size, float transx, float transy, float transz\)](./enusappapi_enuCreate3DBox.md)  
 [ HNODE enuCreate3DText\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strString, wchar\_t\* strValue, float fontSize, float transx, float transy, float transz\)](./enusappapi_enuCreate3DText.md)  
 [ HNODE enuCreate3DInline\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strUrl, float transx, float transy, float transz\)](./enusappapi_enuCreate3DInline.md)  
 [ HNODE enuCreate3DLineSet\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy, float transz\)](./enusappapi_enuCreate3DLineSet.md)  
 [ HNODE enuCreate3DFaceSet\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strPoints, wchar\_t\* strVectors, float transx, float transy, float transz\)](./enusappapi_enuCreate3DFaceSet.md)  
 [ HNODE enuCreate3DCylinder\(HX3D pX3DHandler, wchar\_t\* strID, float height, float radius, float slices, float transx, float transy, float transz\)](./enusappapi_enuCreate3DCylinder.md)  
 [ HNODE enuCreate3DTerrain\(HX3D pX3DHandler, wchar\_t\* strID, float size, float subdivision, float transx, float transy, float transz\)](./enusappapi_enuCreate3DTerrain.md)  
 [ void enuCreate3DSphereAsync\(HX3D pX3DHandler, wchar\_t\* strID, float radius, float slices, float transx, float transy, float transz\)](./enusappapi_enuCreate3DSphereAsync.md)  
 [ void enuCreate3DConeAsync\(HX3D pX3DHandler, wchar\_t\* strID, float bottomRadius, float height, float slices, float transx, float transy, float transz\)](./enusappapi_enuCreate3DConeAsync.md)  
 [ void enuCreate3DBoxAsync\(HX3D pX3DHandler, wchar\_t\* strID, float size, float transx, float transy, float transz\)](./enusappapi_enuCreate3DBoxAsync.md)  
 [ void enuCreate3DTextAsync\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strString, wchar\_t\* strValue, float fontSize, float transx, float transy, float transz\)](./enusappapi_enuCreate3DTextAsync.md)  
 [ void enuCreate3DInlineAsync\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strUrl, float transx, float transy, float transz\)](./enusappapi_enuCreate3DInlineAsync.md)  
 [ void enuCreate3DLineSetAsync\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy, float transz\)](./enusappapi_enuCreate3DLineSetAsync.md)  
 [ void enuCreate3DFaceSetAsync\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strPoints, wchar\_t\* strVectors, float transx, float transy, float transz\)](./enusappapi_enuCreate3DFaceSetAsync.md)  
 [ void enuCreate3DCylinderAsync\(HX3D pX3DHandler, wchar\_t\* strID, float height, float radius, float slices, float transx, float transy, float transz\)](./enusappapi_enuCreate3DCylinderAsync.md)  
 [ void enuCreate3DTerrainAsync\(HX3D pX3DHandler, wchar\_t\* strID, float size, float subdivision, float transx, float transy, float transz\)](./enusappapi_enuCreate3DTerrainAsync.md)  
 [ void enuSetAttribute3DByNode\(HX3D pX3DHandler, HNODE pObject, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](./enusappapi_enuSetAttribute3DByNode.md)   
 [ void enuSetAttribute3DByNodeSync\(HX3D pX3DHandler, HNODE pObject, wchar\_t\* pStrVariable, wchar\_t\* pStrValue, bool bHistory, bool bScript\)](./enusappapi_enuSetAttribute3DByNodeSync.md)  
 [ void enuGetAttribute3DByNode\(HX3D pX3DHandler, HNODE pObject, wchar\_t\* pStrVariable, VariableStruct\* pData\)](./enusappapi_enuGetAttribute3DByNode.md)  
 [ void enuSetAttribute3D\(HX3D pX3DHandler, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](./enusappapi_enuSetAttribute3D.md)  
 [ HNODE enuGet3DObjectById\(HX3D pX3DHandler, wchar\_t\* objectid\)](./enusappapi_enuGet3DObjectById.md)  
 [ HNODE enuGetAppearanceFromShape\(HX3D pX3DHandler, HNODE node\)](./enusappapi_enuGetAppearanceFromShape.md)  
 [ HNODE enuGetGeometryFromShape\(HX3D pX3DHandler, HNODE node\)](./enusappapi_enuGetGeometryFromShape.md)  
 [ HNODE enuGetMaterialFromAppearance\(HX3D pX3DHandler, HNODE node\)](./enusappapi_enuGetMaterialFromAppearance.md)  
 [ HNODE enuGetMaterialFromGeometry\(HX3D pX3DHandler, HNODE node\)](./enusappapi_enuGetMaterialFromGeometry.md)  
 [ HNODE enuGetTransformFromGeometry\(HX3D pX3DHandler, HNODE node\)](./enusappapi_enuGetTransformFromGeometry.md)  
 [ HNODE enuGetCoordinateFromIndexedFaceSet\(HX3D pX3DHandler, HNODE node\)](./enusappapi_enuGetCoordinateFromIndexedFaceSet.md)  
 [ HNODE enuGetCoordinateFromLineSet\(HX3D pX3DHandler, HNODE node\)](./enusappapi_enuGetCoordinateFromLineSet.md)  
 [ HNODE enuGetShapeFromGeometry\(HX3D pX3DHandler, HNODE node\)](./enusappapi_enuGetShapeFromGeometry.md)  
 [ void enuDelete3DObjectByNode\(HX3D pX3DHandler, HNODE pTarget\)](./enusappapi_enuDelete3DObjectByNode.md)

## Script Interface

[ void enuSet3DLuaScriptByNode\(HX3D pX3D, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)](./enusappapi_enuSet3DLuaScriptByNode.md)  
 [ void enuSet3DJavaScriptByNode\(HX3D pX3D, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)](./enusappapi_enuSet3DJavaScriptByNode.md)  
 [ void enuExecute3DFunction\(HX3D pX3D, wchar\_t\* strFunction\)](./enusappapi_enuExecute3DFunction.md)  
 [ void enuExecute3DFunctionByNode\(HX3D pX3D, HNODE pNode, wchar\_t\* strFunction\)](./enusappapi_enuExecute3DFunctionByNode.md)
