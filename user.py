# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 900))
        self.frame.setStyleSheet("QFrame#frame{\n"
"    background-image: url(:/images/images/map.png);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1280, 900))
        self.graphicsView.setStyleSheet("background-color: transparent;")
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.setObjectName("graphicsView")
        self.node_1 = QtWidgets.QPushButton(self.frame)
        self.node_1.setGeometry(QtCore.QRect(840, 560, 30, 30))
        self.node_1.setStyleSheet("QPushButton:hover{\n"
"    image: url(:/images/images/current.png);\n"
"}")
        self.node_1.setText("")
        self.node_1.setObjectName("node_1")
        self.node_2 = QtWidgets.QPushButton(self.frame)
        self.node_2.setGeometry(QtCore.QRect(850, 320, 30, 30))
        self.node_2.setStyleSheet("QPushButton:hover{\n"
"    image: url(:/images/images/current.png);\n"
"}")
        self.node_2.setText("")
        self.node_2.setObjectName("node_2")
        self.node_3 = QtWidgets.QPushButton(self.frame)
        self.node_3.setGeometry(QtCore.QRect(610, 310, 30, 30))
        self.node_3.setText("")
        self.node_3.setObjectName("node_3")
        self.node_4 = QtWidgets.QPushButton(self.frame)
        self.node_4.setGeometry(QtCore.QRect(600, 550, 30, 30))
        self.node_4.setStyleSheet("color: rgb(85, 170, 0);\n"
"font: 63 16pt \"Bahnschrift SemiBold\";")
        self.node_4.setText("")
        self.node_4.setObjectName("node_4")
        self.node_5 = QtWidgets.QPushButton(self.frame)
        self.node_5.setGeometry(QtCore.QRect(190, 540, 30, 30))
        self.node_5.setStyleSheet("QPushButton:hover{\n"
"    image: url(:/images/images/current.png);\n"
"}")
        self.node_5.setText("")
        self.node_5.setObjectName("node_5")
        self.node_6 = QtWidgets.QPushButton(self.frame)
        self.node_6.setGeometry(QtCore.QRect(190, 710, 30, 30))
        self.node_6.setStyleSheet("QPushButton:hover{\n"
"    image: url(:/images/images/current.png);\n"
"}")
        self.node_6.setText("")
        self.node_6.setObjectName("node_6")
        self.start_frame = QtWidgets.QFrame(self.frame)
        self.start_frame.setGeometry(QtCore.QRect(650, 340, 99, 80))
        self.start_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.start_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.start_frame.setObjectName("start_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.start_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.start_point = QtWidgets.QPushButton(self.start_frame)
        self.start_point.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";")
        self.start_point.setObjectName("start_point")
        self.verticalLayout.addWidget(self.start_point)
        self.end_point = QtWidgets.QPushButton(self.start_frame)
        self.end_point.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";")
        self.end_point.setObjectName("end_point")
        self.verticalLayout.addWidget(self.end_point)
        self.start_btn = QtWidgets.QPushButton(self.frame)
        self.start_btn.setGeometry(QtCore.QRect(300, 640, 131, 51))
        self.start_btn.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";")
        self.start_btn.setObjectName("start_btn")
        self.node_7 = QtWidgets.QPushButton(self.frame)
        self.node_7.setGeometry(QtCore.QRect(641, 753, 30, 30))
        self.node_7.setStyleSheet("QPushButton:hover{\n"
"    image: url(:/images/images/current.png);\n"
"}")
        self.node_7.setText("")
        self.node_7.setObjectName("node_7")
        self.node_8 = QtWidgets.QPushButton(self.frame)
        self.node_8.setGeometry(QtCore.QRect(834, 770, 30, 30))
        self.node_8.setStyleSheet("QPushButton:hover{\n"
"    image: url(:/images/images/current.png);\n"
"}")
        self.node_8.setText("")
        self.node_8.setObjectName("node_8")
        self.node_9 = QtWidgets.QPushButton(self.frame)
        self.node_9.setGeometry(QtCore.QRect(170, 80, 30, 30))
        self.node_9.setStyleSheet("QPushButton:hover{\n"
"    image: url(:/images/images/current.png);\n"
"}")
        self.node_9.setText("")
        self.node_9.setObjectName("node_9")
        self.node_10 = QtWidgets.QPushButton(self.frame)
        self.node_10.setGeometry(QtCore.QRect(620, 150, 30, 30))
        self.node_10.setStyleSheet("QPushButton:hover{\n"
"    image: url(:/images/images/goto.png);\n"
"}")
        self.node_10.setText("")
        self.node_10.setObjectName("node_10")
        self.node_11 = QtWidgets.QPushButton(self.frame)
        self.node_11.setGeometry(QtCore.QRect(870, 180, 30, 30))
        self.node_11.setStyleSheet("QPushButton:hover{\n"
"    image: url(:/images/images/current.png);\n"
"}")
        self.node_11.setText("")
        self.node_11.setObjectName("node_11")
        self.node_12 = QtWidgets.QPushButton(self.frame)
        self.node_12.setGeometry(QtCore.QRect(10, 300, 30, 30))
        self.node_12.setStyleSheet("QPushButton:hover{\n"
"    image: url(:/images/images/current.png);\n"
"}")
        self.node_12.setText("")
        self.node_12.setObjectName("node_12")
        self.animation_frame = QtWidgets.QFrame(self.frame)
        self.animation_frame.setGeometry(QtCore.QRect(290, 50, 40, 40))
        self.animation_frame.setStyleSheet("image: url(:/images/images/animation.png);")
        self.animation_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.animation_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.animation_frame.setObjectName("animation_frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(1280, 0, 321, 201))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.depart_line = QtWidgets.QLineEdit(self.frame_2)
        self.depart_line.setGeometry(QtCore.QRect(30, 50, 241, 41))
        self.depart_line.setStyleSheet("QLineEdit{\n"
"    font: 63 12pt \"Bahnschrift\";\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius: 8px;\n"
"background-color: transparent;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 1px solid rgb(32, 166, 255);\n"
"}")
        self.depart_line.setInputMask("")
        self.depart_line.setCursorPosition(0)
        self.depart_line.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.depart_line.setPlaceholderText("")
        self.depart_line.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.depart_line.setClearButtonEnabled(False)
        self.depart_line.setObjectName("depart_line")
        self.reverse_btn = QtWidgets.QPushButton(self.frame_2)
        self.reverse_btn.setGeometry(QtCore.QRect(280, 79, 25, 30))
        self.reverse_btn.setStyleSheet("QPushButton{\n"
"border: 0px;\n"
"    image: url(:/images/images/swap.png);\n"
"}\n"
"QPushButton:hover{\n"
"border-radius: 10px;\n"
"    background-color: rgb(209, 209, 209);\n"
"}")
        self.reverse_btn.setText("")
        self.reverse_btn.setObjectName("reverse_btn")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(6, 56, 20, 81))
        self.frame_3.setStyleSheet("image: url(:/images/images/location.png);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.depaarture_line = QtWidgets.QLineEdit(self.frame_2)
        self.depaarture_line.setGeometry(QtCore.QRect(30, 100, 241, 41))
        self.depaarture_line.setStyleSheet("QLineEdit{\n"
"    font: 63 12pt \"Bahnschrift\";\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius: 8px;\n"
"background-color: transparent;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 1px solid rgb(32, 166, 255);\n"
"}")
        self.depaarture_line.setInputMask("")
        self.depaarture_line.setCursorPosition(0)
        self.depaarture_line.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.depaarture_line.setPlaceholderText("")
        self.depaarture_line.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.depaarture_line.setClearButtonEnabled(False)
        self.depaarture_line.setObjectName("depaarture_line")
        self.preferences_btn = QtWidgets.QPushButton(self.frame_2)
        self.preferences_btn.setGeometry(QtCore.QRect(160, 160, 111, 31))
        self.preferences_btn.setStyleSheet("QPushButton{\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius: 10px;\n"
"    image: url(:/images/images/preferences.png);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(209, 209, 209);\n"
"}")
        self.preferences_btn.setText("")
        self.preferences_btn.setObjectName("preferences_btn")
        self.change_time_btn = QtWidgets.QPushButton(self.frame_2)
        self.change_time_btn.setGeometry(QtCore.QRect(30, 160, 111, 31))
        self.change_time_btn.setStyleSheet("QPushButton{\n"
"    color: #ff3d00;\n"
"border: 0px;\n"
"border-radius: 10px;\n"
"    font: 63 12pt \"Bahnschrift SemiBold\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(209, 209, 209);\n"
"}")
        self.change_time_btn.setObjectName("change_time_btn")
        self.set_time_frame = QtWidgets.QFrame(self.centralwidget)
        self.set_time_frame.setGeometry(QtCore.QRect(1310, 200, 171, 0))
        self.set_time_frame.setStyleSheet("QFrame#set_time_frame{\n"
"\n"
"\n"
"}")
        self.set_time_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.set_time_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.set_time_frame.setObjectName("set_time_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.set_time_frame)
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.depart_now = QtWidgets.QPushButton(self.set_time_frame)
        self.depart_now.setMinimumSize(QtCore.QSize(0, 31))
        self.depart_now.setMaximumSize(QtCore.QSize(89, 16777215))
        self.depart_now.setStyleSheet("QPushButton{\n"
"    color: rgb(108, 108, 108);\n"
"border: 2px solid  transparent;\n"
"    font: 63 12pt \"Bahnschrift SemiBold\";\n"
"}\n"
"QPushButton:hover{\n"
"border-left: 2px solid  #ff3d00;\n"
"}")
        self.depart_now.setObjectName("depart_now")
        self.verticalLayout_2.addWidget(self.depart_now)
        self.change_time = QtWidgets.QPushButton(self.set_time_frame)
        self.change_time.setMinimumSize(QtCore.QSize(0, 31))
        self.change_time.setMaximumSize(QtCore.QSize(160, 16777215))
        self.change_time.setStyleSheet("QPushButton{\n"
"    color: rgb(108, 108, 108);\n"
"border: 2px solid  transparent;\n"
"    font: 63 12pt \"Bahnschrift SemiBold\";\n"
"}\n"
"QPushButton:hover{\n"
"border-left: 2px solid  #ff3d00;\n"
"}")
        self.change_time.setObjectName("change_time")
        self.verticalLayout_2.addWidget(self.change_time)
        self.time_frame = QtWidgets.QFrame(self.centralwidget)
        self.time_frame.setGeometry(QtCore.QRect(1340, 280, 171, 151))
        self.time_frame.setStyleSheet("")
        self.time_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.time_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.time_frame.setObjectName("time_frame")
        self.ok_btn = QtWidgets.QPushButton(self.time_frame)
        self.ok_btn.setGeometry(QtCore.QRect(10, 70, 151, 31))
        self.ok_btn.setStyleSheet("QPushButton{\n"
"    color: rgb(248, 248, 248);\n"
"    font: 63 12pt \"Bahnschrift SemiBold\";\n"
"border: 0px;\n"
"    background-color: rgb(30, 144, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(45, 45, 45);\n"
"    background-color: rgb(209, 209, 209);\n"
"}")
        self.ok_btn.setObjectName("ok_btn")
        self.cancel_btn = QtWidgets.QPushButton(self.time_frame)
        self.cancel_btn.setGeometry(QtCore.QRect(10, 100, 151, 31))
        self.cancel_btn.setStyleSheet("QPushButton{\n"
"    font: 63 12pt \"Bahnschrift SemiBold\";\n"
"border: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(209, 209, 209);\n"
"}")
        self.cancel_btn.setObjectName("cancel_btn")
        self.hours_combo = QtWidgets.QComboBox(self.time_frame)
        self.hours_combo.setGeometry(QtCore.QRect(10, 21, 51, 31))
        self.hours_combo.setStyleSheet("QComboBox{\n"
"    color: rgb(47, 47, 47);\n"
"background-color: transparent;\n"
"    font: 63 12pt \"Bahnschrift SemiBold\";\n"
"}")
        self.hours_combo.setCurrentText("")
        self.hours_combo.setObjectName("hours_combo")
        self.label = QtWidgets.QLabel(self.time_frame)
        self.label.setGeometry(QtCore.QRect(80, 20, 21, 31))
        self.label.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.min_combo = QtWidgets.QComboBox(self.time_frame)
        self.min_combo.setGeometry(QtCore.QRect(107, 21, 51, 31))
        self.min_combo.setStyleSheet("QComboBox{\n"
"    color: rgb(47, 47, 47);\n"
"background-color: transparent;\n"
"    font: 63 12pt \"Bahnschrift SemiBold\";\n"
"}")
        self.min_combo.setCurrentText("")
        self.min_combo.setObjectName("min_combo")
        self.find_path_btn = QtWidgets.QPushButton(self.centralwidget)
        self.find_path_btn.setGeometry(QtCore.QRect(1310, 210, 241, 41))
        self.find_path_btn.setStyleSheet("QPushButton{\n"
"    font: 63 14pt \"Bahnschrift SemiBold\";\n"
"    color: rgb(239, 239, 239);\n"
"border: 1px solid rgb(239, 239, 239);\n"
"border-radius: 10px;\n"
"    background-color: rgb(30, 144, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(45, 45, 45);\n"
"    background-color: rgb(209, 209, 209);\n"
"}")
        self.find_path_btn.setObjectName("find_path_btn")
        self.preferences_frame = QtWidgets.QFrame(self.centralwidget)
        self.preferences_frame.setGeometry(QtCore.QRect(1551, 200, 0, 221))
        self.preferences_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.preferences_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.preferences_frame.setObjectName("preferences_frame")
        self.label_2 = QtWidgets.QLabel(self.preferences_frame)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 151, 41))
        self.label_2.setStyleSheet("font: 63 18pt \"Bahnschrift SemiBold\";")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.close_btn = QtWidgets.QPushButton(self.preferences_frame)
        self.close_btn.setGeometry(QtCore.QRect(190, 0, 41, 41))
        self.close_btn.setStyleSheet("QPushButton{\n"
"    color: rgb(136, 136, 136);\n"
"    font: 63 14pt \"Bahnschrift SemiBold\";\n"
"border: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(63, 63, 63);\n"
"}")
        self.close_btn.setObjectName("close_btn")
        self.fastest_btn = QtWidgets.QPushButton(self.preferences_frame)
        self.fastest_btn.setGeometry(QtCore.QRect(20, 60, 91, 31))
        self.fastest_btn.setMinimumSize(QtCore.QSize(0, 31))
        self.fastest_btn.setMaximumSize(QtCore.QSize(160, 16777215))
        self.fastest_btn.setStyleSheet("QPushButton{\n"
"    color: rgb(108, 108, 108);\n"
"border: 2px solid  transparent;\n"
"    font: 63 12pt \"Bahnschrift SemiBold\";\n"
"}\n"
"QPushButton:hover{\n"
"border-left: 2px solid   rgb(63, 63, 63);\n"
"    color:  rgb(63, 63, 63);\n"
"}")
        self.fastest_btn.setObjectName("fastest_btn")
        self.shortest_btn = QtWidgets.QPushButton(self.preferences_frame)
        self.shortest_btn.setGeometry(QtCore.QRect(20, 100, 91, 31))
        self.shortest_btn.setMinimumSize(QtCore.QSize(0, 31))
        self.shortest_btn.setMaximumSize(QtCore.QSize(160, 16777215))
        self.shortest_btn.setStyleSheet("QPushButton{\n"
"    color: rgb(108, 108, 108);\n"
"border: 2px solid  transparent;\n"
"    font: 63 12pt \"Bahnschrift SemiBold\";\n"
"}\n"
"QPushButton:hover{\n"
"border-left: 2px solid   rgb(63, 63, 63);\n"
"    color:  rgb(63, 63, 63);\n"
"}")
        self.shortest_btn.setObjectName("shortest_btn")
        self.find_path_btn_2 = QtWidgets.QPushButton(self.preferences_frame)
        self.find_path_btn_2.setGeometry(QtCore.QRect(0, 150, 241, 41))
        self.find_path_btn_2.setStyleSheet("QPushButton{\n"
"    font: 63 14pt \"Bahnschrift SemiBold\";\n"
"    color: rgb(239, 239, 239);\n"
"border: 1px solid rgb(239, 239, 239);\n"
"border-radius: 10px;\n"
"    background-color: rgb(30, 144, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(45, 45, 45);\n"
"    background-color: rgb(209, 209, 209);\n"
"}")
        self.find_path_btn_2.setObjectName("find_path_btn_2")
        self.trafiksiz_frame = QtWidgets.QFrame(self.centralwidget)
        self.trafiksiz_frame.setGeometry(QtCore.QRect(1310, 460, 241, 81))
        self.trafiksiz_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.trafiksiz_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.trafiksiz_frame.setObjectName("trafiksiz_frame")
        self.label_3 = QtWidgets.QLabel(self.trafiksiz_frame)
        self.label_3.setGeometry(QtCore.QRect(0, 10, 21, 21))
        self.label_3.setStyleSheet("color: rgb(0, 85, 255);\n"
"font: 63 38pt \"Bahnschrift SemiBold\";")
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.trafiksiz_frame)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 131, 21))
        self.label_4.setStyleSheet("font: 63 14pt \"Bahnschrift SemiBold\";\n"
"color: rgb(75, 75, 75);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.trafiksiz_frame)
        self.label_5.setGeometry(QtCore.QRect(30, 30, 71, 21))
        self.label_5.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";\n"
"color: rgb(106, 106, 106);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.trafiksiz_frame)
        self.label_6.setGeometry(QtCore.QRect(30, 50, 91, 21))
        self.label_6.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";\n"
"color: rgb(106, 106, 106);")
        self.label_6.setObjectName("label_6")
        self.trafiksiz_distance = QtWidgets.QLabel(self.trafiksiz_frame)
        self.trafiksiz_distance.setGeometry(QtCore.QRect(170, 30, 71, 21))
        self.trafiksiz_distance.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";\n"
