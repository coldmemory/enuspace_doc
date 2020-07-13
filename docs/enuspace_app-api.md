---
layout: default
title: Application API
has_children: true
nav_order: i
---



## Project Interface

[ bool enuLoadProjectFile\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuLoadProjectFile.html)  
 [ HPROJECT enuCreateProject\(\)](//ApplicationAPI/enuCreateProject.html)  
 [ void enuDestoryProject\(HPROJECT pProject\)](//ApplicationAPI/enuDestoryProject.html)  
 [ bool enuSetActiveProject\(HPROJECT pHANDLE\)](//ApplicationAPI/enuSetActiveProject.html)  
 [ HPROJECT enuGetActiveProject\(\)](//ApplicationAPI/enuGetActiveProject.html)  
 [ void enuSetWidgetProject\(\)](//ApplicationAPI/enuSetWidgetProject.html)  
 [ bool enuSaveProjectFile\(\)](//ApplicationAPI/enuSaveProjectFile.html)  
 [ bool enuCloseProjectFile\(\)](//ApplicationAPI/enuCloseProjectFile.html)  
 [ wchar\_t\* enuGetProjectName\(\)](//ApplicationAPI/enuGetProjectName.html)  
 [ wchar\_t\* enuGetProjectFullName\(\)](//ApplicationAPI/enuGetProjectFullName.html)  
 [ wchar\_t\* enuGetProjectPath\(\)](//ApplicationAPI/enuGetProjectPath.html)  
 [ wchar\_t\* enuGetProjectType\(\)](//ApplicationAPI/enuGetProjectType.html)  
 [ void enuSetProjectName\(wchar\_t\* projectname\)](//ApplicationAPI/enuSetProjectName.html)  
 [ void enuSetModifyProject\(bool bFlag\)](//ApplicationAPI/enuSetModifyProject.html)  
 [ bool enuGetModifyProject\(\)](//ApplicationAPI/enuGetModifyProject.html)

## Operation Interface

## Script Operation Interface

[ void enuSetScriptOperationMode\(bool bFlag\)](//ApplicationAPI/enuSetScriptOperationMode.html)  
 [ bool enuGetScriptOperationMode\(\)](//ApplicationAPI/enuGetScriptOperationMode.html)  
 [ void enuSetHMIScriptUpdateTime\(int iMiliSecond\)](//ApplicationAPI/enuSetHMIScriptUpdateTime.html)

## Edit Operation Interface

[ void enuSetEditOperationMode\(HVIEW pENUView, bool bFlag\)](//ApplicationAPI/enuSetEditOperationMode.html)  
 [ bool enuGetEditOperationMode\(HVIEW pENUVie\)](//ApplicationAPI/enuGetEditOperationMode.html)

## Mouse Interface

[ void enuSetLButtonDownCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](//ApplicationAPI/enuSetLButtonDownCallBack.html)  
 [ void enuSetLButtonUpCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](//ApplicationAPI/enuSetLButtonUpCallBack.html)  
 [ void enuSetRButtonDownCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](//ApplicationAPI/enuSetRButtonDownCallBack.html)  
 [ void enuSetRButtonUpCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](//ApplicationAPI/enuSetRButtonUpCallBack.html)  
 [ void enuSetMButtonDownCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](//ApplicationAPI/enuSetMButtonDownCallBack.html)  
 [ void enuSetMButtonUpCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](//ApplicationAPI/enuSetMButtonUpCallBack.html)  
 [ void enuSetMouseMoveCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](//ApplicationAPI/enuSetMouseMoveCallBack.html)  
 [ void enuSetMouseWheelCallBack\(HVIEW pENUView, void functioncb\(float, float, float\) \)](//ApplicationAPI/enuSetMouseWheelCallBack.html)  
 [ void enuSetLButtonDblClkCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](//ApplicationAPI/enuSetLButtonDblClkCallBack.html)  
 [ void enuOnMouseWheel\(HVIEW pENUView, UINT nFlags, short zDelta, CPoint pt\)](//ApplicationAPI/enuOnMouseWheel.html)  
 [ POINTF enuGetLocalPosition\(HVIEW pENUView, POINT point\)](//ApplicationAPI/enuGetLocalPosition.html)  
 [ POINT enuGetCursorPos\(\)](//ApplicationAPI/enuGetCursorPos.html)  
 [ void enuSetDefaultWheelControl\(HVIEW pENUView, bool bDefault\)](//ApplicationAPI/enuSetDefaultWheelControl.html)

## View Interface

[ void enuActivateView\(HVIEW pENUView\)](//ApplicationAPI/enuActivateView.html)  
 [ void enuDeactivateView\(HVIEW pENUView\)](//ApplicationAPI/enuDeactivateView.html)  
 [ void enuSetRenderObjectPreReset\(HVIEW pENUView\)](//ApplicationAPI/enuSetRenderObjectPreReset.html)  
 [ void enuSetRenderObjectReset\(HVIEW pENUView\)](//ApplicationAPI/enuSetRenderObjectReset.html)

## File IO Interface

[ HSVG enuLoadSvgPageFile\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuLoadSvgPageFile.html)  
 [ HSVG enuLoadSvgHmiFile\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuLoadSvgHmiFile.html)  
 [ HSVG enuLoadSvgLogicFile\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuLoadSvgLogicFile.html)  
 [ HSVG enuLoadSvgResourceFile\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuLoadSvgResourceFile.html)  
 [ HSVG enuLoadSvgGlobalFile\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuLoadSvgGlobalFile.html)  
 [ HSVG enuNewSvgPageFile\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuNewSvgPageFile.html)  
 [ HSVG enuNewSvgHmiFile\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuNewSvgHmiFile.html)  
 [ HSVG enuNewSvgLogicFile\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuNewSvgLogicFile.html)  
 [ HSVG enuNewSvgGlobalFile\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuNewSvgGlobalFile.html)  
 [ HSVG enuNewSvgResourceFile\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuNewSvgResourceFile.html)  
 [ bool enuSaveAsSvgPageFile\(wchar\_t\* strTaget, wchar\_t\* strSource\)](//ApplicationAPI/enuSaveAsSvgPageFile.html)  
 [ bool enuSaveAsSvgHmiFile\(wchar\_t\* strTaget, wchar\_t\* strSource\)](//ApplicationAPI/enuSaveAsSvgHmiFile.html)  
 [ bool enuSaveAsSvgLogicFile\(wchar\_t\* strTaget, wchar\_t\* strSource\)](//ApplicationAPI/enuSaveAsSvgLogicFile.html)  
 [ bool enuSaveAsSvgGlobalFile\(wchar\_t\* strTaget, wchar\_t\* strSource\)](//ApplicationAPI/enuSaveAsSvgGlobalFile.html)  
 [ bool enuSaveAsSvgResourceFile\(wchar\_t\* strTaget, wchar\_t\* strSource\)](//ApplicationAPI/enuSaveAsSvgResourceFile.html)  
 [ bool enuSaveSvgFile\(HSVG pSvgHandler, wchar\_t\* strFileName= L""\)](//ApplicationAPI/enuSaveSvgFile.html)  
 [ bool enuDeleteSvgPageFile\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuDeleteSvgPageFile.html)  
 [ bool enuDeleteSvgHmiFile\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuDeleteSvgHmiFile.html)  
 [ bool enuDeleteSvgLogicFile\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuDeleteSvgLogicFile.html)  
 [ bool enuDeleteSvgResourceFile\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuDeleteSvgResourceFile.html)  
 [ bool enuDeleteSvgGlobalFile\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuDeleteSvgGlobalFile.html)  
 [ bool enuExportWebStyleSvg\(wchar\_t\* strTaget, wchar\_t\* strSource\)](//ApplicationAPI/enuExportWebStyleSvg.html)  
 [ void enuSetAutoSaveMode\(bool bAuto\)](//ApplicationAPI/enuSetAutoSaveMode.html)

## File handle Interface
[ HSVG enuGetPageClass\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuGetPageClass.html)  
 [ HSVG enuGetSvgPageClass\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuGetSvgPageClass.html)  
 [ HSVG enuGetLogicClass\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuGetLogicClass.html)  
 [ HSVG enuGetHmiClass\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuGetHmiClass.html)  
 [ HSVG enuGetGlobalClass\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuGetGlobalClass.html)  
 [ HSVG enuGetResourceClass\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuGetResourceClass.html)  
 [ void\* enuGetPageList\(\)](//ApplicationAPI/enuGetPageList.html)  
 [ void\* enuGetHmiList\(\)](//ApplicationAPI/enuGetHmiList.html)  
 [ void\* enuGetLogicList\(\)](//ApplicationAPI/enuGetLogicList.html)  
 [ void\* enuGetGlobalList\(\)](//ApplicationAPI/enuGetGlobalList.html)  
 [ void\* enuGetResourceList\(\)](//ApplicationAPI/enuGetResourceList.html)  
 [ bool enuGetModifyPage\(wchar\_t\* pStrFilename\)](//ApplicationAPI/enuGetModifyPage.html)  
 [ bool enuGetModifyHmi\(wchar\_t\* pStrFilename\)](//ApplicationAPI/enuGetModifyHmi.html)  
 [ bool enuGetModifyLogic\(wchar\_t\* pStrFilename\)](//ApplicationAPI/enuGetModifyLogic.html)  
 [ bool enuGetModifyGlobal\(wchar\_t\* pStrFilename\)](//ApplicationAPI/enuGetModifyGlobal.html)  
 [ bool enuGetModifyResource\(wchar\_t\* pStrFilename\)](//ApplicationAPI/enuGetModifyResource.html)
 [ bool enuSetPageProperty\(void\_t\* pPage, wchar\_t\* pAttribute, wchar\_t\* pValue\)](//ApplicationAPI/enuSetPageProperty.html)
 [ bool enuSetLogicProperty\(HSVG pSvg, wchar\_t\* pAttribute, wchar\_t\* pValue\)](//ApplicationAPI/enuSetLogicProperty.html)
 [ bool enuSetHmiProperty\(HSVG pSvg, wchar\_t\* pAttribute, wchar\_t\* pValue\)](//ApplicationAPI/enuSetHmiProperty.html)
 [ bool enuSetGlobalProperty\(HSVG pSvg, wchar\_t\* pAttribute, wchar\_t\* pValue\)](//ApplicationAPI/enuSetGlobalProperty.html) 
 [ bool enuSetResourceProperty\(HSVG pSvg, wchar\_t\* pAttribute, wchar\_t\* pValue\)](//ApplicationAPI/enuSetResourceProperty.html)  
## Library Interface

[ bool enuLogicCreateSymbolNode\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)](//ApplicationAPI/enuLogicCreateSymbolNode.html)  
 [ bool enuLogicCreateSymbolLink\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)](//ApplicationAPI/enuLogicCreateSymbolLink.html)  
 [ bool enuHmiCreateSymbol\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)](//ApplicationAPI/enuHmiCreateSymbol.html)  
 [ bool enuResourceCreateStyle\(wchar\_t\* pStrFilename, wchar\_t\* pStrStyle\)](//ApplicationAPI/enuResourceCreateStyle.html)  
 [ bool enuDeleteLogicSymbol\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)](//ApplicationAPI/enuDeleteLogicSymbol.html)  
 [ bool enuDeleteHmiSymbol\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)](//ApplicationAPI/enuDeleteHmiSymbol.html)  
 [ wchar\_t\* enuLogicGetSymbolType\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)](//ApplicationAPI/enuLogicGetSymbolType.html)  
 [ void\* enuGetHmiSymbolList\(wchar\_t\* pStrFilename\)](//ApplicationAPI/enuGetHmiSymbolList.html)  
 [ void\* enuGetLogicSymbolList\(wchar\_t\* pStrFilename\)](//ApplicationAPI/enuGetLogicSymbolList.html)

## Global Interface

[ bool enuAddGlobalStruct\(wchar\_t\* pStrFileName, wchar\_t\* pStrStructName, CPtrList\* pItem\)](//ApplicationAPI/enuAddGlobalStruct.html)  
 [ void\* enuGetGlobalPgStructList\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuGetGlobalPgStructList.html)  
 [ void\* enuGetGlobalVariableList\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuGetGlobalVariableList.html)  
 [ void\* enuGetGlobalPgAttributeList\(wchar\_t\* pStrFileName, wchar\_t\* pStrStructName\)](//ApplicationAPI/enuGetGlobalPgAttributeList.html)  
 [ HNODE enuGetGlobalVariableNode\(wchar\_t\* pStrVariable\)](//ApplicationAPI/enuGetGlobalVariableNode.html)  
 [ bool enuAddGlobalVariable\(wchar\_t\* pStrFileName, wchar\_t\* pStrType, wchar\_t\* strVariable, wchar\_t\* strInitValue=L"", wchar\_t\* strDescription=L""\)](//ApplicationAPI/enuAddGlobalVariable.html)  
 [ bool enuDeleteGlobalVariable\(wchar\_t\* pStrFileName, wchar\_t\* strVariable\)](//ApplicationAPI/enuDeleteGlobalVariable.html)  
 [ bool enuModifyGlobalVariable\(wchar\_t\* pStrFileName, wchar\_t\* strVariable, wchar\_t\* strNewType, wchar\_t\* strNewVariable, wchar\_t\* strNewDescription\)](//ApplicationAPI/enuModifyGlobalVariable.html)  
 [ bool enuDeleteGlobalStruct\(wchar\_t\* pStrFileName, wchar\_t\* strStruct\)](//ApplicationAPI/enuDeleteGlobalStruct.html)  
 [ bool enuModifyGlobalStruct\(wchar\_t\* pStrFileName, wchar\_t\* strStruct, wchar\_t\* strNewStruct, CPtrList\* pItem\)](//ApplicationAPI/enuModifyGlobalStruct.html)  
 [ void enuReloadPicture\(HVIEW pENUView\)](//ApplicationAPI/enuReloadPicture.html)  
 [ bool enuIsModifyPage\(HVIEW pENUView\)](//ApplicationAPI/enuIsModifyPage.html)

## Window Interface

[ void enuSetZoomScale\(HVIEW pENUView, float fPercent\)](//ApplicationAPI/enuSetZoomScale.html)  
 [ float enuGetZoomScale\(HVIEW pENUView\)](//ApplicationAPI/enuGetZoomScale.html)  
 [ float enuGetCanvasWidth\(HVIEW pENUView\)](//ApplicationAPI/enuGetCanvasWidth.html)  
 [ float enuGetCanvasHeight\(HVIEW pENUView\)](//ApplicationAPI/enuGetCanvasHeight.html)  
 [ void enuSetCanvasSize\(HVIEW pENUView, float cx, float cy\)](//ApplicationAPI/enuSetCanvasSize.html)  
 [ void enuSetMoveCanvas\(HVIEW pENUView, float transx, float transy\)](//ApplicationAPI/enuSetMoveCanvas.html)  
 [ void enuGetMoveCanvas\(HVIEW pENUView, float\* transx, float\* transy\)](//ApplicationAPI/enuGetMoveCanvas.html)  
 [ void enuSetCanvasColor\(HVIEW pENUView, byte iR, byte iG, byte iB\)](//ApplicationAPI/enuSetCanvasColor.html)  
 [ void enuSetWindowColor\(HVIEW pENUView, byte iR, byte iG, byte iB\)](//ApplicationAPI/enuSetWindowColor.html)  
 [ bool enuSelConnectionPin\(HVIEW pENUView, wchar\_t\* strPicture, wchar\_t\* strSymbol\)](//ApplicationAPI/enuSelConnectionPin.html)  
 [ bool enuIsEnableConnectionPin\(HVIEW pENUView\)](//ApplicationAPI/enuIsEnableConnectionPin.html)

## Symbol Interface

[ float enuGetSymbolWidth\(HVIEW pENUView, wchar\_t\* strSymbol\)](//ApplicationAPI/enuGetSymbolWidth.html)  
 [ float enuGetSymbolHeight\(HVIEW pENUView, wchar\_t\* strSymbol\)](//ApplicationAPI/enuGetSymbolHeight.html)  
 [ void enuSetSymbolSize\(HVIEW pENUView,  wchar\_t\* strSymbol, float fWidth, float fHeight\)](//ApplicationAPI/enuSetSymbolSize.html)

## Edit Interface

[ void enuSetSelectToolBar\(int iSel\)](//ApplicationAPI/enuSetSelectToolBar.html)  
 [ void enuSetCallBackSelectToolBar\(void fcbSelectToolBar\(int\)\)](//ApplicationAPI/enuSetCallBackSelectToolBar.html)  
 [ void enuSetCallBackSelectEvent\(void fcbSelectObject\(CPtrList\*, void\*\)\)](//ApplicationAPI/enuSetCallBackSelectEvent.html)  
 [ void enuSetCallBackDebugMessage\(void fcbDebugMessage\(wchar\_t\*\)\)](//ApplicationAPI/enuSetCallBackDebugMessage.html)  
 [ bool enuIsEnablePaste\(\)](//ApplicationAPI/enuIsEnablePaste.html)  
 [ bool enuIsSelectObject\(HVIEW pENUView\)](//ApplicationAPI/enuIsEnablePaste.html)  
 [ void enuSetSelectFontname\(HVIEW pENUView,  wchar\_t\* strFontName\)](//ApplicationAPI/enuSetSelectFontname.html)  
 [ void enuSetSelectFontsize\(HVIEW pENUView,  float fSize\)](//ApplicationAPI/enuSetSelectFontsize.html)  
 [ void enuSetSelectFontcolor\(HVIEW pENUView,  wchar\_t\* strFontColor\)](//ApplicationAPI/enuSetSelectFontcolor.html)  
 [ void enuSetSelectFontIncrease\(HVIEW pENUView\)](//ApplicationAPI/enuSetSelectFontIncrease.html)  
 [ void enuSetSelectFontDecrease\(HVIEW pENUView\)](//ApplicationAPI/enuSetSelectFontDecrease.html)  
 [ void enuSetSelectFontBold\(HVIEW pENUView, bool bFlag\)](//ApplicationAPI/enuSetSelectFontBold.html)  
 [ void enuSetSelectFontItalic\(HVIEW pENUView, bool bFlag\)](//ApplicationAPI/enuSetSelectFontItalic.html)  
 [ void enuSetSelectFontUnderline\(HVIEW pENUView, bool bFlag\)](//ApplicationAPI/enuSetSelectFontUnderline.html)  
 [ void enuSetSelectFontStrikethough\(HVIEW pENUView, bool bFlag\)](//ApplicationAPI/enuSetSelectFontStrikethough.html)  
 [ void enuSetSelectFontSubscript\(HVIEW pENUView, bool bFlag\)](//ApplicationAPI/enuSetSelectFontSubscript.html)  
 [ void enuSetSelectFontSuperscript\(HVIEW pENUView, bool bFlag\)](//ApplicationAPI/enuSetSelectFontSuperscript.html)  
 [ void enuSetSelectFontHilight\(HVIEW pENUView, bool bFlag\)](//ApplicationAPI/enuSetSelectFontHilight.html)  
 [ bool enuIsSelectFontBold\(HVIEW pENUView\)](//ApplicationAPI/enuIsSelectFontBold.html)  
 [ bool enuIsSelectFontItalic\(HVIEW pENUView\)](//ApplicationAPI/enuIsSelectFontItalic.html)  
 [ bool enuIsSelectFontUnderline\(HVIEW pENUView\)](//ApplicationAPI/enuIsSelectFontUnderline.html)  
 [ bool enuIsSelectFontStrikethough\(HVIEW pENUView\)](//ApplicationAPI/enuIsSelectFontStrikethough.html)  
 [ bool enuIsSelectFontSubscript\(HVIEW pENUView\)](//ApplicationAPI/enuIsSelectFontSubscript.html)  
 [ bool enuIsSelectFontSuperscript\(HVIEW pENUView\)](//ApplicationAPI/enuIsSelectFontSuperscript.html)  
 [ void enuSetSelectFillcolor\(HVIEW pENUView,  wchar\_t\* strColor\)](//ApplicationAPI/enuSetSelectFillcolor.html)  
 [ void enuSetSelectFillOpacity\(HVIEW pENUView, wchar\_t\* strOpacity\)](//ApplicationAPI/enuSetSelectFillOpacity.html)  
 [ void enuSetSelectLinecolor\(HVIEW pENUView,  wchar\_t\* strColor\)](//ApplicationAPI/enuSetSelectLinecolor.html)  
 [ void enuSetSelectLineOpacity\(HVIEW pENUView, wchar\_t\* strOpacity\)](//ApplicationAPI/enuSetSelectLineOpacity.html)  
 [ void enuSetSelectLineWidth\(HVIEW pENUView, float fWidth\)](//ApplicationAPI/enuSetSelectLineWidth.html)  
 [ void enuSetSelectLineDashes\(HVIEW pENUView, wchar\_t\* strDashes\)](//ApplicationAPI/enuSetSelectLineDashes.html)  
 [ void enuSetSelectAlign\(HVIEW pENUView, int iType\)](//ApplicationAPI/enuSetSelectAlign.html)  
 [ void enuSetSelectRotation\(HVIEW pENUView, float fAngle\)](//ApplicationAPI/enuSetSelectRotation.html)  
 [ void enuSetSelectFlip\(HVIEW pENUView, int iType\)](//ApplicationAPI/enuSetSelectFlip.html)  
 [ HNODE enuGetSelectSingleObject\(HVIEW pENUView\)](//ApplicationAPI/enuGetSelectSingleObject.html)  
 [ void enuSetSelectAll\(HVIEW pENUView\)](//ApplicationAPI/enuSetSelectAll.html)  
 [ bool enuSetSelectObject\(HVIEW pENUView, wchar\_t\* strSelectID\)](//ApplicationAPI/enuSetSelectObject.html)  
 [ void enuSetFindObjectCallBack\(void fcbFindMessage\(HNODE, int, wchar\_t\*, wchar\_t\*\), wchar\_t\* pStrSearch, bool bMatchCase, bool bWholeWord\)](//ApplicationAPI/enuSetFindObjectCallBack.html)  
 [ wchar\_t\* enuGetPrevPageName\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuGetPrevPageName.html)  
 [ wchar\_t\* enuGetNextPageName\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuGetNextPageName.html)  
 [ void enuSetSelectZOrder\(HVIEW pENUView, int iType\)](//ApplicationAPI/enuSetSelectZOrder.html)  
 [ void enuSetSelectGroup\(HVIEW pENUView\)](//ApplicationAPI/enuSetSelectGroup.html)  
 [ void enuSetSelectUnGroup\(HVIEW pENUView\)](//ApplicationAPI/enuSetSelectUnGroup.html)  
 [ void enuMoveObjectUp\(HVIEW pENUView\)](//ApplicationAPI/enuMoveObjectUp.html)  
 [ void enuMoveObjectDown\(HVIEW pENUView\)](//ApplicationAPI/enuMoveObjectDown.html)  
 [ void enuMoveObjectLeft\(HVIEW pENUView\)](//ApplicationAPI/enuMoveObjectLeft.html)  
 [ void enuMoveObjectRight\(HVIEW pENUView\)](//ApplicationAPI/enuMoveObjectRight.html)  
 [ void enuSetEditCopy\(HVIEW pENUView\)](//ApplicationAPI/enuSetEditCopy.html)  
 [ void enuSetEditCut\(HVIEW pENUView\)](//ApplicationAPI/enuSetEditCut.html)  
 [ void enuSetEditPaste\(HVIEW pENUView\)](//ApplicationAPI/enuSetEditPaste.html)  
 [ void enuSetEditLock\(HVIEW pENUView\)](//ApplicationAPI/enuSetEditLock.html)  
 [ void enuSetEditUnLock\(HVIEW pENUView\)](//ApplicationAPI/enuSetEditUnLock.html)  
 [ void enuSetEditUndo\(HVIEW pENUView\)](//ApplicationAPI/enuSetEditUndo.html)  
 [ void enuSetEditRedo\(HVIEW pENUView\)](//ApplicationAPI/enuSetEditRedo.html)  
 [ bool enuIsEditUndo\(HVIEW pENUView\)](//ApplicationAPI/enuIsEditUndo.html)  
 [ bool enuIsEditRedo\(HVIEW pENUView\)](//ApplicationAPI/enuIsEditRedo.html)

## Runtime Interface

[ void enuSetCallBackAddTable\( void fcbAddTable\(HNODE\) \)](//ApplicationAPI/enuSetCallBackAddTable.html)  
 [ HSVG enuNewSvgExternalPageFile\(wchar\_t\* pFileName\)](//ApplicationAPI/enuNewSvgExternalPageFile.html)  
 [ HSVG enuLoadSvgExternalPageFile\(wchar\_t\* pFileName\)](//ApplicationAPI/enuLoadSvgExternalPageFile.html)  
 [ bool enuDeleteSvgExternalPageFile\(wchar\_t\* pFileName\)](//ApplicationAPI/enuDeleteSvgExternalPageFile.html)  
 [ bool enuSetSvgExternalPageView\(HVIEW pENUView, HSVG pSvg\)](//ApplicationAPI/enuSetSvgExternalPageView.html)  
 [ bool enuShowRuntimeView\(HWND hWnd\)](//ApplicationAPI/enuShowRuntimeView.html)  
 [ void enuDestoryRuntimeView\(\)](//ApplicationAPI/enuDestoryRuntimeView.html)  
 [ bool enuIsRuntimeView\(\)](//ApplicationAPI/enuIsRuntimeView.html)  
 [ void enuChangePicture\(wchar\_t\* strWindow, wchar\_t\* strPicName\)](//ApplicationAPI/enuChangePicture.html)  
 [ void enuChangePictureAsync\(wchar\_t\* strWindow, wchar\_t\* strPicName\)](//ApplicationAPI/enuChangePictureAsync.html)  
 [ void enuSaveImageToFile\(HVIEW pENUView, wchar\_t\* strFileName, wchar\_t\* strFileType\)](//ApplicationAPI/enuSaveImageToFile.html)  
 [ void enuSetModifyUseHref\(wchar\_t\* strSrcId, wchar\_t\* strNewId\)](//ApplicationAPI/enuSetModifyUseHref.html)  
 [ bool enuGetWindowSize\(wchar\_t\* strWindowID, RECT\* rect\)](//ApplicationAPI/enuGetWindowSize.html)  
 [ bool enuSetWindowSize\(wchar\_t\* strWindowID, int x, int y, int width, int height\)](//ApplicationAPI/enuSetWindowSize.html)  
 [ bool enuRegisterFunction\(wchar\_t\* strFunction, int \(\*pfunc\)\(lua\_State\* L\)\)](//ApplicationAPI/enuRegisterFunction.html)  
 [ HVIEW enuGetWindowView\(wchar\_t\* strWindowID\)](//ApplicationAPI/enuGetWindowView.html)

## View Interface

[ HVIEW enuCreateView\(HWND hWnd\)](//ApplicationAPI/enuCreateView.html)  
 [ void enuDestoryView\(HVIEW pENUView\)](//ApplicationAPI/enuDestoryView.html)  
 [ void enuSetViewID\(HVIEW pENUView, wchar\_t\* strID\)](//ApplicationAPI/enuSetViewID.html)  
 [ void enuSetComponentMode\(HVIEW pView, bool bOper\)](//ApplicationAPI/enuSetComponentMode.html)  
 [ void enuUpdateScreen\(HVIEW pENUView\)](//ApplicationAPI/enuUpdateScreen.html)  
 [ void enuInvalidateView\(HVIEW pENUView\)](//ApplicationAPI/enuInvalidateView.html)  
 [ bool enuSetLogicComponent\(HVIEW pENUView, wchar\_t\* pStrFileName, wchar\_t\* pStrSymbol\)](//ApplicationAPI/enuSetLogicComponent.html)  
 [ bool enuSetHmiComponent\(HVIEW pENUView, wchar\_t\* pStrFileName, wchar\_t\* pStrSymbol\)](//ApplicationAPI/enuSetHmiComponent.html) 
 [ bool enuSetSvgView\(HVIEW pENUView, HSVG\_t\* pSvg\)](//ApplicationAPI/enuSetSvgView.html)  
 [ bool enuSetSvgPageView\(HVIEW pENUView, wchar\_t\* pStrFileName\)](//ApplicationAPI/enuSetSvgPageView.html)  
 [ bool enuSetSvgHmiView\(HVIEW pENUView, wchar\_t\* pStrFileName\)](//ApplicationAPI/enuSetSvgHmiView.html)  
 [ bool enuSetSvgLogicView\(HVIEW pENUView, wchar\_t\* pStrFileName\)](//ApplicationAPI/enuSetSvgLogicView.html)  
 [ HSVG enuGetSvgHandler\(HVIEW pENUView\)](//ApplicationAPI/enuGetSvgHandler.html)  
 [ void enuSetWindowPos\(HVIEW pENUView, int x, int y, int cx, int cy\)](//ApplicationAPI/enuSetWindowPos.html)  
 [ void enuSetWindowCenter\(HVIEW pENUView\)](//ApplicationAPI/enuSetWindowCenter.html)

## Object Interface

[ void enuSetSymbolValue\(HSVG pSvgHandler, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](//ApplicationAPI/enuSetSymbolValue.html)  
 [ void enuSetSymbolValueByNode\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](//ApplicationAPI/enuSetSymbolValueByNode.html)  
 [ void enuSetGlobalValue\(HSVG pSvgHandler, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](//ApplicationAPI/enuSetGlobalValue.html)  
 [ void enuDeleteObjectByName\(HSVG pSvgHandler, wchar\_t\* pStrVariable\)](//ApplicationAPI/enuDeleteObjectByName.html)  
 [ void enuDeleteObjectByNode\(HSVG pSvgHandler, HNODE pTarget\)](//ApplicationAPI/enuDeleteObjectByNode.html)  
 [ void enuDeleteUseObjectByHref\(HSVG pSvgHandler, wchar\_t\* pStrHref\)](//ApplicationAPI/enuDeleteUseObjectByHref.html)  
 [ void enuDeleteAllObject\(HSVG pSvgHandler\)](//ApplicationAPI/enuDeleteAllObject.html)  
 [ void enuSetAttribute\(HSVG pSvgHandler, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](//ApplicationAPI/enuSetAttribute.html)  
 [ void enuSetAttributeByNode\(HSVG pSvgHandler, HNODE pObject, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](//ApplicationAPI/enuSetAttributeByNode.html)  
 [ bool enuSetAttributeByNodeSync\(HSVG pSvgHandler, HNODE pObject, wchar\_t\* pStrVariable, wchar\_t\* pStrValue, bool bHistory=false, bool bScript=false\)](//ApplicationAPI/enuSetAttributeByNodeSync.html)  
 [ void enuGetAttributeByNode\(HSVG pSvgHandler, HNODE pObject, wchar\_t\* pStrVariable, VariableStruct\* pData\)](//ApplicationAPI/enuGetAttributeByNode.html)  
 [ HNODE enuAddTrendSeriesByNode\(HSVG pSvgHandler, HNODE TrendNode, wchar\_t\* strSeriesID\)](//ApplicationAPI/enuAddTrendSeriesByNode.html)  
 [ void enuSetUseInterfaceByNode\(HSVG pSvgHandler, HNODE pUse, wchar\_t\* strVariable, wchar\_t\* strValue\)](//ApplicationAPI/enuSetUseInterfaceByNode.html)  
 [ void enuSetUseInterface\(HSVG pSvgHandler, wchar\_t\* strVariable, wchar\_t\* strValue\)](//ApplicationAPI/enuSetUseInterface.html)  
 [ HNODE enuGetObjectById\(HSVG pSvgHandler, wchar\_t\* objectid\)](//ApplicationAPI/enuGetObjectById.html)  
 [ HNODE enuGetDefsSymbolById\(HSVG pSvgHandler, wchar\_t\* objectid\)](//ApplicationAPI/enuGetDefsSymbolById.html) 
 [ HNODE enuCreateLine\(HSVG pSvgHandler, wchar\_t\* strID, float x1, float y1, float x2, float y2, float transx, float transy\)](//ApplicationAPI/enuCreateLine.html)  
 [ HNODE enuCreatePolyline\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy\)](//ApplicationAPI/enuCreatePolyline.html)  
 [ HNODE enuCreatePolygon\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy\)](//ApplicationAPI/enuCreatePolygon.html)  
 [ HNODE enuCreateCircle\(HSVG pSvgHandler, wchar\_t\* strID, float r, float cx, float cy, float transx, float transy\)](//ApplicationAPI/enuCreateCircle.html)  
 [ HNODE enuCreateEllipse\(HSVG pSvgHandler, wchar\_t\* strID, float rx, float ry, float cx, float cy, float transx, float transy\)](//ApplicationAPI/enuCreateEllipse.html)  
 [ HNODE enuCreateRect\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, float transx, float transy\)](//ApplicationAPI/enuCreateRect.html)  
 [ HNODE enuCreateText\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float dx, float dy, wchar\_t\* text, float transx, float transy\)](//ApplicationAPI/enuCreateText.html)  
 [ HNODE enuCreateImage\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, wchar\_t\* xlink\_href, float transx, float transy\)](//ApplicationAPI/enuCreateImage.html)  
 [ HNODE enuCreateTrend\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, float transx, float transy\)](//ApplicationAPI/enuCreateTrend.html)  
 [ HNODE enuCreatePath\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* pStrValue, float transx, float transy\)](//ApplicationAPI/enuCreatePath.html)  
 [ HNODE enuCreateUse\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, wchar\_t\* xlink\_href, wchar\_t\* strType, float transx = 0, float transy = 0\)](//ApplicationAPI/enuCreateUse.html)  
 [ void enuCreateLineAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x1, float y1, float x2, float y2, float transx, float transy\)](//ApplicationAPI/enuCreateLineAsync.html)  
 [ void enuCreatePolylineAsync\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy\)](//ApplicationAPI/enuCreatePolylineAsync.html)  
 [ void enuCreatePolygonAsync\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy\)](//ApplicationAPI/enuCreatePolygonAsync.html)  
 [ void enuCreateCircleAsync\(HSVG pSvgHandler, wchar\_t\* strID, float r, float cx, float cy, float transx, float transy\)](//ApplicationAPI/enuCreateCircleAsync.html)  
 [ void enuCreateEllipseAsync\(HSVG pSvgHandler, wchar\_t\* strID, float rx, float ry, float cx, float cy, float transx, float transy\)](//ApplicationAPI/enuCreateEllipseAsync.html)  
 [ void enuCreateRectAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, float transx, float transy\)](//ApplicationAPI/enuCreateRectAsync.html)  
 [ void enuCreateTextAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float dx, float dy, wchar\_t\* text, float transx, float transy\)](//ApplicationAPI/enuCreateTextAsync.html)  
 [ void enuCreateImageAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, wchar\_t\* xlink\_href, float transx, float transy\)](//ApplicationAPI/enuCreateImageAsync.html)  
 [ void enuCreateTrendAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, float transx, float transy\)](//ApplicationAPI/enuCreateTrendAsync.html)  
 [ void enuCreatePathAsync\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* pStrValue, float transx, float transy\)](//ApplicationAPI/enuCreatePathAsync.html)  
 [ void enuCreateUseAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, wchar\_t\* xlink\_href, wchar\_t\* strType, float transx, float transy\)](//ApplicationAPI/enuCreateUseAsync.html)  
 [ void enuSetEditDelete\(HVIEW pENUView\)](//ApplicationAPI/enuSetEditDelete.html)  
 [ void enuSetEditDeleteAsync\(HVIEW pENUView\)](//ApplicationAPI/enuSetEditDeleteAsync.html)  
 [ void enuExecuteString\(wchar\_t\* pStrPageName, wchar\_t\* pStrEvent\)](//ApplicationAPI/enuExecuteString.html)  
 [ void enuSetVariableValue\(HSVG pSvgHandler, wchar\_t\* strVariable, wchar\_t\* strValue\)](//ApplicationAPI/enuSetVariableValue.html)  
 [ HNODE enuCreateUseAtView\(HVIEW pENUView, float transx, float transy, wchar\_t\* xlink\_href, wchar\_t\* strType\)](//ApplicationAPI/enuCreateUseAtView.html)  
 [ HNODE enuCreateImageAtView\(HVIEW pENUView, wchar\_t\* strID, float x, float y, float width, float height, wchar\_t\* xlink\_href, float transx, float transy\)](//ApplicationAPI/enuCreateImageAtView.html)  
 [ HNODE enuDuplicateLogicSymbol\(wchar\_t\* strPicture, wchar\_t\* strSymbol\)](//ApplicationAPI/enuDuplicateLogicSymbol.html)  
 [ HNODE enuDuplicateHmiSymbol\(wchar\_t\* strPicture, wchar\_t\* strSymbol\)](//ApplicationAPI/enuDuplicateHmiSymbol.html)  
 [ void enuSetUseAttribute\_interface\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strValue\)](//ApplicationAPI/enuSetUseAttribute_interface.html)  
 [ void enuSetUseAttribute\_interface\_id\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strValue\)](//ApplicationAPI/enuSetUseAttribute_interface_id.html)  
 [ void enuGetVariablePointer\(HSVG pSvgHandler, wchar\_t\* pStrVariable, VariableStruct\* pData\)](//ApplicationAPI/enuGetVariablePointer.html)  
 [ void enuSetReShapeArrayValue\(wchar\_t\* pVariable, void\* fValue, int iType, int iSize\)](//ApplicationAPI/enuSetReShapeArrayValue.html)  
 [ bool enuSetModifySymbolAccept\(wchar\_t\* strPicture, wchar\_t\* strSymbol, int iFileType\)](//ApplicationAPI/enuSetModifySymbolAccept.html)

## Script Interface

[ void enuExecuteFunction\(HSVG pSvgHandler, wchar\_t\* strFunction\)](//ApplicationAPI/enuExecuteFunction.html)  
 [ void enuExecuteFunctionByNode\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strFunction\)](//ApplicationAPI/enuExecuteFunctionByNode.html)  
 [ void enuSetLuaScriptByNode\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)](//ApplicationAPI/enuSetLuaScriptByNode.html)  
 [ void enuSetJavaScriptByNode\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)](//ApplicationAPI/enuSetJavaScriptByNode.html)  
 [ bool enuRegisterLuaScript\(wchar\_t\* pStrScript\)](//ApplicationAPI/enuRegisterLuaScript.html)  
 [ wchar\_t\* enuExecuteLuaScript\(wchar\_t\* pStrExecute\)](//ApplicationAPI/enuExecuteLuaScript.html)  
 [ bool enuRegisterJavaScript\(wchar\_t\* pStrScript\)](//ApplicationAPI/enuRegisterJavaScript.html)  
 [ wchar\_t\* enuExecuteJavaScript\(wchar\_t\* pStrExecute\)](//ApplicationAPI/enuExecuteJavaScript.html)  
 [ void enuRegisterLuaScriptById\(wchar\_t\* strPagename, wchar\_t\* strID, wchar\_t\* strFunction, wchar\_t\* strScript\)](//ApplicationAPI/enuRegisterLuaScriptById.html)  
 [ void enuRegisterJavaScriptById\(wchar\_t\* strPagename, wchar\_t\* strID, wchar\_t\* strFunction, wchar\_t\* strScript\)](//ApplicationAPI/enuRegisterJavaScriptById.html)  
 [ void enuRegisterLuaScriptByNode\(wchar\_t\* strPagename, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)](//ApplicationAPI/enuRegisterLuaScriptByNode.html)  
 [ void enuRegisterJavaScriptByNode\(wchar\_t\* strPagename, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)](//ApplicationAPI/enuRegisterJavaScriptByNode.html)

## Widget Interface

[ HVIEW enuCreateWidget\(HWND hWnd\)](//ApplicationAPI/enuCreateWidget.html)  
 [ void enuDestoryWidget\(HVIEW pView\)](//ApplicationAPI/enuDestoryWidget.html)  
 [ bool enuSetWidgetSize\(HVIEW pENUView, int x, int y, int width, int height\)](//ApplicationAPI/enuSetWidgetSize.html)  
 [ HNODE enuCreateUseWidget\(HVIEW pENUView, float transx, float transy, wchar\_t\* xlink\_href, wchar\_t\* strType\)](//ApplicationAPI/enuCreateUseWidget.html)  
 [ HNODE enuCreateImageWidget\(HVIEW pENUView, wchar\_t\* xlink\_href\)](//ApplicationAPI/enuCreateImageWidget.html)  
 [ HNODE enuCreateTrendWidget\(HVIEW pENUView, float x, float y, float width, float height, float transx, float transy, float angle\)](//ApplicationAPI/enuCreateTrendWidget.html)  
 [ void enuWidgetFunctionByNode\(HVIEW pENUView, HNODE pNode, wchar\_t\* strFunction\)](//ApplicationAPI/enuWidgetFunctionByNode.html)

## Runtime Interface

[ void enuShowDebugMessage\(bool bShow\)](//ApplicationAPI/enuShowDebugMessage.html)  
 [ void enuSetRuntimeMode\(bool bRunTime\)](//ApplicationAPI/enuSetRuntimeMode.html)  
 [ void enuOpenWindow\(wchar\_t\* strWindow, float posX, float posY, wchar\_t\* strHref\)](//ApplicationAPI/enuOpenWindow.html)  
 [ void enuCloseWindow\(wchar\_t\* strWindow\)](//ApplicationAPI/enuCloseWindow.html)  
 [ void enuMoveWindow\(wchar\_t\* strWindow, float posX, float posY\)](//ApplicationAPI/enuMoveWindow.html)  
 [ void enuSetRuntimeView\(HVIEW pENUView, bool bRuntime\)](//ApplicationAPI/enuSetRuntimeView.html)  
 [ void\* enuCreatePopupTrend\(int iType, wchar\_t\* strVariables, int x = 0, int y = 0, int width = 0, int height = 0\)](//ApplicationAPI/enuCreatePopupTrend.html)  
 [ void enuDestoryPopupTrend\(void\* pTrend\)](//ApplicationAPI/enuDestoryPopupTrend.html)

## DataBase Interface

[ void enuSetDBGeneration\(\)](//ApplicationAPI/enuSetDBGeneration.html)  
 [ void enuShowTagList\(\)](//ApplicationAPI/enuShowTagList.html)  
 [ void enuShowDeviceList\(\)](//ApplicationAPI/enuShowDeviceList.html)  
 [ void enuSelectObjectListClear\(HVIEW pENUView\)](//ApplicationAPI/enuSelectObjectListClear.html)  
 [ void enuAddSelectObjectByNode\(HVIEW pENUView, HNODE hNode\)](//ApplicationAPI/enuAddSelectObjectByNode.html)

## Configuration Interface

[ wchar\_t\* enuGetConfiguration\(wchar\_t\* pAttribute\)](//ApplicationAPI/enuGetConfiguration.html)  
 [ bool enuSetConfiguration\(wchar\_t\* pAttribute, wchar\_t\* pValue\)](//ApplicationAPI/enuSetConfiguration.html)  
 [ void enuShowUserList\(\)](//ApplicationAPI/enuShowUserList.html)

## Communication Interface

[ bool enuIsWebServerStart\(\)](//ApplicationAPI/enuIsWebServerStart.html)  
 [ bool enuIsEnuServerStart\(\)](//ApplicationAPI/enuIsEnuServerStart.html)  
 [ void enuWebServerStart\(\)](//ApplicationAPI/enuWebServerStart.html)  
 [ void enuWebServerStop\(\)](//ApplicationAPI/enuWebServerStop.html)  
 [ void enuLinkServerStart\(\)](//ApplicationAPI/enuLinkServerStart.html)  
 [ void enuLinkServerStop\(\)](//ApplicationAPI/enuLinkServerStop.html)  
 [ void enuSendNetData\(wchar\_t\* system, char\* data, int length\)](//ApplicationAPI/enuSendNetData.html)  
 [ void enuRecvNetData\(void functioncb\(wchar\_t\* system, char\* buffer, int length\)\)](//ApplicationAPI/enuRecvNetData.html)

## Media Interface

[ void enuPlaySoundX\(wchar\_t\* wavfilename\)](//ApplicationAPI/enuPlaySoundX.html)  
 [ void enuStopSoundX\(wchar\_t\* wavfilename\)](//ApplicationAPI/enuStopSoundX.html)  
 [ void enuSetVolumeX\(int iVolume\)](//ApplicationAPI/enuSetVolumeX.html)

## Task Operation Interface

[ void enuSetTaskOperationMode\(int iMode, int iStep\)](//ApplicationAPI/enuSetTaskOperationMode.html)  
 [ bool enuAddTask\(wchar\_t\* pStrTaskID, wchar\_t\* pStrTaskModule, wchar\_t\* pStrCycle\)](//ApplicationAPI/enuAddTask.html)  
 [ bool enuRemoveTask\(wchar\_t\* pStrTaskID)](//ApplicationAPI/enuRemoveTask.html)   
 [ wchar\_t\* enuGetTaskList\(\)](//ApplicationAPI/enuGetTaskList.html)  
 [ TaskStruct\* enuGetTaskProperty\(wchar\_t\* pStrTaskID\)](//ApplicationAPI/enuGetTaskProperty.html)  
 [ bool enuSetTaskProperty\(wchar\_t\* pStrTaskID, wchar\_t\* pStrProp, wchar\_t\* pStrValue\)](//ApplicationAPI/enuSetTaskProperty.html)  
 [ void enuSetSnapFile\(wchar\_t\* strFilename\)](//ApplicationAPI/enuSetSnapFile.html)  
 [ void enuSetResetFile\(wchar\_t\* strFilename\)](//ApplicationAPI/enuSetResetFile.html)  
 [ \_\_int64 enuGetCurrentTime\(\)](//ApplicationAPI/enuGetCurrentTime.html)

## 3D Interface

## View Interface

[ HVIEW enuCreate3DView\(HWND hWnd\)](//ApplicationAPI/enuCreate3DView.html)  
 [ bool enuSetX3dPageView\(HVIEW pENUView, wchar\_t\* pStrFileName\)](//ApplicationAPI/enuSetX3dPageView.html)  
 [ HX3D enuGetX3DHandler\(HVIEW pENUView\)](//ApplicationAPI/enuGetX3DHandler.html)

## File IO Interface

[ HX3D enuNewX3DPageFile\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuNewX3DPageFile.html)  
 [ HSVG enuLoadX3DPageFile\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuLoadX3DPageFile.html)  
 [ bool enuSaveX3DFile\(HX3D pX3DHandler, wchar\_t\* strFileName = L""\)](//ApplicationAPI/enuSaveX3DFile.html)  
 [ bool enuDeleteX3dPageFile\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuDeleteX3dPageFile.html)

## File handle Interface

[ HX3D enuGetX3dPageClass\(wchar\_t\* pStrFileName\)](//ApplicationAPI/enuGetX3dPageClass.html)

## Edit Interface

[ void enuSetCallBackSelectEvent3D\(void fcbSelectObject\(CPtrList\*, void\*\)\)](//ApplicationAPI/enuSetCallBackSelectEvent3D.html)  
 [ void enuSetSelectDiffuseColor\(HVIEW pENUView, wchar\_t\* strColor\)](//ApplicationAPI/enuSetSelectDiffuseColor.html)  
 [ void enuSetSelectEmissiveColor\(HVIEW pENUView, wchar\_t\* strColor\)](//ApplicationAPI/enuSetSelectEmissiveColor.html)  
 [ void enuSetSelectSpecularColor\(HVIEW pENUView, wchar\_t\* strColor\)](//ApplicationAPI/enuSetSelectSpecularColor.html)  
 [ void enuSetSelect3DToolBar\(int iSel\)](//ApplicationAPI/enuSetSelect3DToolBar.html)  
 [ void enuSetCallBackSelect3DToolBar\(void fcbSelectToolBar\(int\)\)](//ApplicationAPI/enuSetCallBackSelect3DToolBar.html)

## Window Interface

[ void enuSetMove3DCanvas\(HVIEW pENUView, float transx, float transy, float transz\)](//ApplicationAPI/enuSetMove3DCanvas.html)

## Object Interface

[ HNODE enuCreate3DSphere\(HX3D pX3DHandler, wchar\_t\* strID, float radius, float slices, float transx, float transy, float transz\)](//ApplicationAPI/enuCreate3DSphere.html)  
 [ HNODE enuCreate3DCone\(HX3D pX3DHandler, wchar\_t\* strID, float bottomRadius, float height, float slices, float transx, float transy, float transz\)](//ApplicationAPI/enuCreate3DCone.html)  
 [ HNODE enuCreate3DBox\(HX3D pX3DHandler, wchar\_t\* strID, float size, float transx, float transy, float transz\)](//ApplicationAPI/enuCreate3DBox.html)  
 [ HNODE enuCreate3DText\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strString, wchar\_t\* strValue, float fontSize, float transx, float transy, float transz\)](//ApplicationAPI/enuCreate3DText.html)  
 [ HNODE enuCreate3DInline\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strUrl, float transx, float transy, float transz\)](//ApplicationAPI/enuCreate3DInline.html)  
 [ HNODE enuCreate3DLineSet\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy, float transz\)](//ApplicationAPI/enuCreate3DLineSet.html)  
 [ HNODE enuCreate3DFaceSet\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strPoints, wchar\_t\* strVectors, float transx, float transy, float transz\)](//ApplicationAPI/enuCreate3DFaceSet.html)  
 [ HNODE enuCreate3DCylinder\(HX3D pX3DHandler, wchar\_t\* strID, float height, float radius, float slices, float transx, float transy, float transz\)](//ApplicationAPI/enuCreate3DCylinder.html)  
 [ HNODE enuCreate3DTerrain\(HX3D pX3DHandler, wchar\_t\* strID, float size, float subdivision, float transx, float transy, float transz\)](//ApplicationAPI/enuCreate3DTerrain.html)  
 [ void enuCreate3DSphereAsync\(HX3D pX3DHandler, wchar\_t\* strID, float radius, float slices, float transx, float transy, float transz\)](//ApplicationAPI/enuCreate3DSphereAsync.html)  
 [ void enuCreate3DConeAsync\(HX3D pX3DHandler, wchar\_t\* strID, float bottomRadius, float height, float slices, float transx, float transy, float transz\)](//ApplicationAPI/enuCreate3DConeAsync.html)  
 [ void enuCreate3DBoxAsync\(HX3D pX3DHandler, wchar\_t\* strID, float size, float transx, float transy, float transz\)](//ApplicationAPI/enuCreate3DBoxAsync.html)  
 [ void enuCreate3DTextAsync\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strString, wchar\_t\* strValue, float fontSize, float transx, float transy, float transz\)](//ApplicationAPI/enuCreate3DTextAsync.html)  
 [ void enuCreate3DInlineAsync\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strUrl, float transx, float transy, float transz\)](//ApplicationAPI/enuCreate3DInlineAsync.html)  
 [ void enuCreate3DLineSetAsync\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy, float transz\)](//ApplicationAPI/enuCreate3DLineSetAsync.html)  
 [ void enuCreate3DFaceSetAsync\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strPoints, wchar\_t\* strVectors, float transx, float transy, float transz\)](//ApplicationAPI/enuCreate3DFaceSetAsync.html)  
 [ void enuCreate3DCylinderAsync\(HX3D pX3DHandler, wchar\_t\* strID, float height, float radius, float slices, float transx, float transy, float transz\)](//ApplicationAPI/enuCreate3DCylinderAsync.html)  
 [ void enuCreate3DTerrainAsync\(HX3D pX3DHandler, wchar\_t\* strID, float size, float subdivision, float transx, float transy, float transz\)](//ApplicationAPI/enuCreate3DTerrainAsync.html)  
 [ void enuSetAttribute3DByNode\(HX3D pX3DHandler, HNODE pObject, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](//ApplicationAPI/enuSetAttribute3DByNode.html)   
 [ void enuSetAttribute3DByNodeSync\(HX3D pX3DHandler, HNODE pObject, wchar\_t\* pStrVariable, wchar\_t\* pStrValue, bool bHistory, bool bScript\)](//ApplicationAPI/enuSetAttribute3DByNodeSync.html)  
 [ void enuGetAttribute3DByNode\(HX3D pX3DHandler, HNODE pObject, wchar\_t\* pStrVariable, VariableStruct\* pData\)](//ApplicationAPI/enuGetAttribute3DByNode.html)  
 [ void enuSetAttribute3D\(HX3D pX3DHandler, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](//ApplicationAPI/enuSetAttribute3D.html)  
 [ HNODE enuGet3DObjectById\(HX3D pX3DHandler, wchar\_t\* objectid\)](//ApplicationAPI/enuGet3DObjectById.html)  
 [ HNODE enuGetAppearanceFromShape\(HX3D pX3DHandler, HNODE node\)](//ApplicationAPI/enuGetAppearanceFromShape.html)  
 [ HNODE enuGetGeometryFromShape\(HX3D pX3DHandler, HNODE node\)](//ApplicationAPI/enuGetGeometryFromShape.html)  
 [ HNODE enuGetMaterialFromAppearance\(HX3D pX3DHandler, HNODE node\)](//ApplicationAPI/enuGetMaterialFromAppearance.html)  
 [ HNODE enuGetMaterialFromGeometry\(HX3D pX3DHandler, HNODE node\)](//ApplicationAPI/enuGetMaterialFromGeometry.html)  
 [ HNODE enuGetTransformFromGeometry\(HX3D pX3DHandler, HNODE node\)](//ApplicationAPI/enuGetTransformFromGeometry.html)  
 [ HNODE enuGetCoordinateFromIndexedFaceSet\(HX3D pX3DHandler, HNODE node\)](//ApplicationAPI/enuGetCoordinateFromIndexedFaceSet.html)  
 [ HNODE enuGetCoordinateFromLineSet\(HX3D pX3DHandler, HNODE node\)](//ApplicationAPI/enuGetCoordinateFromLineSet.html)  
 [ HNODE enuGetShapeFromGeometry\(HX3D pX3DHandler, HNODE node\)](//ApplicationAPI/enuGetShapeFromGeometry.html)  
 [ void enuDelete3DObjectByNode\(HX3D pX3DHandler, HNODE pTarget\)](//ApplicationAPI/enuDelete3DObjectByNode.html)

## Script Interface

[ void enuSet3DLuaScriptByNode\(HX3D pX3D, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)](//ApplicationAPI/enuSet3DLuaScriptByNode.html)  
 [ void enuSet3DJavaScriptByNode\(HX3D pX3D, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)](//ApplicationAPI/enuSet3DJavaScriptByNode.html)  
 [ void enuExecute3DFunction\(HX3D pX3D, wchar\_t\* strFunction\)](//ApplicationAPI/enuExecute3DFunction.html)  
 [ void enuExecute3DFunctionByNode\(HX3D pX3D, HNODE pNode, wchar\_t\* strFunction\)](//ApplicationAPI/enuExecute3DFunctionByNode.html)

