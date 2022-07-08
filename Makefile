
.PHONY: clean start install up down downup docker-build docker-run

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

start:
	FLASK_ENV=development PYTHONPATH=.:src python api/api.py

activate:
	. venv/bin/activate

test:
	PYTHONPATH=.:src python -m unittest discover tests/unit \*tests.py -v

integration-test:
	PYTHONPATH=.:src hallmonitor --file $(f) --path tests/integration/

install:
	virtualenv venv && . venv/bin/activate && pip install -r requirements.txt && export DYLD_FALLBACK_LIBRARY_PATH=/usr/local/lib

up:
	docker-compose build && docker-compose up

down:
	docker-compose -f docker-compose.yml down

downup:
	make down && make up
