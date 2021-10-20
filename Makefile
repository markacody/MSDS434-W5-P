setup:
	python3 -m venv ~/.MSDS434-W5-P 

install:
	pip install -r requirements.txt

test:
	python -m pytest -vv --cov=mlib tests/*.py

lint:
	pylint --disable=R,C mlib