"color: rgb(0, 85, 255);")
        self.trafiksiz_distance.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.trafiksiz_distance.setObjectName("trafiksiz_distance")
        self.trafiksiz_time = QtWidgets.QLabel(self.trafiksiz_frame)
        self.trafiksiz_time.setGeometry(QtCore.QRect(170, 50, 71, 21))
        self.trafiksiz_time.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";\n"
"color: rgb(0, 85, 255);")
        self.trafiksiz_time.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.trafiksiz_time.setObjectName("trafiksiz_time")
        self.trafikli_frame = QtWidgets.QFrame(self.centralwidget)
        self.trafikli_frame.setGeometry(QtCore.QRect(1310, 540, 241, 81))
        self.trafikli_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.trafikli_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.trafikli_frame.setObjectName("trafikli_frame")
        self.label_9 = QtWidgets.QLabel(self.trafikli_frame)
        self.label_9.setGeometry(QtCore.QRect(0, 10, 21, 21))
        self.label_9.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 63 38pt \"Bahnschrift SemiBold\";")
        self.label_9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.trafikli_frame)
        self.label_10.setGeometry(QtCore.QRect(30, 10, 131, 21))
        self.label_10.setStyleSheet("font: 63 14pt \"Bahnschrift SemiBold\";\n"
"color: rgb(75, 75, 75);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.trafikli_frame)
        self.label_11.setGeometry(QtCore.QRect(30, 30, 71, 21))
        self.label_11.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";\n"
"color: rgb(106, 106, 106);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.trafikli_frame)
        self.label_12.setGeometry(QtCore.QRect(30, 50, 91, 21))
        self.label_12.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";\n"
"color: rgb(106, 106, 106);")
        self.label_12.setObjectName("label_12")
        self.trafikli_distance = QtWidgets.QLabel(self.trafikli_frame)
        self.trafikli_distance.setGeometry(QtCore.QRect(170, 30, 71, 21))
        self.trafikli_distance.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";\n"
