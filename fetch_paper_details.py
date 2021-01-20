"""Script for extracting metadata about a given paper on JOSS"""
import sys
import json
from bs4 import BeautifulSoup as bs
import requests
import lxml
from dateutil.parser import parse

def get_response(page_url):
    """Returns response to html request on page_url"""
    response = requests.get(page_url)
    # print(page_url, response.status_code)
    return response

def main():
    """Main function"""
    url = sys.argv[1]
    response = get_response(url)
    soup = bs(response.content, 'lxml')

    # find meta block
    meta = soup.find('div', class_='paper-meta')

    # extract title
    title = meta.h1.string
    # print(title)

    # extract submission and publish dates
    date_spans = meta.find_all('span', class_='small')
    date_strings = [
        parse(" ".join(span.string.split()[1:]))
        for span in date_spans
    ]
    # print(date_strings)

    # extract language tags
    lang_spans = meta.find_all('span', class_='badge-lang')
    lang_tags = [span.string for span in lang_spans]
    # print(lang_tags)

    # Find sidebar
    sidebar = soup.find('div', class_='paper-sidebar')
    # print(sidebar)

    # Extract field tags
    tag_spans = sidebar.find_all('span', class_='badge-lang')
    field_tags = [span.string for span in tag_spans]
    # print(field_tags)

    # Extract software repo url
    repo_url = soup.find('a', class_='paper-btn').get('href')
    # print(repo_url)

    data = {
        "title": title,
        "submission_date": str(date_strings[0]),
        "publish_date": str(date_strings[1]),
        "lang_tags": lang_tags,
        "field_tags": field_tags,
        "repo_url": repo_url
    }

    print(json.dumps(data))

main()
