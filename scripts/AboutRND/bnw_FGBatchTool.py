#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = bnw_FGBatchTool
__author__ = zhangben 
__mtime__ = 2021/2/22 : 9:51
__description__: 

    code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import re,os,sys
try:
    from PySide.QtGui import *
    from PySide.QtCore import *
    from PySide.QtUiTools import QUiLoader
    import pysideuic as uic

except:
    from PySide2.QtWidgets import *
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtUiTools import QUiLoader
    import pyside2uic as uic
if str(sys.executable).endswith("maya.exe"):
    import maya.cmds as mc
    import pymel.core as pm
    import maya.OpenMaya as om
    import maya.api.OpenMaya as om2
    import maya.OpenMayaUI as mui
    try:
        import shiboken as sbk
    except:
        import shiboken2 as sbk
def getMayaWindow():
    if str(sys.executable).endswith("maya.exe"):
        ptr = mui.MQtUtil.mainWindow()
        if ptr is not None:
            return sbk.wrapInstance(long(ptr), QWidget)
#  ============= ===live template require variables =====================
#  b  nw_FGBatchTool B Bnw_FGBatchTool || Bnw_FGBatchTool  nwFgbatchtool
class Bnw_FGBatchTool_Ui(QMainWindow):
    def __init__(self,parent=getMayaWindow()):
        super(Bnw_FGBatchTool_Ui,self).__init__(parent)
        self.setObjectName("Bnw_FGBatchTool_mainWin")
        self.centralWidget = QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.voticalLayout = QVBoxLayout(self.centralWidget)
        # self.horizantalLayout =

    def setupUI2(self):
        """
            set up ui
        :return:
        """

def main_ui():
    for widget in qApp.allWidgets():
        if hasattr(widget, "objectName"):
            # if widget.objectName() == '****':
            if widget.objectName() == "Bnw_FGBatchTool_mainWin": #'Ui_MainWindow'
                widget.close()
    view = Bnw_FGBatchTool_Ui(parent=getMayaWindow())
    view.show()

if __name__ == "__main__":
    """ 
        #===========================================dereict invoke main_ui================================
        from  import bnw_FGBatchTool
        bnwFgBatchTool.main_ui()
        #=================================================================================================
        import sys,os
        from PySide2.QtWidgets import *
        sys.path.append(os.path.dirName(r'F:\Development\Oem\OEM4Maya\scripts\AboutRND\bnw_FGBatchTool.py'))
        for win in qApp.allWidgets():
            if hasattr(win, "objectName"):
                # if win.objectName() == '****':
                if win.objectName() == "Bnw_FGBatchTool_mainWin": 
                    win.close()
        import bnw_FGBatchTool as xxx;reload(xxx)
        myui = xxx.Bnw_FGBatchTool_Ui(xxx.getMayaWindow())
        myui.show()
        #xxx.main_ui()
    """
    app = QApplication(sys.argv)
    # view = UI()
    view = Bnw_FGBatchTool_Ui()
    view.show()
    sys.exit(app.exec_())
