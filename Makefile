build:
	poetry install
	poetry run src/static-page.py
	riot --formatted turtle data/nta8035.ttl > data/concat/nta8035.ttl
	riot --formatted rdfxml data/nta8035.ttl > data/concat/nta8035.rdf
	poetry run src/gen-trig.py
	
serve:
	poetry install
	poetry run src/static-page.py
	riot --formatted turtle data/nta8035.ttl > data/concat/nta8035.ttl
	riot --formatted rdfxml data/nta8035.ttl > data/concat/nta8035.rdf
	poetry run src/gen-trig.py
	bundle exec jekyll serve
	