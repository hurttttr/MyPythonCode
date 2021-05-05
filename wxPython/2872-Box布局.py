import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Box布局', size=(300, 200))
        self.Center()

        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(parent=panel, label='Hello')

        b1 = wx.Button(parent=panel, id=10, label='Button1')
        b2 = wx.Button(parent=panel, id=11, label='Button2')
        self.Bind(wx.EVT_BUTTON, self.on_click, id=10, id2=20)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(b1, 0, wx.EXPAND | wx.BOTTOM, 5)
        hbox.Add(b2, 0, wx.EXPAND | wx.BOTTOM, 5)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.statictext, proportion=2,
                 flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER, border=10)
        vbox.Add(hbox, proportion=1, flag=wx.CENTER)

        panel.SetSizer(vbox)

    def on_click(self, event):
        event_id = event.GetId()
        if event_id == 10:
            self.statictext.SetLabelText('Button1单击')
        else:
            self.statictext.SetLabelText('Button2单击')


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()
