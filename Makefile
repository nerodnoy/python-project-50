install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

build:
	poetry build

lint:
	poetry run flake8 gendiff

report:
	coverage report

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/
