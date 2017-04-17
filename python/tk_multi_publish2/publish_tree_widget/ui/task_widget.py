# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task_widget.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_TaskWidget(object):
    def setupUi(self, TaskWidget):
        TaskWidget.setObjectName("TaskWidget")
        TaskWidget.resize(338, 36)
        self.verticalLayout = QtGui.QVBoxLayout(TaskWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QFrame(TaskWidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 32))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkbox = QtGui.QCheckBox(self.frame)
        self.checkbox.setObjectName("checkbox")
        self.horizontalLayout.addWidget(self.checkbox)
        self.icon = QtGui.QLabel(self.frame)
        self.icon.setMinimumSize(QtCore.QSize(24, 24))
        self.icon.setMaximumSize(QtCore.QSize(24, 24))
        self.icon.setPixmap(QtGui.QPixmap(":/tk_multi_publish2/shotgun.png"))
        self.icon.setScaledContents(True)
        self.icon.setAlignment(QtCore.Qt.AlignCenter)
        self.icon.setObjectName("icon")
        self.horizontalLayout.addWidget(self.icon)
        self.header = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setObjectName("header")
        self.horizontalLayout.addWidget(self.header)
        self.settings = QtGui.QToolButton(self.frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tk_multi_publish2/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings.setIcon(icon)
        self.settings.setIconSize(QtCore.QSize(20, 20))
        self.settings.setObjectName("settings")
        self.horizontalLayout.addWidget(self.settings)
        self.status = QtGui.QToolButton(self.frame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/tk_multi_publish2/status_publish.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.status.setIcon(icon1)
        self.status.setIconSize(QtCore.QSize(20, 20))
        self.status.setObjectName("status")
        self.horizontalLayout.addWidget(self.status)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(TaskWidget)
        QtCore.QMetaObject.connectSlotsByName(TaskWidget)

    def retranslateUi(self, TaskWidget):
        TaskWidget.setWindowTitle(QtGui.QApplication.translate("TaskWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox.setToolTip(QtGui.QApplication.translate("TaskWidget", "hint: shift-click to toggle all items of this type", None, QtGui.QApplication.UnicodeUTF8))
        self.header.setText(QtGui.QApplication.translate("TaskWidget", "<big>Alembic Caches</big>", None, QtGui.QApplication.UnicodeUTF8))
        self.settings.setToolTip(QtGui.QApplication.translate("TaskWidget", "Click for publish settings", None, QtGui.QApplication.UnicodeUTF8))
        self.settings.setText(QtGui.QApplication.translate("TaskWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.status.setToolTip(QtGui.QApplication.translate("TaskWidget", "Click for more details", None, QtGui.QApplication.UnicodeUTF8))
        self.status.setText(QtGui.QApplication.translate("TaskWidget", "...", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc