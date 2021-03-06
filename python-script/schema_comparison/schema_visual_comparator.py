# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'schema_visual_comparator.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1541, 1069)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnPrevA = QtWidgets.QPushButton(self.centralwidget)
        self.btnPrevA.setGeometry(QtCore.QRect(490, 710, 91, 41))
        self.btnPrevA.setObjectName("btnPrevA")
        self.btnNextA = QtWidgets.QPushButton(self.centralwidget)
        self.btnNextA.setGeometry(QtCore.QRect(590, 710, 91, 41))
        self.btnNextA.setObjectName("btnNextA")
        self.btnPrevB = QtWidgets.QPushButton(self.centralwidget)
        self.btnPrevB.setGeometry(QtCore.QRect(900, 710, 91, 41))
        self.btnPrevB.setObjectName("btnPrevB")
        self.btnNextB = QtWidgets.QPushButton(self.centralwidget)
        self.btnNextB.setGeometry(QtCore.QRect(1000, 710, 91, 41))
        self.btnNextB.setObjectName("btnNextB")
        self.btnMatch = QtWidgets.QPushButton(self.centralwidget)
        self.btnMatch.setGeometry(QtCore.QRect(740, 710, 121, 41))
        self.btnMatch.setObjectName("btnMatch")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(1200, 1000, 331, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.tableASelection = QtWidgets.QComboBox(self.centralwidget)
        self.tableASelection.setGeometry(QtCore.QRect(30, 380, 291, 22))
        self.tableASelection.setObjectName("tableASelection")
        self.tableBSelection = QtWidgets.QComboBox(self.centralwidget)
        self.tableBSelection.setGeometry(QtCore.QRect(1220, 380, 291, 22))
        self.tableBSelection.setObjectName("tableBSelection")
        self.listSuggestA = QtWidgets.QListWidget(self.centralwidget)
        self.listSuggestA.setGeometry(QtCore.QRect(30, 440, 291, 241))
        self.listSuggestA.setObjectName("listSuggestA")
        self.listSuggestB = QtWidgets.QListWidget(self.centralwidget)
        self.listSuggestB.setGeometry(QtCore.QRect(1220, 440, 291, 241))
        self.listSuggestB.setObjectName("listSuggestB")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 120, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1310, 120, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_schemaA = QtWidgets.QLabel(self.centralwidget)
        self.label_schemaA.setGeometry(QtCore.QRect(50, 160, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_schemaA.setFont(font)
        self.label_schemaA.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_schemaA.setAutoFillBackground(False)
        self.label_schemaA.setAlignment(QtCore.Qt.AlignCenter)
        self.label_schemaA.setObjectName("label_schemaA")
        self.label_schemaB = QtWidgets.QLabel(self.centralwidget)
        self.label_schemaB.setGeometry(QtCore.QRect(1230, 160, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_schemaB.setFont(font)
        self.label_schemaB.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_schemaB.setAutoFillBackground(False)
        self.label_schemaB.setAlignment(QtCore.Qt.AlignCenter)
        self.label_schemaB.setObjectName("label_schemaB")
        self.label_headerA = QtWidgets.QLabel(self.centralwidget)
        self.label_headerA.setGeometry(QtCore.QRect(40, 300, 281, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_headerA.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_headerA.setFont(font)
        self.label_headerA.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_headerA.setAutoFillBackground(False)
        self.label_headerA.setAlignment(QtCore.Qt.AlignCenter)
        self.label_headerA.setObjectName("label_headerA")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 230, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1320, 230, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_headerB = QtWidgets.QLabel(self.centralwidget)
        self.label_headerB.setGeometry(QtCore.QRect(1230, 300, 281, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_headerB.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_headerB.setFont(font)
        self.label_headerB.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_headerB.setAutoFillBackground(False)
        self.label_headerB.setAlignment(QtCore.Qt.AlignCenter)
        self.label_headerB.setObjectName("label_headerB")
        self.label_headerNA = QtWidgets.QLabel(self.centralwidget)
        self.label_headerNA.setGeometry(QtCore.QRect(140, 270, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_headerNA.setFont(font)
        self.label_headerNA.setAlignment(QtCore.Qt.AlignCenter)
        self.label_headerNA.setObjectName("label_headerNA")
        self.label_headerNB = QtWidgets.QLabel(self.centralwidget)
        self.label_headerNB.setGeometry(QtCore.QRect(1330, 270, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_headerNB.setFont(font)
        self.label_headerNB.setAlignment(QtCore.Qt.AlignCenter)
        self.label_headerNB.setObjectName("label_headerNB")
        self.listViewA = QtWidgets.QListWidget(self.centralwidget)
        self.listViewA.setGeometry(QtCore.QRect(450, 110, 321, 451))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listViewA.setFont(font)
        self.listViewA.setObjectName("listViewA")
        self.listViewB = QtWidgets.QListWidget(self.centralwidget)
        self.listViewB.setGeometry(QtCore.QRect(790, 110, 311, 451))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listViewB.setFont(font)
        self.listViewB.setObjectName("listViewB")
        self.listViewIntersection = QtWidgets.QListWidget(self.centralwidget)
        self.listViewIntersection.setGeometry(QtCore.QRect(450, 570, 651, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listViewIntersection.setFont(font)
        self.listViewIntersection.setObjectName("listViewIntersection")
        self.listView = QtWidgets.QListWidget(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(430, 910, 691, 111))
        self.listView.setObjectName("listView")
        self.progressBar_IntA = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_IntA.setGeometry(QtCore.QRect(460, 870, 291, 23))
        self.progressBar_IntA.setProperty("value", 0)
        self.progressBar_IntA.setObjectName("progressBar_IntA")
        self.progressBar_IntB = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_IntB.setGeometry(QtCore.QRect(820, 870, 291, 23))
        self.progressBar_IntB.setProperty("value", 0)
        self.progressBar_IntB.setObjectName("progressBar_IntB")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(540, 840, 81, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(920, 840, 81, 16))
        self.label_6.setObjectName("label_6")
        self.progressBar_IntHeader = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_IntHeader.setGeometry(QtCore.QRect(660, 810, 291, 23))
        self.progressBar_IntHeader.setProperty("value", 0)
        self.progressBar_IntHeader.setObjectName("progressBar_IntHeader")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(760, 780, 81, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 740, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1250, 740, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.headerSelectorA = QtWidgets.QComboBox(self.centralwidget)
        self.headerSelectorA.setGeometry(QtCore.QRect(30, 790, 291, 22))
        self.headerSelectorA.setObjectName("headerSelectorA")
        self.headerSelectorB = QtWidgets.QComboBox(self.centralwidget)
        self.headerSelectorB.setGeometry(QtCore.QRect(1220, 790, 291, 22))
        self.headerSelectorB.setObjectName("headerSelectorB")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(650, 10, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.categorySelector = QtWidgets.QComboBox(self.centralwidget)
        self.categorySelector.setGeometry(QtCore.QRect(620, 60, 291, 22))
        self.categorySelector.setObjectName("categorySelector")
        self.listSchemaMatched = QtWidgets.QListWidget(self.centralwidget)
        self.listSchemaMatched.setGeometry(QtCore.QRect(10, 910, 371, 111))
        self.listSchemaMatched.setObjectName("listSchemaMatched")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(80, 870, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1541, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionSave_Result = QtWidgets.QAction(MainWindow)
        self.actionSave_Result.setObjectName("actionSave_Result")
        self.actionReset_Data = QtWidgets.QAction(MainWindow)
        self.actionReset_Data.setObjectName("actionReset_Data")
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Result)
        self.menuEdit.addAction(self.actionReset_Data)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnPrevA.setText(_translate("MainWindow", "Prev Column"))
        self.btnNextA.setText(_translate("MainWindow", "Next Column"))
        self.btnPrevB.setText(_translate("MainWindow", "Prev Column"))
        self.btnNextB.setText(_translate("MainWindow", "Next Column"))
        self.btnMatch.setText(_translate("MainWindow", "Match"))
        self.label.setText(_translate("MainWindow", "Table A"))
        self.label_2.setText(_translate("MainWindow", "Table B"))
        self.label_schemaA.setText(_translate("MainWindow", "www.fjfjdjsfjdsf.com.json.csv"))
        self.label_schemaB.setText(_translate("MainWindow", "www.fjfjdjsfjdsf.com.json.csv"))
        self.label_headerA.setText(_translate("MainWindow", "color"))
        self.label_3.setText(_translate("MainWindow", "Column"))
        self.label_4.setText(_translate("MainWindow", "Column"))
        self.label_headerB.setText(_translate("MainWindow", "color"))
        self.label_headerNA.setText(_translate("MainWindow", "1 of 30"))
        self.label_headerNB.setText(_translate("MainWindow", "1 of 30"))
        self.label_5.setText(_translate("MainWindow", "Intersection A"))
        self.label_6.setText(_translate("MainWindow", "Intersection B"))
        self.label_7.setText(_translate("MainWindow", "Jaccard Header"))
        self.label_8.setText(_translate("MainWindow", "Column A Selector"))
        self.label_9.setText(_translate("MainWindow", "Column B Selector"))
        self.label_10.setText(_translate("MainWindow", "Category Selector"))
        self.label_11.setText(_translate("MainWindow", "Schema Matched"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionSave_Result.setText(_translate("MainWindow", "Save Result .."))
        self.actionReset_Data.setText(_translate("MainWindow", "Reset Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
