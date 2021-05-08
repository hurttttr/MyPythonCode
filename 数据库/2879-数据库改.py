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
        sql = 'update student set name = %s where number = %s'
        data = [
            ('李炎黄', '1501'),
            ('吕萌', '1505'),
            ('石灰', '1509')
        ]
        cursor.executemany(sql, data)
        conn.commit()
except pymysql.DatabaseError:
    conn.rollback()
finally:
    conn.close()
