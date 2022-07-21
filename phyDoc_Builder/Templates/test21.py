# # from bs4 import BeautifulSoup
# from pdfrw import PdfWriter
from string import Template
import pdfkit

f = open("C://Users//User//Desktop//PDB_drf//phyDoc_Builder_Project//phyDoc_Builder//Template//21jul.html", "r")
html_content = f.read()
template = Template(html_content)
# final_html = template.substitute(name_placeholder='Anusha', age_placeholder=21, location_placeholder="rr nagar")
config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files (x86)\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
pdfkit.from_string(template, "D:/anu.pdf", configuration=config)

    