"color: rgb(255, 0, 0);")
        self.trafikli_distance.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.trafikli_distance.setObjectName("trafikli_distance")
        self.trafikli_time = QtWidgets.QLabel(self.trafikli_frame)
        self.trafikli_time.setGeometry(QtCore.QRect(170, 50, 71, 21))
        self.trafikli_time.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";\n"
"color: rgb(255, 0, 0);")
        self.trafikli_time.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.trafikli_time.setObjectName("trafikli_time")
        self.filtered_label = QtWidgets.QLabel(self.centralwidget)
        self.filtered_label.setGeometry(QtCore.QRect(1360, 410, 141, 31))
        self.filtered_label.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold\";\n"
"color: rgb(23, 135, 255);")
        self.filtered_label.setObjectName("filtered_label")
        self.start_path_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_path_btn.setGeometry(QtCore.QRect(1310, 260, 241, 41))
        self.start_path_btn.setStyleSheet("QPushButton{\n"
"    font: 63 14pt \"Bahnschrift SemiBold\";\n"
"    color: rgb(239, 239, 239);\n"
"border: 1px solid rgb(239, 239, 239);\n"
"border-radius: 10px;\n"
"    background-color: #ff3d00;\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(45, 45, 45);\n"
"    background-color: rgb(209, 209, 209);\n"
"}")
        self.start_path_btn.setObjectName("start_path_btn")
        self.frame.raise_()
        self.frame_2.raise_()
        self.time_frame.raise_()
        self.find_path_btn.raise_()
        self.set_time_frame.raise_()
        self.preferences_frame.raise_()
        self.trafiksiz_frame.raise_()
        self.trafikli_frame.raise_()
        self.filtered_label.raise_()
        self.start_path_btn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.hours_combo.setCurrentIndex(-1)
        self.min_combo.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_point.setText(_translate("MainWindow", "Ba??lang????"))
        self.end_point.setText(_translate("MainWindow", "Bitti??"))
        self.start_btn.setText(_translate("MainWindow", "Ba??lat"))
        self.change_time_btn.setText(_translate("MainWindow", "??imdi ayr??l ???"))
        self.depart_now.setText(_translate("MainWindow", "??imdi ayr??l"))
        self.change_time.setText(_translate("MainWindow", "Kalk???? saatini ayarla"))
        self.ok_btn.setText(_translate("MainWindow", "Tamam"))
        self.cancel_btn.setText(_translate("MainWindow", "??ptal"))
        self.label.setText(_translate("MainWindow", ":"))
        self.find_path_btn.setText(_translate("MainWindow", "Yolu bul"))
        self.label_2.setText(_translate("MainWindow", "Tercihler"))
        self.close_btn.setText(_translate("MainWindow", "X"))
        self.fastest_btn.setText(_translate("MainWindow", "En h??zl?? yol"))
        self.shortest_btn.setText(_translate("MainWindow", "En k??sa yol"))
        self.find_path_btn_2.setText(_translate("MainWindow", "Yolu bul"))
        self.label_3.setText(_translate("MainWindow", "_"))
        self.label_4.setText(_translate("MainWindow", "Trafiksiz yol"))
        self.label_5.setText(_translate("MainWindow", "Mesafe"))
        self.label_6.setText(_translate("MainWindow", "Zaman"))
        self.trafiksiz_distance.setText(_translate("MainWindow", "4.6 km"))
        self.trafiksiz_time.setText(_translate("MainWindow", "5 min"))
        self.label_9.setText(_translate("MainWindow", "_"))
        self.label_10.setText(_translate("MainWindow", "Trafikli yol"))
        self.label_11.setText(_translate("MainWindow", "Mesafe"))
        self.label_12.setText(_translate("MainWindow", "Zaman"))
        self.trafikli_distance.setText(_translate("MainWindow", "1.6 km"))
        self.trafikli_time.setText(_translate("MainWindow", "8 min"))
        self.filtered_label.setText(_translate("MainWindow", "En h??zl?? yol"))
        self.start_path_btn.setText(_translate("MainWindow", "Ba??lat"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
