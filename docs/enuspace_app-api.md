---
layout: default
title: Application API
has_children: true
nav_order: i
---



## Project Interface

[ bool enuLoadProjectFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuloadprojectfile.md)  
 [ HPROJECT enuCreateProject\(\)](./enusappapi_enucreateproject.md)  
 [ void enuDestoryProject\(HPROJECT pProject\)](./enusappapi_enudestoryproject.md)  
 [ bool enuSetActiveProject\(HPROJECT pHANDLE\)](./enusappapi_enusetactiveproject.md)  
 [ HPROJECT enuGetActiveProject\(\)](./enusappapi_enugetactiveproject.md)  
 [ void enuSetWidgetProject\(\)](./enusappapi_enusetwidgetproject.md)  
 [ bool enuSaveProjectFile\(\)](./enusappapi_enusaveprojectfile.md)  
 [ bool enuCloseProjectFile\(\)](./enusappapi_enucloseprojectfile.md)  
 [ wchar\_t\* enuGetProjectName\(\)](./enusappapi_enugetprojectname.md)  
 [ wchar\_t\* enuGetProjectFullName\(\)](./enusappapi_enugetprojectfullname.md)  
 [ wchar\_t\* enuGetProjectPath\(\)](./enusappapi_enugetprojectpath.md)  
 [ wchar\_t\* enuGetProjectType\(\)](./enusappapi_enugetprojecttype.md)  
 [ void enuSetProjectName\(wchar\_t\* projectname\)](./enusappapi_enusetprojectname.md)  
 [ void enuSetModifyProject\(bool bFlag\)](./enusappapi_enusetmodifyproject.md)  
 [ bool enuGetModifyProject\(\)](./enusappapi_enugetmodifyproject.md)

## Operation Interface

## Script Operation Interface

[ void enuSetScriptOperationMode\(bool bFlag\)](./enusappapi_enusetscriptoperationmode.md)  
 [ bool enuGetScriptOperationMode\(\)](./enusappapi_enugetscriptoperationmode.md)  
 [ void enuSetHMIScriptUpdateTime\(int iMiliSecond\)](./enusappapi_enusethmiscriptupdatetime.md)

## Edit Operation Interface

[ void enuSetEditOperationMode\(HVIEW pENUView, bool bFlag\)](./enusappapi_enuseteditoperationmode.md)  
 [ bool enuGetEditOperationMode\(HVIEW pENUVie\)](./enusappapi_enugeteditoperationmode.md)

## Mouse Interface

[ void enuSetLButtonDownCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](./enusappapi_enusetlbuttondowncallback.md)  
 [ void enuSetLButtonUpCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](./enusappapi_enusetlbuttonupcallback.md)  
 [ void enuSetRButtonDownCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](./enusappapi_enusetrbuttondowncallback.md)  
 [ void enuSetRButtonUpCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](./enusappapi_enusetrbuttonupcallback.md)  
 [ void enuSetMButtonDownCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](./enusappapi_enusetmbuttondowncallback.md)  
 [ void enuSetMButtonUpCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](./enusappapi_enusetmbuttonupcallback.md)  
 [ void enuSetMouseMoveCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](./enusappapi_enusetmousemovecallback.md)  
 [ void enuSetMouseWheelCallBack\(HVIEW pENUView, void functioncb\(float, float, float\) \)](./enusappapi_enusetmousewheelcallback.md)  
 [ void enuSetLButtonDblClkCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](./enusappapi_enusetlbuttondblclkcallback.md)  
 [ void enuOnMouseWheel\(HVIEW pENUView, UINT nFlags, short zDelta, CPoint pt\)](./enusappapi_enuonmousewheel.md)  
 [ POINTF enuGetLocalPosition\(HVIEW pENUView, POINT point\)](./enusappapi_enugetlocalposition.md)  
 [ POINT enuGetCursorPos\(\)](./enusappapi_enugetcursorpos.md)  
 [ void enuSetDefaultWheelControl\(HVIEW pENUView, bool bDefault\)](./enusappapi_enusetdefaultwheelcontrol.md)

## View Interface

[ void enuActivateView\(HVIEW pENUView\)](./enusappapi_enuactivateview.md)  
 [ void enuDeactivateView\(HVIEW pENUView\)](./enusappapi_enudeactivateview.md)  
 [ void enuSetRenderObjectPreReset\(HVIEW pENUView\)](./enusappapi_enusetrenderobjectprereset.md)  
 [ void enuSetRenderObjectReset\(HVIEW pENUView\)](./enusappapi_enusetrenderobjectreset.md)

## File IO Interface

[ HSVG enuLoadSvgPageFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuloadsvgpagefile.md)  
 [ HSVG enuLoadSvgHmiFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuloadsvghmifile.md)  
 [ HSVG enuLoadSvgLogicFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuloadsvglogicfile.md)  
 [ HSVG enuLoadSvgResourceFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuloadsvgresourcefile.md)  
 [ HSVG enuLoadSvgGlobalFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuloadsvgglobalfile.md)  
 [ HSVG enuNewSvgPageFile\(wchar\_t\* pStrFileName\)](./enusappapi_enunewsvgpagefile.md)  
 [ HSVG enuNewSvgHmiFile\(wchar\_t\* pStrFileName\)](./enusappapi_enunewsvghmifile.md)  
 [ HSVG enuNewSvgLogicFile\(wchar\_t\* pStrFileName\)](./enusappapi_enunewsvglogicfile.md)  
 [ HSVG enuNewSvgGlobalFile\(wchar\_t\* pStrFileName\)](./enusappapi_enunewsvgglobalfile.md)  
 [ HSVG enuNewSvgResourceFile\(wchar\_t\* pStrFileName\)](./enusappapi_enunewsvgresourcefile.md)  
 [ bool enuSaveAsSvgPageFile\(wchar\_t\* strTaget, wchar\_t\* strSource\)](./enusappapi_enusaveassvgpagefile.md)  
 [ bool enuSaveAsSvgHmiFile\(wchar\_t\* strTaget, wchar\_t\* strSource\)](./enusappapi_enusaveassvghmifile.md)  
 [ bool enuSaveAsSvgLogicFile\(wchar\_t\* strTaget, wchar\_t\* strSource\)](./enusappapi_enusaveassvglogicfile.md)  
 [ bool enuSaveAsSvgGlobalFile\(wchar\_t\* strTaget, wchar\_t\* strSource\)](./enusappapi_enusaveassvgglobalfile.md)  
 [ bool enuSaveAsSvgResourceFile\(wchar\_t\* strTaget, wchar\_t\* strSource\)](./enusappapi_enusaveassvgresourcefile.md)  
 [ bool enuSaveSvgFile\(HSVG pSvgHandler, wchar\_t\* strFileName= L""\)](./enusappapi_enusavesvgfile.md)  
 [ bool enuDeleteSvgPageFile\(wchar\_t\* pStrFileName\)](./enusappapi_enudeletesvgpagefile.md)  
 [ bool enuDeleteSvgHmiFile\(wchar\_t\* pStrFileName\)](./enusappapi_enudeletesvghmifile.md)  
 [ bool enuDeleteSvgLogicFile\(wchar\_t\* pStrFileName\)](./enusappapi_enudeletesvglogicfile.md)  
 [ bool enuDeleteSvgResourceFile\(wchar\_t\* pStrFileName\)](./enusappapi_enudeletesvgresourcefile.md)  
 [ bool enuDeleteSvgGlobalFile\(wchar\_t\* pStrFileName\)](./enusappapi_enudeletesvgglobalfile.md)  
 [ bool enuExportWebStyleSvg\(wchar\_t\* strTaget, wchar\_t\* strSource\)](./enusappapi_enuexportwebstylesvg.md)  
 [ void enuSetAutoSaveMode\(bool bAuto\)](./enusappapi_enusetautosavemode.md)

