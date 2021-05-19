import socket
import wx

#  定义套接字 s
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 定义窗口类


class MyFrame(wx.Frame):
    # 初始化这里就是生成界面，然后绑定了按钮事件，其他没了
    def __init__(self):
        super().__init__(parent=None, size=(350, 250), title="圆的面积：客户端")
        self.Center()
        panel = wx.Panel(self)
        self.text = wx.TextCtrl(parent=panel, id=-1,
                                style=wx.TE_MULTILINE, size=(100, 150))
        startbutton = wx.Button(parent=panel, id=1, label="连接服务器")
        self.inputtext = wx.TextCtrl(parent=panel, id=-1)
        # st = wx.StaticBox(parent=panel, id=-1, label="Enter a radius:")
        button = wx.Button(parent=panel, id=2, label="发送")
        self.Bind(wx.EVT_BUTTON, self.Talk, id=1)
        # self.Bind(wx.EVT_TEXT_ENTER, self.on_button, id=2)
        self.Bind(wx.EVT_BUTTON, self.on_button, id=2)
        box1 = wx.BoxSizer()
        box1.Add(startbutton, 1, flag=wx.ALL | wx.EXPAND, border=10)
        # box1.Add(st, 1, flag=wx.ALL | wx.EXPAND, border=10)
        box1.Add(self.inputtext, 1, flag=wx.ALL | wx.EXPAND, border=10)
        box1.Add(button, 1, flag=wx.ALL | wx.EXPAND, border=10)
        mainbox = wx.BoxSizer(wx.VERTICAL)
        mainbox.Add(self.text, flag=wx.EXPAND)
        mainbox.Add(box1, flag=wx.EXPAND)
        panel.SetSizer(mainbox)

    # 连接服务器函数
    def Talk(self, event):
        s.connect(("127.0.0.1", 8888))
        print('连接成功')
        return

    # 发送信息给服务器端
    def on_button(self, event):
        msg = self.inputtext.GetValue()
        s.send(msg.encode())
        msg = float(msg)
        self.text.LabelText += "Radius is：{:.1f}\r\n".format(msg)

        data = s.recv(1024)
        if data:
            self.text.LabelText += "Area received from the server:{}\r\n".format(float(data.decode()))


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == "__main__":
    app = App()
    app.MainLoop()
