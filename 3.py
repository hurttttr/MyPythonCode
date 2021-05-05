import pymssql

conn = pymssql.connect(host='localhost',
                       port='1433', user='sa', password='123456', database='HRMS')
# host填写数据库名称（本地的可以使用计算机名，127.0.0.1，localhost,网络的填写ip）
# port填写端口

# 查看连接是否成功
cursor = conn.cursor()
sql = 'select * from dbo.tb_Login'
cursor.execute(sql)
# 用一个rs变量获取数据
rs = cursor.fetchall()
conn.close()

print(rs)
