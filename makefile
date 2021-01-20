ID_FILE=data/id_list.txt
IDS=$(file < $(ID_FILE))
JSON_FILES=$(addprefix data/,$(addsuffix .json,$(IDS)))
GH_FILES=$(addprefix data/,$(addsuffix _github.txt,$(IDS)))

all: $(GH_FILES)

data/%.json:
	python ./fetch_paper_details.py https://joss.theoj.org/papers/10.21105/joss.$* > $@

data/%_github.txt: data/%.json
	python ./does_paper_use_ci.py $< > $@
