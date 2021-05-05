import wx
from wx.core import Choice, TextCompleter


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='列表', size=(500, 280))
        self.Center()

        panel = wx.Panel(parent=self)  # 内容面板
        self.statictext = wx.StaticText(parent=panel)

        st1 = wx.StaticText(panel, label='选择你喜欢的编程语言：')
        st2 = wx.StaticText(panel, label='选择你喜欢吃的食物：')

        self.lst1 = ['Python', 'Java', 'C++']
        ch1 = wx.ListBox(panel, -1, choices=self.lst1,
                         style=wx.LB_SINGLE | wx.LB_EXTENDED)
        self.Bind(wx.EVT_LISTBOX, self.on_listbox1, ch1)

        self.lst2 = ['苹果', '橘子', '香蕉']
        ch2 = wx.ListBox(panel, -1, choices=self.lst2,
                         style=wx.LB_MULTIPLE)
        self.Bind(wx.EVT_LISTBOX, self.on_listbox2, ch2)

        fgs = wx.FlexGridSizer(4, 2, 10, 10)
        fgs.AddMany([st1, [ch1, 1, wx.ALL | wx.EXPAND],
                     st2, [ch2, 1, wx.ALL | wx.EXPAND]])
        fgs.AddGrowableCol(0, 1)
        fgs.AddGrowableRow(1, 3)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(fgs, flag=wx.ALL | wx.EXPAND, border=10)

        panel.SetSizer(vbox)

        self.CreateStatusBar()
        self.SetStatusText('准备就绪')

    def on_listbox1(self, event):
        lb = event.GetEventObject()
        s = '选择 {}'.format(self.lst1[int(lb.GetSelections()[0])])
        self.SetStatusText(s)

    def on_listbox2(self, event):
        lb = event.GetEventObject()
        tmp = lb.GetSelections()
        res = []
        for x in tmp:
            res.append(self.lst2[int(x)])
        s = '选择 {}'.format(','.join(res))
        self.SetStatusText(s)


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()
