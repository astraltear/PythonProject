'''
layout management :Sizer
'''

import wx


class Example(wx.Frame):
    def __init__(self,parent,title):
        super(Example,self).__init__(parent,title=title,size=(300,300))
        
        panel1 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)
        panel2 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)
        
        panel1.SetBackgroundColour("BLUE")
        panel2.SetBackgroundColour("RED")
        
        box = wx.BoxSizer(wx.HORIZONTAL)
        
        box.Add(panel1, 1,wx.EXPAND)
        box.Add(panel2, 2,wx.EXPAND)
        
        self.SetSizer(box)
        self.Center()
        self.Show(show=True)
        

if __name__ =='__main__':
    app = wx.App(False)
    Example(None,'BUTTON test')
    app.MainLoop()        