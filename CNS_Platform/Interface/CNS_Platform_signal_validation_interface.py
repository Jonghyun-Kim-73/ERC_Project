# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './/Interface\CNS_Platform_signal_validation_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1091, 842)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self._main_frame = QtWidgets.QFrame(Form)
        self._main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self._main_frame.setObjectName("_main_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self._main_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self._area_title = QtWidgets.QFrame(self._main_frame)
        self._area_title.setMaximumSize(QtCore.QSize(16777215, 30))
        self._area_title.setFrameShape(QtWidgets.QFrame.Box)
        self._area_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self._area_title.setLineWidth(2)
        self._area_title.setObjectName("_area_title")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self._area_title)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self._title = QtWidgets.QLabel(self._area_title)
        self._title.setObjectName("_title")
        self.verticalLayout_2.addWidget(self._title)
        self.verticalLayout.addWidget(self._area_title)
        self._area_para = QtWidgets.QFrame(self._main_frame)
        self._area_para.setFrameShape(QtWidgets.QFrame.Box)
        self._area_para.setFrameShadow(QtWidgets.QFrame.Raised)
        self._area_para.setLineWidth(2)
        self._area_para.setObjectName("_area_para")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self._area_para)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self._area_para_grid = QtWidgets.QGridLayout()
        self._area_para_grid.setSpacing(0)
        self._area_para_grid.setObjectName("_area_para_grid")
        self.verticalLayout_3.addLayout(self._area_para_grid)
        self.verticalLayout.addWidget(self._area_para)
        self.gridLayout.addWidget(self._main_frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Signal Validation Monitoring [by.DL]"))
        self._title.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Signal Valdation Monitoring</span></p></body></html>"))
