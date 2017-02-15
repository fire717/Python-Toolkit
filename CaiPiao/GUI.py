#! /usr/bin/env python
#-*- coding: utf-8 -*-


import wx
import main  

class MyFrame(wx.Frame):
    
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, u'双色球号码随机生成器',
                             size = (300, 300),pos=(600,200))     
        #创建面板
        panel = wx.Panel(self,-1)        
        #在Panel上添加Button
        button = wx.Button(panel, label = u'生成', pos = (100, 90), size = (100, 60))     
        #绑定单击事件
        self.Bind(wx.EVT_BUTTON, self.CreateNumber, button)
        
  

    def CreateNumber(self, event):
        global number 
        numberX=''+str(number[0])+' '+str(number[1])+' '+str(number[2])+' '+str(number[3])+' '+str(number[4])+' '+str(number[5])+' - '+str(number[6])
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.  
        dlg = wx.MessageDialog( self, numberX, "About Sample Editor", wx.OK)  
        dlg.ShowModal() # Show it  
        dlg.Destroy() # finally destroy it when finished.  

number=main.number

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyFrame(parent = None, id = -1)
    frame.Show()
    app.MainLoop()
