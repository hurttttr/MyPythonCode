import wx
from wx.core import Sleep


class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title='分隔窗口', size=(350, 180))
        self.Center()

        splitter = wx.SplitterWindow(self, -1)
        self.left = wx.Panel(splitter)
        self.right = wx.Panel(splitter)
        splitter.SplitVertically(self.left, self.right, 100)
        splitter.SetMinimumPaneSize(80)

        # 左边窗口
        lst = ['苹果', '橘子', '香蕉']
        lb = wx.ListBox(self.left, -1, choices=lst, style=wx.LB_SINGLE)
        self.Bind(wx.EVT_LISTBOX, self.on_listBox, lb)

        # 右边窗口
        self.statictext = wx.StaticText(self.right, -1, '右侧面板')

        # 布局
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox1.Add(lb, 1, flag=wx.ALL | wx.EXPAND, border=5)

        vbox2 = wx.BoxSizer(wx.VERTICAL)
        vbox2.Add(self.statictext, 1, flag=wx.ALL | wx.EXPAND, border=5)

        self.left.SetSizer(vbox1)
        self.right.SetSizer(vbox2)

    def on_listBox(self, event):
        t = event.GetString()
        if t == '苹果':
            s = '选择 苹果'
        elif t == '橘子':
            s = '选择 橘子'
        elif t == '香蕉':
            s = '选择 香蕉'
        self.statictext.SetLabelText(s)


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()
