import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_cdc_supplier_page_list(index_page_url: str) -> [str]:
        
    getpage= requests.get(index_page_url)

    getpage_soup= BeautifulSoup(getpage.text, 'html.parser')

    # Get the 

    links_div = getpage_soup.findAll(
        'div',
        attrs = { 'class': "card bt-3 bb-3 bt-secondary bb-secondary mb-3"},
    )

    all_links= links_div[1].findAll(
        'a', 
        attrs = {'class' : '', 'id' : ''},
        )

    urllist = []

    for link in all_links:
        href = link.get('href')
        url = urljoin(index_page_url, href)
        if url not in urllist:
            urllist.append(url)

    return urllist
    
# indexpage_url = 'https://www.cdc.gov/niosh/npptl/topics/respirators/disp_part/N95list1.html'

# print(get_cdc_supplier_page_list(indexpage_url))
