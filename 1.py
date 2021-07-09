import random
from datetime import datetime, timedelta


def create_jieyue():
    book_count = 57
    reader_count = 30
    with open("借阅.txt", 'w', encoding='utf-8') as f:
        for i in range(100):
            book = '00{:02}'.format(random.randint(1, book_count))
            reader = '100{:02}'.format(random.randint(1, reader_count))
            borrow_time = datetime.strptime(
                '2019-04-01', "%Y-%m-%d")+timedelta(days=random.randint(0, 100))
            return_time = borrow_time+timedelta(days=random.randint(3, 10))
            sql_insert = "insert into 借阅表(book_id,reader_id,borrow_date) values('{}','{}','{}')".format(
                book, reader, borrow_time.strftime("%Y-%m-%d"))
            sql_update = "update 借阅表 set return_date='{}' where borrow_date='{}' and book_id='{}'".format(
                return_time.strftime("%Y-%m-%d"), borrow_time.strftime("%Y-%m-%d"), book)
            # print(sql_insert)
            # print(sql_update)
            f.write(sql_insert+'\n')
            f.write(sql_update+'\n')


def create_reader():
    str = [['赵', '钱', '孙', '李', '周', '吴', '郑', '王'],
           ['伟', '昀', '琛', '东', '凡', '玉', '宇', '奇'],
           ['坤', '艳', '志', '新', '轩', '非', '艳', '星']]
    for i in range(30):
        name_length = random.randint(2, 3)
        name = ''
        if name_length == 3:
            name = str[0][random.randint(
                0, 7)]+str[1][random.randint(0, 7)]+str[2][random.randint(0, 7)]
        else:
            name = str[0][random.randint(0, 7)]+str[1][random.randint(0, 7)]
        reader_id = '100{:02}'.format(i+1)
        phone = '132xxxx{}'.format(random.randint(1000, 9999))
        address = '温州大学'
        count = 10
        sql = "insert into 借阅者表 values('{}','{}','{}','{}',{})".format(
            reader_id, name, phone, address, count)
        print(sql)


if __name__ == "__main__":
    # create_reader()
    create_jieyue()
