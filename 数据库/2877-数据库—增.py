# import pymssql

# conn = pymssql.connect(
#     host="localhost",
#     post='3306',
#     user='root',
#     passwd='123456',
#     db='mydatabase',
#     charset='utf8'
# )

# try:
#     with conn.cursor() as cursor:
#         sql = 'insert into student(number,name,sex,math,english,computer) values(%s,%s,%s,%s,%s,%s)'
#         data = [('1501', '炎黄', 'M', 78.5, 70.0, 100.0),
#                 ('1505', '吕萌萌', 'M', 100.0, 90.0, 95.0),
#                 ('1509', '石耀举', 'F', 60.5, 90.0, 70.0), ]
#         cursor.executemany(sql, data)
#         conn.commit()
# except pymssql.DatabaseError:
#     conn.rollback()
# finally:
#     conn.close()
print('1')
