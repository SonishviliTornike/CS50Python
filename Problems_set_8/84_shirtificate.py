from fpdf import FPDF
from PIL import Image

name = input("Name: ")

pdf = FPDF('P', 'mm', (210, 297) )

pdf.add_page(format='A4')

pdf.image("shirtificate.png", x=0, y=60)

pdf.set_font("Helvetica", 'B', 35)
pdf.cell(200, 50, text='CS50 Shirtificate', align="C")

pdf.set_font("Helvetica", 'B', 28)
pdf.cell(-200, 250, text=name, align='C')


pdf.output("shirtificate.pdf")