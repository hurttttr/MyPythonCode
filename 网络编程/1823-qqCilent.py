# 案列使用TCP连接
# 这是客户端
import socket
import wx

#  定义套接字 s
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 定义窗口类
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, size=(350, 250), title="QQ聊天：客户端")
        self.Center()
        panel = wx.Panel(self)
        self.text = wx.TextCtrl(parent=panel, id=-1, style=wx.TE_MULTILINE, size=(100, 150))
        startbutton = wx.Button(parent=panel, id=1, label="连接服务器")
        self.inputtext = wx.TextCtrl(parent=panel, id=-1)
        button = wx.Button(parent=panel, id=2, label="发送")
        self.Bind(wx.EVT_BUTTON, self.Talk, id=1)
        self.Bind(wx.EVT_BUTTON, self.on_button, id=2)
        box1 = wx.BoxSizer()
        box1.Add(startbutton, 1, flag=wx.ALL | wx.EXPAND, border=10)
        box1.Add(self.inputtext, 1, flag=wx.ALL | wx.EXPAND, border=10)
        box1.Add(button, 1, flag=wx.ALL | wx.EXPAND, border=10)
        mainbox = wx.BoxSizer(wx.VERTICAL)
        mainbox.Add(self.text, flag=wx.EXPAND)
        mainbox.Add(box1, flag=wx.EXPAND)
        panel.SetSizer(mainbox)

    # 连接服务器函数
    def Talk(self, event):
        s.connect(("127.0.0.1", 8888))
        return

    # 发送信息给服务器端
    def on_button(self, event):
        msg = self.inputtext.GetValue()
        s.send(msg.encode())
        self.text.LabelText += "客户端 对 服务器端说：" + msg + "\r\n"

        data = s.recv(1024)
        if len(data) != 0:
            self.text.LabelText += "服务器端 对 客户端说：" + data.decode() + "\r\n"

class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

if __name__=="__main__":
    app=App()
    app.MainLoop()
