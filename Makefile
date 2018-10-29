ALGORITHM = sa
run:
	source ./env/bin/activate; \
	python main.py $(ALGORITHM)

prepare:
	python -m venv ./env

test_sa:
	source ./env/bin/activate; \
	python ./sa.py

flake8:
	flake8 *.py
