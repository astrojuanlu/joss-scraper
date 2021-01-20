# JOSS CI Coverage

This is a project on discovering the number of papers submitted to JOSS which have some kind of CI set up.

Using BeautifulSoup to scrape the [JOSS index](https://joss.theoj.org/papers?page=1) and produce a set of urls, one for each paper in the journal.

Turns out only the ID on the end of the url is unique so we can use this as an ID for e.g. make:

`cat paper_url_list.txt | sed 's/"//g' | sed 's/, /\n/g' | awk -F. '{print $5}' > id_list.txt`

Discovered the $* automatic variable in make! Fills in the '%' match from the target.
