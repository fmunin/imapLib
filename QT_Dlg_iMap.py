# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'iMap-MailBoxClnUp.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDateTimeEdit,
    QFrame, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(1081, 759)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: blue;\n"
"    padding:20px;\n"
"}\n"
"\n"
"QStatusBar { \n"
"font-size: 14pt;\n"
"color :#FEFEFE;\n"
"font-weight:bold}\n"
"\n"
"#label_3  { \n"
"font-size: 14pt;\n"
"color :#FEFEFE;\n"
"font-weight:bold}")
        self.actionClose_App = QAction(MainWindow)
        self.actionClose_App.setObjectName(u"actionClose_App")
        self.mi_ApplyFilter = QAction(MainWindow)
        self.mi_ApplyFilter.setObjectName(u"mi_ApplyFilter")
        self.mi_ApplyFilter.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(776, 0))
        self.centralwidget.setStyleSheet(u"#centralwidget{  \n"
"    background:  blue ;\n"
"    padding:15px;            \n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.emailGroup = QGroupBox(self.centralwidget)
        self.emailGroup.setObjectName(u"emailGroup")
        palette = QPalette()
        brush = QBrush(QColor(170, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        gradient = QLinearGradient(0, 0, 0, 1)
        gradient.setSpread(QGradient.PadSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(0, 191, 255, 255))
        gradient.setColorAt(0.75, QColor(254, 254, 254, 255))
        brush1 = QBrush(gradient)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        gradient1 = QLinearGradient(0, 0, 0, 1)
        gradient1.setSpread(QGradient.PadSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(0, 191, 255, 255))
        gradient1.setColorAt(0.75, QColor(254, 254, 254, 255))
        brush2 = QBrush(gradient1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        gradient2 = QLinearGradient(0, 0, 0, 1)
        gradient2.setSpread(QGradient.PadSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(0, 191, 255, 255))
        gradient2.setColorAt(0.75, QColor(254, 254, 254, 255))
        brush3 = QBrush(gradient2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        gradient3 = QLinearGradient(0, 0, 0, 1)
        gradient3.setSpread(QGradient.PadSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(0, 191, 255, 255))
        gradient3.setColorAt(0.75, QColor(254, 254, 254, 255))
        brush4 = QBrush(gradient3)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        gradient4 = QLinearGradient(0, 0, 0, 1)
        gradient4.setSpread(QGradient.PadSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(0, 191, 255, 255))
        gradient4.setColorAt(0.75, QColor(254, 254, 254, 255))
        brush5 = QBrush(gradient4)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        gradient5 = QLinearGradient(0, 0, 0, 1)
        gradient5.setSpread(QGradient.PadSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(0, 191, 255, 255))
        gradient5.setColorAt(0.75, QColor(254, 254, 254, 255))
        brush6 = QBrush(gradient5)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        gradient6 = QLinearGradient(0, 0, 0, 1)
        gradient6.setSpread(QGradient.PadSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(0, 191, 255, 255))
        gradient6.setColorAt(0.75, QColor(254, 254, 254, 255))
        brush7 = QBrush(gradient6)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        gradient7 = QLinearGradient(0, 0, 0, 1)
        gradient7.setSpread(QGradient.PadSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(0, 191, 255, 255))
        gradient7.setColorAt(0.75, QColor(254, 254, 254, 255))
        brush8 = QBrush(gradient7)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        gradient8 = QLinearGradient(0, 0, 0, 1)
        gradient8.setSpread(QGradient.PadSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(0, 191, 255, 255))
        gradient8.setColorAt(0.75, QColor(254, 254, 254, 255))
        brush9 = QBrush(gradient8)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        self.emailGroup.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Segoe MDL2 Assets"])
        font.setPointSize(16)
        self.emailGroup.setFont(font)
        self.emailGroup.setStyleSheet(u"  #emailGroup{\n"
"	background: qlineargradient(x1: 0, y1: 0,\n"
"                x2: 0, y2: 1,\n"
"                stop: 0 #00BFFF,\n"
"                stop: 0.75 #FEFEFE );\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.emailGroup)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.emailCB = QComboBox(self.emailGroup)
        self.emailCB.setObjectName(u"emailCB")

        self.verticalLayout_2.addWidget(self.emailCB)

        self.emailDetals = QLabel(self.emailGroup)
        self.emailDetals.setObjectName(u"emailDetals")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emailDetals.sizePolicy().hasHeightForWidth())
        self.emailDetals.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Segoe MDL2 Assets"])
        font1.setPointSize(12)
        self.emailDetals.setFont(font1)
        self.emailDetals.setStyleSheet(u"body {\n"
"	background: linear-gradient(0deg,rgba(135, 206, 250, 1) 0%, 		   rgba(254, 254, 254, 1) 100%);\n"
"}\n"
"\n"
"dl {\n"
"  margin-bottom: 20px;\n"
"}\n"
"\n"
"dt {\n"
"  font-weight: bold;\n"
"  margin-top: 10px;\n"
"}\n"
"\n"
"dd {\n"
"  margin-left: 20px;\n"
"  line-height: 1.5;\n"
"}")
        self.emailDetals.setTextFormat(Qt.RichText)

        self.verticalLayout_2.addWidget(self.emailDetals)

        self.frame_3 = QFrame(self.emailGroup)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(2)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(394, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.LogInBtn = QPushButton(self.frame_3)
        self.LogInBtn.setObjectName(u"LogInBtn")

        self.horizontalLayout_3.addWidget(self.LogInBtn)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.emailGroup)

        self.bottomPanel = QFrame(self.centralwidget)
        self.bottomPanel.setObjectName(u"bottomPanel")
        self.bottomPanel.setStyleSheet(u"#bottomPanel {\n"
"	background: qlineargradient(x1: 0, y1: 0,\n"
"                x2: 0, y2: 1,\n"
"                stop: 0  #FEFEFE ,\n"
"                stop: 0.75  #00BFFF);\n"
"}")
        self.bottomPanel.setFrameShape(QFrame.Box)
        self.bottomPanel.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.bottomPanel)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Age_Group = QGroupBox(self.bottomPanel)
        self.Age_Group.setObjectName(u"Age_Group")
        self.Age_Group.setMinimumSize(QSize(50, 0))
        self.verticalLayout_8 = QVBoxLayout(self.Age_Group)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.AgeFilterResults_Group = QGroupBox(self.Age_Group)
        self.AgeFilterResults_Group.setObjectName(u"AgeFilterResults_Group")
        self.verticalLayout_7 = QVBoxLayout(self.AgeFilterResults_Group)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frm_Avail_Folders = QFrame(self.AgeFilterResults_Group)
        self.frm_Avail_Folders.setObjectName(u"frm_Avail_Folders")
        self.frm_Avail_Folders.setFrameShape(QFrame.StyledPanel)
        self.frm_Avail_Folders.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frm_Avail_Folders)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.cb_Folder_Names = QComboBox(self.frm_Avail_Folders)
        self.cb_Folder_Names.setObjectName(u"cb_Folder_Names")

        self.horizontalLayout_4.addWidget(self.cb_Folder_Names)

        self.lbl_Folder_Details = QLabel(self.frm_Avail_Folders)
        self.lbl_Folder_Details.setObjectName(u"lbl_Folder_Details")

        self.horizontalLayout_4.addWidget(self.lbl_Folder_Details)


        self.verticalLayout_7.addWidget(self.frm_Avail_Folders)

        self.AgeFilterContols_Group = QGroupBox(self.AgeFilterResults_Group)
        self.AgeFilterContols_Group.setObjectName(u"AgeFilterContols_Group")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.AgeFilterContols_Group.sizePolicy().hasHeightForWidth())
        self.AgeFilterContols_Group.setSizePolicy(sizePolicy2)
        self.AgeFilterContols_Group.setMinimumSize(QSize(0, 130))
        self.AgeFilterContols_Group.setMaximumSize(QSize(16777215, 81))
        self.AgeFilterContols_Group.setBaseSize(QSize(0, 150))
        self.AgeFilterContols_Group.setAlignment(Qt.AlignCenter)
        self.AgeFilterContols_Group.setFlat(False)
        self.horizontalLayout_2 = QHBoxLayout(self.AgeFilterContols_Group)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_AgeEdit = QFrame(self.AgeFilterContols_Group)
        self.frame_AgeEdit.setObjectName(u"frame_AgeEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_AgeEdit.sizePolicy().hasHeightForWidth())
        self.frame_AgeEdit.setSizePolicy(sizePolicy3)
        self.frame_AgeEdit.setFrameShape(QFrame.StyledPanel)
        self.frame_AgeEdit.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_AgeEdit)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_Age = QLabel(self.frame_AgeEdit)
        self.label_Age.setObjectName(u"label_Age")

        self.verticalLayout_3.addWidget(self.label_Age)

        self.AgeEdit = QSpinBox(self.frame_AgeEdit)
        self.AgeEdit.setObjectName(u"AgeEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.AgeEdit.sizePolicy().hasHeightForWidth())
        self.AgeEdit.setSizePolicy(sizePolicy4)
        self.AgeEdit.setMinimumSize(QSize(40, 30))

        self.verticalLayout_3.addWidget(self.AgeEdit)


        self.horizontalLayout_2.addWidget(self.frame_AgeEdit)

        self.frame_As_Of_Dt_Edit = QFrame(self.AgeFilterContols_Group)
        self.frame_As_Of_Dt_Edit.setObjectName(u"frame_As_Of_Dt_Edit")
        sizePolicy3.setHeightForWidth(self.frame_As_Of_Dt_Edit.sizePolicy().hasHeightForWidth())
        self.frame_As_Of_Dt_Edit.setSizePolicy(sizePolicy3)
        self.frame_As_Of_Dt_Edit.setFrameShape(QFrame.StyledPanel)
        self.frame_As_Of_Dt_Edit.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_As_Of_Dt_Edit)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_AsOfDt = QLabel(self.frame_As_Of_Dt_Edit)
        self.label_AsOfDt.setObjectName(u"label_AsOfDt")

        self.verticalLayout_4.addWidget(self.label_AsOfDt)

        self.AsOfDt_Edit = QDateEdit(self.frame_As_Of_Dt_Edit)
        self.AsOfDt_Edit.setObjectName(u"AsOfDt_Edit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.AsOfDt_Edit.sizePolicy().hasHeightForWidth())
        self.AsOfDt_Edit.setSizePolicy(sizePolicy5)
        self.AsOfDt_Edit.setMinimumSize(QSize(0, 30))
        self.AsOfDt_Edit.setCurrentSection(QDateTimeEdit.DaySection)
        self.AsOfDt_Edit.setCalendarPopup(True)

        self.verticalLayout_4.addWidget(self.AsOfDt_Edit)


        self.horizontalLayout_2.addWidget(self.frame_As_Of_Dt_Edit)

        self.frame_Filter_Tool_Bar = QFrame(self.AgeFilterContols_Group)
        self.frame_Filter_Tool_Bar.setObjectName(u"frame_Filter_Tool_Bar")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_Filter_Tool_Bar.sizePolicy().hasHeightForWidth())
        self.frame_Filter_Tool_Bar.setSizePolicy(sizePolicy6)
        self.frame_Filter_Tool_Bar.setMinimumSize(QSize(114, 100))
        self.frame_Filter_Tool_Bar.setFrameShape(QFrame.StyledPanel)
        self.frame_Filter_Tool_Bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_Filter_Tool_Bar)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_Apply_Filter = QPushButton(self.frame_Filter_Tool_Bar)
        self.btn_Apply_Filter.setObjectName(u"btn_Apply_Filter")
        sizePolicy4.setHeightForWidth(self.btn_Apply_Filter.sizePolicy().hasHeightForWidth())
        self.btn_Apply_Filter.setSizePolicy(sizePolicy4)
        self.btn_Apply_Filter.setMinimumSize(QSize(110, 25))
        self.btn_Apply_Filter.setToolTipDuration(-1)
        icon = QIcon()
        icon.addFile(u":/buttons/img/funnel-small.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_Apply_Filter.setIcon(icon)
        self.btn_Apply_Filter.setIconSize(QSize(16, 16))

        self.verticalLayout_5.addWidget(self.btn_Apply_Filter)

        self.btn_View_Filtered = QPushButton(self.frame_Filter_Tool_Bar)
        self.btn_View_Filtered.setObjectName(u"btn_View_Filtered")
        sizePolicy4.setHeightForWidth(self.btn_View_Filtered.sizePolicy().hasHeightForWidth())
        self.btn_View_Filtered.setSizePolicy(sizePolicy4)
        self.btn_View_Filtered.setMinimumSize(QSize(110, 25))
        icon1 = QIcon()
        icon1.addFile(u":/buttons/img/folder-export.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_View_Filtered.setIcon(icon1)

        self.verticalLayout_5.addWidget(self.btn_View_Filtered)

        self.btn_View__GroupBy_URL = QPushButton(self.frame_Filter_Tool_Bar)
        self.btn_View__GroupBy_URL.setObjectName(u"btn_View__GroupBy_URL")
        sizePolicy4.setHeightForWidth(self.btn_View__GroupBy_URL.sizePolicy().hasHeightForWidth())
        self.btn_View__GroupBy_URL.setSizePolicy(sizePolicy4)
        self.btn_View__GroupBy_URL.setMinimumSize(QSize(110, 25))
        self.btn_View__GroupBy_URL.setIcon(icon1)

        self.verticalLayout_5.addWidget(self.btn_View__GroupBy_URL)


        self.horizontalLayout_2.addWidget(self.frame_Filter_Tool_Bar)

        self.frame_Filter_Tool_Bar.raise_()
        self.frame_AgeEdit.raise_()
        self.frame_As_Of_Dt_Edit.raise_()

        self.verticalLayout_7.addWidget(self.AgeFilterContols_Group)

        self.AgeFilter_Result_Label = QLabel(self.AgeFilterResults_Group)
        self.AgeFilter_Result_Label.setObjectName(u"AgeFilter_Result_Label")
        font2 = QFont()
        font2.setPointSize(12)
        self.AgeFilter_Result_Label.setFont(font2)

        self.verticalLayout_7.addWidget(self.AgeFilter_Result_Label)


        self.verticalLayout_8.addWidget(self.AgeFilterResults_Group)


        self.horizontalLayout.addWidget(self.Age_Group)

        self.results_Group = QGroupBox(self.bottomPanel)
        self.results_Group.setObjectName(u"results_Group")
        self.verticalLayout_6 = QVBoxLayout(self.results_Group)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.toolBar_Results = QFrame(self.results_Group)
        self.toolBar_Results.setObjectName(u"toolBar_Results")
        self.toolBar_Results.setFrameShape(QFrame.StyledPanel)
        self.toolBar_Results.setFrameShadow(QFrame.Raised)
        self._2 = QHBoxLayout(self.toolBar_Results)
        self._2.setObjectName(u"_2")
        self.btn_Delete_Filtered = QPushButton(self.toolBar_Results)
        self.btn_Delete_Filtered.setObjectName(u"btn_Delete_Filtered")
        sizePolicy4.setHeightForWidth(self.btn_Delete_Filtered.sizePolicy().hasHeightForWidth())
        self.btn_Delete_Filtered.setSizePolicy(sizePolicy4)
        self.btn_Delete_Filtered.setMinimumSize(QSize(110, 25))
        self.btn_Delete_Filtered.setToolTipDuration(-1)
        icon2 = QIcon()
        iconThemeName = u"accessories-character-map"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u":/buttons/img/prohibition.png", QSize(), QIcon.Normal, QIcon.On)

        self.btn_Delete_Filtered.setIcon(icon2)

        self._2.addWidget(self.btn_Delete_Filtered)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addWidget(self.toolBar_Results)

        self.tbl_SearchResult = QTableWidget(self.results_Group)
        self.tbl_SearchResult.setObjectName(u"tbl_SearchResult")

        self.verticalLayout_6.addWidget(self.tbl_SearchResult)


        self.horizontalLayout.addWidget(self.results_Group)


        self.verticalLayout.addWidget(self.bottomPanel)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.emailGroup.raise_()
        self.label_3.raise_()
        self.bottomPanel.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1081, 22))
        self.menuMain = QMenu(self.menubar)
        self.menuMain.setObjectName(u"menuMain")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label_Age.setBuddy(self.AgeEdit)
        self.label_AsOfDt.setBuddy(self.AsOfDt_Edit)
