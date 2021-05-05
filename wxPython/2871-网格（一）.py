import wx
import wx.grid

column_names = ['书籍编号', '书籍名称', '作者', '出版社', '出版日期', '库存数量']
data = [['0036', '高等数学', '李牧', '人民邮电出版社', '20000812', '1'],
        ['0004', 'FLASH精选', '刘杨', '中国纺织出版社', '19990312', '2'],
        ['0026', '软件工程', '牛田', '经济科学出版社', '20000328', '3'],
        ['0015', '人工智能', '周末', '机械农业出版社', '19991223', '4'], ]


class MyGridTable(wx.grid.GridTableBase):
    def __init__(self):
        super(MyGridTable, self).__init__()
        self.colLabels = column_names
        self.oddAttr = wx.grid.GridCellAttr()  # 获取表格属性,一会为奇数行设置属性
        self.oddAttr.SetBackgroundColour("#3299CC")
        self.evenAttr = wx.grid.GridCellAttr()  # 获取表格属性，一会为偶数行设置属性
        self.evenAttr.SetBackgroundColour("#238E6B")

    def GetAttr(self, row, col, kind):
        # 对奇偶行进行过滤
        attr = [self.evenAttr, self.oddAttr][row %
                                             2]  # 对这行每个单元格获取其行，符合标准，设置相应属性
        attr.IncRef()  # 注意这里需要增加引用计数
        return attr

    def GetNumberRows(self):
        return len(data)

    def GetNumberCols(self):
        return len(column_names)

    def GetValue(self, row, col):
        return data[row][col]

    def GetColLabelValue(self, col):  # 返回列标题
        return self.colLabels[col]


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='网格控件', size=(800, 250))
        self.Center()

        self.grid = self.CreateGrid(self)
        self.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK,
                  self.on_selectrow, self.grid)
        self.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.on_selectrow)

        ico = wx.Icon('dog4.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)

    def CreateGrid(slef, parent):
        panel = wx.Panel(parent)
        grid = wx.grid.Grid(panel)  # 创建网格
        table = MyGridTable()  # 创建表格
        grid.SetTable(table, True)
        grid.AutoSize()  # 设置自动化调整行列
        font1 = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                        wx.FONTWEIGHT_NORMAL, faceName='微软雅黑')
        font2 = wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD)
        grid.SetLabelFont(font1)  # 标题字体
        grid.SetDefaultCellFont(font2)  # 单元格字体

        # 设置网格行高
        rowsizes = wx.grid.GridSizesInfo(30, [])
        grid.SetRowSizes(rowsizes)
        # 设置网格列宽
        colsizes = wx.grid.GridSizesInfo(0, [100, 120, 50, 150, 120, 120])
        grid.SetColSizes(colsizes)

        # 设置居中对齐
        grid.SetDefaultCellAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # 设置背景色
        grid.SetDefaultCellBackgroundColour('#EEE9E9')

        box = wx.BoxSizer()
        box.Add(grid, 1, flag=wx.ALL | wx.EXPAND, border=5)
        panel.SetSizer(box)
        return panel

    def on_selectrow(self, event):
        row = event.GetRow()
        col = event.GetCol()
        print('row:{0} col:{1}'.format(row, col))
        if row == -1:
            print(data[len(data)-1])
        else:
            print(data[row])
        event.Skip()


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()
