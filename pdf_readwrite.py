import PyPDF2 as p

with open('F:\\Python\\XL-Word-PDF\\automate_online-materials\\meetingminutes.pdf', 'rb') as file:
    reader = p.PdfFileReader(file)
    # reader.numPages
    page = reader.getPage(0)
    page_text = page.extractText()  # extracts text on page but cannot write using pypdf2
    # print(page_text)
    # page.rotateClockwise(270)
    # To write pages=>writer=>addPage=>
    writer = p.PdfFileWriter()  # Writer object
    writer.addPage(page)  # Add page/text to the end
    with open('writepdf1.pdf', 'wb') as nfile:
        writer.write(nfile)

file.close()
nfile.close()