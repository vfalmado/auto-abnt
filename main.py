from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt

document = Document()

name = input('Insira o nome que quer no arquivo: ')
text = input('Insira o texto do seu trabalho: ')

paragraph = document.add_paragraph(texto)
paragraph.style = document.styles.add_style('ABNT', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.name = 'Arial'
font.size = Pt(12)

document.save(name + ".docx")