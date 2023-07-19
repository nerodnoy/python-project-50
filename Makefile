install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

build:
	poetry build

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff
