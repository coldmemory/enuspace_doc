---
layout: default
title: Application API
has_children: true
nav_order: k
last_modified_date: now
---



## Project Interface

[ bool enuLoadProjectFile\(wchar\_t\* pStrFileName\)](./sdk_api_enuloadprojectfile.md)  
 [ HPROJECT enuCreateProject\(\)](./sdk_api_enucreateproject.md)  
 [ void enuDestoryProject\(HPROJECT pProject\)](./sdk_api_enudestoryproject.md)  
 [ bool enuSetActiveProject\(HPROJECT pHANDLE\)](./sdk_api_enusetactiveproject.md)  
 [ HPROJECT enuGetActiveProject\(\)](./sdk_api_enugetactiveproject.md)  
 [ void enuSetWidgetProject\(\)](./sdk_api_enusetwidgetproject.md)  
 [ bool enuSaveProjectFile\(\)](./sdk_api_enusaveprojectfile.md)  
 [ bool enuCloseProjectFile\(\)](./sdk_api_enucloseprojectfile.md)  
 [ wchar\_t\* enuGetProjectName\(\)](./sdk_api_enugetprojectname.md)  
 [ wchar\_t\* enuGetProjectFullName\(\)](./sdk_api_enugetprojectfullname.md)  
 [ wchar\_t\* enuGetProjectPath\(\)](./sdk_api_enugetprojectpath.md)  
 [ wchar\_t\* enuGetProjectType\(\)](./sdk_api_enugetprojecttype.md)  
 [ void enuSetProjectName\(wchar\_t\* projectname\)](./sdk_api_enusetprojectname.md)  
 [ void enuSetModifyProject\(bool bFlag\)](./sdk_api_enusetmodifyproject.md)  
 [ bool enuGetModifyProject\(\)](./sdk_api_enugetmodifyproject.md)

## Operation Interface

## Script Operation Interface

[ void enuSetScriptOperationMode\(bool bFlag\)](./sdk_api_enusetscriptoperationmode.md)  
 [ bool enuGetScriptOperationMode\(\)](./sdk_api_enugetscriptoperationmode.md)  
 [ void enuSetHMIScriptUpdateTime\(int iMiliSecond\)](./sdk_api_enusethmiscriptupdatetime.md)

## Edit Operation Interface

[ void enuSetEditOperationMode\(HVIEW pENUView, bool bFlag\)](./sdk_api_enuseteditoperationmode.md)  
 [ bool enuGetEditOperationMode\(HVIEW pENUVie\)](./sdk_api_enugeteditoperationmode.md)

## Mouse Interface

[ void enuSetLButtonDownCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](./sdk_api_enusetlbuttondowncallback.md)  
 [ void enuSetLButtonUpCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](./sdk_api_enusetlbuttonupcallback.md)  
 [ void enuSetRButtonDownCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](./sdk_api_enusetrbuttondowncallback.md)  
 [ void enuSetRButtonUpCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](./sdk_api_enusetrbuttonupcallback.md)  
 [ void enuSetMButtonDownCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](./sdk_api_enusetmbuttondowncallback.md)  
 [ void enuSetMButtonUpCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](./sdk_api_enusetmbuttonupcallback.md)  
 [ void enuSetMouseMoveCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](./sdk_api_enusetmousemovecallback.md)  
 [ void enuSetMouseWheelCallBack\(HVIEW pENUView, void functioncb\(float, float, float\) \)](./sdk_api_enusetmousewheelcallback.md)  
 [ void enuSetLButtonDblClkCallBack\(HVIEW pENUView, void functioncb\(float, float\) \)](./sdk_api_enusetlbuttondblclkcallback.md)  
 [ void enuOnMouseWheel\(HVIEW pENUView, UINT nFlags, short zDelta, CPoint pt\)](./sdk_api_enuonmousewheel.md)  
 [ POINTF enuGetLocalPosition\(HVIEW pENUView, POINT point\)](./sdk_api_enugetlocalposition.md)  
 [ POINT enuGetCursorPos\(\)](./sdk_api_enugetcursorpos.md)  
 [ void enuSetDefaultWheelControl\(HVIEW pENUView, bool bDefault\)](./sdk_api_enusetdefaultwheelcontrol.md)

## View Interface

[ void enuActivateView\(HVIEW pENUView\)](./sdk_api_enuactivateview.md)  
 [ void enuDeactivateView\(HVIEW pENUView\)](./sdk_api_enudeactivateview.md)  
 [ void enuSetRenderObjectPreReset\(HVIEW pENUView\)](./sdk_api_enusetrenderobjectprereset.md)  
 [ void enuSetRenderObjectReset\(HVIEW pENUView\)](./sdk_api_enusetrenderobjectreset.md)

## File IO Interface

[ HSVG enuLoadSvgPageFile\(wchar\_t\* pStrFileName\)](./sdk_api_enuloadsvgpagefile.md)  
 [ HSVG enuLoadSvgHmiFile\(wchar\_t\* pStrFileName\)](./sdk_api_enuloadsvghmifile.md)  
 [ HSVG enuLoadSvgLogicFile\(wchar\_t\* pStrFileName\)](./sdk_api_enuloadsvglogicfile.md)  
 [ HSVG enuLoadSvgResourceFile\(wchar\_t\* pStrFileName\)](./sdk_api_enuloadsvgresourcefile.md)  
 [ HSVG enuLoadSvgGlobalFile\(wchar\_t\* pStrFileName\)](./sdk_api_enuloadsvgglobalfile.md)  
 [ HSVG enuNewSvgPageFile\(wchar\_t\* pStrFileName\)](./sdk_api_enunewsvgpagefile.md)  
 [ HSVG enuNewSvgHmiFile\(wchar\_t\* pStrFileName\)](./sdk_api_enunewsvghmifile.md)  
 [ HSVG enuNewSvgLogicFile\(wchar\_t\* pStrFileName\)](./sdk_api_enunewsvglogicfile.md)  
 [ HSVG enuNewSvgGlobalFile\(wchar\_t\* pStrFileName\)](./sdk_api_enunewsvgglobalfile.md)  
 [ HSVG enuNewSvgResourceFile\(wchar\_t\* pStrFileName\)](./sdk_api_enunewsvgresourcefile.md)  
 [ bool enuSaveAsSvgPageFile\(wchar\_t\* strTaget, wchar\_t\* strSource\)](./sdk_api_enusaveassvgpagefile.md)  
 [ bool enuSaveAsSvgHmiFile\(wchar\_t\* strTaget, wchar\_t\* strSource\)](./sdk_api_enusaveassvghmifile.md)  
 [ bool enuSaveAsSvgLogicFile\(wchar\_t\* strTaget, wchar\_t\* strSource\)](./sdk_api_enusaveassvglogicfile.md)  
 [ bool enuSaveAsSvgGlobalFile\(wchar\_t\* strTaget, wchar\_t\* strSource\)](./sdk_api_enusaveassvgglobalfile.md)  
 [ bool enuSaveAsSvgResourceFile\(wchar\_t\* strTaget, wchar\_t\* strSource\)](./sdk_api_enusaveassvgresourcefile.md)  
 [ bool enuSaveSvgFile\(HSVG pSvgHandler, wchar\_t\* strFileName= L""\)](./sdk_api_enusavesvgfile.md)  
 [ bool enuDeleteSvgPageFile\(wchar\_t\* pStrFileName\)](./sdk_api_enudeletesvgpagefile.md)  
 [ bool enuDeleteSvgHmiFile\(wchar\_t\* pStrFileName\)](./sdk_api_enudeletesvghmifile.md)  
 [ bool enuDeleteSvgLogicFile\(wchar\_t\* pStrFileName\)](./sdk_api_enudeletesvglogicfile.md)  
 [ bool enuDeleteSvgResourceFile\(wchar\_t\* pStrFileName\)](./sdk_api_enudeletesvgresourcefile.md)  
 [ bool enuDeleteSvgGlobalFile\(wchar\_t\* pStrFileName\)](./sdk_api_enudeletesvgglobalfile.md)  
 [ bool enuExportWebStyleSvg\(wchar\_t\* strTaget, wchar\_t\* strSource\)](./sdk_api_enuexportwebstylesvg.md)  
 [ void enuSetAutoSaveMode\(bool bAuto\)](./sdk_api_enusetautosavemode.md)

