import datetime
import imaplib
import sys
import os
import re
import pandas as pd
from dotenv import load_dotenv
from imaplib import IMAP4_SSL
#added 11/12/2025 to parse header component directly
import email
from email.parser import HeaderParser
import json

#LOAD LOGIN VARIABLES FROM DOTENV
load_dotenv('env/imap.env')
NETFIRMS_URL = os.environ.get('NETFIRMS_URL', 'default')
NETFIRMS_USERID_FRM = os.environ.get('NETFIRMS_USERID_FRM', 'default')
NETFIRMS_PWD_FRM = os.environ.get('NETFIRMS_PWD_FRM', 'default')

GMAIL_URL = os.environ.get('GMAIL_URL', 'default')
GMAIL_USERID_FRM = os.environ.get('GMAIL_USERID_frm', 'default')
GMAIL_PWD_FRM = os.environ.get('GMAIL_PWD_frm', 'default')

ageLimit = 60

class iMapMailBox():
    '''CLASS is used to connect and perform basic function on IMAP mailbox
    
    User must provide basic connectivity details:
        mailbox URL
        user ID
        user PW
    After connecting, system will select INBOX, then user can search for emails:
        By Date - All prior to CUTOFF Date
        By Sender Domain - return all email ID's for a given domain
            
    '''
    def __init__(self):
        pass
    @property
    def conn(self):
        return self._conn
    @conn.setter
    def conn(self, value):
        self._conn = value

    @property
    def server(self):
        return self._server
    @server.setter
    def server(self, value):
        self._server = value

    @property
    def userID(self):
        return self._userID
    @userID.setter
    def userID(self, value):
        self._userID = value

    @property
    def password(self):
            return self._pwd
    @password.setter
    def password(self, value):
            self._pwd = value

    def createConn(self):
        try:
            self._conn = IMAP4_SSL(self.server)
            return self._conn
        except:
            return False

    def logIn(self):
        try:
            self.conn.login(self.userID, self.password)
            return True
        except:
            print(f'Cannot connect to {self.server} with user id {self.userID} and password {self.password}')
            return False
        
    def close(self):
        self.conn.close()
        self.conn.logout()
        
    def _createQry_BEFORE(self, cutOffDt):
        return  "(BEFORE {0})".format(cutOffDt.strftime("%d-%b-%Y"))
         
    def _createQry_DOMAIN(self, domain):
        return f'(FROM "{domain}")'
    
    def get_Folder_List(self):
        rspns,folder_list = self.conn.list()
        result_list=[]
        for lclFolderNm in folder_list:
            tmpFolderNm = lclFolderNm.decode("utf-8")
            #folder name has structure list
            #(\HasChildren) "." FOLDER
            #SPLIT string
            result_list.append(tmpFolderNm.split('"." ')[-1]) #-1 returns last item in list
        return result_list    

    def select_folder (self, folder_nm):
        typ, detail = self.conn.select(folder_nm)
        return int(detail[0].decode('ASCII'))

    def search_folder(self, qry):
        typ, dtl = self.conn.search(None, qry)
        self.msgArray =dtl[0].decode('ASCII').split(' ')
        return self.msgArray

    def find_eMails_Recent(self):
        qry= '(RECENT)'
        typ, dtl = self.conn.search(None, qry)
        self.msgArray =dtl[0].decode('ASCII').split(' ')
        return len(self.msgArray)

    def find_eMails_priorToDt(self,cutOffDt):
        qry = self._createQry_BEFORE(cutOffDt)
        result = self.search_folder(qry)
        print(f'search for emails {qry} found {len(result)} emails.')
        return result
    
    def find_eMails_byDomain(self,domain):
        qry = self._createQry_DOMAIN(domain)
        print(qry)
        result = self.search_folder(qry)
        print( f'search for emails {qry} found {len(result)} emails.')
        return result
    
     
    def delete_Selected_eMails(self, qry):
        '''Use the supplied IMAP query to select and DELETE emails'''
        try:
            target_list = self.search_folder(qry)#searches for messages            
            return self.delete_eMails_ById(target_list)
        except:
            return False
        
    def delete_eMails_ById(self, idList):
        '''Use the supplied list of email ID's to DELETE emails'''
        try:
            qryList = ','.join(idList)
            self.conn.store(qryList, '+FLAGS', r'(\Deleted)')
            typ , response = self.conn.expunge()
            return response
        except:
            return False    
    
    def __ExtractID__ (self,srcString):
        regEx_id="^(\d+)[^{]+{(\d+)}"
        match = re.search(regEx_id,srcString)
        if match:
            return match.group(1),match.group(2)
        else:
            return False,False    
        
    #reg ex for extracting email===========================
    def __ExtractAddress__ (self,srcString):
        regEx_address="From:([^<]+)<(.+)>"
        match = re.search(regEx_address,srcString)
        if match:
            return match.group(1),match.group(2)
        else:            
            return "",srcString    
        
    def __ExtractDate__ (self,srcString):
        regEx_Dt="Date:(.+)"
        match = re.search(regEx_Dt,srcString)   
        if match:
            dt = match.group(1)        
            dt= dt.strip() 
            try:
                result=datetime.datetime.strptime(dt[0:16],'%a, %d %b %Y')
                return result,srcString
            except ValueError as v:
                return "Date Conversion Error",srcString
        else:
            return "No Date Found",srcString    
        
    def create_JSON_Msg_Headers(self, idList):
        regex_url = r'<(.+)>'
        qry = ",".join(idList)
        typ, dtl = self.conn.fetch(qry, '(BODY.PEEK[HEADER])') #RETRIEVES ALL header fields
        lcl_Header_Parser = HeaderParser() #creates parser object
        result_LIST=[] #blank list
        for raw_Hdr in dtl:
            if type(raw_Hdr) is tuple:
                idList =raw_Hdr[0].decode('UTF-8').split() #take first string, split by spaces
                tmp_Msg_Hdr = lcl_Header_Parser.parsestr(raw_Hdr[1].decode('UTF-8'))
                hdrField_From = tmp_Msg_Hdr['From']
                #trying to extract url from the FROM field using REGEX
                #IF none found, then add full FROM field in URL field
                match = re.search(regex_url,hdrField_From)
                if match:
                    hdrField_url = match.group(1)
                    hdrField_domain = hdrField_url.split("@")[1]
                else:
                    hdrField_url = hdrField_From 
                    hdrField_domain = hdrField_From  
                hdrField_Rcvd_Dt =  tmp_Msg_Hdr['Date']  
                tmp_Hdr={'ID': idList[0],
                        'From':hdrField_From, 
                        'url': hdrField_url,
                        'domain': hdrField_domain,
                        'Rcvd_Date': hdrField_Rcvd_Dt ,
                        'Subject':tmp_Msg_Hdr['Subject'] }
                result_LIST.append(tmp_Hdr)        
        #copy result header into JSON object
        result_JSON_str = json.dumps(result_LIST, indent=4)
        return json.loads(result_JSON_str)   
        
    def create_DF_Msg_Headers(self, idList):
        json_dict =self.create_JSON_Msg_Headers (idList)
        df = pd.DataFrame(json_dict)
        df.set_index('ID',inplace=True)    
        #change received date from string to datetime
        df['Rcvd_Date'] = df['Rcvd_Date'].str.strip()
        df['Rcvd_Date'] = pd.to_datetime(df['Rcvd_Date'].str[:16],
                                         format='%a, %d %b %Y',
                                         errors='ignore')
        df['url']= df['From'].str.extract(r'<(.+)>')
        return df
    
    def create_url_List (self,idList,min_count=5):
        #create dataframe of email header fields
        _df_header = self.create_DF_Msg_Headers(idList)
        #create list of url
        result = _df_header.groupby('url').size().sort_values(ascending=False)
        return result[result >= min_count]



