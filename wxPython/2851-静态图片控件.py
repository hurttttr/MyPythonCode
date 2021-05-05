import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='静态图片控件', size=(300, 300))
        self.Center()

        panel = wx.Panel(parent=self)
        img = wx.Image('bird5.gif', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.staticbitmap = wx.StaticBitmap(
            panel, -1, img, size=(120, 90))

        b1 = wx.Button(parent=panel, id=10, label='Button1')
        b2 = wx.Button(parent=panel, id=11, label='Button2')
        self.Bind(wx.EVT_BUTTON, self.on_click, id=10, id2=20)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(b1, 0, wx.EXPAND | wx.BOTTOM, 5)
        vbox.Add(b2, 0, wx.EXPAND | wx.BOTTOM, 5)
        vbox.Add(self.staticbitmap, proportion=2,
                 flag=wx.FIXED_MINSIZE | wx.BOTTOM | wx.CENTER, border=10)

        panel.SetSizer(vbox)

    def on_click(self, event):
        event_id = event.GetId()
        if event_id == 10:
            img = wx.Image('bird4.gif', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        else:
            img = wx.Image('bird3.gif', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.staticbitmap.SetBitmap(img)


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()