## File handle Interface
[ HSVG enuGetPageClass\(wchar\_t\* pStrFileName\)](./sdk_api_enugetpageclass.md)  
 [ HSVG enuGetSvgPageClass\(wchar\_t\* pStrFileName\)](./sdk_api_enugetsvgpageclass.md)  
 [ HSVG enuGetLogicClass\(wchar\_t\* pStrFileName\)](./sdk_api_enugetlogicclass.md)  
 [ HSVG enuGetHmiClass\(wchar\_t\* pStrFileName\)](./sdk_api_enugethmiclass.md)  
 [ HSVG enuGetGlobalClass\(wchar\_t\* pStrFileName\)](./sdk_api_enugetglobalclass.md)  
 [ HSVG enuGetResourceClass\(wchar\_t\* pStrFileName\)](./sdk_api_enugetresourceclass.md)  
 [ void\* enuGetPageList\(\)](./sdk_api_enugetpagelist.md)  
 [ void\* enuGetHmiList\(\)](./sdk_api_enugethmilist.md)  
 [ void\* enuGetLogicList\(\)](./sdk_api_enugetlogiclist.md)  
 [ void\* enuGetGlobalList\(\)](./sdk_api_enugetgloballist.md)  
 [ void\* enuGetResourceList\(\)](./sdk_api_enugetresourcelist.md)  
 [ bool enuGetModifyPage\(wchar\_t\* pStrFilename\)](./sdk_api_enugetmodifypage.md)  
 [ bool enuGetModifyHmi\(wchar\_t\* pStrFilename\)](./sdk_api_enugetmodifyhmi.md)  
 [ bool enuGetModifyLogic\(wchar\_t\* pStrFilename\)](./sdk_api_enugetmodifylogic.md)  
 [ bool enuGetModifyGlobal\(wchar\_t\* pStrFilename\)](./sdk_api_enugetmodifyglobal.md)  
 [ bool enuGetModifyResource\(wchar\_t\* pStrFilename\)](./sdk_api_enugetmodifyresource.md)
 [ bool enuSetPageProperty\(void\_t\* pPage, wchar\_t\* pAttribute, wchar\_t\* pValue\)](./sdk_api_enusetpageproperty.md)
 [ bool enuSetLogicProperty\(HSVG pSvg, wchar\_t\* pAttribute, wchar\_t\* pValue\)](./sdk_api_enusetlogicproperty.md)
 [ bool enuSetHmiProperty\(HSVG pSvg, wchar\_t\* pAttribute, wchar\_t\* pValue\)](./sdk_api_enusethmiproperty.md)
 [ bool enuSetGlobalProperty\(HSVG pSvg, wchar\_t\* pAttribute, wchar\_t\* pValue\)](./sdk_api_enusetglobalproperty.md) 
 [ bool enuSetResourceProperty\(HSVG pSvg, wchar\_t\* pAttribute, wchar\_t\* pValue\)](./sdk_api_enusetresourceproperty.md)  
## Library Interface

[ bool enuLogicCreateSymbolNode\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)](./sdk_api_enulogiccreatesymbolnode.md)  
 [ bool enuLogicCreateSymbolLink\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)](./sdk_api_enulogiccreatesymbollink.md)  
 [ bool enuHmiCreateSymbol\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)](./sdk_api_enuhmicreatesymbol.md)  
 [ bool enuResourceCreateStyle\(wchar\_t\* pStrFilename, wchar\_t\* pStrStyle\)](./sdk_api_enuresourcecreatestyle.md)  
 [ bool enuDeleteLogicSymbol\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)](./sdk_api_enudeletelogicsymbol.md)  
 [ bool enuDeleteHmiSymbol\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)](./sdk_api_enudeletehmisymbol.md)  
 [ wchar\_t\* enuLogicGetSymbolType\(wchar\_t\* pStrFilename, wchar\_t\* pStrSymbol\)](./sdk_api_enulogicgetsymboltype.md)  
 [ void\* enuGetHmiSymbolList\(wchar\_t\* pStrFilename\)](./sdk_api_enugethmisymbollist.md)  
 [ void\* enuGetLogicSymbolList\(wchar\_t\* pStrFilename\)](./sdk_api_enugetlogicsymbollist.md)

## Global Interface

