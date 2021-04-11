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
        BnStandaloneTools_mainWin.resize(648, 634)
        self.centralwidget = QWidget(BnStandaloneTools_mainWin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(501, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.pb_run = QPushButton(self.widget)
        self.pb_run.setObjectName(u"pb_run")

        self.gridLayout.addWidget(self.pb_run, 3, 1, 1, 1)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frm_opt = QFrame(self.frame)
        self.frm_opt.setObjectName(u"frm_opt")
        self.frm_opt.setFrameShape(QFrame.StyledPanel)
        self.frm_opt.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frm_opt)


        self.gridLayout.addWidget(self.frame, 2, 0, 1, 2)

        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 88))
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.rb_myvs_18 = QRadioButton(self.groupBox)
        self.rb_myvs_18.setObjectName(u"rb_myvs_18")
        self.rb_myvs_18.setChecked(True)

        self.gridLayout_3.addWidget(self.rb_myvs_18, 0, 1, 1, 1)

        self.rb_myvs_oth = QRadioButton(self.groupBox)
        self.rb_myvs_oth.setObjectName(u"rb_myvs_oth")

        self.gridLayout_3.addWidget(self.rb_myvs_oth, 0, 3, 1, 1)

        self.rb_myvs_19 = QRadioButton(self.groupBox)
        self.rb_myvs_19.setObjectName(u"rb_myvs_19")

        self.gridLayout_3.addWidget(self.rb_myvs_19, 0, 2, 1, 1)

        self.rb_myvs_16 = QRadioButton(self.groupBox)
        self.rb_myvs_16.setObjectName(u"rb_myvs_16")

        self.gridLayout_3.addWidget(self.rb_myvs_16, 0, 0, 1, 1)

        self.le_myvsn = QLineEdit(self.groupBox)
        self.le_myvsn.setObjectName(u"le_myvsn")
        self.le_myvsn.setEnabled(False)

        self.gridLayout_3.addWidget(self.le_myvsn, 0, 4, 1, 1)

        self.lb_mayapy = QLabel(self.groupBox)
        self.lb_mayapy.setObjectName(u"lb_mayapy")

        self.gridLayout_3.addWidget(self.lb_mayapy, 1, 0, 1, 5)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.grp_exec = QGroupBox(self.widget)
        self.grp_exec.setObjectName(u"grp_exec")
        self.gridLayout_4 = QGridLayout(self.grp_exec)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.txt_cmd = QTextEdit(self.grp_exec)
        self.txt_cmd.setObjectName(u"txt_cmd")

        self.gridLayout_4.addWidget(self.txt_cmd, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.grp_exec, 1, 0, 1, 2)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        BnStandaloneTools_mainWin.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(BnStandaloneTools_mainWin)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 648, 26))
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
        self.pb_run.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"Run...", None))
        self.groupBox.setTitle(QCoreApplication.translate("BnStandaloneTools_mainWin", u"Maya Version", None))
        self.rb_myvs_18.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"2018", None))
        self.rb_myvs_oth.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"other", None))
        self.rb_myvs_19.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"2019", None))
        self.rb_myvs_16.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"2016", None))
        self.lb_mayapy.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"mayapy:", None))
        self.grp_exec.setTitle(QCoreApplication.translate("BnStandaloneTools_mainWin", u"Execute", None))
    # retranslateUi

