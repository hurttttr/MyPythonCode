import re
import openpyxl
from ftplib import FTP

ftp = FTP()
ftp.connect("10.132.219.5", 6727)
ftp.login()
ftp.encoding = 'GB18030'

wb = openpyxl.Workbook()
del wb['Sheet']

path = '/PythonExercise/实验'
pat = 'AC-(\d*)-(.*?)- 题号(\d*).pdf'

for i in range(1, 8):
    ftp.cwd(path+'%02d' % i)
    lst = ftp.nlst()

    d = {}
    tid_set = set()
    for filename in lst:
        sid, name, tid = re.compile(pat).findall(filename)[0]
        tid_set.add(tid)
        if sid in d:
            d[sid].append(tid)
        else:
            d[sid] = [name, tid]

    sheet = wb.create_sheet('实验'+'%02d' % i)
    tid_lst = sorted(tid_set)
    sheet.append(['学号', '姓名', *tid_lst])
    for k, v in d.items():
        tmp = [k, v[0]]
        for t in tid_lst:
            tmp.append(1 if t in v else 0)
        sheet.append(tmp)

wb.save('实验报告.xlsx')
ftp.quit()