[ bool enuAddGlobalStruct\(wchar\_t\* pStrFileName, wchar\_t\* pStrStructName, CPtrList\* pItem\)](./sdk_api_enuaddglobalstruct.md)  
 [ void\* enuGetGlobalPgStructList\(wchar\_t\* pStrFileName\)](./sdk_api_enugetglobalpgstructlist.md)  
 [ void\* enuGetGlobalVariableList\(wchar\_t\* pStrFileName\)](./sdk_api_enugetglobalvariablelist.md)  
 [ void\* enuGetGlobalPgAttributeList\(wchar\_t\* pStrFileName, wchar\_t\* pStrStructName\)](./sdk_api_enugetglobalpgattributelist.md)  
 [ HNODE enuGetGlobalVariableNode\(wchar\_t\* pStrVariable\)](./sdk_api_enugetglobalvariablenode.md)  
 [ bool enuAddGlobalVariable\(wchar\_t\* pStrFileName, wchar\_t\* pStrType, wchar\_t\* strVariable, wchar\_t\* strInitValue=L"", wchar\_t\* strDescription=L""\)](./sdk_api_enuaddglobalvariable.md)  
 [ bool enuDeleteGlobalVariable\(wchar\_t\* pStrFileName, wchar\_t\* strVariable\)](./sdk_api_enudeleteglobalvariable.md)  
 [ bool enuModifyGlobalVariable\(wchar\_t\* pStrFileName, wchar\_t\* strVariable, wchar\_t\* strNewType, wchar\_t\* strNewVariable, wchar\_t\* strNewDescription\)](./sdk_api_enumodifyglobalvariable.md)  
 [ bool enuDeleteGlobalStruct\(wchar\_t\* pStrFileName, wchar\_t\* strStruct\)](./sdk_api_enudeleteglobalstruct.md)  
 [ bool enuModifyGlobalStruct\(wchar\_t\* pStrFileName, wchar\_t\* strStruct, wchar\_t\* strNewStruct, CPtrList\* pItem\)](./sdk_api_enumodifyglobalstruct.md)  
 [ void enuReloadPicture\(HVIEW pENUView\)](./sdk_api_enureloadpicture.md)  
 [ bool enuIsModifyPage\(HVIEW pENUView\)](./sdk_api_enuismodifypage.md)

## Window Interface

[ void enuSetZoomScale\(HVIEW pENUView, float fPercent\)](./sdk_api_enusetzoomscale.md)  
 [ float enuGetZoomScale\(HVIEW pENUView\)](./sdk_api_enugetzoomscale.md)  
 [ float enuGetCanvasWidth\(HVIEW pENUView\)](./sdk_api_enugetcanvaswidth.md)  
 [ float enuGetCanvasHeight\(HVIEW pENUView\)](./sdk_api_enugetcanvasheight.md)  
 [ void enuSetCanvasSize\(HVIEW pENUView, float cx, float cy\)](./sdk_api_enusetcanvassize.md)  
 [ void enuSetMoveCanvas\(HVIEW pENUView, float transx, float transy\)](./sdk_api_enusetmovecanvas.md)  
 [ void enuGetMoveCanvas\(HVIEW pENUView, float\* transx, float\* transy\)](./sdk_api_enugetmovecanvas.md)  
 [ void enuSetCanvasColor\(HVIEW pENUView, byte iR, byte iG, byte iB\)](./sdk_api_enusetcanvascolor.md)  
 [ void enuSetWindowColor\(HVIEW pENUView, byte iR, byte iG, byte iB\)](./sdk_api_enusetwindowcolor.md)  
 [ bool enuSelConnectionPin\(HVIEW pENUView, wchar\_t\* strPicture, wchar\_t\* strSymbol\)](./sdk_api_enuselconnectionpin.md)  
 [ bool enuIsEnableConnectionPin\(HVIEW pENUView\)](./sdk_api_enuisenableconnectionpin.md)

## Symbol Interface

[ float enuGetSymbolWidth\(HVIEW pENUView, wchar\_t\* strSymbol\)](./sdk_api_enugetsymbolwidth.md)  
 [ float enuGetSymbolHeight\(HVIEW pENUView, wchar\_t\* strSymbol\)](./sdk_api_enugetsymbolheight.md)  
 [ void enuSetSymbolSize\(HVIEW pENUView,  wchar\_t\* strSymbol, float fWidth, float fHeight\)](./sdk_api_enusetsymbolsize.md)

## Edit Interface

