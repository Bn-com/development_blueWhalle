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
        BnStandaloneTools_mainWin.resize(681, 793)
        self.centralwidget = QWidget(BnStandaloneTools_mainWin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
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

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.grp_exec = QGroupBox(self.frame)
        self.grp_exec.setObjectName(u"grp_exec")
        self.verticalLayout_2 = QVBoxLayout(self.grp_exec)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.rb_file = QRadioButton(self.grp_exec)
        self.rb_file.setObjectName(u"rb_file")
        self.rb_file.setChecked(True)

        self.horizontalLayout_3.addWidget(self.rb_file)

        self.rb_py = QRadioButton(self.grp_exec)
        self.rb_py.setObjectName(u"rb_py")

        self.horizontalLayout_3.addWidget(self.rb_py)

        self.rb_mel = QRadioButton(self.grp_exec)
        self.rb_mel.setObjectName(u"rb_mel")

        self.horizontalLayout_3.addWidget(self.rb_mel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.frm_exec = QFrame(self.grp_exec)
        self.frm_exec.setObjectName(u"frm_exec")
        self.frm_exec.setFrameShape(QFrame.StyledPanel)
        self.frm_exec.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frm_exec)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.grp_exec)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.le_search = QLineEdit(self.grp_exec)
        self.le_search.setObjectName(u"le_search")

        self.horizontalLayout.addWidget(self.le_search)

        self.pb_dir_srch = QPushButton(self.grp_exec)
        self.pb_dir_srch.setObjectName(u"pb_dir_srch")

        self.horizontalLayout.addWidget(self.pb_dir_srch)

        self.chbx_sub_srch = QCheckBox(self.grp_exec)
        self.chbx_sub_srch.setObjectName(u"chbx_sub_srch")

        self.horizontalLayout.addWidget(self.chbx_sub_srch)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.grp_exec)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.le_opt = QLineEdit(self.grp_exec)
        self.le_opt.setObjectName(u"le_opt")

        self.horizontalLayout_2.addWidget(self.le_opt)

        self.pb_dir_opt = QPushButton(self.grp_exec)
        self.pb_dir_opt.setObjectName(u"pb_dir_opt")

        self.horizontalLayout_2.addWidget(self.pb_dir_opt)

        self.chbx_sub_opt = QCheckBox(self.grp_exec)
        self.chbx_sub_opt.setObjectName(u"chbx_sub_opt")

        self.horizontalLayout_2.addWidget(self.chbx_sub_opt)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.grp_exec)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 2)

        self.frm_opt = QFrame(self.widget)
        self.frm_opt.setObjectName(u"frm_opt")
        self.frm_opt.setFrameShape(QFrame.StyledPanel)
        self.frm_opt.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frm_opt, 2, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(501, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.pb_run = QPushButton(self.widget)
        self.pb_run.setObjectName(u"pb_run")

        self.gridLayout.addWidget(self.pb_run, 3, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.widget)

        BnStandaloneTools_mainWin.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(BnStandaloneTools_mainWin)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 681, 26))
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
        self.groupBox.setTitle(QCoreApplication.translate("BnStandaloneTools_mainWin", u"Maya Version", None))
        self.rb_myvs_18.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"2018", None))
        self.rb_myvs_oth.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"other", None))
        self.rb_myvs_19.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"2019", None))
        self.rb_myvs_16.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"2016", None))
        self.lb_mayapy.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"mayapy:", None))
        self.grp_exec.setTitle(QCoreApplication.translate("BnStandaloneTools_mainWin", u"Execute", None))
        self.rb_file.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"file", None))
        self.rb_py.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"python command", None))
        self.rb_mel.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"mel command", None))
        self.label.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"\u5904\u7406\u6587\u4ef6\u8def\u5f84", None))
        self.pb_dir_srch.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"...\u6d4f\u89c8", None))
        self.chbx_sub_srch.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"\u5305\u62ec\u5b50\u6587\u4ef6\u5939", None))
        self.label_2.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"\u8f93\u51fa\u8def\u5f84", None))
        self.pb_dir_opt.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"...\u6d4f\u89c8", None))
        self.chbx_sub_opt.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"\u521b\u5efa\u5b50\u6587\u4ef6\u5939", None))
        self.pb_run.setText(QCoreApplication.translate("BnStandaloneTools_mainWin", u"Run...", None))
    # retranslateUi

