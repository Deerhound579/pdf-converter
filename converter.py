from bs4 import BeautifulSoup
import requests
import re
import pdfkit
import os
from PyPDF2 import PdfFileMerger



def little_crawler(url):
    '''
    A function to extract all links to lectures notes on https://www.seas.upenn.edu/~cis194/spring13/
    '''
    page = requests.get(url)
    content = BeautifulSoup(page.text, 'html.parser')
    # All links are in <a href="...">html</a>
    raw_links = content.find_all('a', string='html') 
    links = ['https://www.seas.upenn.edu/~cis194/spring13/' + x['href'] for x in raw_links]
    return links


links = little_crawler('https://www.seas.upenn.edu/~cis194/spring13/lectures.html')

options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
}

# Create pdfs
for index, l in enumerate(links, 1):
   pdfkit.from_url(l, (str(index).zfill(2))+'.pdf', options=options)

# Merge pdfs
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
