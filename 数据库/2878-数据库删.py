import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    database='mydatabase',
    charset='utf8'
)

try:
    with conn.cursor() as cursor:
        sql = 'delete from student where number=%s'
        cursor.executemany(sql, ('1501', '1505', '1509'))
        conn.commit()
except pymysql.DatabaseError:
    conn.rollback()
finally:
    conn.close()
