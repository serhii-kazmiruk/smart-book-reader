# smart-book-reader

# Requirements
To install the requirements for this project, you can use the following command:
```commandline
uv sync
```
To install the development requirements, you can use:
```commandline
uv sync --group dev
```

# Ruff
To check the code with ruff, you can run the following command:
```commandline
uv run ruff check .
```
To automatically fix issues with ruff, you can run:
```commandline
uv run ruff check . --fix
```
# To format the code with ruff, you can run:
```commandline
uv run ruff format .
```


# Pre-Commit Hook
## Install pre-commit hook
To install the pre-commit hook for this project, you need to run the following command in your terminal:
```commandline
uv run pre-commit install
```

## Test pre-commit hook
Ho test your hooks without making a commit or pushing changes, you can run the following command:
```commandline
uv run pre-commit run --all-files
```