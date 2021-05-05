import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Grid布局', size=(300, 200))
        self.Center()

        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(parent=panel)

        grid = wx.GridSizer(3, 3, hgap=0, vgap=0)
        for i in range(1, 10):
            btn = wx.Button(parent=panel, label=str(i))
            grid.Add(btn, 0, wx.EXPAND)

        panel.SetSizer(grid)


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()
