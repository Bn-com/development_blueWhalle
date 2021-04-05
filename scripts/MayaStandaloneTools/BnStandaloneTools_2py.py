# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BnStandaloneTools.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_BnStandaloneTools_mainWin(object):
    def setupUi(self, BnStandaloneTools_mainWin):
        if not BnStandaloneTools_mainWin.objectName():
            BnStandaloneTools_mainWin.setObjectName(u"BnStandaloneTools_mainWin")
        BnStandaloneTools_mainWin.resize(490, 414)
        self.centralwidget = QWidget(BnStandaloneTools_mainWin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_mayapy = QLabel(self.frame)
        self.lb_mayapy.setObjectName(u"lb_mayapy")

        self.verticalLayout.addWidget(self.lb_mayapy)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(343, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.pb_run = QPushButton(self.widget)
        self.pb_run.setObjectName(u"pb_run")

        self.gridLayout.addWidget(self.pb_run, 2, 1, 1, 1)

        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rb_myvs_16 = QRadioButton(self.groupBox)
        self.rb_myvs_16.setObjectName(u"rb_myvs_16")

        self.horizontalLayout.addWidget(self.rb_myvs_16)

        self.rb_myvs_18 = QRadioButton(self.groupBox)
        self.rb_myvs_18.setObjectName(u"rb_myvs_18")
        self.rb_myvs_18.setChecked(True)

        self.horizontalLayout.addWidget(self.rb_myvs_18)

        self.rb_myvs_19 = QRadioButton(self.groupBox)
        self.rb_myvs_19.setObjectName(u"rb_myvs_19")

        self.horizontalLayout.addWidget(self.rb_myvs_19)

        self.rb_myvs_oth = QRadioButton(self.groupBox)
        self.rb_myvs_oth.setObjectName(u"rb_myvs_oth")

        self.horizontalLayout.addWidget(self.rb_myvs_oth)

        self.le_myvsn = QLineEdit(self.groupBox)
        self.le_myvsn.setObjectName(u"le_myvsn")
        self.le_myvsn.setEnabled(False)

        self.horizontalLayout.addWidget(self.le_myvsn)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        BnStandaloneTools_mainWin.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(BnStandaloneTools_mainWin)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 490, 26))
        BnStandaloneTools_mainWin.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(BnStandaloneTools_mainWin)
        self.statusbar.setObjectName(u"statusbar")
        BnStandaloneTools_mainWin.setStatusBar(self.statusbar)

        self.retranslateUi(BnStandaloneTools_mainWin)
        self.rb_myvs_oth.toggled.connect(self.le_myvsn.setEnabled)

        QMetaObject.connectSlotsByName(BnStandaloneTools_mainWin)
    # setupUi

    def retranslateUi(self, BnStandaloneTools_mainWin):
        BnStandaloneTools_mainWin.setWindowTitle(QCoreApplication.translate("BnStandaloneTools_mainWin", u"MainWindow", None))
        self.lb_mayapy.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"mayapy:", None))
        self.pb_run.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"Run...", None))
        self.groupBox.setTitle(QCoreApplication.translate("BnStandaloneTools_mainWin", u"Maya Version", None))
        self.rb_myvs_16.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"2016", None))
        self.rb_myvs_18.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"2018", None))
        self.rb_myvs_19.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"2019", None))
        self.rb_myvs_oth.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"other", None))
    # retranslateUi

