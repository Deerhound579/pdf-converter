from bs4 import BeautifulSoup
import requests

def link_crawler(url, root_name, attr=''):
    '''
    A function to extract all links from a URL.
    Add root name to each link extracted from 'href=', so they can be fed into the PDF converter later.
    '''
    page = requests.get(url)
    content = BeautifulSoup(page.text, 'html.parser')
    # All links are in <a href="...">html</a>
    # raw_links = content.find_all('a', string='html')
    raw_links = content.find_all('a')
    links = [ root_name + x['href'] for x in raw_links ]
    return links


# A filter trying to delete all invalid links and generate the corresponding links for the remaining.
# But I figured out using numbers as file names is better for merging them.

# def is_legal(x):
#     try:
#         return x['href'].split('/')[1].split('.')[0]
#     except:
#         raw_links.remove(x)