def create_CutOffDt(age):
    # looking for cutoff date
    result = datetime.date.today()
    result = result - datetime.timedelta(age)
    return result



def deleteAgedMsg (serverURL, userID, pwd, age):
    #mail box credentials
    mailBox = iMapMailBox()  # create class
    mailBox.server = serverURL
    mailBox.userID = userID
    mailBox.password = pwd
    if not mailBox.createConn():
         print (f"ERROR - Unable to connect to mailbox {mailBox.server}")
         sys.exit() #exit program   
    if not mailBox.logIn():
         print (f"Unable to  to mailbox {mailBox.server}")
         sys.exit()#exit program
    else:
         print (f"BEFORE DELETE PROCESS - inbox has {mailBox.select_folder('INBOX')} emails")
    cutoffDt = create_CutOffDt(age) #cutoff date is any emails older than 90 day
    print(mailBox.find_eMails_priorToDt(cutoffDt))
    qry = mailBox._createQry_BEFORE(cutoffDt)
    mailBox.delete_Selected_eMails(qry)
    print (f"AFTER DELETE PROCESS inbox has {mailBox.select_folder('INBOX')} emails")
    mailBox.close() #clean up connectionsvt

def deleteAged_ByDomain(serverURL, userID, pwd, age,domain):
    mailBox = iMapMailBox()  # create class
    mailBox.server = serverURL
    mailBox.userID = userID
    mailBox.password = pwd
    cutoffDt = create_CutOffDt(age) #cONVERTS AGE in days to an actual date
    if not mailBox.createConn():
         print (f"ERROR - Unable to connect to mailbox {mailBox.server}")
         sys.exit() #exit program   
    if not mailBox.logIn():
         print (f"Unable to  to mailbox {mailBox.server}")
         sys.exit()#exit program
    mailBox.select_folder('INBOX')     
    #find ALL emails from given domain
    series_eMailID_ALL =   mailBox.find_eMails_byDomain(domain) 
    print(f"PRIOR TO DELETE - {len(series_eMailID_ALL)} emails found from {domain} - ANY AGE.")  
    #create dataframe of aged items
    srch_Result_Aged = mailBox.find_eMails_priorToDt(cutoffDt)
    df_Aged = mailBox.create_DF_Sender_ReceiveDt(srch_Result_Aged)
    #filter aged for domain
    fltr = df_Aged['url'].str.contains(domain,regex=True)
    df_fltrd = df_Aged[fltr] #applys filter to AGED items
    series_emailID = df_fltrd.index.tolist() #convert to list so I can use in IMAP functions
    print(f"{len(series_emailID)} emails found from {domain} that were at least {age} days old.")
    imap_qry = ",".join(series_emailID) #qry passed to delete function
    mailBox.delete_Selected_eMails(imap_qry)
    series_eMailID_ALL =   mailBox.find_eMails_byDomain(domain) 
    print(f"AFTER DELETE - {len(series_eMailID_ALL)} emails found from {domain} - ANY AGE.") 




if __name__ == '__main__':
	''' By Default when module called delete aged emails'''
	deleteAgedMsg(
    	NETFIRMS_URL,
    	NETFIRMS_USERID_FRM,
    	NETFIRMS_PWD_FRM,
    	ageLimit
    	)
