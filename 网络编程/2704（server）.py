import socket
import wx
import math

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 定义窗口类


class MyFrame(wx.Frame):
    # 初始化这里就是生成界面，然后绑定了按钮事件，其他没了
    def __init__(self):
        super().__init__(parent=None, size=(350, 250), title="圆的面积")
        self.Center()
        panel = wx.Panel(self)
        self.text = wx.TextCtrl(parent=panel, id=-1,
                                style=wx.TE_MULTILINE, size=(100, 150))
        startbutton = wx.Button(parent=panel, id=1, label="开启服务器")
        # 绑定按钮事件
        self.Bind(wx.EVT_BUTTON, self.Talk, id=1)
        box1 = wx.BoxSizer()
        box1.Add(startbutton, 1, flag=wx.ALL | wx.EXPAND, border=10)
        mainbox = wx.BoxSizer(wx.VERTICAL)
        mainbox.Add(self.text, flag=wx.EXPAND)
        mainbox.Add(box1, flag=wx.EXPAND)
        panel.SetSizer(mainbox)

    # 开启服务器端函数
    def Talk(self, event):
        s.bind(("127.0.0.1", 8888))
        s.listen(5)
        print("服务器启动·····")
        self.conn,self.addess=s.accept()
        data = self.conn.recv(1024)
        if data:
            r = float(data.decode())
            self.text.LabelText += "Radius received from client: {}\r\n".format(
                r)
            area = r*r*math.pi
            self.text.LabelText += "Area is: {}\r\n".format(area)
            self.conn.send(str(area).encode())


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        s.close()  # 关闭socket对象
        return 0


# 进入main函数运行：循环
if __name__ == "__main__":
    app = App()
    app.MainLoop()