## File handle Interface
[ HSVG enuGetPageClass\(wchar\_t\* pStrFileName\)](./enusappapi_enugetpageclass.md)  
 [ HSVG enuGetSvgPageClass\(wchar\_t\* pStrFileName\)](./enusappapi_enugetsvgpageclass.md)  
 [ HSVG enuGetLogicClass\(wchar\_t\* pStrFileName\)](./enusappapi_enugetlogicclass.md)  
 [ HSVG enuGetHmiClass\(wchar\_t\* pStrFileName\)](./enusappapi_enugethmiclass.md)  
 [ HSVG enuGetGlobalClass\(wchar\_t\* pStrFileName\)](./enusappapi_enugetglobalclass.md)  
 [ HSVG enuGetResourceClass\(wchar\_t\* pStrFileName\)](./enusappapi_enugetresourceclass.md)  
 [ void\* enuGetPageList\(\)](./enusappapi_enugetpagelist.md)  
 [ void\* enuGetHmiList\(\)](./enusappapi_enugethmilist.md)  
 [ void\* enuGetLogicList\(\)](./enusappapi_enugetlogiclist.md)  
 [ void\* enuGetGlobalList\(\)](./enusappapi_enugetgloballist.md)  
 [ void\* enuGetResourceList\(\)](./enusappapi_enugetresourcelist.md)  
 [ bool enuGetModifyPage\(wchar\_t\* pStrFilename\)](./enusappapi_enugetmodifypage.md)  
 [ bool enuGetModifyHmi\(wchar\_t\* pStrFilename\)](./enusappapi_enugetmodifyhmi.md)  
 [ bool enuGetModifyLogic\(wchar\_t\* pStrFilename\)](./enusappapi_enugetmodifylogic.md)  
 [ bool enuGetModifyGlobal\(wchar\_t\* pStrFilename\)](./enusappapi_enugetmodifyglobal.md)  
 [ bool enuGetModifyResource\(wchar\_t\* pStrFilename\)](./enusappapi_enugetmodifyresource.md)
 [ bool enuSetPageProperty\(void\_t\* pPage, wchar\_t\* pAttribute, wchar\_t\* pValue\)](./enusappapi_enusetpageproperty.md)
 [ bool enuSetLogicProperty\(HSVG pSvg, wchar\_t\* pAttribute, wchar\_t\* pValue\)](./enusappapi_enusetlogicproperty.md)
 [ bool enuSetHmiProperty\(HSVG pSvg, wchar\_t\* pAttribute, wchar\_t\* pValue\)](./enusappapi_enusethmiproperty.md)
 [ bool enuSetGlobalProperty\(HSVG pSvg, wchar\_t\* pAttribute, wchar\_t\* pValue\)](./enusappapi_enusetglobalproperty.md) 
 [ bool enuSetResourceProperty\(HSVG pSvg, wchar\_t\* pAttribute, wchar\_t\* pValue\)](./enusappapi_enusetresourceproperty.md)  
## Library Interface

[ bool enuLogicCreateSymbolNode\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)](./enusappapi_enulogiccreatesymbolnode.md)  
 [ bool enuLogicCreateSymbolLink\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)](./enusappapi_enulogiccreatesymbollink.md)  
 [ bool enuHmiCreateSymbol\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)](./enusappapi_enuhmicreatesymbol.md)  
 [ bool enuResourceCreateStyle\(wchar\_t\* pStrFilename, wchar\_t\* pStrStyle\)](./enusappapi_enuresourcecreatestyle.md)  
 [ bool enuDeleteLogicSymbol\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)](./enusappapi_enudeletelogicsymbol.md)  
 [ bool enuDeleteHmiSymbol\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)](./enusappapi_enudeletehmisymbol.md)  
 [ wchar\_t\* enuLogicGetSymbolType\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)](./enusappapi_enulogicgetsymboltype.md)  
 [ void\* enuGetHmiSymbolList\(wchar\_t\* pStrFilename\)](./enusappapi_enugethmisymbollist.md)  
 [ void\* enuGetLogicSymbolList\(wchar\_t\* pStrFilename\)](./enusappapi_enugetlogicsymbollist.md)

## Global Interface

[ bool enuAddGlobalStruct\(wchar\_t\* pStrFileName, wchar\_t\* pStrStructName, CPtrList\* pItem\)](./enusappapi_enuaddglobalstruct.md)  
 [ void\* enuGetGlobalPgStructList\(wchar\_t\* pStrFileName\)](./enusappapi_enugetglobalpgstructlist.md)  
 [ void\* enuGetGlobalVariableList\(wchar\_t\* pStrFileName\)](./enusappapi_enugetglobalvariablelist.md)  
 [ void\* enuGetGlobalPgAttributeList\(wchar\_t\* pStrFileName, wchar\_t\* pStrStructName\)](./enusappapi_enugetglobalpgattributelist.md)  
 [ HNODE enuGetGlobalVariableNode\(wchar\_t\* pStrVariable\)](./enusappapi_enugetglobalvariablenode.md)  
 [ bool enuAddGlobalVariable\(wchar\_t\* pStrFileName, wchar\_t\* pStrType, wchar\_t\* strVariable, wchar\_t\* strInitValue=L"", wchar\_t\* strDescription=L""\)](./enusappapi_enuaddglobalvariable.md)  
 [ bool enuDeleteGlobalVariable\(wchar\_t\* pStrFileName, wchar\_t\* strVariable\)](./enusappapi_enudeleteglobalvariable.md)  
 [ bool enuModifyGlobalVariable\(wchar\_t\* pStrFileName, wchar\_t\* strVariable, wchar\_t\* strNewType, wchar\_t\* strNewVariable, wchar\_t\* strNewDescription\)](./enusappapi_enumodifyglobalvariable.md)  
 [ bool enuDeleteGlobalStruct\(wchar\_t\* pStrFileName, wchar\_t\* strStruct\)](./enusappapi_enudeleteglobalstruct.md)  
 [ bool enuModifyGlobalStruct\(wchar\_t\* pStrFileName, wchar\_t\* strStruct, wchar\_t\* strNewStruct, CPtrList\* pItem\)](./enusappapi_enumodifyglobalstruct.md)  
 [ void enuReloadPicture\(HVIEW pENUView\)](./enusappapi_enureloadpicture.md)  
 [ bool enuIsModifyPage\(HVIEW pENUView\)](./enusappapi_enuismodifypage.md)