[ void enuSetSelectToolBar\(int iSel\)](./sdk_api_enusetselecttoolbar.md)  
 [ void enuSetCallBackSelectToolBar\(void fcbSelectToolBar\(int\)\)](./sdk_api_enusetcallbackselecttoolbar.md)  
 [ void enuSetCallBackSelectEvent\(void fcbSelectObject\(CPtrList\*, void\*\)\)](./sdk_api_enusetcallbackselectevent.md)  
 [ void enuSetCallBackDebugMessage\(void fcbDebugMessage\(wchar\_t\*\)\)](./sdk_api_enusetcallbackdebugmessage.md)  
 [ bool enuIsEnablePaste\(\)](./sdk_api_enuisenablepaste.md)  
 [ bool enuIsSelectObject\(HVIEW pENUView\)](./sdk_api_enuisenablepaste.md)  
 [ void enuSetSelectFontname\(HVIEW pENUView,  wchar\_t\* strFontName\)](./sdk_api_enusetselectfontname.md)  
 [ void enuSetSelectFontsize\(HVIEW pENUView,  float fSize\)](./sdk_api_enusetselectfontsize.md)  
 [ void enuSetSelectFontcolor\(HVIEW pENUView,  wchar\_t\* strFontColor\)](./sdk_api_enusetselectfontcolor.md)  
 [ void enuSetSelectFontIncrease\(HVIEW pENUView\)](./sdk_api_enusetselectfontincrease.md)  
 [ void enuSetSelectFontDecrease\(HVIEW pENUView\)](./sdk_api_enusetselectfontdecrease.md)  
 [ void enuSetSelectFontBold\(HVIEW pENUView, bool bFlag\)](./sdk_api_enusetselectfontbold.md)  
 [ void enuSetSelectFontItalic\(HVIEW pENUView, bool bFlag\)](./sdk_api_enusetselectfontitalic.md)  
 [ void enuSetSelectFontUnderline\(HVIEW pENUView, bool bFlag\)](./sdk_api_enusetselectfontunderline.md)  
 [ void enuSetSelectFontStrikethough\(HVIEW pENUView, bool bFlag\)](./sdk_api_enusetselectfontstrikethough.md)  
 [ void enuSetSelectFontSubscript\(HVIEW pENUView, bool bFlag\)](./sdk_api_enusetselectfontsubscript.md)  
 [ void enuSetSelectFontSuperscript\(HVIEW pENUView, bool bFlag\)](./sdk_api_enusetselectfontsuperscript.md)  
 [ void enuSetSelectFontHilight\(HVIEW pENUView, bool bFlag\)](./sdk_api_enusetselectfonthilight.md)  
 [ bool enuIsSelectFontBold\(HVIEW pENUView\)](./sdk_api_enuisselectfontbold.md)  
 [ bool enuIsSelectFontItalic\(HVIEW pENUView\)](./sdk_api_enuisselectfontitalic.md)  
 [ bool enuIsSelectFontUnderline\(HVIEW pENUView\)](./sdk_api_enuisselectfontunderline.md)  
 [ bool enuIsSelectFontStrikethough\(HVIEW pENUView\)](./sdk_api_enuisselectfontstrikethough.md)  
 [ bool enuIsSelectFontSubscript\(HVIEW pENUView\)](./sdk_api_enuisselectfontsubscript.md)  
 [ bool enuIsSelectFontSuperscript\(HVIEW pENUView\)](./sdk_api_enuisselectfontsuperscript.md)  
 [ void enuSetSelectFillcolor\(HVIEW pENUView,  wchar\_t\* strColor\)](./sdk_api_enusetselectfillcolor.md)  
 [ void enuSetSelectFillOpacity\(HVIEW pENUView, wchar\_t\* strOpacity\)](./sdk_api_enusetselectfillopacity.md)  
 [ void enuSetSelectLinecolor\(HVIEW pENUView,  wchar\_t\* strColor\)](./sdk_api_enusetselectlinecolor.md)  
 [ void enuSetSelectLineOpacity\(HVIEW pENUView, wchar\_t\* strOpacity\)](./sdk_api_enusetselectlineopacity.md)  
 [ void enuSetSelectLineWidth\(HVIEW pENUView, float fWidth\)](./sdk_api_enusetselectlinewidth.md)  
 [ void enuSetSelectLineDashes\(HVIEW pENUView, wchar\_t\* strDashes\)](./sdk_api_enusetselectlinedashes.md)  
 [ void enuSetSelectAlign\(HVIEW pENUView, int iType\)](./sdk_api_enusetselectalign.md)  
 [ void enuSetSelectRotation\(HVIEW pENUView, float fAngle\)](./sdk_api_enusetselectrotation.md)  
 [ void enuSetSelectFlip\(HVIEW pENUView, int iType\)](./sdk_api_enusetselectflip.md)  
 [ HNODE enuGetSelectSingleObject\(HVIEW pENUView\)](./sdk_api_enugetselectsingleobject.md)  
 [ void enuSetSelectAll\(HVIEW pENUView\)](./sdk_api_enusetselectall.md)  
 [ bool enuSetSelectObject\(HVIEW pENUView, wchar\_t\* strSelectID\)](./sdk_api_enusetselectobject.md)  
 [ void enuSetFindObjectCallBack\(void fcbFindMessage\(HNODE, int, wchar\_t\*, wchar\_t\*\), wchar\_t\* pStrSearch, bool bMatchCase, bool bWholeWord\)](./sdk_api_enusetfindobjectcallback.md)  
 [ wchar\_t\* enuGetPrevPageName\(wchar\_t\* pStrFileName\)](./sdk_api_enugetprevpagename.md)  
 [ wchar\_t\* enuGetNextPageName\(wchar\_t\* pStrFileName\)](./sdk_api_enugetnextpagename.md)  
 [ void enuSetSelectZOrder\(HVIEW pENUView, int iType\)](./sdk_api_enusetselectzorder.md)  
 [ void enuSetSelectGroup\(HVIEW pENUView\)](./sdk_api_enusetselectgroup.md)  
 [ void enuSetSelectUnGroup\(HVIEW pENUView\)](./sdk_api_enusetselectungroup.md)  
 [ void enuMoveObjectUp\(HVIEW pENUView\)](./sdk_api_enumoveobjectup.md)  
 [ void enuMoveObjectDown\(HVIEW pENUView\)](./sdk_api_enumoveobjectdown.md)  
 [ void enuMoveObjectLeft\(HVIEW pENUView\)](./sdk_api_enumoveobjectleft.md)  
 [ void enuMoveObjectRight\(HVIEW pENUView\)](./sdk_api_enumoveobjectright.md)  
 [ void enuSetEditCopy\(HVIEW pENUView\)](./sdk_api_enuseteditcopy.md)  
 [ void enuSetEditCut\(HVIEW pENUView\)](./sdk_api_enuseteditcut.md)  
 [ void enuSetEditPaste\(HVIEW pENUView\)](./sdk_api_enuseteditpaste.md)  
 [ void enuSetEditLock\(HVIEW pENUView\)](./sdk_api_enuseteditlock.md)  
 [ void enuSetEditUnLock\(HVIEW pENUView\)](./sdk_api_enuseteditunlock.md)  
 [ void enuSetEditUndo\(HVIEW pENUView\)](./sdk_api_enuseteditundo.md)  
 [ void enuSetEditRedo\(HVIEW pENUView\)](./sdk_api_enuseteditredo.md)  
 [ bool enuIsEditUndo\(HVIEW pENUView\)](./sdk_api_enuiseditundo.md)  
 [ bool enuIsEditRedo\(HVIEW pENUView\)](./sdk_api_enuiseditredo.md)

## Runtime Interface

[ void enuSetCallBackAddTable\( void fcbAddTable\(HNODE\) \)](./sdk_api_enusetcallbackaddtable.md)  
 [ HSVG enuNewSvgExternalPageFile\(wchar\_t\* pFileName\)](./sdk_api_enunewsvgexternalpagefile.md)  
 [ HSVG enuLoadSvgExternalPageFile\(wchar\_t\* pFileName\)](./sdk_api_enuloadsvgexternalpagefile.md)  
 [ bool enuDeleteSvgExternalPageFile\(wchar\_t\* pFileName\)](./sdk_api_enudeletesvgexternalpagefile.md)  
 [ bool enuSetSvgExternalPageView\(HVIEW pENUView, HSVG pSvg\)](./sdk_api_enusetsvgexternalpageview.md)  
 [ bool enuShowRuntimeView\(HWND hWnd\)](./sdk_api_enushowruntimeview.md)  
 [ void enuDestoryRuntimeView\(\)](./sdk_api_enudestoryruntimeview.md)  
 [ bool enuIsRuntimeView\(\)](./sdk_api_enuisruntimeview.md)  
 [ void enuChangePicture\(wchar\_t\* strWindow, wchar\_t\* strPicName\)](./sdk_api_enuchangepicture.md)  
 [ void enuChangePictureAsync\(wchar\_t\* strWindow, wchar\_t\* strPicName\)](./sdk_api_enuchangepictureasync.md)  
 [ void enuSaveImageToFile\(HVIEW pENUView, wchar\_t\* strFileName, wchar\_t\* strFileType\)](./sdk_api_enusaveimagetofile.md)  
 [ void enuSetModifyUseHref\(wchar\_t\* strSrcId, wchar\_t\* strNewId\)](./sdk_api_enusetmodifyusehref.md)  
 [ bool enuGetWindowSize\(wchar\_t\* strWindowID, RECT\* rect\)](./sdk_api_enugetwindowsize.md)  
 [ bool enuSetWindowSize\(wchar\_t\* strWindowID, int x, int y, int width, int height\)](./sdk_api_enusetwindowsize.md)  
 [ bool enuRegisterFunction\(wchar\_t\* strFunction, int \(\*pfunc\)\(lua\_State\* L\)\)](./sdk_api_enuregisterfunction.md)  
 [ HVIEW enuGetWindowView\(wchar\_t\* strWindowID\)](./sdk_api_enugetwindowview.md)

## View Interface

