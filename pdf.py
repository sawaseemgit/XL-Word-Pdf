import PyPDF2 as p

with open('pdf1.pdf', 'rb') as file:
    reader = p.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateClockwise(270)
    writer = p.PdfFileWriter()
    writer.addPage(page)
    with open('tiltpdf1.pdf', 'wb') as nfile:
        writer.write(nfile)
