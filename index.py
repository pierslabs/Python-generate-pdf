#importing pdfkit
import pdfkit
import os
import pdfkit

WKHTMLTOPDF_PATH = '/usr/local/bin/wkhtmltopdf'

# options = {
#     'page-size': 'A4',
#     'margin-top': '0.75in',
#     'margin-right': '0.75in',
#     'margin-bottom': '0.75in',
#     'margin-left': '0.75in',
#     'encoding': "UTF-8",
#     'custom-header': [
#         ('Accept-Encoding', 'gzip')
#     ],
#     'cookie': [
#         ('cookie-empty-value', '""')
#         ('cookie-name1', 'cookie-value1'),
#         ('cookie-name2', 'cookie-value2'),
#     ],
#     'no-outline': None
# }
# pdfkit.from_file('file.html', 'file.pdf', options=options)
pdfkit.from_file('plantilla.html', 'Example-pdf.pdf')

