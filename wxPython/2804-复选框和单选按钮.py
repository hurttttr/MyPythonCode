import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='复选框和单选按钮', size=(400, 200))
        self.Center()

        panel = wx.Panel(parent=self)  # 内容面板
        self.statictext = wx.StaticText(parent=panel)

        st1 = wx.StaticText(panel, label='你喜欢的编程语言：')
        st2 = wx.StaticText(panel, label='你都性别：')
        st3 = wx.StaticText(panel, label='你喜欢吃的水果：')

        cb1 = wx.CheckBox(panel, 1, 'Python')
        cb2 = wx.CheckBox(panel, 2, 'Java')
        cb3 = wx.CheckBox(panel, 3, 'C++')
        cb2.SetValue(True)  # 选中第2个
        self.Bind(wx.EVT_CHECKBOX, self.cb_click, id=1, id2=3)

        rb1 = wx.RadioButton(panel, 4, '男', style=wx.RB_GROUP)
        rb2 = wx.RadioButton(panel, 5, '女')
        self.Bind(wx.EVT_RADIOBUTTON, self.cb_click, id=1, id2=3)

        rb3 = wx.RadioButton(panel, 6, '苹果', style=wx.RB_GROUP)
        rb4 = wx.RadioButton(panel, 7, '橘子')
        rb5 = wx.RadioButton(panel, 8, '香蕉')
        self.Bind(wx.EVT_RADIOBUTTON, self.rb2_click, id=6, id2=8)

        # 布局
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(cb1, 1, flag=wx.ALL | wx.FIXED_MINSIZE)
        hbox1.Add(cb2, 1, flag=wx.ALL | wx.FIXED_MINSIZE)
        hbox1.Add(cb3, 1, flag=wx.ALL | wx.FIXED_MINSIZE)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(rb1, 1, flag=wx.ALL | wx.FIXED_MINSIZE)
        hbox2.Add(rb2, 1, flag=wx.ALL | wx.FIXED_MINSIZE)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(rb3, 1, flag=wx.ALL | wx.FIXED_MINSIZE)
        hbox3.Add(rb4, 1, flag=wx.ALL | wx.FIXED_MINSIZE)
        hbox3.Add(rb5, 1, flag=wx.ALL | wx.FIXED_MINSIZE)

        fgs = wx.FlexGridSizer(3, 2, 10, 10)
        fgs.AddMany([st1, [hbox1, 1, wx.EXPAND], st2, [
                    hbox2, 1, wx.EXPAND], st3, [hbox3, 1, wx.EXPAND]])
        fgs.AddGrowableCol(0, 1)
        fgs.AddGrowableCol(1, 2)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(fgs, 1, flag=wx.ALL | wx.EXPAND, border=10)
        panel.SetSizer(hbox)

        ico = wx.Icon('dog4.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)

        self.CreateStatusBar()  # 创建状态栏
        self.SetStatusText('准备就绪')

    def cb_click(self, event):
        cb = event.GetEventObject()
        s = '选择{}，状态{}'.format(cb.GetLabel(), event.IsChecked())
        self.SetStatusText(s)

    def rb1_click(self, event):
        rb = event.GetEventObject()
        s = '第一组单选按钮{}被选中'.format(rb.GetLabel())
        self.SetStatusText(s)

    def rb2_click(self, event):
        rb = event.GetEventObject()
        s = '第二组单选按钮{}被选中'.format(rb.GetLabel())
        self.SetStatusText(s)


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()
