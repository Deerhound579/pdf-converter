import pdfkit
import os
from PyPDF2 import PdfFileMerger
from little_crawler import link_crawler


options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
}

links = link_crawler('https://www.seas.upenn.edu/~cis194/spring13/lectures.html')

# Create pdfs
for index, l in enumerate(links, 1):
   pdfkit.from_url(l, (str(index).zfill(2))+'.pdf', options=options)

Merge pdfs
files_dir = os.getcwd()

pdfs = list()
# Add in main text file.
file_name = [f for f in os.listdir(files_dir) if '.pdf' in f]
pdfs.extend(file_name)

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'), import_bookmarks=False)

with open('CIS194_Haskell.pdf', 'wb') as fout:
    merger.write(fout)

# for index, l in enumerate(links, 1):
#    pdfkit.from_url(l, (str(index).zfill(2))+'.pdf', options=options)

# Failed. Only blank pages are generated.
# links = link_crawler(
#     'https://www.cs.cornell.edu/courses/cs3110/2019sp/textbook/',
#     'https://www.cs.cornell.edu/courses/cs3110/2019sp/textbook/')


# for x in links[-6:]:
#     links.remove(x)

# del links[-1]
