#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = outputTxtplan
__author__ = zhangben 
__mtime__ = 2021/3/17 : 18:07
__description__: 

THEOREM: A good programmer should wipe the butts of his predecessors in an amicable way,
    instead of reinventing a new butt.
        As long as this , code is far away from bugs, and with the god animal protecting
            I love animals. They taste delicious.
"""

import sys
import re,os,sys
from PySide.QtGui import *
from PySide.QtCore import *
from PySide import QtXml
from PySide.QtUiTools import QUiLoader
import pysideuic as uic
# from PySide2.QtWidgets import *
# from PySide2.QtGui import *
# from PySide2.QtCore import *
# from PySide2.QtUiTools import QUiLoader
# import pyside2uic as uic
#  ============= ===live template require variables =====================
#  o  utputTxtplan O OutputTxtplan || OutputTxtplan  utputtxtplan
class Stream(QObject):
    newText = Signal(str)
    # def __init__(self):
    #     super(Stream,self).__init__()
    def write(self, text):
        self.newText.emit(str(text).decode('gb2312'))
import logging
# logger = logging.getLogger(__name__)
#
# class QtHandler(logging.Handler):
#
#     def __init__(self):
#         logging.Handler.__init__(self)
#
#     def emit(self, record):
#         record = self.format(record)
#         Stream.stdout().write("{}\n".format(record))
#
# handler = QtHandler()
# handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
# logger.addHandler(handler)
# logger.setLevel(logging.DEBUG)


class ExecTxtEdt(QTextEdit):
    SgExecObj = Signal(str)
    def __init__(self,*args,**kwargs):
        super(ExecTxtEdt, self).__init__(*args,**kwargs)
        self._executeobj = None
        self.setAcceptDrops(True)

    def initUI_process(self):
        # Layout are better for placing widgets
        # QProcess object for external app
        self.process = QProcess(self)
        # QProcess emits `readyRead` when there is data to be read
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        self.process.readyRead.connect(self.dataReady)
        # Just to prevent accidentally running multiple times
        # Disable the button when process starts, and enable it when it finishes
        # self.process.started.connect(lambda: self.runButton.setEnabled(False))
        # self.process.finished.connect(lambda: self.runButton.setEnabled(True))
    
    @Slot()
    def dataReady(self):
        cursor = self.output.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(str(self.process.readAll(),'gbk'))
        self.output.setTextCursor(cursor)
        self.output.ensureCursorVisible()

    def callProgram(self,cmd,*args):
        # run the process
        # `start` takes the exec and a list of arguments
        self.process.start(cmd,args)
    def dragEnterEvent(self, event):
        print('drag-enter')
        if event.mimeData().hasUrls():
            print(event.mimeData().urls()[-1])
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, e):
        #        print("DragMove")
        e.accept()

    def dropEvent(self, event):
        url = event.mimeData().urls()[-1]
        self._executeobj  = url.toLocalFile().encode('utf-8')
        f_h,f_ext = os.path.splitext(self._executeobj)
        if f_ext in ['.py','.pyc','.mel']:
            self.SgExecObj.emit(self._executeobj)
            self.setText(self._executeobj)
        # event.setDropAction(Qt.MoveAction)
            event.accept()
        else: event.ignore()

#Function Main Start
def main():
    app = QApplication(sys.argv)
    ui=ExecTxtEdt()
    ui.show()
    # bat = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'exec', 'maya2016.bat')
    # print(bat)
    # ui.callProgram(bat)
    sys.exit(app.exec_())
    print(".....em....")
#Function Main END

if __name__ == '__main__':
    main()
