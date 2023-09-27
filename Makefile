lint:
	poetry run flake8 brain_games

install:
	poetry install

brain-games:
	poerty run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

.PHONY: lint install brain-games build publish package-install
