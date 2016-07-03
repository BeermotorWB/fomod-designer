# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/templates/window_mainframe.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 563)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setObjectName("splitter")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tabWidgetPage1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.preview_label = QtWidgets.QLabel(self.tabWidgetPage1)
        self.preview_label.setAlignment(QtCore.Qt.AlignCenter)
        self.preview_label.setWordWrap(True)
        self.preview_label.setObjectName("preview_label")
        self.horizontalLayout_4.addWidget(self.preview_label)
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.tabWidgetPage2)
        self.label.setLineWidth(1)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.xml_code_browser = QtWidgets.QTextBrowser(self.tabWidgetPage2)
        self.xml_code_browser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.xml_code_browser.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.xml_code_browser.setObjectName("xml_code_browser")
        self.verticalLayout.addWidget(self.xml_code_browser)
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.horizontalLayout_3.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.property_editor = QtWidgets.QDockWidget(MainWindow)
        self.property_editor.setMinimumSize(QtCore.QSize(250, 63))
        self.property_editor.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.property_editor.setObjectName("property_editor")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.layout_prop_editor = QtWidgets.QFormLayout(self.dockWidgetContents)
        self.layout_prop_editor.setObjectName("layout_prop_editor")
        self.property_editor.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.property_editor)
        self.node_tree = QtWidgets.QDockWidget(MainWindow)
        self.node_tree.setEnabled(True)
        self.node_tree.setMinimumSize(QtCore.QSize(250, 222))
        self.node_tree.setFloating(False)
        self.node_tree.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.node_tree.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.node_tree.setObjectName("node_tree")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button_wizard = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.button_wizard.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_wizard.sizePolicy().hasHeightForWidth())
        self.button_wizard.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.button_wizard.setFont(font)
        self.button_wizard.setCheckable(False)
        self.button_wizard.setFlat(False)
        self.button_wizard.setObjectName("button_wizard")
        self.verticalLayout_2.addWidget(self.button_wizard)
        self.node_tree_view = QtWidgets.QTreeView(self.dockWidgetContents_2)
        self.node_tree_view.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.node_tree_view.sizePolicy().hasHeightForWidth())
        self.node_tree_view.setSizePolicy(sizePolicy)
        self.node_tree_view.setMinimumSize(QtCore.QSize(151, 0))
        self.node_tree_view.setAcceptDrops(True)
        self.node_tree_view.setDragEnabled(True)
        self.node_tree_view.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.node_tree_view.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.node_tree_view.setAlternatingRowColors(True)
        self.node_tree_view.setIndentation(10)
        self.node_tree_view.setHeaderHidden(True)
        self.node_tree_view.setObjectName("node_tree_view")
        self.verticalLayout_2.addWidget(self.node_tree_view)
        self.node_tree.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.node_tree)
        self.children_box = QtWidgets.QDockWidget(MainWindow)
        self.children_box.setMinimumSize(QtCore.QSize(250, 83))
        self.children_box.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.children_box.setObjectName("children_box")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.layout_box = QtWidgets.QVBoxLayout(self.dockWidgetContents_3)
        self.layout_box.setContentsMargins(3, 3, 3, 3)
        self.layout_box.setSpacing(3)
        self.layout_box.setObjectName("layout_box")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layout_box.addItem(spacerItem)
        self.children_box.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.children_box)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menuBar.setObjectName("menuBar")
        self.menu_File = QtWidgets.QMenu(self.menuBar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Recent_Files = QtWidgets.QMenu(self.menu_File)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../logos/logo_recent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_Recent_Files.setIcon(icon)
        self.menu_Recent_Files.setObjectName("menu_Recent_Files")
        self.menu_Tools = QtWidgets.QMenu(self.menuBar)
        self.menu_Tools.setObjectName("menu_Tools")
        self.menu_View = QtWidgets.QMenu(self.menuBar)
        self.menu_View.setObjectName("menu_View")
        self.menu_Help = QtWidgets.QMenu(self.menuBar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menuBar)
        self.action_Open = QtWidgets.QAction(MainWindow)
        self.action_Open.setEnabled(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../logos/logo_open_file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Open.setIcon(icon1)
        self.action_Open.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_Open.setAutoRepeat(True)
        self.action_Open.setObjectName("action_Open")
        self.action_Save = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../logos/logo_floppy_disk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Save.setIcon(icon2)
        self.action_Save.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_Save.setObjectName("action_Save")
        self.actionO_ptions = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../logos/logo_gear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionO_ptions.setIcon(icon3)
        self.actionO_ptions.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionO_ptions.setObjectName("actionO_ptions")
        self.action_Refresh = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../logos/logo_refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Refresh.setIcon(icon4)
        self.action_Refresh.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_Refresh.setObjectName("action_Refresh")
        self.action_Delete = QtWidgets.QAction(MainWindow)
        self.action_Delete.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../logos/logo_cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Delete.setIcon(icon5)
        self.action_Delete.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_Delete.setObjectName("action_Delete")
        self.action_About = QtWidgets.QAction(MainWindow)
        self.action_About.setEnabled(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../logos/logo_notepad.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_About.setIcon(icon6)
        self.action_About.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_About.setObjectName("action_About")
        self.actionHe_lp = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../logos/logo_info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHe_lp.setIcon(icon7)
        self.actionHe_lp.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionHe_lp.setObjectName("actionHe_lp")
        self.action_Object_Tree = QtWidgets.QAction(MainWindow)
        self.action_Object_Tree.setCheckable(True)
        self.action_Object_Tree.setChecked(True)
        self.action_Object_Tree.setObjectName("action_Object_Tree")
        self.action_Property_Editor = QtWidgets.QAction(MainWindow)
        self.action_Property_Editor.setCheckable(True)
        self.action_Property_Editor.setChecked(True)
        self.action_Property_Editor.setObjectName("action_Property_Editor")
        self.actionObject_Box = QtWidgets.QAction(MainWindow)
        self.actionObject_Box.setCheckable(True)
        self.actionObject_Box.setChecked(True)
        self.actionObject_Box.setObjectName("actionObject_Box")
        self.actionClear = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../logos/logo_clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClear.setIcon(icon8)
        self.actionClear.setObjectName("actionClear")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../logos/logo_copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon9)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../logos/logo_paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon10)
        self.actionPaste.setObjectName("actionPaste")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setEnabled(False)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../logos/logo_undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon11)
        self.actionUndo.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setEnabled(False)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../logos/logo_redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon12)
        self.actionRedo.setObjectName("actionRedo")
        self.actionExpand_All = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("../logos/logo_expand.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExpand_All.setIcon(icon13)
        self.actionExpand_All.setObjectName("actionExpand_All")
        self.actionCollapse_All = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("../logos/logo_collapse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCollapse_All.setIcon(icon14)
        self.actionCollapse_All.setObjectName("actionCollapse_All")
        self.menu_Recent_Files.addAction(self.actionClear)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.menu_Recent_Files.menuAction())
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionO_ptions)
        self.menu_Tools.addAction(self.actionExpand_All)
        self.menu_Tools.addAction(self.actionCollapse_All)
        self.menu_Tools.addSeparator()
        self.menu_Tools.addAction(self.action_Refresh)
        self.menu_Tools.addSeparator()
        self.menu_Tools.addAction(self.action_Delete)
        self.menu_Tools.addSeparator()
        self.menu_Tools.addAction(self.actionCopy)
        self.menu_Tools.addAction(self.actionPaste)
        self.menu_Tools.addSeparator()
        self.menu_Tools.addAction(self.actionUndo)
        self.menu_Tools.addAction(self.actionRedo)
        self.menu_View.addAction(self.action_Object_Tree)
        self.menu_View.addAction(self.action_Property_Editor)
        self.menu_View.addAction(self.actionObject_Box)
        self.menu_Help.addAction(self.action_About)
        self.menu_Help.addAction(self.actionHe_lp)
        self.menuBar.addAction(self.menu_File.menuAction())
        self.menuBar.addAction(self.menu_Tools.menuAction())
        self.menuBar.addAction(self.menu_View.menuAction())
        self.menuBar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FOMOD Designer"))
        self.preview_label.setText(_translate("MainWindow", "<html><head/><body><p>The preview is not ready yet!</p><p>Meanwhile, try to install your mod using NMM or MO to check if everything is ok.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("MainWindow", "Preview"))
        self.label.setText(_translate("MainWindow", "Generated XML Code"))
        self.xml_code_browser.setPlaceholderText(_translate("MainWindow", "Click a node to see the generated XML code here."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), _translate("MainWindow", "XML Preview"))
        self.property_editor.setStatusTip(_translate("MainWindow", "A list of all the properties and the means to edit them."))
        self.property_editor.setWindowTitle(_translate("MainWindow", "Property Editor"))
        self.node_tree.setStatusTip(_translate("MainWindow", "The tree containing all the existing nodes."))
        self.node_tree.setWindowTitle(_translate("MainWindow", "Node Tree"))
        self.button_wizard.setText(_translate("MainWindow", "Start Wizard"))
        self.children_box.setStatusTip(_translate("MainWindow", "A list with the possible nodes to add."))
        self.children_box.setWindowTitle(_translate("MainWindow", "Children Box"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Recent_Files.setStatusTip(_translate("MainWindow", "Your recent files in an easy-to-open list."))
        self.menu_Recent_Files.setTitle(_translate("MainWindow", "&Recent Files"))
        self.menu_Tools.setTitle(_translate("MainWindow", "&Tools"))
        self.menu_View.setTitle(_translate("MainWindow", "&View"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.action_Open.setText(_translate("MainWindow", "&New/&Open"))
        self.action_Open.setToolTip(_translate("MainWindow", "New/Open"))
        self.action_Open.setStatusTip(_translate("MainWindow", "Select a folder to open or create an installer there."))
        self.action_Open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_Save.setText(_translate("MainWindow", "&Save"))
        self.action_Save.setStatusTip(_translate("MainWindow", "Save the current installer."))
        self.action_Save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionO_ptions.setText(_translate("MainWindow", "Settings"))
        self.actionO_ptions.setIconText(_translate("MainWindow", "Settings"))
        self.actionO_ptions.setToolTip(_translate("MainWindow", "Settings"))
        self.actionO_ptions.setStatusTip(_translate("MainWindow", "Open up the settings menu"))
        self.actionO_ptions.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.action_Refresh.setText(_translate("MainWindow", "&Refresh"))
        self.action_Refresh.setStatusTip(_translate("MainWindow", "Refresh the previews."))
        self.action_Refresh.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.action_Delete.setText(_translate("MainWindow", "&Delete"))
        self.action_Delete.setStatusTip(_translate("MainWindow", "Delete the currently selected node."))
        self.action_Delete.setShortcut(_translate("MainWindow", "Del"))
        self.action_About.setText(_translate("MainWindow", "&About"))
        self.action_About.setIconText(_translate("MainWindow", "About"))
        self.action_About.setToolTip(_translate("MainWindow", "About"))
        self.action_About.setStatusTip(_translate("MainWindow", "Who made this and license details."))
        self.action_About.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionHe_lp.setText(_translate("MainWindow", "He&lp"))
        self.actionHe_lp.setStatusTip(_translate("MainWindow", "Haaaaaalp!"))
        self.actionHe_lp.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.action_Object_Tree.setText(_translate("MainWindow", "Object &Tree"))
        self.action_Object_Tree.setStatusTip(_translate("MainWindow", "Toggle the visibility of the Object Tree."))
        self.action_Property_Editor.setText(_translate("MainWindow", "&Property Editor"))
        self.action_Property_Editor.setStatusTip(_translate("MainWindow", "Toggle the visibility of the Property Editor."))
        self.actionObject_Box.setText(_translate("MainWindow", "Object &Box"))
        self.actionObject_Box.setStatusTip(_translate("MainWindow", "Toggle the visibility of the Object Box."))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionClear.setStatusTip(_translate("MainWindow", "Clear all the recent files."))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z"))
        self.actionExpand_All.setText(_translate("MainWindow", "Expand All"))
        self.actionExpand_All.setShortcut(_translate("MainWindow", "Ctrl+*"))
        self.actionCollapse_All.setText(_translate("MainWindow", "Collapse All"))
        self.actionCollapse_All.setShortcut(_translate("MainWindow", "Ctrl+."))