## Window Interface

[ void enuSetZoomScale\(HVIEW pENUView, float fPercent\)](./enusappapi_enusetzoomscale.md)  
 [ float enuGetZoomScale\(HVIEW pENUView\)](./enusappapi_enugetzoomscale.md)  
 [ float enuGetCanvasWidth\(HVIEW pENUView\)](./enusappapi_enugetcanvaswidth.md)  
 [ float enuGetCanvasHeight\(HVIEW pENUView\)](./enusappapi_enugetcanvasheight.md)  
 [ void enuSetCanvasSize\(HVIEW pENUView, float cx, float cy\)](./enusappapi_enusetcanvassize.md)  
 [ void enuSetMoveCanvas\(HVIEW pENUView, float transx, float transy\)](./enusappapi_enusetmovecanvas.md)  
 [ void enuGetMoveCanvas\(HVIEW pENUView, float\* transx, float\* transy\)](./enusappapi_enugetmovecanvas.md)  
 [ void enuSetCanvasColor\(HVIEW pENUView, byte iR, byte iG, byte iB\)](./enusappapi_enusetcanvascolor.md)  
 [ void enuSetWindowColor\(HVIEW pENUView, byte iR, byte iG, byte iB\)](./enusappapi_enusetwindowcolor.md)  
 [ bool enuSelConnectionPin\(HVIEW pENUView, wchar\_t\* strPicture, wchar\_t\* strSymbol\)](./enusappapi_enuselconnectionpin.md)  
 [ bool enuIsEnableConnectionPin\(HVIEW pENUView\)](./enusappapi_enuisenableconnectionpin.md)

## Symbol Interface

[ float enuGetSymbolWidth\(HVIEW pENUView, wchar\_t\* strSymbol\)](./enusappapi_enugetsymbolwidth.md)  
 [ float enuGetSymbolHeight\(HVIEW pENUView, wchar\_t\* strSymbol\)](./enusappapi_enugetsymbolheight.md)  
 [ void enuSetSymbolSize\(HVIEW pENUView,  wchar\_t\* strSymbol, float fWidth, float fHeight\)](./enusappapi_enusetsymbolsize.md)

## Edit Interface

