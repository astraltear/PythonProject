'''
Created on 2015. 11. 21.

@author: user
'''
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"미니 계산기", pos = wx.DefaultPosition, size = wx.Size( 300,280 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
#         self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"숫자1", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.txtSu1 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtSu1, 0, wx.ALL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"숫자2", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        self.txtSu2 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.txtSu2, 0, wx.ALL, 5 )
        
        
        self.m_panel2.SetSizer( bSizer3 )
        self.m_panel2.Layout()
        bSizer3.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        radioData=['+','-','*','/']
        m_radioBox1Choices = [ u"Radio Button" ]
#         self.m_radioBox1 = wx.RadioBox( self.m_panel3, wx.ID_ANY, u"연산자선택", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS )
#         self.m_radioBox1 = wx.RadioBox( self.m_panel3, wx.ID_ANY, u"연산자선택", wx.DefaultPosition, wx.DefaultSize, radioData, 1, wx.RA_SPECIFY_COLS )
        self.m_radioBox1 = wx.RadioBox( self.m_panel3, pos=(200,200), choices=radioData)
#         self.m_radioBox1 = wx.RadioBox( self.m_panel3, wx.ID_ANY, u"연산자선택", wx.DefaultPosition,(200,200), radioData, 1, wx.RA_SPECIFY_COLS )
        self.m_radioBox1.SetSelection( 0 )
        bSizer4.Add( self.m_radioBox1, 1, wx.ALL, 5 )
        
        
        self.m_panel3.SetSizer( bSizer4 )
        self.m_panel3.Layout()
        bSizer4.Fit( self.m_panel3 )
        bSizer1.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"결과", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer5.Add( self.m_staticText5, 0, wx.ALL, 5 )
        
        self.staResult = wx.StaticText( self.m_panel4, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staResult.Wrap( -1 )
        bSizer5.Add( self.staResult, 0, wx.ALL, 5 )
        
        
        self.m_panel4.SetSizer( bSizer5 )
        self.m_panel4.Layout()
        bSizer5.Fit( self.m_panel4 )
        bSizer1.Add( self.m_panel4, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.btnCalc = wx.Button( self.m_panel5, 1, u"계산", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.btnCalc, 0, wx.ALL, 5 )
        
        self.btnClear = wx.Button( self.m_panel5, 2, u"초기화", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.btnClear, 0, wx.ALL, 5 )
        
        self.btnExit = wx.Button( self.m_panel5, 3, u"종료", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.btnExit, 0, wx.ALL, 5 )
        
        
        self.m_panel5.SetSizer( bSizer6 )
        self.m_panel5.Layout()
        bSizer6.Fit( self.m_panel5 )
        bSizer1.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        
        self.btnCalc.id=1
        self.btnClear.id=2
        self.btnExit.id=3
        
        self.btnCalc.Bind( wx.EVT_BUTTON, self.OnClick )
        self.btnClear.Bind( wx.EVT_BUTTON, self.OnClick )
        self.btnExit.Bind( wx.EVT_BUTTON, self.OnClick )
    
    
    # Virtual event handlers, overide them in your derived class
    def OnClick( self, event ):
        idLable = event.GetEventObject().id
        print(event.GetEventObject())
        
        if idLable == 1:
            op = self.m_radioBox1.GetStringSelection()
            print('op: ',op)
             
            data1 = self.txtSu1.GetValue()
            data2 = self.txtSu2.GetValue()
            print(data1,data2)
             
            if data1 == '' or data2 == '':
                wx.MessageBox('input value !!','input Value',wx.OK)
                return  
                 
            value1 = int(data1)
            value2 = int(data2)
            result = 0
                 
            if op == '+':
                 result = value1+value2
            elif op =='-':
                 result = value1-value2
            elif op =='*':
                 result = value1*value2
            elif op =='/':
                if value2 ==0:
                    wx.MessageBox(' not allow zero divide','error',wx.OK)
                    return   
                result = value1/value2
            
            self.staResult.SetLabel(str(result))
                 
        if idLable == 2:
            self.txtSu1.SetLabel('')
            self.txtSu2.SetLabel('')
            self.m_radioBox1.SetSelection(0)
            self.staResult.SetLabel('0')
            self.txtSu1.SetFocus()
             
        elif idLable == 3:
            dlg = wx.MessageDialog(self, '종료할까요',"종료",wx.YES_NO)
            res = dlg.ShowModal()
            if res == wx.ID_YES:
                self.Close(force=True)
                dlg.Destroy()
        
if __name__ =='__main__'    :
    app = wx.App(False)
    MyFrame1(None).Show(show=True)
    app.MainLoop()     
