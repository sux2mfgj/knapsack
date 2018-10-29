run:
	source ./env/bin/activate; \
	python main.py

prepare:
	python -m venv ./env

test_sa:
	source ./env/bin/activate; \
	python ./sa.py
