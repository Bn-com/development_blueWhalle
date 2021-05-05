#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = diyPallet
__author__ = Ben 
__mtime__ = 2021/4/5 : 23:04
__description__: 

THEOREM: A good programmer should wipe the butts of his predecessors in an amicable way,
    instead of reinventing a new butt.
        As long as this , code is far away from bugs, and with the god animal protecting
            I love animals. They taste delicious.
"""
from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtUiTools import QUiLoader
import pysideuic as uic

class MyPaletter(QPalette):
    def __init__(self,*args,**kwargs):
        super(myPaletter,self).__init__(*args,**kwargs)
        self._mainColor = QColor(1, 22, 39)
    @property
    def mainColor(self):
        return self._mainColor
    mainColor.setter
    def mainColor(self,color):
        self._mainColor = color
    def _setPlatter(self):
        # self.setStyle("Windows")
        # self.setStyle(QStyleFactory.create('Windows'))
        # palette = QPalette()
        self.setColor(QPalette.Window,self.mainColor)
        # self.setColor(QPalette.Window, QColor(33, 33, 33))
        # self.setColor(QPalette.Window, QColor(60, 66, 72))
        self.setColor(QPalette.WindowText, QColor(255, 128, 0))
        # self.setColor(QPalette.Base, QColor(25, 25, 25))
        self.setColor(QPalette.Base, QColor(33, 50, 63))
        self.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        self.setColor(QPalette.ToolTipBase, Qt.black)
        self.setColor(QPalette.ToolTipText, Qt.white)
        self.setColor(QPalette.Text, QColor(255, 128, 0))
        # self.setColor(QPalette.Button, QColor(0, 0, 0))
        self.setColor(QPalette.ButtonText, QColor(88, 155, 122))
        self.setColor(QPalette.BrightText, Qt.red)
        self.setColor(QPalette.Link, QColor(42, 130, 218))
        self.setColor(QPalette.Highlight, QColor(42, 130, 218))
        self.setColor(QPalette.HighlightedText, QColor(127, 235, 255))
        # self.parent.setPallet(self)