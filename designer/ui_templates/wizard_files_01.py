# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/templates/wizard_files_01.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(470, 539)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(Form)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.button_add_file = QtWidgets.QPushButton(Form)
        self.button_add_file.setObjectName("button_add_file")
        self.verticalLayout.addWidget(self.button_add_file)
        self.scrollarea_file = QtWidgets.QScrollArea(Form)
        self.scrollarea_file.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollarea_file.setWidgetResizable(True)
        self.scrollarea_file.setObjectName("scrollarea_file")
        self.scroll_file = QtWidgets.QWidget()
        self.scroll_file.setGeometry(QtCore.QRect(0, 0, 431, 125))
        self.scroll_file.setObjectName("scroll_file")
        self.layout_file = QtWidgets.QVBoxLayout(self.scroll_file)
        self.layout_file.setContentsMargins(3, 0, 3, 0)
        self.layout_file.setObjectName("layout_file")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layout_file.addItem(spacerItem)
        self.scrollarea_file.setWidget(self.scroll_file)
        self.verticalLayout.addWidget(self.scrollarea_file)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.button_add_folder = QtWidgets.QPushButton(Form)
        self.button_add_folder.setObjectName("button_add_folder")
        self.verticalLayout.addWidget(self.button_add_folder)
        self.scrollarea_folder = QtWidgets.QScrollArea(Form)
        self.scrollarea_folder.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollarea_folder.setWidgetResizable(True)
        self.scrollarea_folder.setObjectName("scrollarea_folder")
        self.scroll_folder = QtWidgets.QWidget()
        self.scroll_folder.setGeometry(QtCore.QRect(0, 0, 431, 125))
        self.scroll_folder.setObjectName("scroll_folder")
        self.layout_folder = QtWidgets.QVBoxLayout(self.scroll_folder)
        self.layout_folder.setContentsMargins(3, 0, 3, 0)
        self.layout_folder.setObjectName("layout_folder")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layout_folder.addItem(spacerItem1)
        self.scrollarea_folder.setWidget(self.scroll_folder)
        self.verticalLayout.addWidget(self.scrollarea_folder)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.finish_button = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.finish_button.sizePolicy().hasHeightForWidth())
        self.finish_button.setSizePolicy(sizePolicy)
        self.finish_button.setObjectName("finish_button")
        self.horizontalLayout.addWidget(self.finish_button)
        self.cancel_button = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Files and Folders Wizard"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"justify\">Select the files and folders to be installed. The &quot;<span style=\" font-style:italic;\">Source&quot;</span> fields are used to select the file/folder to be installed. The <span style=\" font-style:italic;\">&quot;Destination&quot;</span> fields are used to select where the item will be installed to - a blank fields corresponds to the <span style=\" font-style:italic;\">Data</span> folder itself.</p><p align=\"justify\">See the <span style=\" text-decoration: underline;\">Help</span> for more information.</p></body></html>"))
        self.label_2.setText(_translate("Form", "Files To Be Installed:"))
        self.button_add_file.setText(_translate("Form", "Add File"))
        self.label_3.setText(_translate("Form", "Folders To Be Installed:"))
        self.button_add_folder.setText(_translate("Form", "Add Folder"))
        self.finish_button.setText(_translate("Form", "Finish"))
        self.cancel_button.setText(_translate("Form", "Cancel"))
