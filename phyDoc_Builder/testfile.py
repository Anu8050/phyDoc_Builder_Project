# # from bs4 import BeautifulSoup
# from pdfrw import PdfWriter
import cgitb 
from string import Template
import pdfkit
# C://Users//User//Desktop//PDB_drf//phyDoc_Builder_Project//phyDoc_Builder//Template//21jul.html
f = open("C://Users//User//Desktop//PDB_drf//phyDoc_Builder_Project//phyDoc_Builder//Template//21jul.html", "r")

html_content = f.read()

template = Template(html_content)
final_html = template.substitute(name_placeholder='Anusha', age_placeholder=21, location_placeholder="rr nagar")


config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files (x86)\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

# pw.write(f"rajesh.pdf",final_html)
pdfkit.from_string(final_html, "D:/anu.pdf", configuration=config)
# for line in BeautifulSoup(final_html).get_text().split("\n"):
#     pw.write(line)
    
