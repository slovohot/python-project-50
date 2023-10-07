full-install:
	poetry install
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl
	python3 -m pip install --force-reinstall --user dist/*.whl

lint:
	poetry run flake8 gendiff
