import wx
from wx.core import Choice


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='下拉列表', size=(500, 280))
        self.Center()

        panel = wx.Panel(parent=self)  # 内容面板
        self.statictext = wx.StaticText(parent=panel)

        st1 = wx.StaticText(panel, label='你喜欢的编程语言：')
        st2 = wx.StaticText(panel, label='你的性别：')

        lst1 = ['Python', 'Java', 'C++']

        ch1 = wx.ComboBox(panel, -1, value='C++', choices=lst1,
                          style=wx.CB_SORT | wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_COMBOBOX, self.on_combobox, ch1)

        lst2 = ['男', '女']
        ch2 = wx.Choice(panel, -1, choices=lst2)
        ch2.SetSelection(0)
        self.Bind(wx.EVT_CHOICE, self.on_choice, ch2)

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

    def on_combobox(self, event):
        s = '选择 {}'.format(event.GetString())
        self.SetStatusText(s)

    def on_choice(self, event):
        s = '选择 {}'.format(event.GetString())
        self.SetStatusText(s)


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()
