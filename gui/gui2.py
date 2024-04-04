'''
gui2

'''

import wx
from cProfile import label

class Example(wx.Frame):
    def __init__(self,parent,title):
        super(Example,self).__init__(parent,title=title,size=(300,300))
        
        self.InitUi()
        
        self.Center()
        self.Show(show=True)
    
    def InitUi(self):
        panel = wx.Panel(self)
        
        wx.StaticText(panel,label='id : ',pos=(5,5))
        wx.StaticText(panel,label='pw : ',pos=(5,40))
        
        self.txt1 =  wx.TextCtrl(panel, pos=(30,5),size=(200,-1))
        self.txt2 =  wx.TextCtrl(panel, pos=(30,40),size=(200,-1))
        
        btn1 = wx.Button(panel,label="Normal", pos=(5,100))
        btn2 = wx.ToggleButton(panel,label="Toggle", pos=(100,100))
        btn3 = wx.Button(panel,label="Exit", pos=(200,100),size=(50,-1))
        
        '''
        btn1.Bind(wx.EVT_BUTTON , self.OnClick1)
        btn2.Bind(wx.EVT_TOGGLEBUTTON , self.OnClick2)
        btn3.Bind(wx.EVT_BUTTON , self.OnClick3)
        '''
        
        btn1.id = 1; btn2.id = 2; btn3.id = 3;
        
        btn1.Bind(wx.EVT_BUTTON , self.OnClickMethd)
        btn2.Bind(wx.EVT_TOGGLEBUTTON , self.OnClickMethd)
        btn3.Bind(wx.EVT_BUTTON , self.OnClickMethd)
        
    
    def OnClickMethd(self,event):
        if event.GetEventObject().id == 1 :
            self.txt1.SetLabelText('first button')
        
        elif event.GetEventObject().id == 2 :
            self.txt1.SetLabelText('second button')
        
        elif event.GetEventObject().id == 3 :
            self.Close(force=True)
        
    def OnClick1(self,event):
        dlg = wx.MessageDialog(self,'MessageBox','Box',wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    
    def OnClick2(self,event):
        #print(event.GetEventObject().GetValue())
        if event.GetEventObject().GetValue() :
            self.SetTitle('Hello!!!')
        else:
            self.SetTitle('nice to meet you!!')
     
    def OnClick3(self,event):
        self.Close(force=True) 

if __name__ =='__main__':
    app = wx.App(False)
    Example(None,'BUTTON test')
    app.MainLoop()
            