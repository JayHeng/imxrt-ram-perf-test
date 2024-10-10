# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\github_repo_jay\MCU-MemTestUtility\gui\MCU-MemTestUtility.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_memTesterWin(object):
    def setupUi(self, memTesterWin):
        memTesterWin.setObjectName("memTesterWin")
        memTesterWin.resize(995, 603)
        self.centralwidget = QtWidgets.QWidget(memTesterWin)
        self.centralwidget.setObjectName("centralwidget")
        self.mcuFrame = QtWidgets.QFrame(self.centralwidget)
        self.mcuFrame.setGeometry(QtCore.QRect(10, 10, 241, 391))
        self.mcuFrame.setAutoFillBackground(False)
        self.mcuFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mcuFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mcuFrame.setLineWidth(1)
        self.mcuFrame.setObjectName("mcuFrame")
        self.label_mcuDevice = QtWidgets.QLabel(self.mcuFrame)
        self.label_mcuDevice.setGeometry(QtCore.QRect(10, 10, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_mcuDevice.setFont(font)
        self.label_mcuDevice.setObjectName("label_mcuDevice")
        self.comboBox_mcuDevice = QtWidgets.QComboBox(self.mcuFrame)
        self.comboBox_mcuDevice.setGeometry(QtCore.QRect(130, 10, 101, 22))
        self.comboBox_mcuDevice.setObjectName("comboBox_mcuDevice")
        self.comboBox_mcuDevice.addItem("")
        self.textEdit_mixspiConnection = QtWidgets.QTextEdit(self.mcuFrame)
        self.textEdit_mixspiConnection.setEnabled(True)
        self.textEdit_mixspiConnection.setGeometry(QtCore.QRect(10, 80, 221, 131))
        self.textEdit_mixspiConnection.setReadOnly(True)
        self.textEdit_mixspiConnection.setObjectName("textEdit_mixspiConnection")
        self.label_cpuSpeed = QtWidgets.QLabel(self.mcuFrame)
        self.label_cpuSpeed.setGeometry(QtCore.QRect(20, 220, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_cpuSpeed.setFont(font)
        self.label_cpuSpeed.setObjectName("label_cpuSpeed")
        self.lineEdit_cpuSpeed = QtWidgets.QLineEdit(self.mcuFrame)
        self.lineEdit_cpuSpeed.setGeometry(QtCore.QRect(130, 220, 91, 20))
        self.lineEdit_cpuSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_cpuSpeed.setObjectName("lineEdit_cpuSpeed")
        self.checkBox_enableL1Cache = QtWidgets.QCheckBox(self.mcuFrame)
        self.checkBox_enableL1Cache.setGeometry(QtCore.QRect(60, 250, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_enableL1Cache.setFont(font)
        self.checkBox_enableL1Cache.setObjectName("checkBox_enableL1Cache")
        self.checkBox_enablePrefetch = QtWidgets.QCheckBox(self.mcuFrame)
        self.checkBox_enablePrefetch.setGeometry(QtCore.QRect(60, 280, 111, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_enablePrefetch.setFont(font)
        self.checkBox_enablePrefetch.setObjectName("checkBox_enablePrefetch")
        self.label_prefetchBufferSize = QtWidgets.QLabel(self.mcuFrame)
        self.label_prefetchBufferSize.setGeometry(QtCore.QRect(10, 310, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_prefetchBufferSize.setFont(font)
        self.label_prefetchBufferSize.setObjectName("label_prefetchBufferSize")
        self.comboBox_prefetchBufferSize = QtWidgets.QComboBox(self.mcuFrame)
        self.comboBox_prefetchBufferSize.setGeometry(QtCore.QRect(130, 310, 91, 22))
        self.comboBox_prefetchBufferSize.setMaxVisibleItems(13)
        self.comboBox_prefetchBufferSize.setObjectName("comboBox_prefetchBufferSize")
        self.comboBox_prefetchBufferSize.addItem("")
        self.comboBox_prefetchBufferSize.addItem("")
        self.comboBox_prefetchBufferSize.addItem("")
        self.pushButton_mixspiConnectionConfiguration = QtWidgets.QPushButton(self.mcuFrame)
        self.pushButton_mixspiConnectionConfiguration.setGeometry(QtCore.QRect(14, 40, 211, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_mixspiConnectionConfiguration.setFont(font)
        self.pushButton_mixspiConnectionConfiguration.setObjectName("pushButton_mixspiConnectionConfiguration")
        self.pushButton_mixspiAdvancedConfiguration = QtWidgets.QPushButton(self.mcuFrame)
        self.pushButton_mixspiAdvancedConfiguration.setGeometry(QtCore.QRect(14, 350, 211, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_mixspiAdvancedConfiguration.setFont(font)
        self.pushButton_mixspiAdvancedConfiguration.setObjectName("pushButton_mixspiAdvancedConfiguration")
        self.uartFrame = QtWidgets.QFrame(self.centralwidget)
        self.uartFrame.setGeometry(QtCore.QRect(10, 410, 241, 151))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.uartFrame.setFont(font)
        self.uartFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.uartFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.uartFrame.setObjectName("uartFrame")
        self.label_comPort = QtWidgets.QLabel(self.uartFrame)
        self.label_comPort.setGeometry(QtCore.QRect(30, 20, 61, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(True)
        font.setWeight(75)
        self.label_comPort.setFont(font)
        self.label_comPort.setObjectName("label_comPort")
        self.label_baudrate = QtWidgets.QLabel(self.uartFrame)
        self.label_baudrate.setGeometry(QtCore.QRect(30, 80, 61, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_baudrate.setFont(font)
        self.label_baudrate.setObjectName("label_baudrate")
        self.comboBox_comPort = QtWidgets.QComboBox(self.uartFrame)
        self.comboBox_comPort.setGeometry(QtCore.QRect(100, 20, 111, 22))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.comboBox_comPort.setFont(font)
        self.comboBox_comPort.setObjectName("comboBox_comPort")
        self.comboBox_baudrate = QtWidgets.QComboBox(self.uartFrame)
        self.comboBox_baudrate.setGeometry(QtCore.QRect(100, 80, 111, 22))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.comboBox_baudrate.setFont(font)
        self.comboBox_baudrate.setObjectName("comboBox_baudrate")
        self.comboBox_baudrate.addItem("")
        self.pushButton_connect = QtWidgets.QPushButton(self.uartFrame)
        self.pushButton_connect.setGeometry(QtCore.QRect(60, 110, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_connect.setFont(font)
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.lineEdit_uartPad = QtWidgets.QLineEdit(self.uartFrame)
        self.lineEdit_uartPad.setGeometry(QtCore.QRect(30, 50, 181, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.lineEdit_uartPad.setFont(font)
        self.lineEdit_uartPad.setAutoFillBackground(True)
        self.lineEdit_uartPad.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_uartPad.setReadOnly(True)
        self.lineEdit_uartPad.setObjectName("lineEdit_uartPad")
        self.memFrame = QtWidgets.QFrame(self.centralwidget)
        self.memFrame.setGeometry(QtCore.QRect(260, 10, 721, 71))
        self.memFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.memFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.memFrame.setObjectName("memFrame")
        self.label_memType = QtWidgets.QLabel(self.memFrame)
        self.label_memType.setGeometry(QtCore.QRect(210, 10, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_memType.setFont(font)
        self.label_memType.setObjectName("label_memType")
        self.comboBox_memType = QtWidgets.QComboBox(self.memFrame)
        self.comboBox_memType.setGeometry(QtCore.QRect(280, 10, 111, 22))
        self.comboBox_memType.setObjectName("comboBox_memType")
        self.comboBox_memType.addItem("")
        self.comboBox_memType.addItem("")
        self.comboBox_memType.addItem("")
        self.comboBox_memType.addItem("")
        self.comboBox_memType.addItem("")
        self.label_memChip = QtWidgets.QLabel(self.memFrame)
        self.label_memChip.setGeometry(QtCore.QRect(400, 10, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_memChip.setFont(font)
        self.label_memChip.setObjectName("label_memChip")
        self.comboBox_memChip = QtWidgets.QComboBox(self.memFrame)
        self.comboBox_memChip.setGeometry(QtCore.QRect(470, 10, 241, 22))
        self.comboBox_memChip.setObjectName("comboBox_memChip")
        self.comboBox_memChip.addItem("")
        self.label_memSpeed = QtWidgets.QLabel(self.memFrame)
        self.label_memSpeed.setGeometry(QtCore.QRect(10, 40, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_memSpeed.setFont(font)
        self.label_memSpeed.setObjectName("label_memSpeed")
        self.comboBox_memSpeed = QtWidgets.QComboBox(self.memFrame)
        self.comboBox_memSpeed.setGeometry(QtCore.QRect(90, 40, 111, 22))
        self.comboBox_memSpeed.setObjectName("comboBox_memSpeed")
        self.comboBox_memSpeed.addItem("")
        self.comboBox_memSpeed.addItem("")
        self.comboBox_memSpeed.addItem("")
        self.comboBox_memSpeed.addItem("")
        self.comboBox_memSpeed.addItem("")
        self.comboBox_memSpeed.addItem("")
        self.comboBox_memSpeed.addItem("")
        self.comboBox_memSpeed.addItem("")
        self.comboBox_memSpeed.addItem("")
        self.comboBox_memSpeed.addItem("")
        self.comboBox_memSpeed.addItem("")
        self.comboBox_memSpeed.addItem("")
        self.comboBox_memSpeed.addItem("")
        self.comboBox_memSpeed.addItem("")
        self.label_memMode = QtWidgets.QLabel(self.memFrame)
        self.label_memMode.setGeometry(QtCore.QRect(210, 40, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_memMode.setFont(font)
        self.label_memMode.setObjectName("label_memMode")
        self.comboBox_memIoPadsMode = QtWidgets.QComboBox(self.memFrame)
        self.comboBox_memIoPadsMode.setGeometry(QtCore.QRect(280, 40, 111, 22))
        self.comboBox_memIoPadsMode.setObjectName("comboBox_memIoPadsMode")
        self.comboBox_memIoPadsMode.addItem("")
        self.comboBox_memIoPadsMode.addItem("")
        self.comboBox_memIoPadsMode.addItem("")
        self.comboBox_memIoPadsMode.addItem("")
        self.comboBox_memIoPadsMode.addItem("")
        self.comboBox_memInterfaceMode = QtWidgets.QComboBox(self.memFrame)
        self.comboBox_memInterfaceMode.setGeometry(QtCore.QRect(400, 40, 160, 22))
        self.comboBox_memInterfaceMode.setObjectName("comboBox_memInterfaceMode")
        self.comboBox_memInterfaceMode.addItem("")
        self.comboBox_memInterfaceMode.addItem("")
        self.comboBox_memInterfaceMode.addItem("")
        self.comboBox_memInterfaceMode.addItem("")
        self.comboBox_memInterfaceMode.addItem("")
        self.comboBox_memSampleRateMode = QtWidgets.QComboBox(self.memFrame)
        self.comboBox_memSampleRateMode.setGeometry(QtCore.QRect(570, 40, 141, 22))
        self.comboBox_memSampleRateMode.setObjectName("comboBox_memSampleRateMode")
        self.comboBox_memSampleRateMode.addItem("")
        self.comboBox_memSampleRateMode.addItem("")
        self.label_memVendor = QtWidgets.QLabel(self.memFrame)
        self.label_memVendor.setGeometry(QtCore.QRect(10, 10, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_memVendor.setFont(font)
        self.label_memVendor.setObjectName("label_memVendor")
        self.comboBox_memVendor = QtWidgets.QComboBox(self.memFrame)
        self.comboBox_memVendor.setGeometry(QtCore.QRect(90, 10, 111, 22))
        self.comboBox_memVendor.setObjectName("comboBox_memVendor")
        self.comboBox_memVendor.addItem("")
        self.comboBox_memVendor.addItem("")
        self.comboBox_memVendor.addItem("")
        self.comboBox_memVendor.addItem("")
        self.comboBox_memVendor.addItem("")
        self.comboBox_memVendor.addItem("")
        self.comboBox_memVendor.addItem("")
        self.comboBox_memVendor.addItem("")
        self.comboBox_memVendor.addItem("")
        self.dispFrame = QtWidgets.QFrame(self.centralwidget)
        self.dispFrame.setGeometry(QtCore.QRect(260, 90, 721, 471))
        self.dispFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dispFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.dispFrame.setObjectName("dispFrame")
        self.pushButton_memRegs = QtWidgets.QPushButton(self.dispFrame)
        self.pushButton_memRegs.setGeometry(QtCore.QRect(200, 10, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_memRegs.setFont(font)
        self.pushButton_memRegs.setObjectName("pushButton_memRegs")
        self.textEdit_displayWin = QtWidgets.QTextEdit(self.dispFrame)
        self.textEdit_displayWin.setGeometry(QtCore.QRect(10, 50, 701, 171))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.textEdit_displayWin.setFont(font)
        self.textEdit_displayWin.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_displayWin.setReadOnly(True)
        self.textEdit_displayWin.setObjectName("textEdit_displayWin")
        self.pushButton_perfTest = QtWidgets.QPushButton(self.dispFrame)
        self.pushButton_perfTest.setGeometry(QtCore.QRect(380, 10, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_perfTest.setFont(font)
        self.pushButton_perfTest.setObjectName("pushButton_perfTest")
        self.progressBar_action = QtWidgets.QProgressBar(self.dispFrame)
        self.progressBar_action.setGeometry(QtCore.QRect(10, 440, 701, 20))
        self.progressBar_action.setProperty("value", 100)
        self.progressBar_action.setObjectName("progressBar_action")
        self.textEdit_packetWin = QtWidgets.QTextEdit(self.dispFrame)
        self.textEdit_packetWin.setGeometry(QtCore.QRect(10, 330, 701, 101))
        self.textEdit_packetWin.setObjectName("textEdit_packetWin")
        self.pushButton_configSystem = QtWidgets.QPushButton(self.dispFrame)
        self.pushButton_configSystem.setGeometry(QtCore.QRect(100, 10, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_configSystem.setFont(font)
        self.pushButton_configSystem.setObjectName("pushButton_configSystem")
        self.pushButton_clearScreen = QtWidgets.QPushButton(self.dispFrame)
        self.pushButton_clearScreen.setGeometry(QtCore.QRect(620, 280, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_clearScreen.setFont(font)
        self.pushButton_clearScreen.setObjectName("pushButton_clearScreen")
        self.pushButton_stressTest = QtWidgets.QPushButton(self.dispFrame)
        self.pushButton_stressTest.setGeometry(QtCore.QRect(470, 10, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stressTest.setFont(font)
        self.pushButton_stressTest.setObjectName("pushButton_stressTest")
        self.pushButton_pinTest = QtWidgets.QPushButton(self.dispFrame)
        self.pushButton_pinTest.setGeometry(QtCore.QRect(10, 10, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_pinTest.setFont(font)
        self.pushButton_pinTest.setObjectName("pushButton_pinTest")
        self.pushButton_Go = QtWidgets.QPushButton(self.dispFrame)
        self.pushButton_Go.setGeometry(QtCore.QRect(620, 240, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Go.setFont(font)
        self.pushButton_Go.setObjectName("pushButton_Go")
        self.pushButton_rwTest = QtWidgets.QPushButton(self.dispFrame)
        self.pushButton_rwTest.setGeometry(QtCore.QRect(290, 10, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_rwTest.setFont(font)
        self.pushButton_rwTest.setObjectName("pushButton_rwTest")
        self.groupBox_pinWaveform = QtWidgets.QGroupBox(self.dispFrame)
        self.groupBox_pinWaveform.setGeometry(QtCore.QRect(10, 230, 601, 91))
        self.groupBox_pinWaveform.setObjectName("groupBox_pinWaveform")
        memTesterWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(memTesterWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 995, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menu_loadFirmware = QtWidgets.QMenu(self.menuTools)
        self.menu_loadFirmware.setInputMethodHints(QtCore.Qt.ImhNone)
        self.menu_loadFirmware.setObjectName("menu_loadFirmware")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        memTesterWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(memTesterWin)
        self.statusbar.setObjectName("statusbar")
        memTesterWin.setStatusBar(self.statusbar)
        self.menuHelpAction_homePage = QtWidgets.QAction(memTesterWin)
        self.menuHelpAction_homePage.setObjectName("menuHelpAction_homePage")
        self.menuHelpAction_aboutAuthor = QtWidgets.QAction(memTesterWin)
        self.menuHelpAction_aboutAuthor.setObjectName("menuHelpAction_aboutAuthor")
        self.menuHelpAction_revisionHistory = QtWidgets.QAction(memTesterWin)
        self.menuHelpAction_revisionHistory.setObjectName("menuHelpAction_revisionHistory")
        self.menuLoadFwAction_No = QtWidgets.QAction(memTesterWin)
        self.menuLoadFwAction_No.setCheckable(True)
        self.menuLoadFwAction_No.setChecked(False)
        self.menuLoadFwAction_No.setObjectName("menuLoadFwAction_No")
        self.menuLoadFwAction_Yes = QtWidgets.QAction(memTesterWin)
        self.menuLoadFwAction_Yes.setCheckable(True)
        self.menuLoadFwAction_Yes.setChecked(True)
        self.menuLoadFwAction_Yes.setObjectName("menuLoadFwAction_Yes")
        self.menu_loadFirmware.addAction(self.menuLoadFwAction_Yes)
        self.menu_loadFirmware.addAction(self.menuLoadFwAction_No)
        self.menuTools.addAction(self.menu_loadFirmware.menuAction())
        self.menuHelp.addAction(self.menuHelpAction_homePage)
        self.menuHelp.addAction(self.menuHelpAction_aboutAuthor)
        self.menuHelp.addAction(self.menuHelpAction_revisionHistory)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(memTesterWin)
        self.comboBox_prefetchBufferSize.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(memTesterWin)

    def retranslateUi(self, memTesterWin):
        _translate = QtCore.QCoreApplication.translate
        memTesterWin.setWindowTitle(_translate("memTesterWin", "MCU Mem Test Utility"))
        self.label_mcuDevice.setText(_translate("memTesterWin", "MCU Device:"))
        self.comboBox_mcuDevice.setItemText(0, _translate("memTesterWin", "i.MXRT117x"))
        self.label_cpuSpeed.setText(_translate("memTesterWin", "CPU Speed (MHz):"))
        self.lineEdit_cpuSpeed.setText(_translate("memTesterWin", "500"))
        self.checkBox_enableL1Cache.setText(_translate("memTesterWin", "Enable L1 Cache"))
        self.checkBox_enablePrefetch.setText(_translate("memTesterWin", "Enable Prefetch"))
        self.label_prefetchBufferSize.setText(_translate("memTesterWin", "Prefetch Buffer Size:"))
        self.comboBox_prefetchBufferSize.setItemText(0, _translate("memTesterWin", "64bit"))
        self.comboBox_prefetchBufferSize.setItemText(1, _translate("memTesterWin", "2KB"))
        self.comboBox_prefetchBufferSize.setItemText(2, _translate("memTesterWin", "4KB"))
        self.pushButton_mixspiConnectionConfiguration.setText(_translate("memTesterWin", "MixSPI Connection Configuration"))
        self.pushButton_mixspiAdvancedConfiguration.setText(_translate("memTesterWin", "MixSPI Advanced Configuration"))
        self.label_comPort.setText(_translate("memTesterWin", "COM Port:"))
        self.label_baudrate.setText(_translate("memTesterWin", "Baudrate:"))
        self.comboBox_baudrate.setItemText(0, _translate("memTesterWin", "57600"))
        self.pushButton_connect.setText(_translate("memTesterWin", "Connect"))
        self.lineEdit_uartPad.setText(_translate("memTesterWin", "LPUART1 - GPIO_AD[25:24]"))
        self.label_memType.setText(_translate("memTesterWin", "Mem Type:"))
        self.comboBox_memType.setItemText(0, _translate("memTesterWin", "QuadSPI NOR"))
        self.comboBox_memType.setItemText(1, _translate("memTesterWin", "OctalSPI NOR"))
        self.comboBox_memType.setItemText(2, _translate("memTesterWin", "HyperFlash"))
        self.comboBox_memType.setItemText(3, _translate("memTesterWin", "PSRAM"))
        self.comboBox_memType.setItemText(4, _translate("memTesterWin", "HyperRAM"))
        self.label_memChip.setText(_translate("memTesterWin", "Mem Chip:"))
        self.comboBox_memChip.setItemText(0, _translate("memTesterWin", "ISSI_IS25WP128-JBLE"))
        self.label_memSpeed.setText(_translate("memTesterWin", "Mem Speed:"))
        self.comboBox_memSpeed.setItemText(0, _translate("memTesterWin", "30MHz"))
        self.comboBox_memSpeed.setItemText(1, _translate("memTesterWin", "50MHz"))
        self.comboBox_memSpeed.setItemText(2, _translate("memTesterWin", "60MHz"))
        self.comboBox_memSpeed.setItemText(3, _translate("memTesterWin", "80MHz"))
        self.comboBox_memSpeed.setItemText(4, _translate("memTesterWin", "100MHz"))
        self.comboBox_memSpeed.setItemText(5, _translate("memTesterWin", "120MHz"))
        self.comboBox_memSpeed.setItemText(6, _translate("memTesterWin", "133MHz"))
        self.comboBox_memSpeed.setItemText(7, _translate("memTesterWin", "166MHz"))
        self.comboBox_memSpeed.setItemText(8, _translate("memTesterWin", "200MHz"))
        self.comboBox_memSpeed.setItemText(9, _translate("memTesterWin", "240MHz"))
        self.comboBox_memSpeed.setItemText(10, _translate("memTesterWin", "250MHz"))
        self.comboBox_memSpeed.setItemText(11, _translate("memTesterWin", "266MHz"))
        self.comboBox_memSpeed.setItemText(12, _translate("memTesterWin", "332MHz"))
        self.comboBox_memSpeed.setItemText(13, _translate("memTesterWin", "400MHz"))
        self.label_memMode.setText(_translate("memTesterWin", "Mem Mode:"))
        self.comboBox_memIoPadsMode.setItemText(0, _translate("memTesterWin", "Single I/O"))
        self.comboBox_memIoPadsMode.setItemText(1, _translate("memTesterWin", "Dual I/O"))
        self.comboBox_memIoPadsMode.setItemText(2, _translate("memTesterWin", "Quad I/O"))
        self.comboBox_memIoPadsMode.setItemText(3, _translate("memTesterWin", "Octal I/O"))
        self.comboBox_memIoPadsMode.setItemText(4, _translate("memTesterWin", "Hex I/O"))
        self.comboBox_memInterfaceMode.setItemText(0, _translate("memTesterWin", "Standard/Dual/Quad SPI"))
        self.comboBox_memInterfaceMode.setItemText(1, _translate("memTesterWin", "Ouad Peripheral Interface"))
        self.comboBox_memInterfaceMode.setItemText(2, _translate("memTesterWin", "Octa Peripheral Interface"))
        self.comboBox_memInterfaceMode.setItemText(3, _translate("memTesterWin", "HyperBus"))
        self.comboBox_memInterfaceMode.setItemText(4, _translate("memTesterWin", "HyperBus-Extend-IO"))
        self.comboBox_memSampleRateMode.setItemText(0, _translate("memTesterWin", "Single Date Rate"))
        self.comboBox_memSampleRateMode.setItemText(1, _translate("memTesterWin", "Double Transfer Rate"))
        self.label_memVendor.setText(_translate("memTesterWin", "Mem Vendor:"))
        self.comboBox_memVendor.setItemText(0, _translate("memTesterWin", "Winbond"))
        self.comboBox_memVendor.setItemText(1, _translate("memTesterWin", "Macronix"))
        self.comboBox_memVendor.setItemText(2, _translate("memTesterWin", "GigaDevice"))
        self.comboBox_memVendor.setItemText(3, _translate("memTesterWin", "Infineon_Cypress_Spansion"))
        self.comboBox_memVendor.setItemText(4, _translate("memTesterWin", "Micron"))
        self.comboBox_memVendor.setItemText(5, _translate("memTesterWin", "ISSI"))
        self.comboBox_memVendor.setItemText(6, _translate("memTesterWin", "Renesas_Dialog__Adesto"))
        self.comboBox_memVendor.setItemText(7, _translate("memTesterWin", "APMemory"))
        self.comboBox_memVendor.setItemText(8, _translate("memTesterWin", "Misc"))
        self.pushButton_memRegs.setText(_translate("memTesterWin", "Mem REGs"))
        self.pushButton_perfTest.setText(_translate("memTesterWin", "Perf Test"))
        self.pushButton_configSystem.setText(_translate("memTesterWin", "Config System"))
        self.pushButton_clearScreen.setText(_translate("memTesterWin", "Clear Screen"))
        self.pushButton_stressTest.setText(_translate("memTesterWin", "Stress Test"))
        self.pushButton_pinTest.setText(_translate("memTesterWin", "Pin Test"))
        self.pushButton_Go.setText(_translate("memTesterWin", "Go"))
        self.pushButton_rwTest.setText(_translate("memTesterWin", "R/W Test"))
        self.groupBox_pinWaveform.setTitle(_translate("memTesterWin", "Pin Waveform"))
        self.menuFile.setTitle(_translate("memTesterWin", "File"))
        self.menuEdit.setTitle(_translate("memTesterWin", "Edit"))
        self.menuView.setTitle(_translate("memTesterWin", "View"))
        self.menuTools.setTitle(_translate("memTesterWin", "Tools"))
        self.menu_loadFirmware.setTitle(_translate("memTesterWin", "Load Firmware"))
        self.menuWindow.setTitle(_translate("memTesterWin", "Window"))
        self.menuHelp.setTitle(_translate("memTesterWin", "Help"))
        self.menuHelpAction_homePage.setText(_translate("memTesterWin", "Home Page"))
        self.menuHelpAction_aboutAuthor.setText(_translate("memTesterWin", "About Author"))
        self.menuHelpAction_revisionHistory.setText(_translate("memTesterWin", "Revision History"))
        self.menuLoadFwAction_No.setText(_translate("memTesterWin", "No - For Dev"))
        self.menuLoadFwAction_Yes.setText(_translate("memTesterWin", "Yes"))
