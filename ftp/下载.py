import re
from ftplib import FTP
import os

ftp = FTP()
ftp.connect("10.132.219.5", 6727)
ftp.login()
ftp.encoding = 'GB18030'

path = '/PythonExercise/实验'
pat = 'AC-(\d*)-(.*?)- 题号(\d*).pdf'

sid_list = ['19211835111']

for i in range(1, 8):
    ftp.cwd(path+'%02d' % i)
    lst = ftp.nlst()
    for filename in lst:
        sid, name, tid = re.compile(pat).findall(filename)[0]
        if sid in sid_list:
            handler = open(os.path.join('1/', filename), "wb").write
            ftp.retrbinary('RETR '+filename, handler)
ftp.quit()
