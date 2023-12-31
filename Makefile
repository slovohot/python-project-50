full-install:
	poetry install
	poetry build
	poetry publish --dry-run
	python3 -m pip install --force-reinstall --user dist/*.whl

lint:
	poetry run flake8 gendiff

coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/