[ HVIEW enuCreateView\(HWND hWnd\)](./sdk_api_enucreateview.md)  
 [ void enuDestoryView\(HVIEW pENUView\)](./sdk_api_enudestoryview.md)  
 [ void enuSetViewID\(HVIEW pENUView, wchar\_t\* strID\)](./sdk_api_enusetviewid.md)  
 [ void enuSetComponentMode\(HVIEW pView, bool bOper\)](./sdk_api_enusetcomponentmode.md)  
 [ void enuUpdateScreen\(HVIEW pENUView\)](./sdk_api_enuupdatescreen.md)  
 [ void enuInvalidateView\(HVIEW pENUView\)](./sdk_api_enuinvalidateview.md)  
 [ bool enuSetLogicComponent\(HVIEW pENUView, wchar\_t\* pStrFileName, wchar\_t\* pStrSymbol\)](./sdk_api_enusetlogiccomponent.md)  
 [ bool enuSetHmiComponent\(HVIEW pENUView, wchar\_t\* pStrFileName, wchar\_t\* pStrSymbol\)](./sdk_api_enusethmicomponent.md) 
 [ bool enuSetSvgView\(HVIEW pENUView, HSVG\_t\* pSvg\)](./sdk_api_enusetsvgview.md)  
 [ bool enuSetSvgPageView\(HVIEW pENUView, wchar\_t\* pStrFileName\)](./sdk_api_enusetsvgpageview.md)  
 [ bool enuSetSvgHmiView\(HVIEW pENUView, wchar\_t\* pStrFileName\)](./sdk_api_enusetsvghmiview.md)  
 [ bool enuSetSvgLogicView\(HVIEW pENUView, wchar\_t\* pStrFileName\)](./sdk_api_enusetsvglogicview.md)  
 [ HSVG enuGetSvgHandler\(HVIEW pENUView\)](./sdk_api_enugetsvghandler.md)  
 [ void enuSetWindowPos\(HVIEW pENUView, int x, int y, int cx, int cy\)](./sdk_api_enusetwindowpos.md)  
 [ void enuSetWindowCenter\(HVIEW pENUView\)](./sdk_api_enusetwindowcenter.md)

## Object Interface

[ void enuSetSymbolValue\(HSVG pSvgHandler, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](./sdk_api_enusetsymbolvalue.md)  
 [ void enuSetSymbolValueByNode\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](./sdk_api_enusetsymbolvaluebynode.md)  
 [ void enuSetGlobalValue\(HSVG pSvgHandler, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](./sdk_api_enusetglobalvalue.md)  
 [ void enuDeleteObjectByName\(HSVG pSvgHandler, wchar\_t\* pStrVariable\)](./sdk_api_enudeleteobjectbyname.md)  
 [ void enuDeleteObjectByNode\(HSVG pSvgHandler, HNODE pTarget\)](./sdk_api_enudeleteobjectbynode.md)  
 [ void enuDeleteUseObjectByHref\(HSVG pSvgHandler, wchar\_t\* pStrHref\)](./sdk_api_enudeleteuseobjectbyhref.md)  
 [ void enuDeleteAllObject\(HSVG pSvgHandler\)](./sdk_api_enudeleteallobject.md)  
 [ void enuSetAttribute\(HSVG pSvgHandler, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](./sdk_api_enusetattribute.md)  
 [ void enuSetAttributeByNode\(HSVG pSvgHandler, HNODE pObject, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](./sdk_api_enusetattributebynode.md)  
 [ bool enuSetAttributeByNodeSync\(HSVG pSvgHandler, HNODE pObject, wchar\_t\* pStrVariable, wchar\_t\* pStrValue, bool bHistory=false, bool bScript=false\)](./sdk_api_enusetattributebynodesync.md)  
 [ void enuGetAttributeByNode\(HSVG pSvgHandler, HNODE pObject, wchar\_t\* pStrVariable, VariableStruct\* pData\)](./sdk_api_enugetattributebynode.md)  
 [ HNODE enuAddTrendSeriesByNode\(HSVG pSvgHandler, HNODE TrendNode, wchar\_t\* strSeriesID\)](./sdk_api_enuaddtrendseriesbynode.md)  
 [ void enuSetUseInterfaceByNode\(HSVG pSvgHandler, HNODE pUse, wchar\_t\* strVariable, wchar\_t\* strValue\)](./sdk_api_enusetuseinterfacebynode.md)  
 [ void enuSetUseInterface\(HSVG pSvgHandler, wchar\_t\* strVariable, wchar\_t\* strValue\)](./sdk_api_enusetuseinterface.md)  
 [ HNODE enuGetObjectById\(HSVG pSvgHandler, wchar\_t\* objectid\)](./sdk_api_enugetobjectbyid.md)  
 [ HNODE enuGetDefsSymbolById\(HSVG pSvgHandler, wchar\_t\* objectid\)](./sdk_api_enugetdefssymbolbyid.md) 
 [ HNODE enuCreateLine\(HSVG pSvgHandler, wchar\_t\* strID, float x1, float y1, float x2, float y2, float transx, float transy\)](./sdk_api_enucreateline.md)  
 [ HNODE enuCreatePolyline\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy\)](./sdk_api_enucreatepolyline.md)  
 [ HNODE enuCreatePolygon\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy\)](./sdk_api_enucreatepolygon.md)  
 [ HNODE enuCreateCircle\(HSVG pSvgHandler, wchar\_t\* strID, float r, float cx, float cy, float transx, float transy\)](./sdk_api_enucreatecircle.md)  
 [ HNODE enuCreateEllipse\(HSVG pSvgHandler, wchar\_t\* strID, float rx, float ry, float cx, float cy, float transx, float transy\)](./sdk_api_enucreateellipse.md)  
 [ HNODE enuCreateRect\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, float transx, float transy\)](./sdk_api_enucreaterect.md)  
 [ HNODE enuCreateText\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float dx, float dy, wchar\_t\* text, float transx, float transy\)](./sdk_api_enucreatetext.md)  
 [ HNODE enuCreateImage\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, wchar\_t\* xlink\_href, float transx, float transy\)](./sdk_api_enucreateimage.md)  
 [ HNODE enuCreateTrend\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, float transx, float transy\)](./sdk_api_enucreatetrend.md)  
 [ HNODE enuCreatePath\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* pStrValue, float transx, float transy\)](./sdk_api_enucreatepath.md)  
 [ HNODE enuCreateUse\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, wchar\_t\* xlink\_href, wchar\_t\* strType, float transx = 0, float transy = 0\)](./sdk_api_enucreateuse.md)  
 [ void enuCreateLineAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x1, float y1, float x2, float y2, float transx, float transy\)](./sdk_api_enucreatelineasync.md)  
 [ void enuCreatePolylineAsync\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy\)](./sdk_api_enucreatepolylineasync.md)  
 [ void enuCreatePolygonAsync\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy\)](./sdk_api_enucreatepolygonasync.md)  
 [ void enuCreateCircleAsync\(HSVG pSvgHandler, wchar\_t\* strID, float r, float cx, float cy, float transx, float transy\)](./sdk_api_enucreatecircleasync.md)  
 [ void enuCreateEllipseAsync\(HSVG pSvgHandler, wchar\_t\* strID, float rx, float ry, float cx, float cy, float transx, float transy\)](./sdk_api_enucreateellipseasync.md)  
 [ void enuCreateRectAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, float transx, float transy\)](./sdk_api_enucreaterectasync.md)  
 [ void enuCreateTextAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float dx, float dy, wchar\_t\* text, float transx, float transy\)](./sdk_api_enucreatetextasync.md)  
 [ void enuCreateImageAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, wchar\_t\* xlink\_href, float transx, float transy\)](./sdk_api_enucreateimageasync.md)  
 [ void enuCreateTrendAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, float width, float height, float transx, float transy\)](./sdk_api_enucreatetrendasync.md)  
 [ void enuCreatePathAsync\(HSVG pSvgHandler, wchar\_t\* strID, wchar\_t\* pStrValue, float transx, float transy\)](./sdk_api_enucreatepathasync.md)  
 [ void enuCreateUseAsync\(HSVG pSvgHandler, wchar\_t\* strID, float x, float y, wchar\_t\* xlink\_href, wchar\_t\* strType, float transx, float transy\)](./sdk_api_enucreateuseasync.md)  
 [ void enuSetEditDelete\(HVIEW pENUView\)](./sdk_api_enuseteditdelete.md)  
 [ void enuSetEditDeleteAsync\(HVIEW pENUView\)](./sdk_api_enuseteditdeleteasync.md)  
 [ void enuExecuteString\(wchar\_t\* pStrPageName, wchar\_t\* pStrEvent\)](./sdk_api_enuexecutestring.md)  
 [ void enuSetVariableValue\(HSVG pSvgHandler, wchar\_t\* strVariable, wchar\_t\* strValue\)](./sdk_api_enusetvariablevalue.md)  
 [ HNODE enuCreateUseAtView\(HVIEW pENUView, float transx, float transy, wchar\_t\* xlink\_href, wchar\_t\* strType\)](./sdk_api_enucreateuseatview.md)  
 [ HNODE enuCreateImageAtView\(HVIEW pENUView, wchar\_t\* strID, float x, float y, float width, float height, wchar\_t\* xlink\_href, float transx, float transy\)](./sdk_api_enucreateimageatview.md)  
 [ HNODE enuDuplicateLogicSymbol\(wchar\_t\* strPicture, wchar\_t\* strSymbol\)](./sdk_api_enuduplicatelogicsymbol.md)  
 [ HNODE enuDuplicateHmiSymbol\(wchar\_t\* strPicture, wchar\_t\* strSymbol\)](./sdk_api_enuduplicatehmisymbol.md)  
 [ void enuSetUseAttribute\_interface\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strValue\)](./sdk_api_enusetuseattribute_interface.md)  
 [ void enuSetUseAttribute\_interface\_id\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strValue\)](./sdk_api_enusetuseattribute_interface_id.md)  
 [ void enuGetVariablePointer\(HSVG pSvgHandler, wchar\_t\* pStrVariable, VariableStruct\* pData\)](./sdk_api_enugetvariablepointer.md)  
 [ void enuSetReShapeArrayValue\(wchar\_t\* pVariable, void\* fValue, int iType, int iSize\)](./sdk_api_enusetreshapearrayvalue.md)  
 [ bool enuSetModifySymbolAccept\(wchar\_t\* strPicture, wchar\_t\* strSymbol, int iFileType\)](./sdk_api_enusetmodifysymbolaccept.md)

