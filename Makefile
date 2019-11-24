run:
	.venv/bin/python -m web.run

dev:
	.venv/bin/python -m web.run --debug=True --port=$(port)

test:
	.venv/bin/python -m unittest

fetch_loop:
	.venv/bin/python -m web.crawlers.run_loop

migrations:
	.venv/bin/alembic revision --autogenerate -m "$(msg)"

migrate:
	.venv/bin/alembic upgrade head

startapp:
	.venv/bin/python -m web.startapp $(name)
