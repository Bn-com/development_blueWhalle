#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = bnStandalongeTools
__author__ = Ben 
__mtime__ = 2021/4/5 : 14:10
__description__: 

THEOREM: A good programmer should wipe the butts of his predecessors in an amicable way,
    instead of reinventing a new butt.
        As long as this , code is far away from bugs, and with the god animal protecting
            I love animals. They taste delicious.
"""
import sys,re,os,copy,inspect,random
import xml.etree.ElementTree as xml
try:
    from cStringIO import StringIO
except:
    from io import StringIO
import logging
logger = logging.getLogger(__name__)
if str(sys.executable).endswith("maya.exe"):
    import maya.OpenMayaUI as mui
    try:
        import shiboken as sbk
    except:
        import shiboken2 as sbk
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
def getMayaWindow():
    ptr = mui.MQtUtil.mainWindow()
    if ptr is not None:
        return sbk.wrapInstance(long(ptr), QWidget)
def loadUiType(uiFile):
    parsed = xml.parse(uiFile)
    widget_class = parsed.find('widget').get('class')
    form_class = parsed.find('class').text
    with open(uiFile, 'r') as f:
        o = StringIO()
        frame = {}
        uic.compileUi(f, o, indent=0)
        pyc = compile(o.getvalue(), '<string>', 'exec')
        exec(pyc,frame)
        # Fetch the base_class and form class based on their type in the xml from designer
        form_class = frame['Ui_%s' % form_class]
        base_class = eval('%s' % widget_class)
    return form_class, base_class
## live tempelate require variables b B  BnStandaloneTools nStandaloneTools
ui_name = 'bnStandaloneTools.ui'
import command as cmd
import upEnv
import optTxtEdt
import diyPallet
class BnStandaloneTools_UI(QMainWindow):
    def __init__(self, parent=None):
        super(BnStandaloneTools_UI, self).__init__(parent)
        # dir_path = os.path.dirname(sys.argv[0])
        dir_path = os.path.dirname(__file__)
        ui_file = os.path.normpath(os.path.join(dir_path, "uis/{}".format(ui_name)))
        form, base = loadUiType(ui_file)
        self.bs = base()
        self.ui = form()
        self.ui.setupUi(self)
        try: 1/0; import BnStandaloneTools_2py as xx;self.ui = xx.Ui_BnStandaloneTools_mainWin()
        except: pass
        self.pb_lst = self.findChildren(QPushButton)
        self.setupUi2()
        self.move(200,200)
        # self.resize()
        #---------------------variables-------------------------
        self.maya_version = None
        self._maya_location = None
        self._python_home = None

    def setupUi2(self):
        self.buttonGroup = QButtonGroup(self)
        self.buttonGroup.addButton(self.ui.rb_myvs_16)
        self.buttonGroup.addButton(self.ui.rb_myvs_18)
        self.buttonGroup.addButton(self.ui.rb_myvs_19)
        self.buttonGroup.addButton(self.ui.rb_myvs_oth)
        # self.ui.
        self.opt = optTxtEdt.OptTxEdt(self.ui.frm_opt)
        self.opt_ly = QVBoxLayout(self.ui.frm_opt)
        self.opt_ly.addWidget(self.opt)
        self.opt.redirectOPT()
        for e_bt in self.pb_lst:
            # print(e_pt.objectName())
            if e_bt.objectName() not in ['pb_run']:
                _fuction = getattr(self, "_cmd_{}".format(e_bt.objectName()))  if "_cmd_{}".format(e_bt.objectName()) in self.__class__.__dict__ else lambda :self.someFunc(e_bt)
                e_bt.clicked.connect(_fuction)
        try:
            self.ui.pb_run.clicked.connect(self.runIt)
        except:
            pass
        # self._diyplatter = diyPallet.MyPaletter(self)
        # self._diyplatter._setPlatter()
        self._setPlatter()
    def reset(self):
        self.maya_version = None
        self._maya_location = None
        self._python_home = None
    def runIt(self):
        print("Em.......................")
        self._preprocess()

    def _preprocess(self):
        self.reset()
        self._fn_maya_location()
        self._set_mayapy()
    def someFunc(self,q):
        print(q.objectName())
    def _fn_q_maya_version(self):
        sel_rb_vsn  = self.buttonGroup.checkedButton()
        vs_str = str(sel_rb_vsn.text())
        mayaVsn = None
        if vs_str in ['other']:
            mayaVsn = str(self.ui.le_myvsn.text())
        else:
            mayaVsn = vs_str
        return mayaVsn
    def _set_mayapy(self):
        """
            set mayapy lable text
        """
        if self._maya_location:
            self.ui.lb_mayapy.setText(cmd.joinpath(self._maya_location, 'bin', 'mayapy.exe'))
        else:
            self.ui.lb_mayapy.setText(u"没有找到maya{}安装路径".format(self.maya_version))


    def _fn_maya_location(self):
        self.maya_version = self._fn_q_maya_version()
        print(self.maya_version)
        winenv = upEnv.Win32Environment()
        winenv.subkey=r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Autodesk Maya {}".format(self.maya_version)
        winenv.name="InstallLocation"
        maya_loc = winenv.getenv()
        if not maya_loc:
            logger.error(u"您的系统中没有找到 maya{} 的安装路径".format(self.maya_version))
            return
        self._maya_location = maya_loc
        self._python_home = cmd.normalJoinpath(maya_loc,'Python')

    def fn_set_env(self):
        os.environ["MAYA_LOCATION"] = self._maya_location
        os.environ["PYTHONHOME"] = self._python_home
        # os.environ["PATH"] = "C:\\Program Files\\Autodesk\\Maya2014\\bin;" + os.environ["PATH"]
        # sys.path.append("C:\Program Files\Autodesk\Maya2014\Python\lib\site-packages\setuptools-0.6c9-py2.6.egg")
        # sys.path.append("C:\Program Files\Autodesk\Maya2014\Python\lib\site-packages\pymel-1.0.0-py2.6.egg")
        # sys.path.append("C:\Program Files\Autodesk\Maya2014\Python\lib\site-packages\ipython-0.10.1-py2.6.egg")
        # sys.path.append("C:\Program Files\Autodesk\Maya2014\Python\lib\site-packages\ply-3.3-py2.6.egg")
        # sys.path.append("C:\Program Files\Autodesk\Maya2014\\bin\python26.zip")
        # sys.path.append("C:\Program Files\Autodesk\Maya2014\Python\DLLs")
        # sys.path.append("C:\Program Files\Autodesk\Maya2014\Python\lib")
        # sys.path.append("C:\Program Files\Autodesk\Maya2014\Python\lib\plat-win")
        # sys.path.append("C:\Program Files\Autodesk\Maya2014\Python\lib\lib-tk")
        # sys.path.append("C:\Program Files\Autodesk\Maya2014\\bin")
        # sys.path.append("C:\Program Files\Autodesk\Maya2014\Python")
        # sys.path.append("C:\Program Files\Autodesk\Maya2014\Python\lib\site-packages")
    def _setPlatter(self):
        # self.setStyle("Windows")
        # self.setStyle(QStyleFactory.create('Windows'))
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(1, 22, 39))
        # palette.setColor(QPalette.Window, QColor(33, 33, 33))
        # palette.setColor(QPalette.Window, QColor(60, 66, 72))
        palette.setColor(QPalette.WindowText, QColor(255, 128, 0))
        # palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.Base, QColor(33, 50, 63))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.black)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, QColor(255, 128, 0))
        # palette.setColor(QPalette.Button, QColor(0, 0, 0))
        palette.setColor(QPalette.ButtonText, QColor(88, 155, 122))
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, QColor(127, 235, 255))
        self.setPalette(palette)
def main_ui():
    for widget in qApp.allWidgets():
        if hasattr(widget, "objectName"):
            # if widget.objectName() == '****':
            if widget.objectName() == "BnStandaloneTools_mainWin": #'Ui_MainWindow'
                widget.close()
    view = BnStandaloneTools_UI(parent=getMayaWindow())
    view.show()        
if __name__ == '__main__':
    import sys
    """
import sys
sys.path.append(r'&FILE PATH PASTE HERE& ')
from PySide2.QtWidgets import *

import bnStandaloneTools as xxx;reload(xxx)
#xxx.main_ui()
for widget in qApp.allWidgets():
    if hasattr(widget, "objectName"):
        if widget.objectName() == "BnStandaloneTools_mainWin":
            widget.close()
xx = xxx.BnStandaloneTools_UI(xxx.getMayaWindow())
xx.show()
    """
    app = QApplication(sys.argv)
    # view = UI()
    view = BnStandaloneTools_UI()
    view.show()
    sys.exit(app.exec_())
    