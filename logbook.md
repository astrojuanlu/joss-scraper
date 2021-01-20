# JOSS CI Coverage

This is a project with the aim of discovering the number of papers submitted to JOSS which have some kind of CI set up.

Using BeautifulSoup to scrape the [JOSS index](https://joss.theoj.org/papers?page=1) and produce a set of urls, one for each paper in the journal.

Turns out only the ID on the end of the url is unique so we can use this as an ID for e.g. make:

`cat paper_url_list.txt | sed 's/"//g' | sed 's/, /\n/g' | awk -F. '{print $5}' > id_list.txt`

Discovered the $* automatic variable in make! Fills in the '%' match from the target.

We can find the different source code repository hosts using

`cat *.json | sed 's/, /\n/g' | grep repo_url  | awk -F'/' '{print $3}' | sort | uniq -c`

```
   17 bitbucket.org
    1 c4science.ch
    1 doi.org
    1 framagit.org
 1086 github.com
    1 git.iws.uni-stuttgart.de
   22 gitlab.com
    1 gitlab.gwdg.de
    3 gitlab.inria.fr
    1 gricad-gitlab.univ-grenoble-alpes.fr
    1 marcoalopez.github.io
    1 mutabit.com
    1 savannah.nongnu.org
    1 sourceforge.net
    3 ts-gitlab.iup.uni-heidelberg.de
    1 www.idpoisson.fr
```

I think this suggests we can get fairly valid statistics from concentrating only on scraping Github.

## Results

Of the 1112 papers analysed, just under 25% of them use one of the more popular CI platforms. Even assuming our False signal is overly sensitive to a degree, this is indicative of a large portion of scientific code not using any form of CI.

```
 13 circle-ci
837 False
 46 github-actions
 66 github-folder
 55 not-github
 95 travis
```
