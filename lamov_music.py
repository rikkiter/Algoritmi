# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lamov_music.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 557)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 450))
        MainWindow.setSizeIncrement(QSize(0, 0))
        MainWindow.setStyleSheet(u"background-color: rgb(44, 44, 44);")
        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Bespoke Serif"])
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(141, 65, 255);\n"
"background-color: rgb(40, 40, 40);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        font1 = QFont()
        font1.setFamilies([u"Bespoke Serif"])
        font1.setBold(True)

        self.normal_queue = QPushButton(self.widget)
        self.normal_queue.setObjectName(u"normal_queue")
        self.normal_queue.setFont(font1)
        self.normal_queue.setStyleSheet(u"color: rgb(141, 65, 255);\n"
                                        "background-color: rgb(40, 40, 40);")

        self.horizontalLayout_2.addWidget(self.normal_queue)

        self.new_json = QPushButton(self.widget)
        self.new_json.setObjectName(u"new_json")

        self.new_json.setFont(font1)
        self.new_json.setStyleSheet(u"color: rgb(141, 65, 255);\n"
"background-color: rgb(40, 40, 40);")

        self.horizontalLayout_2.addWidget(self.new_json)

        self.update_json = QPushButton(self.widget)
        self.update_json.setObjectName(u"update_json")
        self.update_json.setFont(font1)
        self.update_json.setStyleSheet(u"color: rgb(141, 65, 255);\n"
"background-color: rgb(40, 40, 40);")

        self.horizontalLayout_2.addWidget(self.update_json)

        self.json_queue = QPushButton(self.widget)
        self.json_queue.setObjectName(u"json_queue")
        self.json_queue.setFont(font1)
        self.json_queue.setStyleSheet(u"color: rgb(141, 65, 255);\n"
"background-color: rgb(40, 40, 40);")

        self.horizontalLayout_2.addWidget(self.json_queue)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.listwidget = QListWidget(self.widget)
        self.listwidget.setObjectName(u"listwidget")
        self.listwidget.setFont(font1)
        self.listwidget.setStyleSheet(u"color: rgb(141, 65, 255);")

        self.verticalLayout.addWidget(self.listwidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.previous = QPushButton(self.widget)
        self.previous.setObjectName(u"previous")
        self.previous.setEnabled(True)
        self.previous.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 30);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(225, 255, 255, 40);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/previous.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.previous.setIcon(icon)
        self.previous.setIconSize(QSize(37, 37))

        self.horizontalLayout.addWidget(self.previous)

        self.play = QPushButton(self.widget)
        self.play.setObjectName(u"play")
        self.play.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 30);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(225, 255, 255, 40);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/play.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.play.setIcon(icon1)
        self.play.setIconSize(QSize(37, 37))

        self.horizontalLayout.addWidget(self.play)

        self.stop = QPushButton(self.widget)
        self.stop.setObjectName(u"stop")
        self.stop.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 30);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(225, 255, 255, 40);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/stop.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stop.setIcon(icon2)
        self.stop.setIconSize(QSize(37, 37))

        self.horizontalLayout.addWidget(self.stop)

        self.next = QPushButton(self.widget)
        self.next.setObjectName(u"next")
        self.next.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 30);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(225, 255, 255, 40);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/next.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.next.setIcon(icon3)
        self.next.setIconSize(QSize(37, 37))

        self.horizontalLayout.addWidget(self.next)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.widget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Lamov Music", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Lamov Music", None))
        self.new_json.setText(QCoreApplication.translate("MainWindow", u"NEW JSON", None))
        self.normal_queue.setText(QCoreApplication.translate("MainWindow", u"NORMAL QUEUE", None))
        self.update_json.setText(QCoreApplication.translate("MainWindow", u"UPDATE JSON", None))
        self.json_queue.setText(QCoreApplication.translate("MainWindow", u"JSON QUEUE", None))
        self.previous.setText("")
        self.play.setText("")
        self.stop.setText("")
        self.next.setText("")
    # retranslateUi

