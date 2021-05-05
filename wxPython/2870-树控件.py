import wx


class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title="树控件", size=(500, 450))
        self.Center()
        swindow = wx.SplitterWindow(parent=self, id=-1)
        left = wx.Panel(parent=swindow)
        right = wx.Panel(parent=swindow)

        # 设置左右布局的分割窗口left和right
        swindow.SplitVertically(left, right, 200)

        # 设置最小窗格大小，左右布局指左边窗口大小
        swindow.SetMinimumPaneSize(80)

        # 创建一棵树
        self.tree = self.CreateTreeCtrl(left)
        self.Bind(wx.EVT_TREE_SEL_CHANGING, self.on_click, self.tree)

        # 为left面板设置一个布局管理器
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        left.SetSizer(vbox1)
        vbox1.Add(self.tree, 1, flag=wx.EXPAND | wx.ALL, border=5)

        # 为right面板设置一个布局管理器
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        right.SetSizer((vbox2))
        self.st = wx.StaticText(right, 2, label='右侧面板')
        vbox2.Add(self.st, 1, flag=wx.EXPAND | wx.ALL, border=5)

    def on_click(self, event):
        item = event.GetItem()
        self.st.SetLabel(self.tree.GetItemText(item))

    def CreateTreeCtrl(self, parent):
        tree = wx.TreeCtrl(parent)

        # 通过wx.ImageList()创建一个图像列表imglist并保存在树中
        imglist = wx.ImageList(16, 16, True, 2)
        imglist.Add(wx.ArtProvider.GetBitmap(
            wx.ART_FOLDER, size=wx.Size(16, 16)))
        imglist.Add(wx.ArtProvider.GetBitmap(
            wx.ART_NORMAL_FILE, size=(16, 16)))
        tree.AssignImageList(imglist)

        # 创建根节点和5个子节点并展开
        root = tree.AddRoot('TreeRoot', image=0)
        item1 = tree.AppendItem(root, 'Item1', 0)
        item2 = tree.AppendItem(root, 'Item2', 0)
        item3 = tree.AppendItem(root, 'Item3', 0)
        item4 = tree.AppendItem(root, 'Item4', 0)
        item5 = tree.AppendItem(root, 'Item5', 0)
        tree.Expand(root)
        tree.SelectItem(root)

        # 给item节点添加5个子节点
        item1 = self.additem(tree, item1)
        item2 = self.additem(tree, item2)
        item3 = self.additem(tree, item3)
        item4 = self.additem(tree, item4)
        item5 = self.additem(tree, item5)

        # 展开Item 1、4
        tree.Expand(item1)
        tree.Expand(item4)

        # 返回树对象
        return tree

    def additem(self, tree, item):
        tree.AppendItem(item, 'Subitem 1', 1)
        tree.AppendItem(item, 'Subitem 2', 1)
        tree.AppendItem(item, 'Subitem 3', 1)
        tree.AppendItem(item, 'Subitem 4', 1)
        tree.AppendItem(item, 'Subitem 5', 1)
        return item


class App(wx.App):

    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print("应用程序退出")
        return 0


if __name__ == '__main__':
    app = App()
    app.MainLoop()