## Script Interface

[ void enuExecuteFunction\(HSVG pSvgHandler, wchar\_t\* strFunction\)](./sdk_api_enuexecutefunction.md)  
 [ void enuExecuteFunctionByNode\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strFunction\)](./sdk_api_enuexecutefunctionbynode.md)  
 [ void enuSetLuaScriptByNode\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)](./sdk_api_enusetluascriptbynode.md)  
 [ void enuSetJavaScriptByNode\(HSVG pSvgHandler, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)](./sdk_api_enusetjavascriptbynode.md)  
 [ bool enuRegisterLuaScript\(wchar\_t\* pStrScript\)](./sdk_api_enuregisterluascript.md)  
 [ wchar\_t\* enuExecuteLuaScript\(wchar\_t\* pStrExecute\)](./sdk_api_enuexecuteluascript.md)  
 [ bool enuRegisterJavaScript\(wchar\_t\* pStrScript\)](./sdk_api_enuregisterjavascript.md)  
 [ wchar\_t\* enuExecuteJavaScript\(wchar\_t\* pStrExecute\)](./sdk_api_enuexecutejavascript.md)  
 [ void enuRegisterLuaScriptById\(wchar\_t\* strPagename, wchar\_t\* strID, wchar\_t\* strFunction, wchar\_t\* strScript\)](./sdk_api_enuregisterluascriptbyid.md)  
 [ void enuRegisterJavaScriptById\(wchar\_t\* strPagename, wchar\_t\* strID, wchar\_t\* strFunction, wchar\_t\* strScript\)](./sdk_api_enuregisterjavascriptbyid.md)  
 [ void enuRegisterLuaScriptByNode\(wchar\_t\* strPagename, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)](./sdk_api_enuregisterluascriptbynode.md)  
 [ void enuRegisterJavaScriptByNode\(wchar\_t\* strPagename, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)](./sdk_api_enuregisterjavascriptbynode.md)

## Widget Interface

[ HVIEW enuCreateWidget\(HWND hWnd\)](./sdk_api_enucreatewidget.md)  
 [ void enuDestoryWidget\(HVIEW pView\)](./sdk_api_enudestorywidget.md)  
 [ bool enuSetWidgetSize\(HVIEW pENUView, int x, int y, int width, int height\)](./sdk_api_enusetwidgetsize.md)  
 [ HNODE enuCreateUseWidget\(HVIEW pENUView, float transx, float transy, wchar\_t\* xlink\_href, wchar\_t\* strType\)](./sdk_api_enucreateusewidget.md)  
 [ HNODE enuCreateImageWidget\(HVIEW pENUView, wchar\_t\* xlink\_href\)](./sdk_api_enucreateimagewidget.md)  
 [ HNODE enuCreateTrendWidget\(HVIEW pENUView, float x, float y, float width, float height, float transx, float transy, float angle\)](./sdk_api_enucreatetrendwidget.md)  
 [ void enuWidgetFunctionByNode\(HVIEW pENUView, HNODE pNode, wchar\_t\* strFunction\)](./sdk_api_enuwidgetfunctionbynode.md)

## Runtime Interface

