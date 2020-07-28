import PyPDF2 as p

template = p.PdfFileReader(open('merged_pdf.pdf', 'rb'))
water = p.PdfFileReader(open('pdf3.pdf', 'rb'))
output = p.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(water.getPage(0))
    output.addPage(page)

with open('watermarkedPdf.pdf', 'wb') as file:
    output.write(file)
