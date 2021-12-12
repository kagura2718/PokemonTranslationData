WIKI_POKEMON_URL = "https://wiki.xn--rckteqa2e.com/wiki/%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3%E3%81%AE%E5%A4%96%E5%9B%BD%E8%AA%9E%E5%90%8D%E4%B8%80%E8%A6%A7"
WIKI_MOVES_URL = "https://wiki.xn--rckteqa2e.com/wiki/%E3%82%8F%E3%81%96%E3%81%AE%E5%A4%96%E5%9B%BD%E8%AA%9E%E5%90%8D%E4%B8%80%E8%A6%A7"

PUBLISH_FILES = \
	data/pokemon.json data/pokemon.pretty.json \
	data/moves.json data/moves.pretty.json \
	data/type.json \
	data/weather.json \


GENERATED_FILES = \
	$(PUBLISH_FILES) \
	run-error.log \
	.datasource/moves.html .datasource/pokemon.html \


all: $(PUBLISH_FILES)

clean:
	rm -vf $(GENERATED_FILES)

.datasource/pokemon.html:
	wget $(WIKI_POKEMON_URL) -O $@

.datasource/moves.html:
	wget $(WIKI_MOVES_URL) -O $@

data/pokemon.json: ./bin/pokemon.py .datasource/pokemon.html
	./bin/pokemon.py .datasource/pokemon.html 2>> run-error.log > $@

data/pokemon.pretty.json: data/pokemon.json
	json_pp < $< > $@

data/moves.json: ./bin/moves.py .datasource/moves.html
	./bin/moves.py .datasource/moves.html 2>> run-error.log > $@

data/moves.pretty.json: data/moves.json
	json_pp < $< > $@

# This entry is created manually
data/type.pretty.json:

data/type.json: data/type.pretty.json
	json_pp -json_opt ascii < $< > $@

data/weather.json: data/weather.pretty.json
	json_pp -json_opt ascii < $< > $@
