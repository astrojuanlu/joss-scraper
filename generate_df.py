import os
from glob import glob
import json

import pandas as pd

papers = []
for paper_fname in glob("*.json"):
    with open(paper_fname) as fh:
        paper = json.load(fh)
        paper["id"] = os.path.splitext(paper_fname)[0]
        papers.append(paper)

df = pd.DataFrame(papers)
df.insert(0, "name", df["title"].str.split(":").str.get(0))
df.insert(2, "doi", "10.21105/joss." + df["id"])
df["publish_date"] = pd.to_datetime(df["publish_date"]).dt.strftime("%Y-%m-%dT%H:%M:%SZ")
df["submission_date"] = pd.to_datetime(df["submission_date"]).dt.strftime("%Y-%m-%dT%H:%M:%SZ")

df.to_csv("data/all_data.csv")
