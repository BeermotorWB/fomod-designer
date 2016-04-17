#!/usr/bin/env python

# Copyright 2016 Daniel Nunes
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from PyQt5 import QtWidgets, QtGui, QtCore
from .templates import mainframe as template


class MainFrame(QtWidgets.QMainWindow, template.Ui_MainWindow):
    def __init__(self):
        super(MainFrame, self).__init__()
        self.setupUi(self)

        # setup the icons properly
        icon_open = QtGui.QIcon()
        icon_open.addPixmap(QtGui.QPixmap("fomod/gui/logos/logo_open_file.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Open.setIcon(icon_open)

        icon_save = QtGui.QIcon()
        icon_save.addPixmap(QtGui.QPixmap("fomod/gui/logos/logo_floppy_disk.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Save.setIcon(icon_save)

        icon_options = QtGui.QIcon()
        icon_options.addPixmap(QtGui.QPixmap("fomod/gui/logos/logo_gear.png"),
                               QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionO_ptions.setIcon(icon_options)

        icon_refresh = QtGui.QIcon()
        icon_refresh.addPixmap(QtGui.QPixmap("fomod/gui/logos/logo_refresh.png"),
                               QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Refresh.setIcon(icon_refresh)

        icon_delete = QtGui.QIcon()
        icon_delete.addPixmap(QtGui.QPixmap("fomod/gui/logos/logo_cross.png"),
                              QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Delete.setIcon(icon_delete)

        icon_about = QtGui.QIcon()
        icon_about.addPixmap(QtGui.QPixmap("fomod/gui/logos/logo_notepad.png"),
                             QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_About.setIcon(icon_about)

        icon_help = QtGui.QIcon()
        icon_help.addPixmap(QtGui.QPixmap("fomod/gui/logos/logo_info.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHe_lp.setIcon(icon_help)

        # setup any additional info left from designer
        self.delete_sec_shortcut = QtWidgets.QShortcut(self)
        self.delete_sec_shortcut.setKey(QtCore.Qt.Key_Delete)

        self.action_Open.triggered.connect(self.open)
        self.action_Save.triggered.connect(self.save)
        self.actionO_ptions.triggered.connect(self.options)
        self.action_Refresh.triggered.connect(self.refresh)
        self.action_Delete.triggered.connect(self.delete)
        self.delete_sec_shortcut.activated.connect(self.delete)
        self.actionHe_lp.triggered.connect(self.help)
        self.action_About.triggered.connect(self.about)

        self.object_tree_view.clicked.connect(self.selected_object_tree)
        self.object_box_list.activated.connect(self.selected_object_list)

        self.fomod_changed = False
        self.original_title = self.windowTitle()
        self.package_path = ""
        self.package_name = ""
        self.info_root = None
        self.config_root = None
        self.current_item = None
        self.current_object = None
        self.current_prop_list = []
        self.current_children_list = []
        self.tree_model = QtGui.QStandardItemModel()
        self.list_model = QtGui.QStandardItemModel()

        self.object_tree_view.setModel(self.tree_model)
        self.object_tree_view.header().hide()
        self.object_box_list.setModel(self.list_model)

    def open(self):
        from os.path import expanduser, normpath, basename
        from ..parser import parse

        open_dialog = QtWidgets.QFileDialog()
        self.package_path = open_dialog.getExistingDirectory(self, "Select package root directory:", expanduser("~"))

        if self.package_path:
            info_root, config_root = parse(normpath(self.package_path))

            if not info_root or not config_root:
                return

            self.tree_model.clear()

            self.info_root = info_root
            self.config_root = config_root

            self.tree_model.appendRow(self.info_root.model_item)
            self.tree_model.appendRow(self.config_root.model_item)

            self.package_name = basename(normpath(self.package_path))
            self.fomod_modified(False)

    def save(self):
        from ..serializer import serialize

        if not self.fomod_changed:
            from . import generic
            generic.generic_errorbox("I REFUSE TO SAVE",
                                     "There are no changes to save!")
        elif not self.info_root and not self.config_root:
            from . import generic
            generic.generic_errorbox("I REFUSE TO SAVE",
                                     "There is nothing... literally.")
        else:
            serialize(self.info_root, self.config_root, self.package_path)
            self.fomod_modified(False)

    def options(self):
        from . import generic
        generic.not_implemented()

    def refresh(self):
        from . import generic
        generic.not_implemented()

    def delete(self):
        try:
            if self.current_object:
                object_to_delete = self.current_object
                object_to_delete.parent.remove_child(object_to_delete)

                new_index = self.tree_model.indexFromItem(self.current_object.parent.model_item)
                self.selected_object_tree(new_index)
            else:
                from . import generic
                generic.generic_errorbox("What are trying to do? o.O",
                                         "You can't delete nothing... Try to select something before deleting.")
        except AttributeError:
            from . import generic
            generic.generic_errorbox("You can't do that...",
                                     "You can't delete root objects!")

    def help(self):
        from . import generic
        generic.not_implemented()

    def about(self):
        from . import generic
        generic.not_implemented()

    def selected_object_tree(self, index):
        self.current_item, self.current_object = self.get_from_index(index)

        self.update_box_list()
        self.update_props_list()

    def update_box_list(self):
        from ..exceptions import InstanceCreationException, AddChildException

        self.list_model.clear()
        self.current_children_list.clear()

        for child in self.current_object.allowed_children:
            new_object = child()
            try:
                self.current_object.can_add_child(new_object)
            except (InstanceCreationException, AddChildException):
                continue

            self.list_model.appendRow(new_object.model_item)
            self.current_children_list.append(new_object)

    def update_props_list(self):
        from ..props import PropertyCombo, PropertyInt, PropertyText

        self.current_prop_list.clear()
        for index in reversed(range(self.formLayout.count())):
            widget = self.formLayout.takeAt(index).widget()
            if widget is not None:
                widget.deleteLater()

        prop_index = 0
        prop_list = self.current_prop_list
        props = self.current_object.properties

        if self.current_object.allow_text:
            text_label = QtWidgets.QLabel(self.dockWidgetContents)
            text_label.setObjectName("text_label")
            text_label.setText("Text")
            self.formLayout.setWidget(prop_index, QtWidgets.QFormLayout.LabelRole, text_label)
            prop_list.append(QtWidgets.QLineEdit(self.dockWidgetContents))
            prop_list[prop_index].setObjectName(str(prop_index))
            prop_list[prop_index].setText(self.current_object.text)
            prop_list[prop_index].textEdited[str].connect(self.current_object.set_text)
            prop_list[prop_index].textEdited[str].connect(self.fomod_modified)
            self.formLayout.setWidget(prop_index, QtWidgets.QFormLayout.FieldRole,
                                      prop_list[prop_index])

            prop_index += 1

        for key in props:
            if not props[key].editable:
                continue

            label = QtWidgets.QLabel(self.dockWidgetContents)
            label.setObjectName("label_" + str(prop_index))
            label.setText(props[key].name)
            self.formLayout.setWidget(prop_index, QtWidgets.QFormLayout.LabelRole, label)

            if type(props[key]) == PropertyText:
                prop_list.append(QtWidgets.QLineEdit(self.dockWidgetContents))
                prop_list[prop_index].setText(props[key].value)
                prop_list[prop_index].textEdited[str].connect(props[key].set_value)
                prop_list[prop_index].textEdited[str].connect(self.fomod_modified)
                if key == "name" or key == "source":
                    prop_list[prop_index].textEdited[str].connect(self.current_object.set_item_name)

            elif type(props[key]) == PropertyInt:
                prop_list.append(QtWidgets.QSpinBox(self.dockWidgetContents))
                prop_list[prop_index].setValue(int(props[key].value))
                prop_list[prop_index].valueChanged.connect(props[key].set_value)
                prop_list[prop_index].valueChanged.connect(self.fomod_modified)
                prop_list[prop_index].setMinimum(props[key].min)
                prop_list[prop_index].setMaximum(props[key].max)

            elif type(props[key]) == PropertyCombo:
                prop_list.append(QtWidgets.QComboBox(self.dockWidgetContents))
                prop_list[prop_index].insertItems(0, props[key].values)
                prop_list[prop_index].activated[str].connect(props[key].set_value)
                prop_list[prop_index].activated[str].connect(self.fomod_modified)

            """self.widget = QtWidgets.QWidget(self.dockWidgetContents)
            self.widget.setObjectName("widget")
            self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
            self.horizontalLayout_4.setObjectName("horizontalLayout_4")
            self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
            self.lineEdit_2.setObjectName("lineEdit_2")
            self.horizontalLayout_4.addWidget(self.lineEdit_2)
            self.pushButton = QtWidgets.QPushButton(self.widget)
            self.pushButton.setObjectName("pushButton")
            self.horizontalLayout_4.addWidget(self.pushButton)
            self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.widget)"""

            self.formLayout.setWidget(prop_index, QtWidgets.QFormLayout.FieldRole,
                                      prop_list[prop_index])
            prop_list[prop_index].setObjectName(str(prop_index))
            prop_index += 1

    def get_from_index(self, index):

        item = self.tree_model.itemFromIndex(index)

        for node in self.info_root.iter():
            if node.model_item is item:
                return item, node

        for node in self.config_root.iter():
            if node.model_item is item:
                return item, node

        return None

    def selected_object_list(self, index):
        item = self.list_model.itemFromIndex(index)

        for child in self.current_children_list:
            if child.model_item is item:
                new_child = type(child)()
                self.current_object.add_child(new_child)

                # reload the object box
                self.update_box_list()

                # expand the parent
                current_index = self.tree_model.indexFromItem(self.current_item)
                self.object_tree_view.expand(current_index)

                # select the new item
                self.object_tree_view.setCurrentIndex(self.tree_model.indexFromItem(new_child.model_item))
                self.selected_object_tree(self.tree_model.indexFromItem(new_child.model_item))

                # set the installer as changed
                self.fomod_modified(True)

    def fomod_modified(self, changed):
        if changed is False:
            self.fomod_changed = False
            self.setWindowTitle(self.package_name + " - " + self.original_title)
        else:
            self.fomod_changed = True
            self.setWindowTitle("*" + self.package_name + " - " + self.original_title)


def main():
    window = MainFrame()
    window.exec_()


# For testing and debugging.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainFrame()
    window.show()
    sys.exit(app.exec_())
