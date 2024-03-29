# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\szozat-solver-gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1548, 837)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 471, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.txt_present = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_present.setText("")
        self.txt_present.setObjectName("txt_present")
        self.verticalLayout.addWidget(self.txt_present)
        self.btn_present = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_present.setObjectName("btn_present")
        self.verticalLayout.addWidget(self.btn_present)
        self.lst_present = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.lst_present.setEnabled(True)
        self.lst_present.setObjectName("lst_present")
        self.verticalLayout.addWidget(self.lst_present)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(520, 0, 471, 391))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.txt_not_present = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.txt_not_present.setObjectName("txt_not_present")
        self.verticalLayout_2.addWidget(self.txt_not_present)
        self.btn_not_present = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_not_present.setObjectName("btn_not_present")
        self.verticalLayout_2.addWidget(self.btn_not_present)
        self.lst_not_present = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.lst_not_present.setEnabled(True)
        self.lst_not_present.setObjectName("lst_not_present")
        self.verticalLayout_2.addWidget(self.lst_not_present)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(1030, 310, 511, 81))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txt_regex1 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.txt_regex1.setObjectName("txt_regex1")
        self.horizontalLayout.addWidget(self.txt_regex1)
        self.txt_regex2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.txt_regex2.setObjectName("txt_regex2")
        self.horizontalLayout.addWidget(self.txt_regex2)
        self.txt_regex3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.txt_regex3.setObjectName("txt_regex3")
        self.horizontalLayout.addWidget(self.txt_regex3)
        self.txt_regex4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.txt_regex4.setObjectName("txt_regex4")
        self.horizontalLayout.addWidget(self.txt_regex4)
        self.txt_regex5 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.txt_regex5.setObjectName("txt_regex5")
        self.horizontalLayout.addWidget(self.txt_regex5)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(490, 400, 581, 24))
        self.btn_search.setObjectName("btn_search")
        self.lst_usable_words = QtWidgets.QListWidget(self.centralwidget)
        self.lst_usable_words.setGeometry(QtCore.QRect(300, 460, 921, 371))
        self.lst_usable_words.setObjectName("lst_usable_words")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(710, 430, 141, 16))
        self.label_4.setObjectName("label_4")
        self.txt_lang = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_lang.setGeometry(QtCore.QRect(1280, 30, 113, 22))
        self.txt_lang.setObjectName("txt_lang")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1200, 30, 71, 21))
        self.label_5.setObjectName("label_5")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(1240, 80, 75, 24))
        self.btn_clear.setObjectName("btn_clear")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "szozat-solver GUI"))
        self.label.setText(_translate("MainWindow", "Szereplő betűk"))
        self.btn_present.setText(_translate("MainWindow", "Szereplő betű hozzáadása"))
        self.label_2.setText(_translate("MainWindow", "Nem szereplő betűk"))
        self.btn_not_present.setText(_translate("MainWindow", "Nem szereplő betű hozzáadása"))
        self.label_3.setText(_translate("MainWindow", "Regex"))
        self.txt_regex1.setText(_translate("MainWindow", "."))
        self.txt_regex2.setText(_translate("MainWindow", "."))
        self.txt_regex3.setText(_translate("MainWindow", "."))
        self.txt_regex4.setText(_translate("MainWindow", "."))
        self.txt_regex5.setText(_translate("MainWindow", "."))
        self.btn_search.setText(_translate("MainWindow", "Szavak keresése"))
        self.label_4.setText(_translate("MainWindow", "Használható szavak listája"))
        self.txt_lang.setText(_translate("MainWindow", "hu"))
        self.label_5.setText(_translate("MainWindow", "Lang/type"))
        self.btn_clear.setText(_translate("MainWindow", "Clear ALL"))
