from docx import Document

try:
    d = Document('F:\\Python\\XL-Word-PDF\\demo.docx')

    r = d.paragraphs[1]
    # print(r.runs[2].text) #prints the text of style of run[2]
    # print(r.runs[2]) #prints the style of run[2]
    # r.runs[4].text = ' italic and underlined. '  # changes style of run[0] to I & B
    r.style = 'Title'
    d.save('F:\\Python\\XL-Word-PDF\\demo3.docx')
except Exception as err:
    print("error occured", err)
