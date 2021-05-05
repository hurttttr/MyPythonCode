import wx
from wx.core import Panel


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Grid布局', size=(400, 300))
        self.Center()

        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(parent=panel)

        flex = wx.FlexGridSizer(3, 2, 10, 10)

        statictext1 = wx.StaticText(parent=panel, label='标题')
        statictext2 = wx.StaticText(parent=panel, label='作者')
        statictext3 = wx.StaticText(parent=panel, label='内容')

        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel)
        tc3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

        flex.AddMany([(statictext1), (tc1, 1, wx.EXPAND), (statictext2),
                      (tc2, 1, wx.EXPAND), (statictext3), (tc3, 1, wx.EXPAND)])
        flex.AddGrowableRow(2, 1)
        flex.AddGrowableCol(1, 1)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(flex, proportion=2, flag=wx.ALL | wx.EXPAND, border=15)

        panel.SetSizer(hbox)


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()