[ void enuShowDebugMessage\(bool bShow\)](./sdk_api_enushowdebugmessage.md)  
 [ void enuSetRuntimeMode\(bool bRunTime\)](./sdk_api_enusetruntimemode.md)  
 [ void enuOpenWindow\(wchar\_t\* strWindow, float posX, float posY, wchar\_t\* strHref\)](./sdk_api_enuopenwindow.md)  
 [ void enuCloseWindow\(wchar\_t\* strWindow\)](./sdk_api_enuclosewindow.md)  
 [ void enuMoveWindow\(wchar\_t\* strWindow, float posX, float posY\)](./sdk_api_enumovewindow.md)  
 [ void enuSetRuntimeView\(HVIEW pENUView, bool bRuntime\)](./sdk_api_enusetruntimeview.md)  
 [ void\* enuCreatePopupTrend\(int iType, wchar\_t\* strVariables, int x = 0, int y = 0, int width = 0, int height = 0\)](./sdk_api_enucreatepopuptrend.md)  
 [ void enuDestoryPopupTrend\(void\* pTrend\)](./sdk_api_enudestorypopuptrend.md)

## DataBase Interface

[ void enuSetDBGeneration\(\)](./sdk_api_enusetdbgeneration.md)  
 [ void enuShowTagList\(\)](./sdk_api_enushowtaglist.md)  
 [ void enuShowDeviceList\(\)](./sdk_api_enushowdevicelist.md)  
 [ void enuSelectObjectListClear\(HVIEW pENUView\)](./sdk_api_enuselectobjectlistclear.md)  
 [ void enuAddSelectObjectByNode\(HVIEW pENUView, HNODE hNode\)](./sdk_api_enuaddselectobjectbynode.md)

## Configuration Interface

[ wchar\_t\* enuGetConfiguration\(wchar\_t\* pAttribute\)](./sdk_api_enugetconfiguration.md)  
 [ bool enuSetConfiguration\(wchar\_t\* pAttribute, wchar\_t\* pValue\)](./sdk_api_enusetconfiguration.md)  
 [ void enuShowUserList\(\)](./sdk_api_enushowuserlist.md)

## Communication Interface

[ bool enuIsWebServerStart\(\)](./sdk_api_enuiswebserverstart.md)  
 [ bool enuIsEnuServerStart\(\)](./sdk_api_enuisenuserverstart.md)  
 [ void enuWebServerStart\(\)](./sdk_api_enuwebserverstart.md)  
 [ void enuWebServerStop\(\)](./sdk_api_enuwebserverstop.md)  
 [ void enuLinkServerStart\(\)](./sdk_api_enulinkserverstart.md)  
 [ void enuLinkServerStop\(\)](./sdk_api_enulinkserverstop.md)  
 [ void enuSendNetData\(wchar\_t\* system, char\* data, int length\)](./sdk_api_enusendnetdata.md)  
 [ void enuRecvNetData\(void functioncb\(wchar\_t\* system, char\* buffer, int length\)\)](./sdk_api_enurecvnetdata.md)

## Media Interface

[ void enuPlaySoundX\(wchar\_t\* wavfilename\)](./sdk_api_enuplaysoundx.md)  
 [ void enuStopSoundX\(wchar\_t\* wavfilename\)](./sdk_api_enustopsoundx.md)  
 [ void enuSetVolumeX\(int iVolume\)](./sdk_api_enusetvolumex.md)

## Task Operation Interface

[ void enuSetTaskOperationMode\(int iMode, int iStep\)](./sdk_api_enusettaskoperationmode.md)  
 [ bool enuAddTask\(wchar\_t\* pStrTaskID, wchar\_t\* pStrTaskModule, wchar\_t\* pStrCycle\)](./sdk_api_enuaddtask.md)  
 [ bool enuRemoveTask\(wchar\_t\* pStrTaskID)](./sdk_api_enuremovetask.md)   
 [ wchar\_t\* enuGetTaskList\(\)](./sdk_api_enugettasklist.md)  
 [ TaskStruct\* enuGetTaskProperty\(wchar\_t\* pStrTaskID\)](./sdk_api_enugettaskproperty.md)  
 [ bool enuSetTaskProperty\(wchar\_t\* pStrTaskID, wchar\_t\* pStrProp, wchar\_t\* pStrValue\)](./sdk_api_enusettaskproperty.md)  
 [ void enuSetSnapFile\(wchar\_t\* strFilename\)](./sdk_api_enusetsnapfile.md)  
 [ void enuSetResetFile\(wchar\_t\* strFilename\)](./sdk_api_enusetresetfile.md)  
 [ \_\_int64 enuGetCurrentTime\(\)](./sdk_api_enugetcurrenttime.md)

## 3D Interface

## View Interface

[ HVIEW enuCreate3DView\(HWND hWnd\)](./sdk_api_enucreate3dview.md)  
 [ bool enuSetX3dPageView\(HVIEW pENUView, wchar\_t\* pStrFileName\)](./sdk_api_enusetx3dpageview.md)  
 [ HX3D enuGetX3DHandler\(HVIEW pENUView\)](./sdk_api_enugetx3dhandler.md)

## File IO Interface

[ HX3D enuNewX3DPageFile\(wchar\_t\* pStrFileName\)](./sdk_api_enunewx3dpagefile.md)  
 [ HSVG enuLoadX3DPageFile\(wchar\_t\* pStrFileName\)](./sdk_api_enuloadx3dpagefile.md)  
 [ bool enuSaveX3DFile\(HX3D pX3DHandler, wchar\_t\* strFileName = L""\)](./sdk_api_enusavex3dfile.md)  
 [ bool enuDeleteX3dPageFile\(wchar\_t\* pStrFileName\)](./sdk_api_enudeletex3dpagefile.md)

## File handle Interface

[ HX3D enuGetX3dPageClass\(wchar\_t\* pStrFileName\)](./sdk_api_enugetx3dpageclass.md)

## Edit Interface

[ void enuSetCallBackSelectEvent3D\(void fcbSelectObject\(CPtrList\*, void\*\)\)](./sdk_api_enusetcallbackselectevent3d.md)  
 [ void enuSetSelectDiffuseColor\(HVIEW pENUView, wchar\_t\* strColor\)](./sdk_api_enusetselectdiffusecolor.md)  
 [ void enuSetSelectEmissiveColor\(HVIEW pENUView, wchar\_t\* strColor\)](./sdk_api_enusetselectemissivecolor.md)  
 [ void enuSetSelectSpecularColor\(HVIEW pENUView, wchar\_t\* strColor\)](./sdk_api_enusetselectspecularcolor.md)  
 [ void enuSetSelect3DToolBar\(int iSel\)](./sdk_api_enusetselect3dtoolbar.md)  
 [ void enuSetCallBackSelect3DToolBar\(void fcbSelectToolBar\(int\)\)](./sdk_api_enusetcallbackselect3dtoolbar.md)

## Window Interface

[ void enuSetMove3DCanvas\(HVIEW pENUView, float transx, float transy, float transz\)](./sdk_api_enusetmove3dcanvas.md)

