APP_LIST ?= authentication dashboard

run:
	python manage.py runserver 0.0.0.0:8000

install:
	pip install -r requirements.txt

migrations-check:
	python manage.py makemigrations --check --dry-run

test: migrations-check
	@coverage run --source=. manage.py test -v2 $(APP_LIST)

ci: test
	@coverage report