[ void enuSetSelectToolBar\(int iSel\)](./enusappapi_enusetselecttoolbar.md)  
 [ void enuSetCallBackSelectToolBar\(void fcbSelectToolBar\(int\)\)](./enusappapi_enusetcallbackselecttoolbar.md)  
 [ void enuSetCallBackSelectEvent\(void fcbSelectObject\(CPtrList\*, void\*\)\)](./enusappapi_enusetcallbackselectevent.md)  
 [ void enuSetCallBackDebugMessage\(void fcbDebugMessage\(wchar\_t\*\)\)](./enusappapi_enusetcallbackdebugmessage.md)  
 [ bool enuIsEnablePaste\(\)](./enusappapi_enuisenablepaste.md)  
 [ bool enuIsSelectObject\(HVIEW pENUView\)](./enusappapi_enuisenablepaste.md)  
 [ void enuSetSelectFontname\(HVIEW pENUView,  wchar\_t\* strFontName\)](./enusappapi_enusetselectfontname.md)  
 [ void enuSetSelectFontsize\(HVIEW pENUView,  float fSize\)](./enusappapi_enusetselectfontsize.md)  
 [ void enuSetSelectFontcolor\(HVIEW pENUView,  wchar\_t\* strFontColor\)](./enusappapi_enusetselectfontcolor.md)  
 [ void enuSetSelectFontIncrease\(HVIEW pENUView\)](./enusappapi_enusetselectfontincrease.md)  
 [ void enuSetSelectFontDecrease\(HVIEW pENUView\)](./enusappapi_enusetselectfontdecrease.md)  
 [ void enuSetSelectFontBold\(HVIEW pENUView, bool bFlag\)](./enusappapi_enusetselectfontbold.md)  
 [ void enuSetSelectFontItalic\(HVIEW pENUView, bool bFlag\)](./enusappapi_enusetselectfontitalic.md)  
 [ void enuSetSelectFontUnderline\(HVIEW pENUView, bool bFlag\)](./enusappapi_enusetselectfontunderline.md)  
 [ void enuSetSelectFontStrikethough\(HVIEW pENUView, bool bFlag\)](./enusappapi_enusetselectfontstrikethough.md)  
 [ void enuSetSelectFontSubscript\(HVIEW pENUView, bool bFlag\)](./enusappapi_enusetselectfontsubscript.md)  
 [ void enuSetSelectFontSuperscript\(HVIEW pENUView, bool bFlag\)](./enusappapi_enusetselectfontsuperscript.md)  
 [ void enuSetSelectFontHilight\(HVIEW pENUView, bool bFlag\)](./enusappapi_enusetselectfonthilight.md)  
 [ bool enuIsSelectFontBold\(HVIEW pENUView\)](./enusappapi_enuisselectfontbold.md)  
 [ bool enuIsSelectFontItalic\(HVIEW pENUView\)](./enusappapi_enuisselectfontitalic.md)  
 [ bool enuIsSelectFontUnderline\(HVIEW pENUView\)](./enusappapi_enuisselectfontunderline.md)  
 [ bool enuIsSelectFontStrikethough\(HVIEW pENUView\)](./enusappapi_enuisselectfontstrikethough.md)  
 [ bool enuIsSelectFontSubscript\(HVIEW pENUView\)](./enusappapi_enuisselectfontsubscript.md)  
 [ bool enuIsSelectFontSuperscript\(HVIEW pENUView\)](./enusappapi_enuisselectfontsuperscript.md)  
 [ void enuSetSelectFillcolor\(HVIEW pENUView,  wchar\_t\* strColor\)](./enusappapi_enusetselectfillcolor.md)  
 [ void enuSetSelectFillOpacity\(HVIEW pENUView, wchar\_t\* strOpacity\)](./enusappapi_enusetselectfillopacity.md)  
 [ void enuSetSelectLinecolor\(HVIEW pENUView,  wchar\_t\* strColor\)](./enusappapi_enusetselectlinecolor.md)  
 [ void enuSetSelectLineOpacity\(HVIEW pENUView, wchar\_t\* strOpacity\)](./enusappapi_enusetselectlineopacity.md)  
 [ void enuSetSelectLineWidth\(HVIEW pENUView, float fWidth\)](./enusappapi_enusetselectlinewidth.md)  
 [ void enuSetSelectLineDashes\(HVIEW pENUView, wchar\_t\* strDashes\)](./enusappapi_enusetselectlinedashes.md)  
 [ void enuSetSelectAlign\(HVIEW pENUView, int iType\)](./enusappapi_enusetselectalign.md)  
 [ void enuSetSelectRotation\(HVIEW pENUView, float fAngle\)](./enusappapi_enusetselectrotation.md)  
 [ void enuSetSelectFlip\(HVIEW pENUView, int iType\)](./enusappapi_enusetselectflip.md)  
 [ HNODE enuGetSelectSingleObject\(HVIEW pENUView\)](./enusappapi_enugetselectsingleobject.md)  
 [ void enuSetSelectAll\(HVIEW pENUView\)](./enusappapi_enusetselectall.md)  
 [ bool enuSetSelectObject\(HVIEW pENUView, wchar\_t\* strSelectID\)](./enusappapi_enusetselectobject.md)  
 [ void enuSetFindObjectCallBack\(void fcbFindMessage\(HNODE, int, wchar\_t\*, wchar\_t\*\), wchar\_t\* pStrSearch, bool bMatchCase, bool bWholeWord\)](./enusappapi_enusetfindobjectcallback.md)  
 [ wchar\_t\* enuGetPrevPageName\(wchar\_t\* pStrFileName\)](./enusappapi_enugetprevpagename.md)  
 [ wchar\_t\* enuGetNextPageName\(wchar\_t\* pStrFileName\)](./enusappapi_enugetnextpagename.md)  
 [ void enuSetSelectZOrder\(HVIEW pENUView, int iType\)](./enusappapi_enusetselectzorder.md)  
 [ void enuSetSelectGroup\(HVIEW pENUView\)](./enusappapi_enusetselectgroup.md)  
 [ void enuSetSelectUnGroup\(HVIEW pENUView\)](./enusappapi_enusetselectungroup.md)  
 [ void enuMoveObjectUp\(HVIEW pENUView\)](./enusappapi_enumoveobjectup.md)  
 [ void enuMoveObjectDown\(HVIEW pENUView\)](./enusappapi_enumoveobjectdown.md)  
 [ void enuMoveObjectLeft\(HVIEW pENUView\)](./enusappapi_enumoveobjectleft.md)  
 [ void enuMoveObjectRight\(HVIEW pENUView\)](./enusappapi_enumoveobjectright.md)  
 [ void enuSetEditCopy\(HVIEW pENUView\)](./enusappapi_enuseteditcopy.md)  
 [ void enuSetEditCut\(HVIEW pENUView\)](./enusappapi_enuseteditcut.md)  
 [ void enuSetEditPaste\(HVIEW pENUView\)](./enusappapi_enuseteditpaste.md)  
 [ void enuSetEditLock\(HVIEW pENUView\)](./enusappapi_enuseteditlock.md)  
 [ void enuSetEditUnLock\(HVIEW pENUView\)](./enusappapi_enuseteditunlock.md)  
 [ void enuSetEditUndo\(HVIEW pENUView\)](./enusappapi_enuseteditundo.md)  
 [ void enuSetEditRedo\(HVIEW pENUView\)](./enusappapi_enuseteditredo.md)  
 [ bool enuIsEditUndo\(HVIEW pENUView\)](./enusappapi_enuiseditundo.md)  
 [ bool enuIsEditRedo\(HVIEW pENUView\)](./enusappapi_enuiseditredo.md)

## Runtime Interface

[ void enuSetCallBackAddTable\( void fcbAddTable\(HNODE\) \)](./enusappapi_enusetcallbackaddtable.md)  
 [ HSVG enuNewSvgExternalPageFile\(wchar\_t\* pFileName\)](./enusappapi_enunewsvgexternalpagefile.md)  
 [ HSVG enuLoadSvgExternalPageFile\(wchar\_t\* pFileName\)](./enusappapi_enuloadsvgexternalpagefile.md)  
 [ bool enuDeleteSvgExternalPageFile\(wchar\_t\* pFileName\)](./enusappapi_enudeletesvgexternalpagefile.md)  
 [ bool enuSetSvgExternalPageView\(HVIEW pENUView, HSVG pSvg\)](./enusappapi_enusetsvgexternalpageview.md)  
 [ bool enuShowRuntimeView\(HWND hWnd\)](./enusappapi_enushowruntimeview.md)  
 [ void enuDestoryRuntimeView\(\)](./enusappapi_enudestoryruntimeview.md)  
 [ bool enuIsRuntimeView\(\)](./enusappapi_enuisruntimeview.md)  
 [ void enuChangePicture\(wchar\_t\* strWindow, wchar\_t\* strPicName\)](./enusappapi_enuchangepicture.md)  
 [ void enuChangePictureAsync\(wchar\_t\* strWindow, wchar\_t\* strPicName\)](./enusappapi_enuchangepictureasync.md)  
 [ void enuSaveImageToFile\(HVIEW pENUView, wchar\_t\* strFileName, wchar\_t\* strFileType\)](./enusappapi_enusaveimagetofile.md)  
 [ void enuSetModifyUseHref\(wchar\_t\* strSrcId, wchar\_t\* strNewId\)](./enusappapi_enusetmodifyusehref.md)  
 [ bool enuGetWindowSize\(wchar\_t\* strWindowID, RECT\* rect\)](./enusappapi_enugetwindowsize.md)  
 [ bool enuSetWindowSize\(wchar\_t\* strWindowID, int x, int y, int width, int height\)](./enusappapi_enusetwindowsize.md)  
 [ bool enuRegisterFunction\(wchar\_t\* strFunction, int \(\*pfunc\)\(lua\_State\* L\)\)](./enusappapi_enuregisterfunction.md)  
 [ HVIEW enuGetWindowView\(wchar\_t\* strWindowID\)](./enusappapi_enugetwindowview.md)

## View Interface

