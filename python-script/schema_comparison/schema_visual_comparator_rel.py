# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'schema_visual_comparator.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import json
from common_utilities import  jaccard
from datetime import datetime
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


        ####Event

        self.actionOpen_File.triggered.connect(self.LoadResultFile)
        self.actionSave_Result.triggered.connect(self.SaveResult)
        self.actionReset_Data.triggered.connect(self.ResetData)

        self.tableASelection.activated.connect(self.OnSelectTableA)
        self.tableBSelection.activated.connect(self.OnSelectTableB)

        self.btnNextA.clicked.connect(self.OnNextColumnA)
        self.btnNextB.clicked.connect(self.OnNextColumnB)
        self.btnPrevA.clicked.connect(self.OnPrevColumnA)
        self.btnPrevB.clicked.connect(self.OnPrevColumnB)

        self.btnMatch.clicked.connect(self.OnMatch)

        self.headerSelectorA.activated.connect(self.OnSelectColumnA)
        self.headerSelectorB.activated.connect(self.OnSelectColumnB)
        self.categorySelector.activated.connect(self.OnSelectCategory)
        ##############
        ### Init Logic

        self.__initLogic()

        #######

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


    def ResetData(self):
        self.ClearMatch()
        self.ClearAllExceptResult()

    def LoadResultFile(self):
        self.listView.addItem("Loading Start File")
        with open(f"C:/Users/ludovico/Desktop/tesi/benchmark/common_corpus/match_result/16-12-2020-20-33-07.txt", "r", encoding="utf-8") as resultFile:
            self.resultFileData = json.load(resultFile)
        
        self.categories = list(self.resultFileData.keys())
        self.categorySelector.addItems(self.categories)
        self.listView.addItem("Completed Start File")

    def OnSelectCategory(self, index):

        self.ClearAllExceptResult()

        self.category = self.categories[index]

        self.LoadMetaInformationFromResult()
        self.tableASelection.addItems(sorted(self.mappingSugg.keys()))
        self.tableBSelection.addItems(sorted(self.mappingSugg.keys()))

        if self.category in self.matchDictionary.keys():
            self.listSchemaMatched.addItems(self.matchDictionary[self.category])
    
    def LoadMetaInformationFromResult(self):
        self.listView.addItem("Scanning information file")
        for hostProcessingSuggestion in self.resultFileData[self.category].values():
            countSuggestions = len(hostProcessingSuggestion)
            processed = 0
            for suggestion in hostProcessingSuggestion:
                srcFile = suggestion['src_file']
                dstFile = suggestion['dst_file']
                if not srcFile in self.mappingSugg.keys():
                    self.mappingSugg[srcFile] = []
                if not dstFile in self.mappingSugg.keys():
                    self.mappingSugg[dstFile] = []
                self.mappingSugg[srcFile].append(dstFile)
                self.mappingSugg[dstFile].append(srcFile)
                processed +=1
                self.progressBar.setValue( (processed / countSuggestions) * 100)
        self.listView.addItem("Scanning Completed")

    def OnSelectTableA(self, index):
        if not self.schemaFileNameA == self.tableASelection.itemText(index):
            self.schemaFileNameA = self.tableASelection.itemText(index)

            self.listViewA.clear()
            self.listSuggestA.clear()

            ###BuildingSchemaMap
            self.listView.addItem(f"Building Schema {self.schemaFileNameA}")
            self.schemaA = {}

            with open(f"C:/Users/ludovico/Desktop/tesi/benchmark/common_corpus/schemas/{self.category}/{self.schemaFileNameA}", "r", encoding="utf-8") as schemaFile:
                schemaRows = schemaFile.readlines()
                rowsNumber = len(schemaRows)
                self.headersA = schemaRows[0].rstrip("\n").split(";")[1:]
                headersNumber = len(self.headersA)
                for header in self.headersA:
                    self.schemaA[header] = []

                for x in range(1, rowsNumber):
                    self.progressBar.setValue( ((x+1) / rowsNumber) * 100)
                    row = schemaRows[x].rstrip("\n").split(";")[1:]
                    for hx in range(0, headersNumber):
                        self.schemaA[self.headersA[hx]].append(row[hx])

            self.listView.addItem(f"Building Schema {self.schemaFileNameA} Completed")
            self.listView.scrollToBottom()

            self.currentHeaderA = 0

            ######Graphic
            self.headerSelectorA.clear()
            self.headerSelectorA.addItems(self.headersA)
            self.listSuggestA.addItems(sorted(set(self.mappingSugg[self.schemaFileNameA])))
            self.label_schemaA.setText(self.schemaFileNameA)
            self.refreshHeaderA()

    def OnSelectTableB(self, index):
        if not self.schemaFileNameB == self.tableBSelection.itemText(index):
            self.schemaFileNameB = self.tableBSelection.itemText(index)

            self.listViewB.clear()
            self.listSuggestB.clear()

            ###BuildingSchemaMap
            self.listView.addItem(f"Building Schema {self.schemaFileNameA}")
            self.schemaB = {}

            with open(f"C:/Users/ludovico/Desktop/tesi/benchmark/common_corpus/schemas/{self.category}/{self.schemaFileNameB}", "r", encoding="utf-8") as schemaFile:
                schemaRows = schemaFile.readlines()
                rowsNumber = len(schemaRows)
                self.headersB = schemaRows[0].rstrip("\n").split(";")[1:]
                headersNumber = len(self.headersB)
                for header in self.headersB:
                    self.schemaB[header] = []

                for x in range(1, rowsNumber):
                    self.progressBar.setValue( ((x+1) / rowsNumber) * 100)
                    row = schemaRows[x].rstrip("\n").split(";")[1:]
                    for hx in range(0, headersNumber):
                        self.schemaB[self.headersB[hx]].append(row[hx])

            self.listView.addItem(f"Building Schema {self.schemaFileNameB} Completed")
            self.listView.scrollToBottom()

            self.currentHeaderB = 0

            ######Graphic
            self.headerSelectorB.clear()
            self.headerSelectorB.addItems(self.headersB)
            self.listSuggestB.addItems(sorted(set(self.mappingSugg[self.schemaFileNameB])))
            self.label_schemaB.setText(self.schemaFileNameB)
            self.refreshHeaderB()

    def __initLogic(self):
        self.resultFileData = {}
        self.mappingSugg = {}
        self.matchArray = []
        self.matchDictionary = {}
        self.schemaFileNameA = ""
        self.schemaFileNameB = ""
        self.schemaA = {}
        self.headersA = []
        self.schemaB = {}
        self.headersB = []
        self.currentHeaderA = 0
        self.currentHeaderB = 0

        self.categories = []
        self.category = ""


    def refreshHeaderA(self):
        self.label_headerA.setText(f"{self.headersA[self.currentHeaderA]}")
        self.label_headerNA.setText(f"{self.currentHeaderA + 1} of { len(self.headersA)}")
        itemsSet = set(self.schemaA[self.headersA[self.currentHeaderA]])
        itemsSet.discard("")
        self.listViewA.addItems(sorted(itemsSet))
        self.refreshIntersection()


    def refreshHeaderB(self):
        self.label_headerB.setText(f"{self.headersB[self.currentHeaderB]}")
        self.label_headerNB.setText(f"{self.currentHeaderB + 1} of { len(self.headersB)}")
        itemsSet = set(self.schemaB[self.headersB[self.currentHeaderB]])
        itemsSet.discard("")
        self.listViewB.addItems(sorted(itemsSet))
        self.refreshIntersection()
        

    def refreshIntersection(self):
        self.listViewIntersection.clear()
        try:
            set1 = set(self.schemaA[self.headersA[self.currentHeaderA]])
            set1.discard("")
            set2 = set(self.schemaB[self.headersB[self.currentHeaderB]])
            set2.discard("")
            inter = set1.intersection(set2)

            self.progressBar_IntA.setValue( (len(inter) / len(set1)) * 100)
            self.progressBar_IntB.setValue( (len(inter) / len(set2)) * 100)
            self.listViewIntersection.addItems(inter)
            self.progressBar_IntHeader.setValue(jaccard(self.headersA[self.currentHeaderA], self.headersB[self.currentHeaderB]) * 100)
        except:
            pass


    def OnNextColumnA(self):
        if not self.CanPressButton():
            return
        if self.currentHeaderA + 1 == len(self.headersA):
            return
        self.currentHeaderA += 1
        self.listViewA.clear()
        self.headerSelectorA.setCurrentIndex(self.currentHeaderA)
        self.refreshHeaderA()

    def OnNextColumnB(self):
        if not self.CanPressButton():
            return
        if self.currentHeaderB + 1 == len(self.headersB):
            return
        self.currentHeaderB += 1
        self.listViewB.clear()
        self.headerSelectorB.setCurrentIndex(self.currentHeaderB)
        self.refreshHeaderB()

    def OnPrevColumnA(self):
        if not self.CanPressButton():
            return
        if self.currentHeaderA -1 < 0:
            return
        self.currentHeaderA -= 1
        self.listViewA.clear()
        self.headerSelectorA.setCurrentIndex(self.currentHeaderA)
        self.refreshHeaderA()

    def OnPrevColumnB(self):
        if not self.CanPressButton():
            return
        if self.currentHeaderB -1 < 0:
            return
        self.currentHeaderB -= 1
        self.listViewB.clear()
        self.headerSelectorB.setCurrentIndex(self.currentHeaderB)
        self.refreshHeaderB()

    def OnMatch(self):
        if not self.CanPressButton():
            return
        try:
            self.matchArray.append((self.category, self.schemaFileNameA, self.schemaFileNameB, self.headersA[self.currentHeaderA], self.headersB[self.currentHeaderB], str(self.currentHeaderA), str(self.currentHeaderB)))
            self.listView.addItem("; ".join(self.matchArray[-1]))
            self.listView.scrollToBottom()

            if not self.category in self.matchDictionary.keys():
                 self.matchDictionary[self.category] = []
            matchRes = f"[{self.category}]{self.schemaFileNameA} - {self.schemaFileNameB}"
            if not matchRes in self.matchDictionary[self.category]:
                self.matchDictionary[self.category].append(matchRes)
                self.listSchemaMatched.addItem(matchRes)
                self.listSchemaMatched.scrollToBottom()
        except:
            pass

    def OnSelectColumnA(self, index):
        if not self.CanPressButton():
            return
        self.currentHeaderA = index +1
        self.OnPrevColumnA()

    def OnSelectColumnB(self, index):
        if not self.CanPressButton():
            return
        self.currentHeaderB = index +1
        self.OnPrevColumnB()

    def ClearMatch(self):
        self.listSchemaMatched.clear()
        self.matchDictionary = {}
        self.matchArray = []

    def ClearAllExceptResult(self):

        
        self.listViewA.clear()
        self.listViewB.clear()
        self.listSuggestA.clear()
        self.listSuggestB.clear()
        self.listSchemaMatched.clear()

        self.headerSelectorA.clear()
        self.headerSelectorB.clear()

        self.tableASelection.clear()
        self.tableBSelection.clear()

        self.mappingSugg = {}
        self.schemaA = {}
        self.schemaB = {}
        self.headersA = []
        self.headersB = []
        self.schemaFileNameA = ""
        self.schemaFileNameB = ""
        self.currentHeaderA = 0
        self.currentHeaderB = 0

        

    def SaveResult(self):
        dt_string = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
        #fileName = f"match_result_{dt_string}.csv"
        fileName = f"match_result.csv"
        with open(fileName, "a+", encoding="utf-8") as resultFile:
            matchNumber = len(self.matchArray)
            for x in range(0, matchNumber):
                valueToWrite = ";".join(self.matchArray[x])
                resultFile.write(f"{valueToWrite}\n")
                self.progressBar.setValue( ((x+2)/matchNumber) * 100)

        self.listView.addItem("Result Saved!")
        self.listView.scrollToBottom()

    def CanPressButton(self):
        if self.category == "":
            return False
        if len(self.headersA) == 0 or len(self.headersB) == 0:
            return False
        return True




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
