# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        MainWindow.setMinimumSize(QtCore.QSize(400, 600))
        MainWindow.setMaximumSize(QtCore.QSize(400, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/translate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.main_gridLayout = QtWidgets.QGridLayout()
        self.main_gridLayout.setObjectName("main_gridLayout")
        self.comboBox_dest_lang = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_dest_lang.setObjectName("comboBox_dest_lang")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/lang_cn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_dest_lang.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/lang_en.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_dest_lang.addItem(icon2, "")
        self.main_gridLayout.addWidget(self.comboBox_dest_lang, 2, 0, 1, 2)
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_clear.setIcon(icon3)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.main_gridLayout.addWidget(self.pushButton_clear, 2, 3, 1, 1)
        self.pushButton_copy = QtWidgets.QPushButton(self.centralwidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_copy.setIcon(icon4)
        self.pushButton_copy.setObjectName("pushButton_copy")
        self.main_gridLayout.addWidget(self.pushButton_copy, 2, 2, 1, 1)
        self.comboBox_src_lang = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_src_lang.setObjectName("comboBox_src_lang")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/lang_auto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_src_lang.addItem(icon5, "")
        self.comboBox_src_lang.addItem(icon1, "")
        self.comboBox_src_lang.addItem(icon2, "")
        self.main_gridLayout.addWidget(self.comboBox_src_lang, 0, 0, 1, 2)
        self.plainTextEdit_src = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_src.setPlainText("")
        self.plainTextEdit_src.setObjectName("plainTextEdit_src")
        self.main_gridLayout.addWidget(self.plainTextEdit_src, 1, 0, 1, 4)
        self.plainTextEdit_dest = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_dest.setPlainText("")
        self.plainTextEdit_dest.setObjectName("plainTextEdit_dest")
        self.main_gridLayout.addWidget(self.plainTextEdit_dest, 3, 0, 1, 4)
        self.comboBox_trans_api = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_trans_api.setObjectName("comboBox_trans_api")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/translate_google.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_trans_api.addItem(icon6, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/translate_baidu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_trans_api.addItem(icon7, "")
        self.main_gridLayout.addWidget(self.comboBox_trans_api, 0, 2, 1, 2)
        self.gridLayout_2.addLayout(self.main_gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "根号三翻译器"))
        self.comboBox_dest_lang.setItemText(0, _translate("MainWindow", "目标语言：中文"))
        self.comboBox_dest_lang.setItemText(1, _translate("MainWindow", "目标语言：英文"))
        self.pushButton_clear.setText(_translate("MainWindow", "清屏"))
        self.pushButton_copy.setText(_translate("MainWindow", "复制"))
        self.comboBox_src_lang.setCurrentText(_translate("MainWindow", "源语言：自动"))
        self.comboBox_src_lang.setItemText(0, _translate("MainWindow", "源语言：自动"))
        self.comboBox_src_lang.setItemText(1, _translate("MainWindow", "源语言：中文"))
        self.comboBox_src_lang.setItemText(2, _translate("MainWindow", "源语言：英文"))
        self.comboBox_trans_api.setPlaceholderText(_translate("MainWindow", "翻译接口"))
        self.comboBox_trans_api.setItemText(0, _translate("MainWindow", "谷歌"))
        self.comboBox_trans_api.setItemText(1, _translate("MainWindow", "百度"))
