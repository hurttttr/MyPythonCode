import PyPDF2

pdfWriter = PyPDF2.PdfFileWriter()      # 用于写pdf
pdfReader = PyPDF2.PdfFileReader('meetingminutes.pdf')   # 读取pdf内容


def add_watermark(water_file, page_pdf):
    pdfReader = PyPDF2.PdfFileReader(water_file)
    page_pdf.mergePage(pdfReader.getPage(0))
    return page_pdf


page_pdf = add_watermark('watermark.pdf', pdfReader.getPage(0))
pdfWriter.addPage(page_pdf)

for page in range(1, pdfReader.numPages):  # 遍历，跳过第一页
    pageObj = pdfReader.getPage(page)
    pdfWriter.addPage(pageObj)

with open('meetingminutes_watermark.pdf', 'wb') as target_file:
    pdfWriter.write(target_file)
