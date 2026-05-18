.PHONY: test lint compile ci

lint:
	ruff check .

test:
	pytest -q

compile:
	python scripts/compile_release.py

ci: lint test compile
