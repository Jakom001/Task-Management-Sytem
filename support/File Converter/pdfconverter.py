from fpdf import FPDF
# creating a pdf variable to save the FPDF() class
pdf = FPDF()
pdf.add_page()
# set font style and size for pdf
pdf.set_font('Arial', size= 16)
# creating cell
pdf.cell(200, 10, txt = "Trial to generate a pdf file.", ln=2, align='C')
# save file with extension
pdf.output('Attempt.pdf')