#endif // QT_CONFIG(shortcut)

        self.menubar.addAction(self.menuMain.menuAction())
        self.menuMain.addAction(self.actionClose_App)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"IMAP - Library - PYTHON", None))
        self.actionClose_App.setText(QCoreApplication.translate("MainWindow", u"Close Application", None))
        self.mi_ApplyFilter.setText(QCoreApplication.translate("MainWindow", u"Apply Filter", None))
#if QT_CONFIG(tooltip)
        self.mi_ApplyFilter.setToolTip(QCoreApplication.translate("MainWindow", u"Apply Filter", None))
#endif // QT_CONFIG(tooltip)
        self.emailGroup.setTitle(QCoreApplication.translate("MainWindow", u"Available eMail Address", None))
        self.emailDetals.setText(QCoreApplication.translate("MainWindow", u"<html><head>\n"
"<style>\n"
" body{\n"
"	background: linear-gradient(0deg,rgba(135, 206, 250, 1) 0%, rgba(254, 254, 254, 1) 100%);\n"
"}\n"
"\n"
"dl {\n"
"  margin-bottom: 20px;\n"
"}\n"
"\n"
"dt {\n"
"  font-weight: bold;\n"
"  margin-top: 10px;\n"
"}\n"
"\n"
"dd {\n"
"  margin-left: 20px;\n"
"  line-height: 1.5;\n"
" font-size:120;\n"
"}\n"
"</style>\n"
"</head>\n"
"<body><dl><dt>server</dt><dd>yourserver.com</dd>\n"
"<dt>email</dt><dd>email@yourserver.com</dd></dl></html>", None))
        self.LogInBtn.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.Age_Group.setTitle(QCoreApplication.translate("MainWindow", u"Filter By Age", None))
        self.AgeFilterResults_Group.setTitle("")
        self.lbl_Folder_Details.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.AgeFilterContols_Group.setTitle("")
        self.label_Age.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.label_AsOfDt.setText(QCoreApplication.translate("MainWindow", u"As Of Date", None))
