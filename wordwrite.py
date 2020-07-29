from docx import Document

def getText(filename):
    fullText=[]
    doc= Document(filename)
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

print(getText('F:\\Python\\XL-Word-PDF\\demo.docx'))