import PyPDF2

pdfFileObj = open ('Cover letter_Divya_Karippath.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfWriter = PyPDF2.PdfFileWriter()

for page in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(page))
pdfWriter.encrypt('pass1234')
resultPdf = open('encryptedfile.pdf','wb')
pdfWriter.write(resultPdf)
resultPdf.close()





