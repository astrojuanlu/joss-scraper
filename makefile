ID_FILE=data/id_list.txt
IDS=$(file < $(ID_FILE))
JSON_FILES=$(addprefix data/,$(addsuffix .json,$(IDS)))

all: $(JSON_FILES)

data/%.json:
	python ./fetch_paper_details.py https://joss.theoj.org/papers/10.21105/joss.$* > $@