## Object Interface

[ HNODE enuCreate3DSphere\(HX3D pX3DHandler, wchar\_t\* strID, float radius, float slices, float transx, float transy, float transz\)](./sdk_api_enucreate3dsphere.md)  
 [ HNODE enuCreate3DCone\(HX3D pX3DHandler, wchar\_t\* strID, float bottomRadius, float height, float slices, float transx, float transy, float transz\)](./sdk_api_enucreate3dcone.md)  
 [ HNODE enuCreate3DBox\(HX3D pX3DHandler, wchar\_t\* strID, float size, float transx, float transy, float transz\)](./sdk_api_enucreate3dbox.md)  
 [ HNODE enuCreate3DText\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strString, wchar\_t\* strValue, float fontSize, float transx, float transy, float transz\)](./sdk_api_enucreate3dtext.md)  
 [ HNODE enuCreate3DInline\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strUrl, float transx, float transy, float transz\)](./sdk_api_enucreate3dinline.md)  
 [ HNODE enuCreate3DLineSet\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy, float transz\)](./sdk_api_enucreate3dlineset.md)  
 [ HNODE enuCreate3DFaceSet\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strPoints, wchar\_t\* strVectors, float transx, float transy, float transz\)](./sdk_api_enucreate3dfaceset.md)  
 [ HNODE enuCreate3DCylinder\(HX3D pX3DHandler, wchar\_t\* strID, float height, float radius, float slices, float transx, float transy, float transz\)](./sdk_api_enucreate3dcylinder.md)  
 [ HNODE enuCreate3DTerrain\(HX3D pX3DHandler, wchar\_t\* strID, float size, float subdivision, float transx, float transy, float transz\)](./sdk_api_enucreate3dterrain.md)  
 [ void enuCreate3DSphereAsync\(HX3D pX3DHandler, wchar\_t\* strID, float radius, float slices, float transx, float transy, float transz\)](./sdk_api_enucreate3dsphereasync.md)  
 [ void enuCreate3DConeAsync\(HX3D pX3DHandler, wchar\_t\* strID, float bottomRadius, float height, float slices, float transx, float transy, float transz\)](./sdk_api_enucreate3dconeasync.md)  
 [ void enuCreate3DBoxAsync\(HX3D pX3DHandler, wchar\_t\* strID, float size, float transx, float transy, float transz\)](./sdk_api_enucreate3dboxasync.md)  
 [ void enuCreate3DTextAsync\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strString, wchar\_t\* strValue, float fontSize, float transx, float transy, float transz\)](./sdk_api_enucreate3dtextasync.md)  
 [ void enuCreate3DInlineAsync\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strUrl, float transx, float transy, float transz\)](./sdk_api_enucreate3dinlineasync.md)  
 [ void enuCreate3DLineSetAsync\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strPoints, float transx, float transy, float transz\)](./sdk_api_enucreate3dlinesetasync.md)  
 [ void enuCreate3DFaceSetAsync\(HX3D pX3DHandler, wchar\_t\* strID, wchar\_t\* strPoints, wchar\_t\* strVectors, float transx, float transy, float transz\)](./sdk_api_enucreate3dfacesetasync.md)  
 [ void enuCreate3DCylinderAsync\(HX3D pX3DHandler, wchar\_t\* strID, float height, float radius, float slices, float transx, float transy, float transz\)](./sdk_api_enucreate3dcylinderasync.md)  
 [ void enuCreate3DTerrainAsync\(HX3D pX3DHandler, wchar\_t\* strID, float size, float subdivision, float transx, float transy, float transz\)](./sdk_api_enucreate3dterrainasync.md)  
 [ void enuSetAttribute3DByNode\(HX3D pX3DHandler, HNODE pObject, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](./sdk_api_enusetattribute3dbynode.md)   
 [ void enuSetAttribute3DByNodeSync\(HX3D pX3DHandler, HNODE pObject, wchar\_t\* pStrVariable, wchar\_t\* pStrValue, bool bHistory, bool bScript\)](./sdk_api_enusetattribute3dbynodesync.md)  
 [ void enuGetAttribute3DByNode\(HX3D pX3DHandler, HNODE pObject, wchar\_t\* pStrVariable, VariableStruct\* pData\)](./sdk_api_enugetattribute3dbynode.md)  
 [ void enuSetAttribute3D\(HX3D pX3DHandler, wchar\_t\* pStrVariable, wchar\_t\* pStrValue\)](./sdk_api_enusetattribute3d.md)  
 [ HNODE enuGet3DObjectById\(HX3D pX3DHandler, wchar\_t\* objectid\)](./sdk_api_enuget3dobjectbyid.md)  
 [ HNODE enuGetAppearanceFromShape\(HX3D pX3DHandler, HNODE node\)](./sdk_api_enugetappearancefromshape.md)  
 [ HNODE enuGetGeometryFromShape\(HX3D pX3DHandler, HNODE node\)](./sdk_api_enugetgeometryfromshape.md)  
 [ HNODE enuGetMaterialFromAppearance\(HX3D pX3DHandler, HNODE node\)](./sdk_api_enugetmaterialfromappearance.md)  
 [ HNODE enuGetMaterialFromGeometry\(HX3D pX3DHandler, HNODE node\)](./sdk_api_enugetmaterialfromgeometry.md)  
 [ HNODE enuGetTransformFromGeometry\(HX3D pX3DHandler, HNODE node\)](./sdk_api_enugettransformfromgeometry.md)  
 [ HNODE enuGetCoordinateFromIndexedFaceSet\(HX3D pX3DHandler, HNODE node\)](./sdk_api_enugetcoordinatefromindexedfaceset.md)  
 [ HNODE enuGetCoordinateFromLineSet\(HX3D pX3DHandler, HNODE node\)](./sdk_api_enugetcoordinatefromlineset.md)  
 [ HNODE enuGetShapeFromGeometry\(HX3D pX3DHandler, HNODE node\)](./sdk_api_enugetshapefromgeometry.md)  
 [ void enuDelete3DObjectByNode\(HX3D pX3DHandler, HNODE pTarget\)](./sdk_api_enudelete3dobjectbynode.md)

## Script Interface

[ void enuSet3DLuaScriptByNode\(HX3D pX3D, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)](./sdk_api_enuset3dluascriptbynode.md)  
 [ void enuSet3DJavaScriptByNode\(HX3D pX3D, HNODE pNode, wchar\_t\* strFunction, wchar\_t\* strScript\)](./sdk_api_enuset3djavascriptbynode.md)  
 [ void enuExecute3DFunction\(HX3D pX3D, wchar\_t\* strFunction\)](./sdk_api_enuexecute3dfunction.md)  
 [ void enuExecute3DFunctionByNode\(HX3D pX3D, HNODE pNode, wchar\_t\* strFunction\)](./sdk_api_enuexecute3dfunctionbynode.md)
