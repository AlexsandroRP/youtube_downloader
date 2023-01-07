# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'youtube_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(645, 514)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(54, 162, 255, 255), stop:0.98 rgba(0, 0, 0, 255));")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"QRadioButton{\n"
"	background-color: None;\n"
"	color: rgb(247, 247, 247);\n"
"}\n"
"\n"
"QRadioButton:hover{\n"
"	background-color: rgb(227, 24, 54);\n"
"	color: #fff;\n"
"	border-radius: 10px\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.rb_audio = QRadioButton(self.frame)
        self.rb_audio.setObjectName(u"rb_audio")
        self.rb_audio.setMinimumSize(QSize(100, 0))
        self.rb_audio.setFont(font)
        self.rb_audio.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.rb_audio)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.rb_video = QRadioButton(self.frame)
        self.rb_video.setObjectName(u"rb_video")
        self.rb_video.setMinimumSize(QSize(100, 0))
        self.rb_video.setFont(font)
        self.rb_video.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.rb_video)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.rb_playlist = QRadioButton(self.frame)
        self.rb_playlist.setObjectName(u"rb_playlist")
        self.rb_playlist.setMinimumSize(QSize(100, 0))
        self.rb_playlist.setFont(font)
        self.rb_playlist.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.rb_playlist)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.label)

        self.txt_link = QLineEdit(self.frame_2)
        self.txt_link.setObjectName(u"txt_link")
        self.txt_link.setMinimumSize(QSize(0, 29))
        self.txt_link.setFont(font)
        self.txt_link.setStyleSheet(u"background-color:rgb(255,255,255);")
        self.txt_link.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.txt_link)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.btn_download = QPushButton(self.tab)
        self.btn_download.setObjectName(u"btn_download")
        self.btn_download.setMinimumSize(QSize(180, 29))
        self.btn_download.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_download.setStyleSheet(u"QPushButton{\n"
"	background-color: #fff;\n"
"	color:black; border: solid 0px;\n"
"	font: 75 16px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(227, 24,54);\n"
"	color: #fff\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_download, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_5 = QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.txt_file = QLineEdit(self.frame_3)
        self.txt_file.setObjectName(u"txt_file")
        self.txt_file.setMinimumSize(QSize(0, 29))
        font1 = QFont()
        font1.setPointSize(10)
        self.txt_file.setFont(font1)
        self.txt_file.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_file.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.txt_file)

        self.btn_open = QPushButton(self.frame_3)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setMinimumSize(QSize(100, 29))
        self.btn_open.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open.setStyleSheet(u"QPushButton{\n"
"	background-color: #fff;\n"
"	color:black; border: solid 0px;\n"
"	font: 75 16px;\n"
"	border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(227, 24,54);\n"
"	color: #fff\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_open)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_6 = QFrame(self.tab_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QLabel{\n"
"	color:rgb(255, 255, 255);\n"
"	background-color: None\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: None\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_4 = QFrame(self.frame_6)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.txt_segundo_inicial = QLineEdit(self.frame_4)
        self.txt_segundo_inicial.setObjectName(u"txt_segundo_inicial")
        self.txt_segundo_inicial.setMinimumSize(QSize(0, 29))
        self.txt_segundo_inicial.setFont(font)
        self.txt_segundo_inicial.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txt_segundo_inicial)


        self.horizontalLayout_4.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 29))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout_4.addWidget(self.label_5)

        self.txt_segundo_final = QLineEdit(self.frame_5)
        self.txt_segundo_final.setObjectName(u"txt_segundo_final")
        self.txt_segundo_final.setMinimumSize(QSize(0, 29))
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(11)
        self.txt_segundo_final.setFont(font2)
        self.txt_segundo_final.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.txt_segundo_final)


        self.horizontalLayout_4.addWidget(self.frame_5)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.btn_convert = QPushButton(self.tab_2)
        self.btn_convert.setObjectName(u"btn_convert")
        self.btn_convert.setMinimumSize(QSize(180, 29))
        self.btn_convert.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_convert.setStyleSheet(u"QPushButton{\n"
"	background-color: #fff;\n"
"	color:black; border: solid 0px;\n"
"	font: 75 16px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(227, 24,54);\n"
"	color: #fff\n"
"}")

        self.verticalLayout_5.addWidget(self.btn_convert, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/Youtube_36365.png\"/></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#b5b5b5;\">YOUTUBE DOWNLOADER</span></p></body></html>", None))
        self.rb_audio.setText(QCoreApplication.translate("MainWindow", u"\u00c1udio", None))
        self.rb_video.setText(QCoreApplication.translate("MainWindow", u"V\u00eddeo", None))
        self.rb_playlist.setText(QCoreApplication.translate("MainWindow", u"Playlist", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Cole o link do video na caixa abaixo</span></p></body></html>", None))
        self.txt_link.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Link para download do video", None))
        self.btn_download.setText(QCoreApplication.translate("MainWindow", u"BAIXAR", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Download", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/Youtube_36365.png\"/></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#acacac;\">CORTAR PARTES DO VIDEO</span></p></body></html>", None))
        self.txt_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione o v\u00eddeo desejado", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"OPEN", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tempo inicial", None))
        self.txt_segundo_inicial.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Segundo inicial", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tempo final", None))
        self.txt_segundo_final.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Segundo final", None))
        self.btn_convert.setText(QCoreApplication.translate("MainWindow", u"Converter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Video", None))
    # retranslateUi