[ HVIEW enuCreateView\(HWND hWnd\)](./enusappapi_enucreateview.md)  
 [ void enuDestoryView\(HVIEW pENUView\)](./enusappapi_enudestoryview.md)  
 [ void enuSetViewID\(HVIEW pENUView, wchar\_t\* strID\)](./enusappapi_enusetviewid.md)  
 [ void enuSetComponentMode\(HVIEW pView, bool bOper\)](./enusappapi_enusetcomponentmode.md)  
 [ void enuUpdateScreen\(HVIEW pENUView\)](./enusappapi_enuupdatescreen.md)  
 [ void enuInvalidateView\(HVIEW pENUView\)](./enusappapi_enuinvalidateview.md)  
 [ bool enuSetLogicComponent\(HVIEW pENUView, wchar\_t\* pStrFileName, wchar\_t\* pStrSymbol\)](./enusappapi_enusetlogiccomponent.md)  
 [ bool enuSetHmiComponent\(HVIEW pENUView, wchar\_t\* pStrFileName, wchar\_t\* pStrSymbol\)](./enusappapi_enusethmicomponent.md) 
 [ bool enuSetSvgView\(HVIEW pENUView, HSVG\_t\* pSvg\)](./enusappapi_enusetsvgview.md)  
 [ bool enuSetSvgPageView\(HVIEW pENUView, wchar\_t\* pStrFileName\)](./enusappapi_enusetsvgpageview.md)  
 [ bool enuSetSvgHmiView\(HVIEW pENUView, wchar\_t\* pStrFileName\)](./enusappapi_enusetsvghmiview.md)  
 [ bool enuSetSvgLogicView\(HVIEW pENUView, wchar\_t\* pStrFileName\)](./enusappapi_enusetsvglogicview.md)  
 [ HSVG enuGetSvgHandler\(HVIEW pENUView\)](./enusappapi_enugetsvghandler.md)  
 [ void enuSetWindowPos\(HVIEW pENUView, int x, int y, int cx, int cy\)](./enusappapi_enusetwindowpos.md)  
 [ void enuSetWindowCenter\(HVIEW pENUView\)](./enusappapi_enusetwindowcenter.md)

## Object Interface

[ void enuSetSymbolValue\(HSVG pSvgHandler, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](./enusappapi_enusetsymbolvalue.md)  
 [ void enuSetSymbolValueByNode\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](./enusappapi_enusetsymbolvaluebynode.md)  
 [ void enuSetGlobalValue\(HSVG pSvgHandler, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](./enusappapi_enusetglobalvalue.md)  
 [ void enuDeleteObjectByName\(HSVG pSvgHandler, wchar\_t\* pStrVariable\)](./enusappapi_enudeleteobjectbyname.md)  
 [ void enuDeleteObjectByNode\(HSVG pSvgHandler, HNODE pTarget\)](./enusappapi_enudeleteobjectbynode.md)  
 [ void enuDeleteUseObjectByHref\(HSVG pSvgHandler, wchar\_t\* pStrHref\)](./enusappapi_enudeleteuseobjectbyhref.md)  
 [ void enuDeleteAllObject\(HSVG pSvgHandler\)](./enusappapi_enudeleteallobject.md)  
 [ void enuSetAttribute\(HSVG pSvgHandler, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](./enusappapi_enusetattribute.md)  
 [ void enuSetAttributeByNode\(HSVG pSvgHandler, HNODE pObject, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](./enusappapi_enusetattributebynode.md)  
 [ bool enuSetAttributeByNodeSync\(HSVG pSvgHandler, HNODE pObject, wchar\_t\* pStrVariable, wchar\_t\* pStrValue, bool bHistory=false, bool bScript=false\)](./enusappapi_enusetattributebynodesync.md)  
 [ void enuGetAttributeByNode\(HSVG pSvgHandler, HNODE pObject, wchar\_t\* pStrVariable, VariableStruct\* pData\)](./enusappapi_enugetattributebynode.md)  
 [ HNODE enuAddTrendSeriesByNode\(HSVG pSvgHandler, HNODE TrendNode, wchar\_t\* strSeriesID\)](./enusappapi_enuaddtrendseriesbynode.md)  
 [ void enuSetUseInterfaceByNode\(HSVG pSvgHandler, HNODE pUse, wchar\_t\* strVariable, wchar\_t\* strValue\)](./enusappapi_enusetuseinterfacebynode.md)  
 [ void enuSetUseInterface\(HSVG pSvgHandler, wchar\_t\* strVariable, wchar\_t\* strValue\)](./enusappapi_enusetuseinterface.md)  
 [ HNODE enuGetObjectById\(HSVG pSvgHandler, wchar\_t\* objectid\)](./enusappapi_enugetobjectbyid.md)  
 [ HNODE enuGetDefsSymbolById\(HSVG pSvgHandler, wchar\_t\* objectid\)](./enusappapi_enugetdefssymbolbyid.md) 
 [ HNODE enuCreateLine\(HSVG pSvgHandler, wchar\_t\* strID, float x1, float y1, float x2, float y2, float transx, float transy\)](./enusappapi_enucreateline.md)  
 [ HNODE enuCreatePolyline\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy\)](./enusappapi_enucreatepolyline.md)  
 [ HNODE enuCreatePolygon\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy\)](./enusappapi_enucreatepolygon.md)  
 [ HNODE enuCreateCircle\(HSVG pSvgHandler, wchar\_t\* strID, float r, float cx, float cy, float transx, float transy\)](./enusappapi_enucreatecircle.md)  
 [ HNODE enuCreateEllipse\(HSVG pSvgHandler, wchar\_t\* strID, float rx, float ry, float cx, float cy, float transx, float transy\)](./enusappapi_enucreateellipse.md)  
 [ HNODE enuCreateRect\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, float transx, float transy\)](./enusappapi_enucreaterect.md)  
 [ HNODE enuCreateText\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float dx, float dy, wchar\_t\* text, float transx, float transy\)](./enusappapi_enucreatetext.md)  
 [ HNODE enuCreateImage\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, wchar\_t\* xlink\_href, float transx, float transy\)](./enusappapi_enucreateimage.md)  
 [ HNODE enuCreateTrend\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, float transx, float transy\)](./enusappapi_enucreatetrend.md)  
 [ HNODE enuCreatePath\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* pStrValue, float transx, float transy\)](./enusappapi_enucreatepath.md)  
 [ HNODE enuCreateUse\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, wchar\_t\* xlink\_href, wchar\_t\* strType, float transx = 0, float transy = 0\)](./enusappapi_enucreateuse.md)  
 [ void enuCreateLineAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x1, float y1, float x2, float y2, float transx, float transy\)](./enusappapi_enucreatelineasync.md)  
 [ void enuCreatePolylineAsync\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy\)](./enusappapi_enucreatepolylineasync.md)  
 [ void enuCreatePolygonAsync\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy\)](./enusappapi_enucreatepolygonasync.md)  
 [ void enuCreateCircleAsync\(HSVG pSvgHandler, wchar\_t\* strID, float r, float cx, float cy, float transx, float transy\)](./enusappapi_enucreatecircleasync.md)  
 [ void enuCreateEllipseAsync\(HSVG pSvgHandler, wchar\_t\* strID, float rx, float ry, float cx, float cy, float transx, float transy\)](./enusappapi_enucreateellipseasync.md)  
 [ void enuCreateRectAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, float transx, float transy\)](./enusappapi_enucreaterectasync.md)  
 [ void enuCreateTextAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float dx, float dy, wchar\_t\* text, float transx, float transy\)](./enusappapi_enucreatetextasync.md)  
 [ void enuCreateImageAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, wchar\_t\* xlink\_href, float transx, float transy\)](./enusappapi_enucreateimageasync.md)  
 [ void enuCreateTrendAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, float transx, float transy\)](./enusappapi_enucreatetrendasync.md)  
 [ void enuCreatePathAsync\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* pStrValue, float transx, float transy\)](./enusappapi_enucreatepathasync.md)  
 [ void enuCreateUseAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, wchar\_t\* xlink\_href, wchar\_t\* strType, float transx, float transy\)](./enusappapi_enucreateuseasync.md)  
 [ void enuSetEditDelete\(HVIEW pENUView\)](./enusappapi_enuseteditdelete.md)  
 [ void enuSetEditDeleteAsync\(HVIEW pENUView\)](./enusappapi_enuseteditdeleteasync.md)  
 [ void enuExecuteString\(wchar\_t\* pStrPageName, wchar\_t\* pStrEvent\)](./enusappapi_enuexecutestring.md)  
 [ void enuSetVariableValue\(HSVG pSvgHandler, wchar\_t\* strVariable, wchar\_t\* strValue\)](./enusappapi_enusetvariablevalue.md)  
 [ HNODE enuCreateUseAtView\(HVIEW pENUView, float transx, float transy, wchar\_t\* xlink\_href, wchar\_t\* strType\)](./enusappapi_enucreateuseatview.md)  
 [ HNODE enuCreateImageAtView\(HVIEW pENUView, wchar\_t\* strID, float x, float y, float width, float height, wchar\_t\* xlink\_href, float transx, float transy\)](./enusappapi_enucreateimageatview.md)  
 [ HNODE enuDuplicateLogicSymbol\(wchar\_t\* strPicture, wchar\_t\* strSymbol\)](./enusappapi_enuduplicatelogicsymbol.md)  
 [ HNODE enuDuplicateHmiSymbol\(wchar\_t\* strPicture, wchar\_t\* strSymbol\)](./enusappapi_enuduplicatehmisymbol.md)  
 [ void enuSetUseAttribute\_interface\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strValue\)](./enusappapi_enusetuseattribute_interface.md)  
 [ void enuSetUseAttribute\_interface\_id\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strValue\)](./enusappapi_enusetuseattribute_interface_id.md)  
 [ void enuGetVariablePointer\(HSVG pSvgHandler, wchar\_t\* pStrVariable, VariableStruct\* pData\)](./enusappapi_enugetvariablepointer.md)  
 [ void enuSetReShapeArrayValue\(wchar\_t\* pVariable, void\* fValue, int iType, int iSize\)](./enusappapi_enusetreshapearrayvalue.md)  
 [ bool enuSetModifySymbolAccept\(wchar\_t\* strPicture, wchar\_t\* strSymbol, int iFileType\)](./enusappapi_enusetmodifysymbolaccept.md)

