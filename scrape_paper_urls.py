from bs4 import BeautifulSoup as bs
import requests
import lxml

INDEX_URL = "https://joss.theoj.org/papers/published?page="
PAPER_URL_LIST = "data/paper_url_list.txt"

def get_response(page_url):
    """Returns response to html request on page_url"""
    response = requests.get(page_url)
    print(page_url, response.status_code)
    return response

def get_last_page_no():
    """Returns final page in JOSS index"""
    page_url = INDEX_URL + str(1)
    response = get_response(page_url)
    soup = bs(response.content, 'lxml')
    last = soup.find_all('link', rel='last')[0].get('href')[-3:]
    return int(last)

def main():
    """Main function"""
    paper_urls = []
    last_page_no = get_last_page_no()
    for i in range(1, last_page_no+1):
        page_url = INDEX_URL + str(i)
        response = get_response(page_url)
        soup = bs(response.content, 'lxml')
        paper_entries = soup.find_all("entry")
        paper_urls += [entry.link.get('href') for entry in paper_entries]

    with open(PAPER_URL_LIST, 'w') as fp:
        for item in paper_urls:
            fp.write("%s\n" % item)

main()
