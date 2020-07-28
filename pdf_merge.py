import PyPDF2, os

files = []
file_path = 'F:\Python\PDF'

for f in os.listdir(file_path):
    if '.pdf' in f:
        files.append(f)
print(files)


def pdf_merger(inp):
    merger = PyPDF2.PdfFileMerger()
    for pdf in inp:
        print(pdf)
        merger.append(pdf)
    merger.write('merged_pdf.pdf')


pdf_merger(files)
