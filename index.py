from PyPDF2 import PdfFileWriter,PdfFileReader
import getpass

pdfwrite=PdfFileWriter()
pdf=PdfFileReader("index.pdf")

for page_num in range(pdf.numPages):
	pdfwrite.addPage(pdf.getPage(page_num))

passw=getpass.getpass(prompt='introduce password: ')
pdfwrite.encrypt(passw)

with open('ho.pdf','wb') as f:
	pdfwrite.write(f)