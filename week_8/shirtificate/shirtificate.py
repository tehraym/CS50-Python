from fpdf import FPDF
import sys

def main():
    name = input("Please input your name: ")
    pdf = FPDF(orientation = "portrait", format = "A4")
    pdf.add_page()
    pdf.set_font("Times", size = 40)
    pdf.set_font(style = "B")
    pdf.text(55,40,text = "CS50 Shirtificate")
    pdf.image("shirtificate.png", x = 10, y = 60, w=pdf.epw/1)
    pdf.set_text_color(225, 225, 225)
    pdf.set_font("Times", size = 25)
    pdf.cell(0, 240, text = f"{name} took CS50", align = 'C')
    pdf.output("shirtificate.pdf")
    sys.exit()

if __name__ == "__main__":
    main()
