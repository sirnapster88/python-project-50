install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

test:
	uv run pytest 

lint:
	uv run ruff check gendiff

coverage:
	pytest --cov=gendiff --cov-report=html --cov-report=term-missing

coverage-xml:
	pytest --cov=gendiff --cov-report=xml

sonar: coverage-xml
	sonar-scanner