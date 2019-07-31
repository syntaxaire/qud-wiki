# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qud_explorer_window.ui',
# licensing of 'qud_explorer_window.ui' applies.
#
# Created: Tue Jul 30 23:43:53 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout.addWidget(self.plainTextEdit)
        self.tile_label = QtWidgets.QLabel(self.centralwidget)
        self.tile_label.setMinimumSize(QtCore.QSize(160, 240))
        self.tile_label.setStyleSheet("background-color: rgb(15, 59, 58);")
        self.tile_label.setText("")
        self.tile_label.setObjectName("tile_label")
        self.horizontalLayout.addWidget(self.tile_label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.search_label = QtWidgets.QLabel(self.centralwidget)
        self.search_label.setObjectName("search_label")
        self.horizontalLayout_2.addWidget(self.search_label)
        self.search_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.search_line_edit.setObjectName("search_line_edit")
        self.horizontalLayout_2.addWidget(self.search_line_edit)
        self.expand_all_button = QtWidgets.QPushButton(self.centralwidget)
        self.expand_all_button.setObjectName("expand_all_button")
        self.horizontalLayout_2.addWidget(self.expand_all_button)
        self.collapse_all_button = QtWidgets.QPushButton(self.centralwidget)
        self.collapse_all_button.setObjectName("collapse_all_button")
        self.horizontalLayout_2.addWidget(self.collapse_all_button)
        self.restore_all_button = QtWidgets.QPushButton(self.centralwidget)
        self.restore_all_button.setObjectName("restore_all_button")
        self.horizontalLayout_2.addWidget(self.restore_all_button)
        self.check_selected_button = QtWidgets.QPushButton(self.centralwidget)
        self.check_selected_button.setObjectName("check_selected_button")
        self.horizontalLayout_2.addWidget(self.check_selected_button)
        self.upload_templates_button = QtWidgets.QPushButton(self.centralwidget)
        self.upload_templates_button.setObjectName("upload_templates_button")
        self.horizontalLayout_2.addWidget(self.upload_templates_button)
        self.upload_tiles_button = QtWidgets.QPushButton(self.centralwidget)
        self.upload_tiles_button.setObjectName("upload_tiles_button")
        self.horizontalLayout_2.addWidget(self.upload_tiles_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.tree_target_widget = QtWidgets.QWidget(self.centralwidget)
        self.tree_target_widget.setObjectName("tree_target_widget")
        self.verticalLayout_3.addWidget(self.tree_target_widget)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_ObjectBlueprints_xml = QtWidgets.QAction(MainWindow)
        self.actionOpen_ObjectBlueprints_xml.setObjectName("actionOpen_ObjectBlueprints_xml")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen_ObjectBlueprints_xml)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Qud Blueprint Explorer", None, -1))
        self.search_label.setText(QtWidgets.QApplication.translate("MainWindow", "Search:", None, -1))
        self.expand_all_button.setText(QtWidgets.QApplication.translate("MainWindow", "Expand all", None, -1))
        self.collapse_all_button.setText(QtWidgets.QApplication.translate("MainWindow", "Collapse all", None, -1))
        self.restore_all_button.setText(QtWidgets.QApplication.translate("MainWindow", "Default expansion", None, -1))
        self.check_selected_button.setText(QtWidgets.QApplication.translate("MainWindow", "🔁 Scan wiki for selected", None, -1))
        self.upload_templates_button.setText(QtWidgets.QApplication.translate("MainWindow", "⬆ Upload selected templates", None, -1))
        self.upload_tiles_button.setText(QtWidgets.QApplication.translate("MainWindow", "⬆ Upload selected tiles", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.actionOpen_ObjectBlueprints_xml.setText(QtWidgets.QApplication.translate("MainWindow", "Open ObjectBlueprints.xml...", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("MainWindow", "Exit", None, -1))