#if QT_CONFIG(tooltip)
        self.btn_Apply_Filter.setToolTip(QCoreApplication.translate("MainWindow", u"Click to Apply Date Filter", None))
#endif // QT_CONFIG(tooltip)
        self.btn_Apply_Filter.setText(QCoreApplication.translate("MainWindow", u"Apply Filter", None))
#if QT_CONFIG(tooltip)
        self.btn_View_Filtered.setToolTip(QCoreApplication.translate("MainWindow", u"Click to View Filter Results", None))
#endif // QT_CONFIG(tooltip)
        self.btn_View_Filtered.setText(QCoreApplication.translate("MainWindow", u"Show  Headers", None))
#if QT_CONFIG(tooltip)
        self.btn_View__GroupBy_URL.setToolTip(QCoreApplication.translate("MainWindow", u"Click to View Filter Results", None))
#endif // QT_CONFIG(tooltip)
        self.btn_View__GroupBy_URL.setText(QCoreApplication.translate("MainWindow", u"Group By URL", None))
        self.AgeFilter_Result_Label.setText(QCoreApplication.translate("MainWindow", u"Apply Age Filter using controls above", None))
        self.results_Group.setTitle(QCoreApplication.translate("MainWindow", u"Domain Totals", None))
#if QT_CONFIG(tooltip)
        self.btn_Delete_Filtered.setToolTip(QCoreApplication.translate("MainWindow", u"Click to Delete Filtered Items", None))
#endif // QT_CONFIG(tooltip)
        self.btn_Delete_Filtered.setText(QCoreApplication.translate("MainWindow", u"Delete Selected", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menuMain.setTitle(QCoreApplication.translate("MainWindow", u"Main", None))
    # retranslateUi