## Script Interface

[ void enuExecuteFunction\(HSVG pSvgHandler, wchar\_t\* strFunction\)](./enusappapi_enuexecutefunction.md)  
 [ void enuExecuteFunctionByNode\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strFunction\)](./enusappapi_enuexecutefunctionbynode.md)  
 [ void enuSetLuaScriptByNode\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)](./enusappapi_enusetluascriptbynode.md)  
 [ void enuSetJavaScriptByNode\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)](./enusappapi_enusetjavascriptbynode.md)  
 [ bool enuRegisterLuaScript\(wchar\_t\* pStrScript\)](./enusappapi_enuregisterluascript.md)  
 [ wchar\_t\* enuExecuteLuaScript\(wchar\_t\* pStrExecute\)](./enusappapi_enuexecuteluascript.md)  
 [ bool enuRegisterJavaScript\(wchar\_t\* pStrScript\)](./enusappapi_enuregisterjavascript.md)  
 [ wchar\_t\* enuExecuteJavaScript\(wchar\_t\* pStrExecute\)](./enusappapi_enuexecutejavascript.md)  
 [ void enuRegisterLuaScriptById\(wchar\_t\* strPagename, wchar\_t\* strID, wchar\_t\* strFunction, wchar\_t\* strScript\)](./enusappapi_enuregisterluascriptbyid.md)  
 [ void enuRegisterJavaScriptById\(wchar\_t\* strPagename, wchar\_t\* strID, wchar\_t\* strFunction, wchar\_t\* strScript\)](./enusappapi_enuregisterjavascriptbyid.md)  
 [ void enuRegisterLuaScriptByNode\(wchar\_t\* strPagename, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)](./enusappapi_enuregisterluascriptbynode.md)  
 [ void enuRegisterJavaScriptByNode\(wchar\_t\* strPagename, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)](./enusappapi_enuregisterjavascriptbynode.md)

## Widget Interface

[ HVIEW enuCreateWidget\(HWND hWnd\)](./enusappapi_enucreatewidget.md)  
 [ void enuDestoryWidget\(HVIEW pView\)](./enusappapi_enudestorywidget.md)  
 [ bool enuSetWidgetSize\(HVIEW pENUView, int x, int y, int width, int height\)](./enusappapi_enusetwidgetsize.md)  
 [ HNODE enuCreateUseWidget\(HVIEW pENUView, float transx, float transy, wchar\_t\* xlink\_href, wchar\_t\* strType\)](./enusappapi_enucreateusewidget.md)  
 [ HNODE enuCreateImageWidget\(HVIEW pENUView, wchar\_t\* xlink\_href\)](./enusappapi_enucreateimagewidget.md)  
 [ HNODE enuCreateTrendWidget\(HVIEW pENUView, float x, float y, float width, float height, float transx, float transy, float angle\)](./enusappapi_enucreatetrendwidget.md)  
 [ void enuWidgetFunctionByNode\(HVIEW pENUView, HNODE pNode, wchar\_t\* strFunction\)](./enusappapi_enuwidgetfunctionbynode.md)

## Runtime Interface

