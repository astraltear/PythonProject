import wx

'''
app = wx.App(False)  
frame = wx.Frame(None, wx.ID_ANY, "Hello World@@@@@")
frame.Show(True)  
app.MainLoop()
'''

class Example(wx.Frame):
    def __init__(self,parent,title):
        super(Example,self).__init__(parent,title=title,size=(300,400))
        
        self.txtA = wx.TextCtrl(self,style=wx.TE_MULTILINE)
        
        self.CreateStatusBar()
        
        menuBar = wx.MenuBar()
        
        menuFile = wx.Menu()

        menuNew = wx.MenuItem(menuFile, wx.ID_NEW,'New','new document')
        menuFile.Append(menuNew)
        
        menuOpen = menuFile.Append(wx.ID_OPEN,'Open', 'open document')
        menuFile.AppendSeparator()
        menuExit = menuFile.Append(wx.ID_EXIT,'Exit', 'exit document')
        
        menuBar.Append(menuFile, 'File')
        
        self.SetMenuBar(menuBar)
        
        #add event listener
        
        self.Bind(wx.EVT_MENU, self.OnNew, menuNew)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        
        
        self.Center()
        self.Show(show=True)
        
    
    def OnNew(self,event):
        self.txtA.SetLabelText('new doc menu seletecd')

    def OnOpen(self,event):
        self.txtA.SetLabelText('open doc menu seletecd')
        
    def OnExit(self,event):
        self.Close(force=True)
        
if __name__ =='__main__':
    app = wx.App(False)
    Example(None,'test')
    app.MainLoop()

        
        