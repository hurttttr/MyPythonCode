import re
from ftplib import FTP
import os

ftp = FTP()
ftp.connect("10.132.219.5", 6727)
ftp.login()
ftp.encoding = 'GB18030'

ftp.cwd('/PythonExercise/')
local_path = '1/'
for root, dirs, files in os.walk(local_path):
    for filename in files:
        handler = open(os.path.join(local_path, filename), 'rb')
        ftp.storbinary('STOR ' + filename, handler)
quit()
