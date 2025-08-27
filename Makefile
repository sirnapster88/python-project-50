install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

test:
	uv run pytest test/

lint:
	uv run ruff check gendiff

check:
	test lint

test-coverage:
	uv run python -m pytest --cov=gendiff --cov-report=xml tests/