[ void enuShowDebugMessage\(bool bShow\)](./enusappapi_enushowdebugmessage.md)  
 [ void enuSetRuntimeMode\(bool bRunTime\)](./enusappapi_enusetruntimemode.md)  
 [ void enuOpenWindow\(wchar\_t\* strWindow, float posX, float posY, wchar\_t\* strHref\)](./enusappapi_enuopenwindow.md)  
 [ void enuCloseWindow\(wchar\_t\* strWindow\)](./enusappapi_enuclosewindow.md)  
 [ void enuMoveWindow\(wchar\_t\* strWindow, float posX, float posY\)](./enusappapi_enumovewindow.md)  
 [ void enuSetRuntimeView\(HVIEW pENUView, bool bRuntime\)](./enusappapi_enusetruntimeview.md)  
 [ void\* enuCreatePopupTrend\(int iType, wchar\_t\* strVariables, int x = 0, int y = 0, int width = 0, int height = 0\)](./enusappapi_enucreatepopuptrend.md)  
 [ void enuDestoryPopupTrend\(void\* pTrend\)](./enusappapi_enudestorypopuptrend.md)

## DataBase Interface

[ void enuSetDBGeneration\(\)](./enusappapi_enusetdbgeneration.md)  
 [ void enuShowTagList\(\)](./enusappapi_enushowtaglist.md)  
 [ void enuShowDeviceList\(\)](./enusappapi_enushowdevicelist.md)  
 [ void enuSelectObjectListClear\(HVIEW pENUView\)](./enusappapi_enuselectobjectlistclear.md)  
 [ void enuAddSelectObjectByNode\(HVIEW pENUView, HNODE hNode\)](./enusappapi_enuaddselectobjectbynode.md)

## Configuration Interface

[ wchar\_t\* enuGetConfiguration\(wchar\_t\* pAttribute\)](./enusappapi_enugetconfiguration.md)  
 [ bool enuSetConfiguration\(wchar\_t\* pAttribute, wchar\_t\* pValue\)](./enusappapi_enusetconfiguration.md)  
 [ void enuShowUserList\(\)](./enusappapi_enushowuserlist.md)

## Communication Interface

[ bool enuIsWebServerStart\(\)](./enusappapi_enuiswebserverstart.md)  
 [ bool enuIsEnuServerStart\(\)](./enusappapi_enuisenuserverstart.md)  
 [ void enuWebServerStart\(\)](./enusappapi_enuwebserverstart.md)  
 [ void enuWebServerStop\(\)](./enusappapi_enuwebserverstop.md)  
 [ void enuLinkServerStart\(\)](./enusappapi_enulinkserverstart.md)  
 [ void enuLinkServerStop\(\)](./enusappapi_enulinkserverstop.md)  
 [ void enuSendNetData\(wchar\_t\* system, char\* data, int length\)](./enusappapi_enusendnetdata.md)  
 [ void enuRecvNetData\(void functioncb\(wchar\_t\* system, char\* buffer, int length\)\)](./enusappapi_enurecvnetdata.md)

## Media Interface

[ void enuPlaySoundX\(wchar\_t\* wavfilename\)](./enusappapi_enuplaysoundx.md)  
 [ void enuStopSoundX\(wchar\_t\* wavfilename\)](./enusappapi_enustopsoundx.md)  
 [ void enuSetVolumeX\(int iVolume\)](./enusappapi_enusetvolumex.md)

## Task Operation Interface

[ void enuSetTaskOperationMode\(int iMode, int iStep\)](./enusappapi_enusettaskoperationmode.md)  
 [ bool enuAddTask\(wchar\_t\* pStrTaskID, wchar\_t\* pStrTaskModule, wchar\_t\* pStrCycle\)](./enusappapi_enuaddtask.md)  
 [ bool enuRemoveTask\(wchar\_t\* pStrTaskID)](./enusappapi_enuremovetask.md)   
 [ wchar\_t\* enuGetTaskList\(\)](./enusappapi_enugettasklist.md)  
 [ TaskStruct\* enuGetTaskProperty\(wchar\_t\* pStrTaskID\)](./enusappapi_enugettaskproperty.md)  
 [ bool enuSetTaskProperty\(wchar\_t\* pStrTaskID, wchar\_t\* pStrProp, wchar\_t\* pStrValue\)](./enusappapi_enusettaskproperty.md)  
 [ void enuSetSnapFile\(wchar\_t\* strFilename\)](./enusappapi_enusetsnapfile.md)  
 [ void enuSetResetFile\(wchar\_t\* strFilename\)](./enusappapi_enusetresetfile.md)  
 [ \_\_int64 enuGetCurrentTime\(\)](./enusappapi_enugetcurrenttime.md)

## 3D Interface

## View Interface

[ HVIEW enuCreate3DView\(HWND hWnd\)](./enusappapi_enucreate3dview.md)  
 [ bool enuSetX3dPageView\(HVIEW pENUView, wchar\_t\* pStrFileName\)](./enusappapi_enusetx3dpageview.md)  
 [ HX3D enuGetX3DHandler\(HVIEW pENUView\)](./enusappapi_enugetx3dhandler.md)

## File IO Interface

[ HX3D enuNewX3DPageFile\(wchar\_t\* pStrFileName\)](./enusappapi_enunewx3dpagefile.md)  
 [ HSVG enuLoadX3DPageFile\(wchar\_t\* pStrFileName\)](./enusappapi_enuloadx3dpagefile.md)  
 [ bool enuSaveX3DFile\(HX3D pX3DHandler, wchar\_t\* strFileName = L""\)](./enusappapi_enusavex3dfile.md)  
 [ bool enuDeleteX3dPageFile\(wchar\_t\* pStrFileName\)](./enusappapi_enudeletex3dpagefile.md)

## File handle Interface

[ HX3D enuGetX3dPageClass\(wchar\_t\* pStrFileName\)](./enusappapi_enugetx3dpageclass.md)

## Edit Interface

[ void enuSetCallBackSelectEvent3D\(void fcbSelectObject\(CPtrList\*, void\*\)\)](./enusappapi_enusetcallbackselectevent3d.md)  
 [ void enuSetSelectDiffuseColor\(HVIEW pENUView, wchar\_t\* strColor\)](./enusappapi_enusetselectdiffusecolor.md)  
 [ void enuSetSelectEmissiveColor\(HVIEW pENUView, wchar\_t\* strColor\)](./enusappapi_enusetselectemissivecolor.md)  
 [ void enuSetSelectSpecularColor\(HVIEW pENUView, wchar\_t\* strColor\)](./enusappapi_enusetselectspecularcolor.md)  
 [ void enuSetSelect3DToolBar\(int iSel\)](./enusappapi_enusetselect3dtoolbar.md)  
 [ void enuSetCallBackSelect3DToolBar\(void fcbSelectToolBar\(int\)\)](./enusappapi_enusetcallbackselect3dtoolbar.md)

## Window Interface

