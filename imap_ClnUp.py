from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import QApplication,QTableWidget, QTableWidgetItem, QMessageBox,QAbstractItemView

from PySide6.QtCore import Qt
from QT_Dlg_iMap import Ui_MainWindow
from cleanUp_MailBx import iMapMailBox, create_CutOffDt
import yaml 
import sys
import re

#constants
fltrViewId_msgDetail = 0xA0 
fltrViewId_byURL = 0xB0

   
class iMapDialog(QtWidgets.QMainWindow, Ui_MainWindow):
    #create mailBoxConnected signal
    mailBox_Connected = QtCore.Signal() #no arguments passed
    mailBox_Disconnected = QtCore.Signal() #no arguments passed
    
    mailBox_current_Folder_changed = QtCore.Signal() #triggered when current folder changes
    #CAN APPLY DATE FILTERS TO MAILBOX
    #triggered whenever the filtered email list changes
    mailBox_Filter_changed = QtCore.Signal() 
    #Dialog can show different results
    dlgView_changed =QtCore.Signal()
   

    @property
    def isConnected(self):
        return self._isConnected
    
    @isConnected.setter
    def isConnected(self, value):
        self._isConnected = value
        if self._isConnected :
            self.mailBox_Connected.emit()
        else:
            self.mailBox_Disconnected.emit()    

   

    @property 
    def fltrView_Id(self):
        return self._fltrView_Id

    @fltrView_Id.setter
    def fltr_Id(self,value):
        self._fltrView_Id = value
        self.dlgView_changed.emit()    

    """
    The dialog can use three datasets
     - eMailID-List -This is list of email ID's returned by IMAP library from query functions.
     - msgHdr-List - The emailID's can be used to retrieve message headers for display.
     - msgHdr-Dataframe - The msgHdr list can be turned into a dataframe which can be queried etc

        """
    @property 
    def eMailID_List(self):
        return self._eMailID_List

    @eMailID_List.setter
    def eMailID_List(self,value):
        self._eMailID_List = value
        if self._eMailID_List :
            self.mailBox_Filter_changed.emit()        

    @property 
    def Msg_Header_List(self):
        return self._Msg_Header_List

    @Msg_Header_List.setter
    def Msg_Header_List(self,value):
        if value is None:
            self.tbl_SearchResult.setRowCount(0) #clear table
        self._Msg_Header_List = value

    @property 
    def Msg_Header_DF(self):
        return self._Msg_Header_DF

    @Msg_Header_DF.setter
    def Msg_Header_DF(self,value):
        if value is None:
            self.tbl_SearchResult.setRowCount(0) #clear table
        self._Msg_Header_DF = value         

    @property #this property is now readonly
    def Msg_GroupBy_URL_List(self):
        #group the dataframe by url, return anyone over 5 emails
        min_count = 5
        result = self.Msg_Header_DF.groupby('url').size().sort_values(ascending=False)
        return result[result >= min_count] 

    @property
    def current_Folder(self):
        return self._current_Folder

    @current_Folder.setter
    def current_Folder(self,value):
        if self._current_Folder != value:
            self._current_Folder = value
            self.mailBox_current_Folder_changed.emit() #trigger signal

       

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)      
        #default values
        self._fltr_Id = None
        self._userList = self.__extract_UserList__()
        self._current_Folder = None
        #set default values for 3 datasets
        self._eMailID_List = None
        self._Msg_Header_List = None
        self._Msg_Header_DF = None        

        self.__fill_addressCB__(self.emailCB)
        self.__assignEvents__()
        self.__assignCustomSignals__()
        #by default disable log in button
        self.__setControlDefault__()
        
        

    def __setControlDefault__(self):
        self.isConnected = False #not connected by default
        self.LogInBtn.setDisabled(True)
        self.btn_Apply_Filter.setDisabled(True)
        self.btn_View_Filtered.setDisabled(True)
        self.btn_Delete_Filtered.setDisabled(True)
        self.btn_View__GroupBy_URL.setDisabled(True)
        #set default value on spin box
        self.AgeEdit.setMinimum(0)
        self.AgeEdit.setMaximum(180)
        self.AgeEdit.setValue(90) #by default look at items 90 days old
        self.AgeEdit.setSingleStep(1) #move by 1 day
        self.AsOfDt_Edit.setDate(create_CutOffDt(90))
        self.lbl_Folder_Details.setWordWrap(True)
        #style the result table
        self.tbl_SearchResult.setSelectionBehavior(QAbstractItemView.SelectRows)

    def __assignEvents__ (self):
        self.actionClose_App.triggered.connect(self.close)
        self.LogInBtn.clicked.connect(self.onClick_LogIn)
        self.btn_Apply_Filter.clicked.connect(self.onClick_ApplyFilter)
        self.emailCB.currentIndexChanged.connect(self.on_emailCB_changed)
        self.cb_Folder_Names.currentIndexChanged.connect(self.on_Folder_changed)
        self.AgeEdit.valueChanged.connect(self.on_AgeEdit_changed)
        self.AsOfDt_Edit.dateChanged.connect(self.On_AsOfDt_changed)
        self.btn_Delete_Filtered.clicked.connect(self.onClick_DeleteFiltered)
        self.btn_View_Filtered.clicked.connect(self.onClick_View_Detail)
        self.btn_View__GroupBy_URL.clicked.connect(self.onClick_View_ByDomain)
        self.tbl_SearchResult.cellClicked.connect(self.onClick_tbl_Cell)

    def __assignCustomSignals__ (self):
        self.mailBox_Connected.connect(self.onMailBox_Connected)
        self.mailBox_Disconnected.connect(self.onMailBox_disConnected)
        self.mailBox_Filter_changed.connect(self.onFilter_Changed)
        self.mailBox_current_Folder_changed.connect(self.on_current_Folder_changed)
        self.dlgView_changed.connect(self.onView_Changed)

    def __extract_UserList__(self):
        #get user list from yaml file
        with open('env\imap.yaml','r') as file :
            data = yaml.safe_load(file)
        return data['users']  
    
    def __fill_addressCB__(self,cb):
            for user in self._userList:
                cb.addItem(f"{user['name']} ({len(user['mailbox'])} mailboxes)")

    def __fill_folderCB__(self,cb):
            cb.addItems(mailBox.get_Folder_List())

    def _fill_Result_eMailList_ (self, HeaderList):
        self.tbl_SearchResult.setRowCount(len(HeaderList)+1)               
        #use first record in field to populate header
        firstRecord = HeaderList[0]
        self.tbl_SearchResult.clear() #clear current table
        self.tbl_SearchResult.setColumnCount(len(firstRecord))
        self.tbl_SearchResult.setHorizontalHeaderLabels(list(firstRecord.keys()))
        self.tbl_SearchResult.verticalHeader().hide() #removes index column        
        #cycle thru list
        for row_id, msg_Headers in enumerate(HeaderList):
            for col_id, fieldNm in enumerate(msg_Headers):
                cellValue = QTableWidgetItem(msg_Headers[fieldNm])
                self.tbl_SearchResult.setItem(row_id,col_id,cellValue)
        #resize column
        self.tbl_SearchResult.resizeColumnsToContents() 

    def _fill_Result_domainList_ (self,domain_List):
        self.tbl_SearchResult.clear() #clear current table
        self.tbl_SearchResult.setColumnCount(2) #fixed columns.
        self.tbl_SearchResult.setRowCount(len(domain_List)+1)    
        
        self.tbl_SearchResult.setHorizontalHeaderLabels(['url','eMail Count'])
        self.tbl_SearchResult.verticalHeader().hide() #removes index column  
        colId_url = 0
        colId_emailCount = 1
        for url,emailCount in domain_List.items():
            currentRow = domain_List.index.get_loc(url)
            cellValue_url = QTableWidgetItem(url)
            cellValue_emailCount = QTableWidgetItem(str(emailCount))
            print(f"{url} -- {emailCount}")
            self.tbl_SearchResult.setItem(currentRow,colId_url,cellValue_url)
            self.tbl_SearchResult.setItem(currentRow,colId_emailCount,cellValue_emailCount)
        #resize column
        self.tbl_SearchResult.resizeColumnsToContents() 


   

        
    def __findUser__(self,userID):
        for index, user in enumerate(self._userList):
            if user.get('userID') == userID:
                return index
        return -1
    
    def on_emailCB_changed(self, index):
        #check if mail box is connected, and disconnect
        if self.isConnected :
            self.isConnected = False #should disconnect mailbox
        currentSelectedUser = self.emailCB.currentText().split(" ", maxsplit=2)[0]
        self._currentUser = self._userList[self.__findUser__(currentSelectedUser)]
        self.LogInBtn.setDisabled(False)
        newContent = ""
        for mailbox in self._currentUser['mailbox']:
            newContent += f"<dt>server</dt><dd>{mailbox['server']}</dd><dt>email</dt><dd>{mailbox['userID']}</dd>"
        currentContent = self.emailDetals.text() #retrieve current text
        #replace content
        newContent = re.sub('<dl>(.+)<\/dl>',currentContent,newContent)
        self.emailDetals.setText(newContent)

        
    def on_Folder_changed (self, index):
        #apply filter based on selected folder
        self.current_Folder = self.cb_Folder_Names.currentText()             


    def on_AgeEdit_changed(self, index):
        ageFilter = QtCore.QDate.daysTo(self.AsOfDt_Edit.date(), QtCore.QDate.currentDate())
        if ageFilter != index:
            self.AsOfDt_Edit.setDate(create_CutOffDt(index))
        
    def On_AsOfDt_changed(self, date):
        cutOffDt = create_CutOffDt(self.AgeEdit.value())
        #print(cutOffDt)
        if  cutOffDt != date:
            ageFilter = QtCore.QDate.daysTo(date, QtCore.QDate.currentDate())
            print (f'Changing age filter to {ageFilter}')
            self.AgeEdit.setValue(ageFilter)       
    
    def onClick_LogIn(self):
        mailBox.server = self._currentUser['server']
        mailBox.userID = self._currentUser['userID']
        mailBox.password = self._currentUser['pwd']
        if not mailBox.createConn():
            print (f'Unable to connect to mailbox {mailBox.server}')
        if mailBox.logIn():
            self.isConnected = True     
        else:
            self.statusBar().showMessage("Unable to connect")

    def onClick_ApplyFilter(self):  
        #apply age filter to selected inbox
        lcl_cutOffDt = create_CutOffDt (int(self.AgeEdit.text()))
        self.eMailID_List = self.mailBox_ApplyFilter_ByDt (lcl_cutOffDt)        
       
    


    def onClick_DeleteFiltered(self):
        #need to delet all items in Msg_Header_List object
        if self.fltrView_Id == fltrViewId_msgDetail:
            if show_YesNo_messagebox(f"Are you sure you want to delete {len(self.eMailID_List)} messages?",
                                    f"Confirm Message Deletion ") == QMessageBox.StandardButton.Yes:
                self.mailBox_Delete_filteredMsg(self.eMailID_List)
        elif self.fltrView_Id == fltrViewId_byURL:    
            selected_row = self.tbl_SearchResult.currentRow()
            selected_url = self.tbl_SearchResult.item(selected_row,0).text()
            if show_YesNo_messagebox(f"Are you sure you want to delete messages from {selected_url}",
                                    f"Confirm Message Deletion - url - {selected_url}") == QMessageBox.StandardButton.Yes:
                self.mailBox_Delete_byURL(selected_url)
            else:
                show_info_messagebox("you selected no")    

    def onClick_View_Detail(self):
        self.fltr_Id =  fltrViewId_msgDetail        

    def onClick_View_ByDomain(self):
        self.fltr_Id = fltrViewId_byURL

    def onClick_tbl_Cell(self, row, col):
        tblCell = self.tbl_SearchResult.item(row,col)
        show_info_messagebox(f"clicked column {col} and row {row} item {tblCell.text()}")

    def onFilter_Changed(self):
        #when ID list is changed, change all other datasets
        self.Msg_Header_List = None
        self.Msg_Header_DF = None
        filterButtons_Disabled = not(self.eMailID_List)#disable/enable buttons??
        if self.eMailID_List:
            self.AgeFilter_Result_Label.setText(f"Found {len(self.eMailID_List)} prior to {self.AsOfDt_Edit.text()}")
        self.btn_View_Filtered.setDisabled(filterButtons_Disabled)
        self.btn_View__GroupBy_URL.setDisabled(filterButtons_Disabled)
        self.btn_Delete_Filtered.setDisabled(filterButtons_Disabled)

    def onView_Changed(self):
        #check view id to see which results to show
        if self.fltrView_Id == fltrViewId_msgDetail:
            self.results_Group.setTitle ("View Message Header Details")
            if not (self.Msg_Header_List):
                self.Msg_Header_List = self.mailBox_Get_Msg_Headers_List(self.eMailID_List)
            self._fill_Result_eMailList_(self.Msg_Header_List)
        elif self.fltrView_Id == fltrViewId_byURL:
            self.results_Group.setTitle ("View Domain Message Totals")
            if self.Msg_Header_DF is None:
                self.Msg_Header_DF = self.mailBox_Get_Msg_Headers_DF(self.eMailID_List)
            self._fill_Result_domainList_(self.Msg_GroupBy_URL_List)           


    def onMailBox_Connected(self):
        self.__fill_folderCB__(self.cb_Folder_Names)
        self.statusBar().showMessage(f"{self._currentUser['userID']} - Connected",0)          
        self.LogInBtn.setText('Connected') #change caption on login button        
        #enable/disable buttons
        self.btn_Apply_Filter.setDisabled(False) 
        mailBox.select_folder(self.current_Folder) #default folder
       

    def onMailBox_disConnected(self):
        self.statusBar().showMessage("Select Mail Box and Log In")
        self.LogInBtn.setText('Log In') #change caption on login button        
        self.btn_Apply_Filter.setDisabled(True) 
        self.btn_View_Filtered.setDisabled(True)
        self.btn_Delete_Filtered.setDisabled(True)
    
    def on_current_Folder_changed(self):
        if self.isConnected:
            rspns,emailCnt = mailBox.conn.select(self.current_Folder)  
            self.lbl_Folder_Details.setText(f"{self.current_Folder} has {emailCnt[0].decode('utf-8')} emails")          

    def mailBox_ApplyFilter_ByDt(self, cutOffDate):  
        #apply age filter to selected inbox
        tmp_ResultId_list = mailBox.find_eMails_priorToDt(cutOffDate)
        return tmp_ResultId_list
    
    def mailBox_Get_Msg_Headers_List(self,mgsIDList):
        try:
            QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)
            return mailBox.create_JSON_Msg_Headers(mgsIDList)
        finally:
            QApplication.restoreOverrideCursor()

    def mailBox_Get_Msg_Headers_DF(self,mgsIDList):
        try:            
            QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)
            return mailBox.create_DF_Msg_Headers(mgsIDList)
        finally:
            QApplication.restoreOverrideCursor()        

    def mailBox_Delete_byURL (self, target_url):
        lcl_df = self.Msg_Header_DF
        #filter statement
        filter_statement = lcl_df['url'].str.contains(target_url,regex=True,na=False)
        df_fltrd = lcl_df[filter_statement]
        series_id = df_fltrd.index.tolist()        
        result = mailBox.delete_eMails_ById(series_id)
        show_info_messagebox(f"{len(result)}  emails were deleted")

    def mailBox_Delete_filteredMsg(self,eMailID_List):
        result = mailBox.delete_eMails_ById(eMailID_List)
        show_info_messagebox(f"{len(result)}  emails were deleted")    
                
def get_App_qss():
     # Read the QSS file
    with open("stylesheet.qss", "r") as f:
        _style = f.read()
    return _style  
            
def show_info_messagebox(msg):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)

    # setting message for Message Box
    msgBox.setText(msg)
    
    # setting Message box window title
    msgBox.setWindowTitle("Information MessageBox")
    
    # declaring buttons on Message Box
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    
    # start the app
    retval = msgBox.exec_()

def show_YesNo_messagebox(msg_Question,window_Title):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Question)

    # setting message for Message Box
    msgBox.setText(msg_Question)
    
    # setting Message box window title
    msgBox.setWindowTitle(window_Title)
    msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    
    # start the app
    result = msgBox.exec_()
    return result


         


def main():   
    global mailBox
    mailBox = iMapMailBox()
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(get_App_qss()) 
#    app.setWindowIcon("qt_ui\img\imap_mailbox.png")
    MainWindow = iMapDialog()
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()