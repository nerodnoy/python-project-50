install:
        poetry install

build:
        poetry build

publish:
        poetry publish --dry-run

package-install:
        python3 -m pip install --user dist/*.whl

lint:
        poetry run flake8 brain_games

gendiff:
	poetry run gendiff -h