[ void enuSetMove3DCanvas\(HVIEW pENUView, float transx, float transy, float transz\)](./enusappapi_enusetmove3dcanvas.md)

## Object Interface

[ HNODE enuCreate3DSphere\(HX3D pX3DHandler, wchar\_t\* strID, float radius, float slices, float transx, float transy, float transz\)](./enusappapi_enucreate3dsphere.md)  
 [ HNODE enuCreate3DCone\(HX3D pX3DHandler, wchar\_t\* strID, float bottomRadius, float height, float slices, float transx, float transy, float transz\)](./enusappapi_enucreate3dcone.md)  
 [ HNODE enuCreate3DBox\(HX3D pX3DHandler, wchar\_t\* strID, float size, float transx, float transy, float transz\)](./enusappapi_enucreate3dbox.md)  
 [ HNODE enuCreate3DText\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strString, wchar\_t\* strValue, float fontSize, float transx, float transy, float transz\)](./enusappapi_enucreate3dtext.md)  
 [ HNODE enuCreate3DInline\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strUrl, float transx, float transy, float transz\)](./enusappapi_enucreate3dinline.md)  
 [ HNODE enuCreate3DLineSet\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy, float transz\)](./enusappapi_enucreate3dlineset.md)  
 [ HNODE enuCreate3DFaceSet\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strPoints, wchar\_t\* strVectors, float transx, float transy, float transz\)](./enusappapi_enucreate3dfaceset.md)  
 [ HNODE enuCreate3DCylinder\(HX3D pX3DHandler, wchar\_t\* strID, float height, float radius, float slices, float transx, float transy, float transz\)](./enusappapi_enucreate3dcylinder.md)  
 [ HNODE enuCreate3DTerrain\(HX3D pX3DHandler, wchar\_t\* strID, float size, float subdivision, float transx, float transy, float transz\)](./enusappapi_enucreate3dterrain.md)  
 [ void enuCreate3DSphereAsync\(HX3D pX3DHandler, wchar\_t\* strID, float radius, float slices, float transx, float transy, float transz\)](./enusappapi_enucreate3dsphereasync.md)  
 [ void enuCreate3DConeAsync\(HX3D pX3DHandler, wchar\_t\* strID, float bottomRadius, float height, float slices, float transx, float transy, float transz\)](./enusappapi_enucreate3dconeasync.md)  
 [ void enuCreate3DBoxAsync\(HX3D pX3DHandler, wchar\_t\* strID, float size, float transx, float transy, float transz\)](./enusappapi_enucreate3dboxasync.md)  
 [ void enuCreate3DTextAsync\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strString, wchar\_t\* strValue, float fontSize, float transx, float transy, float transz\)](./enusappapi_enucreate3dtextasync.md)  
 [ void enuCreate3DInlineAsync\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strUrl, float transx, float transy, float transz\)](./enusappapi_enucreate3dinlineasync.md)  
 [ void enuCreate3DLineSetAsync\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy, float transz\)](./enusappapi_enucreate3dlinesetasync.md)  
 [ void enuCreate3DFaceSetAsync\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strPoints, wchar\_t\* strVectors, float transx, float transy, float transz\)](./enusappapi_enucreate3dfacesetasync.md)  
 [ void enuCreate3DCylinderAsync\(HX3D pX3DHandler, wchar\_t\* strID, float height, float radius, float slices, float transx, float transy, float transz\)](./enusappapi_enucreate3dcylinderasync.md)  
 [ void enuCreate3DTerrainAsync\(HX3D pX3DHandler, wchar\_t\* strID, float size, float subdivision, float transx, float transy, float transz\)](./enusappapi_enucreate3dterrainasync.md)  
 [ void enuSetAttribute3DByNode\(HX3D pX3DHandler, HNODE pObject, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](./enusappapi_enusetattribute3dbynode.md)   
 [ void enuSetAttribute3DByNodeSync\(HX3D pX3DHandler, HNODE pObject, wchar\_t\* pStrVariable, wchar\_t\* pStrValue, bool bHistory, bool bScript\)](./enusappapi_enusetattribute3dbynodesync.md)  
 [ void enuGetAttribute3DByNode\(HX3D pX3DHandler, HNODE pObject, wchar\_t\* pStrVariable, VariableStruct\* pData\)](./enusappapi_enugetattribute3dbynode.md)  
 [ void enuSetAttribute3D\(HX3D pX3DHandler, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](./enusappapi_enusetattribute3d.md)  
 [ HNODE enuGet3DObjectById\(HX3D pX3DHandler, wchar\_t\* objectid\)](./enusappapi_enuget3dobjectbyid.md)  
 [ HNODE enuGetAppearanceFromShape\(HX3D pX3DHandler, HNODE node\)](./enusappapi_enugetappearancefromshape.md)  
 [ HNODE enuGetGeometryFromShape\(HX3D pX3DHandler, HNODE node\)](./enusappapi_enugetgeometryfromshape.md)  
 [ HNODE enuGetMaterialFromAppearance\(HX3D pX3DHandler, HNODE node\)](./enusappapi_enugetmaterialfromappearance.md)  
 [ HNODE enuGetMaterialFromGeometry\(HX3D pX3DHandler, HNODE node\)](./enusappapi_enugetmaterialfromgeometry.md)  
 [ HNODE enuGetTransformFromGeometry\(HX3D pX3DHandler, HNODE node\)](./enusappapi_enugettransformfromgeometry.md)  
 [ HNODE enuGetCoordinateFromIndexedFaceSet\(HX3D pX3DHandler, HNODE node\)](./enusappapi_enugetcoordinatefromindexedfaceset.md)  
 [ HNODE enuGetCoordinateFromLineSet\(HX3D pX3DHandler, HNODE node\)](./enusappapi_enugetcoordinatefromlineset.md)  
 [ HNODE enuGetShapeFromGeometry\(HX3D pX3DHandler, HNODE node\)](./enusappapi_enugetshapefromgeometry.md)  
 [ void enuDelete3DObjectByNode\(HX3D pX3DHandler, HNODE pTarget\)](./enusappapi_enudelete3dobjectbynode.md)

## Script Interface

[ void enuSet3DLuaScriptByNode\(HX3D pX3D, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)](./enusappapi_enuset3dluascriptbynode.md)  
 [ void enuSet3DJavaScriptByNode\(HX3D pX3D, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)](./enusappapi_enuset3djavascriptbynode.md)  
 [ void enuExecute3DFunction\(HX3D pX3D, wchar\_t\* strFunction\)](./enusappapi_enuexecute3dfunction.md)  
 [ void enuExecute3DFunctionByNode\(HX3D pX3D, HNODE pNode, wchar\_t\* strFunction\)](./enusappapi_enuexecute3dfunctionbynode.md)
