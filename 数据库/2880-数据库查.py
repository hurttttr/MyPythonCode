import pymysql

with pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    database='mydatabase',
    charset='utf8'
) as conn:

    with conn.cursor() as cursor:
        sql = 'select * from student where number >= %s and number <= %s'
        cursor.execute(sql, ('1501', '1509'))
        data = cursor.fetchall()
        for item in data:
            print(item)
        print('共查询到： {} 条数据'.format(cursor.rowcount))
