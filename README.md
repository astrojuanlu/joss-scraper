# JOSS documentation prevalence

This is a project with the aim of discovering the nature of online documentation of papers submitted to JOSS.

(Forked from https://github.com/JamieJQuinn/joss-scraper)

## Usage

First, download all the URLs:

```
$ python scrape_paper_urls.py
$ head -n5 data/paper_url_list.txt
https://joss.theoj.org/papers/10.21105/joss.02095
https://joss.theoj.org/papers/10.21105/joss.03394
https://joss.theoj.org/papers/10.21105/joss.03374
https://joss.theoj.org/papers/10.21105/joss.02276
https://joss.theoj.org/papers/10.21105/joss.03456
```

Next, generate the IDs:

```
$ cd data
$ cat paper_url_list.txt | sed 's/"//g' | sed 's/, /\n/g' | awk -F. '{print $5}' > id_list.txt
```

Then generate the JSON data:

```
$ cd ..
$ make json
```

And finally, generate the CSV:

```
$ python generate_df.py
```

---

To extract the data of a specific paper:

```
$ python fetch_paper_details.py "https://joss.theoj.org/papers/10.21105/joss.03362" | jq
{
  "title": "OSTIR: open source translation initiation rate prediction",
  "submission_date": "2021-06-08 00:00:00",
  "publish_date": "2021-08-22 00:00:00",
  "lang_tags": [
    "R",
    "Python"
  ],
  "field_tags": [
    "synthetic biology",
    "systems biology",
    "bioengineering",
    "ribosome binding site",
    "translation",
    "calculator"
  ],
  "repo_url": "https://github.com/barricklab/ostir"
}
```
