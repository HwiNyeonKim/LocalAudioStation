echo 'isort:'
poetry run isort --skip .venv .
echo 'flake8:'
poetry run flake8 --exclude .venv .
echo 'black:'
poetry run black --exclude .venv .