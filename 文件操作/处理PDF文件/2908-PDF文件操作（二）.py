import PyPDF2
import os

pdfWriter = PyPDF2.PdfFileWriter()   # 用于写pdf


pdfFiles = []
#找到当前目录下所有的pdf
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key = lambda x:x.lower())
print(pdfFiles)

#打开pdf
for filename in pdfFiles:
    pdfReader = PyPDF2.PdfFileReader(filename)
    for page in range(1, pdfReader.numPages):#遍历，跳过第一页
        pageObj = pdfReader.getPage(page)
        pdfWriter.addPage(pageObj)

with open('sum.pdf','wb') as f:
    pdfWriter.write(f)
