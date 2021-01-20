"""Script for determining whether a github repo uses continuous integration"""
import sys
import json
from bs4 import BeautifulSoup as bs
import requests
import lxml

def get_response(page_url):
    """Returns response to html request on page_url"""
    response = requests.get(page_url)
    # print(page_url, response.status_code)
    return response

def which_ci(url):
    """Determines if the github project at the given url uses CI"""
    if "github" not in url:
        return 'not-github'
    response = get_response(url)
    soup = bs(response.content, 'lxml')
    if soup.find('a', title='.circleci'):
        # Is there a folder called .circleci?
        return "circle-ci"
    elif soup.find('span', string='.github/'):
        # GH renders a github actions folder as a <span>
        return "github-actions"
    elif soup.find('a', title='.github'):
        # GH renders a .github folder as an <a>
        return "github-folder"
    elif soup.find('a', title='.travis.yml'):
        # Is there a file called .travis.yml?
        return "travis"
    return False

def main():
    """Main function"""
    json_file = sys.argv[1]
    with open(json_file, 'r') as fp:
        data = json.load(fp)
    print(which_ci(data["repo_url"]))

main()
