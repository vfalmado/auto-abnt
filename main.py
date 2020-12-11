from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt, Cm

document = Document()
sections = document.sections
for section in sections:
  section.top_margin = Cm(3)
  section.right_margin = Cm(2)
  section.bottom_margin = Cm(2)
  section.left_margin = Cm(3)

name = input('Insira o nome que quer no arquivo: ')
text = input('Insira o texto do seu trabalho: ')

paragraph = document.add_paragraph(text)
paragraph.style = document.styles.add_style('ABNT', WD_STYLE_TYPE.PARAGRAPH)

font = paragraph.style.font
font.name = 'Arial'
font.size = Pt(12)

spacing = paragraph.paragraph_format
spacing.space_before = Pt(0)
spacing.space_after = Pt(0)

document.save(name + ".docx")