'''
remote db con with gui
'''

import wx
import wx.xrc
import mysql.connector
from mysql.connector import errorcode

config ={
         'user':'root',
         'password':'root',
         'host':'localhost',
         'database': 'test',
         'port':'3306'
}

# -*- coding: utf-8 -*- 

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"회원관리", pos = wx.DefaultPosition, size = wx.Size( 400,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
#         self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"번호", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.txt_No = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txt_No, 0, wx.ALL, 5 )
        
        self.btnInsert = wx.Button( self.m_panel6, wx.ID_ANY, u"등록", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.btnInsert.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        self.btnInsert.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        
        bSizer2.Add( self.btnInsert, 0, wx.ALL, 5 )
        
        
        self.m_panel6.SetSizer( bSizer2 )
        self.m_panel6.Layout()
        bSizer2.Fit( self.m_panel6 )
        bSizer1.Add( self.m_panel6, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"이름", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        self.txtName = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.txtName, 0, wx.ALL, 5 )
        
        self.btnUpdate = wx.Button( self.m_panel7, wx.ID_ANY, u"수정", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.btnUpdate, 0, wx.ALL, 5 )
        
        self.btnConfirm = wx.Button( self.m_panel7, wx.ID_ANY, u"확인", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.btnConfirm, 0, wx.ALL, 5 )
        
        
        self.m_panel7.SetSizer( bSizer3 )
        self.m_panel7.Layout()
        bSizer3.Fit( self.m_panel7 )
        bSizer1.Add( self.m_panel7, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"전화", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer4.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        self.txtTel = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.txtTel, 0, wx.ALL, 5 )
        
        self.btnDelete = wx.Button( self.m_panel8, wx.ID_ANY, u"삭제", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.btnDelete, 0, wx.ALL, 5 )
        
        
        self.m_panel8.SetSizer( bSizer4 )
        self.m_panel8.Layout()
        bSizer4.Fit( self.m_panel8 )
        bSizer1.Add( self.m_panel8, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        self.lstMem = wx.ListCtrl( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer5.Add( self.lstMem, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel9.SetSizer( bSizer5 )
        self.m_panel9.Layout()
        bSizer5.Fit( self.m_panel9 )
        bSizer1.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"인원수", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer6.Add( self.m_staticText4, 0, wx.ALL, 5 )
        
        self.lblCnt = wx.StaticText( self.m_panel10, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblCnt.Wrap( -1 )
        bSizer6.Add( self.lblCnt, 0, wx.ALL, 5 )
        
        
        self.m_panel10.SetSizer( bSizer6 )
        self.m_panel10.Layout()
        bSizer6.Fit( self.m_panel10 )
        bSizer1.Add( self.m_panel10, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        self.lstMem.InsertColumn(0, 'No', width=50)
        self.lstMem.InsertColumn(1, 'Name', width=200)
        self.lstMem.InsertColumn(2, 'TEL', width=150)
        
        self.btnInsert.id=1
        self.btnUpdate.id=2
        self.btnConfirm.id=3
        self.btnDelete.id =4
    
        
        # Connect Events
        self.btnInsert.Bind( wx.EVT_BUTTON, self.OnBtnClick )
        self.btnUpdate.Bind( wx.EVT_BUTTON, self.OnBtnClick )
        self.btnConfirm.Bind( wx.EVT_BUTTON, self.OnBtnClick )
        self.btnDelete.Bind( wx.EVT_BUTTON, self.OnBtnClick )
        
        self.btnConfirm.Enable(enable=False)
        self.ViewListData()
        
    
    def ViewListData(self):    
        try:
            conn = mysql.connector.connect(**config)
        
            cur = conn.cursor();
            sql_select ="select * from pymem"
            cur.execute(sql_select)
            
            self.lstMem.DeleteAllItems()
            
            count =0
            for data in cur:
                i = self.lstMem.InsertItem(1000,0)
                self.lstMem.SetItem(i,0,str(data[0]))
                self.lstMem.SetItem(i,1,data[1])
                self.lstMem.SetItem(i,2,data[2])
                
                count +=1
            
            self.lblCnt.SetLabel(str(count))
            
        except Exception as err:
            print('reading err!!',err)
        
        finally:
            cur.close()
            conn.close()
        
    
    def MemberInsert(self):
        strNo = self.txt_No.GetValue()
        strName = self.txtName.GetValue()
        strTelNo = self.txtTel.GetValue()
        #print(strNo,strName,strTelNo)
        
        if strNo =='' or strName=='' or strTelNo == '':
            wx.MessageBox('input data','INPUT',wx.OK)
            return
         
        try:
            conn = mysql.connector.connect(**config)
            cur = conn.cursor();
            
            cnt_No = self.SelectData(strNo)
            
            if cnt_No != None:
                wx.MessageBox('exist NO!!!','EXISTS',wx.OK)
                self.txt_No.SetFocus()
                return
            else :
                sql ="insert into pymem values(%s,%s,%s) "
            
                tdata=(strNo,strName,strTelNo)
            
                cur.execute(sql,tdata)
                conn.commit()
            
        except Exception as err:
            print('reading err!!',err)
            conn.rollback()
        
        finally:
            cur.close()
            conn.close()       
    
    def MemberUpdate(self):
        dlg= wx.TextEntryDialog(None,'input No','UPDATE')
        dlg.ShowModal()
        
        if wx.ID_OK:
            upno = dlg.GetValue()
            data = self.SelectData(upno)
            
            if data == None:
                wx.MessageBox(upno+'번은 등록된 자료가 아님 ','알림',wx.OK)
                return
            self.txt_No.SetValue(str(data[0]))
            self.txtName.SetValue(str(data[1]))
            self.txtTel.SetValue(str(data[2]))
            
            self.txt_No.SetEditable(editable=False)
            self.btnConfirm.Enable(enable=True)
            self.btnUpdate.SetLabel("취소")
            self.btnUpdate.id=5 # 취소용으로 전환
            
        else:
            return
        
    
    def MemberUpdateOk(self):
        strNo = self.txt_No.GetValue()
        strName = self.txtName.GetValue()
        strTelNo = self.txtTel.GetValue()
        
        if strNo =='' or strName=='' or strTelNo == '':
            wx.MessageBox('input data','INPUT',wx.OK)
            return
        
        try:
            conn = mysql.connector.connect(**config)
            cur = conn.cursor();
            
            sql ="update pymem set name=%s, junwha=%s where bun=%s"
        
            tdata=(strName,strTelNo,strNo)
        
            cur.execute(sql,tdata)
            conn.commit()
            
            self.txt_No.SetEditable(editable=True)
            self.btnUpdate.SetLabel("수정")
            self.btnUpdate.id=2 # 취소용으로 전환
            self.btnConfirm.Enable(enable=False)
            
        except Exception as err:
            print('reading err!!',err)
            conn.rollback()
        
        finally:
            cur.close()
            conn.close() 
        
    
    def MemberDelete(self):
        dlg= wx.TextEntryDialog(None,'input No','DELETE')
        dlg.ShowModal()
        
        if wx.ID_OK:
            delno = dlg.GetValue()
            data = self.SelectData(delno)
            
            if data == None:
                wx.MessageBox(delno+'번은 등록된 자료가 아님 ','알림',wx.OK)
                return
            
            try:
                conn = mysql.connector.connect(**config)
                cur = conn.cursor();
                
                sql ="delete from pymem where bun=%s"
            
                tdata=(delno,)
            
                cur.execute(sql,tdata)
                conn.commit()
                
            except Exception as err:
                print('reading err!!',err)
                conn.rollback()
            
            finally:
                cur.close()
                conn.close() 
            
        else:
            return
    
    def MemberUpdateCancel(self):
        self.clearInit()
        self.txt_No.SetEditable(editable=True)
        self.btnUpdate.SetLabel("수정")
        self.btnUpdate.id=2 # 원복
        self.btnConfirm.Enable(enable=False)
    
    def clearInit(self):
        self.txt_No.SetValue('')
        self.txtName.SetValue('')
        self.txtTel.SetValue('')
     
    def SelectData(self,no):
        try:
            conn = mysql.connector.connect(**config)
            cur = conn.cursor();
            
            sql="select * from pymem where bun={0}".format(no)
            cur.execute(sql)
            data = cur.fetchone()
            print("SelectData",data)
            return data
            
        except Exception as err:
            print('reading err!!',err)
        
        finally:
            cur.close()
            conn.close()  
           
        
    # Virtual event handlers, overide them in your derived class
    def OnBtnClick( self, event ):
       idLable = event.GetEventObject().id
       #print(idLable)
       
       # insert
       if idLable == 1:
           self.MemberInsert()
           self.ViewListData()
           self.clearInit()
       
       #update
       elif idLable == 2:
           self.MemberUpdate()
           self.ViewListData()
           
       
       #confirm
       elif idLable == 3:
           self.MemberUpdateOk()
           self.ViewListData()
           self.clearInit()
       
       #delete 
       elif idLable == 4:
            self.MemberDelete()
            self.ViewListData()
    
       elif idLable == 5:
           self.MemberUpdateCancel()
           self.ViewListData()
          
    
if __name__ =='__main__'    :
    app = wx.App(False)
    MyFrame1(None).Show(show=True)
    app.MainLoop()     
    


