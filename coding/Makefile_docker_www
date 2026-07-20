SHELL := /bin/bash

VENV=.venv
REQUIREMENTS_SERVER=server/requirements.txt

COMPOSE_PROJECT_NAME=$(subst .,,$(notdir $(patsubst %/,%,$(CURDIR))))
PORT=3001

ifeq ($(OS),Windows_NT)
	VENV_BIN=$(VENV)/Scripts
else
	VENV_BIN=$(VENV)/bin
endif

.PHONY: $(VENV)_upgrade dev prod stop stop_app stop_user_dbs psql dump clean maintenance maintenance_stop logs

prod: stop
	export PORT=$(PORT) && docker compose --profile prod up -d --build
	@tput cnorm

dev: stop
	export PORT=$(PORT) && docker compose --profile dev up --build
	@tput cnorm

logs:
	docker compose --profile dev --profile prod --profile maintenance logs -f
	@tput cnorm

stop:
	docker compose --profile dev --profile prod --profile maintenance down
	@tput cnorm

maintenance:
	docker compose down nginx_prod nginx_dev
	docker compose up -d nginx_maintenance
	@tput cnorm

maintenance_stop:
	docker compose down nginx_maintenance
	@tput cnorm

psql:
	docker exec -it $(COMPOSE_PROJECT_NAME)_db psql -U postgres
	@tput cnorm

dump:
	docker exec -t $(COMPOSE_PROJECT_NAME)_db pg_dump -U postgres -n ww > dump_admin_$(shell date +'%Y.%m.%d-%H.%M.%S').sql
	@tput cnorm

$(VENV):
	python -m venv $(VENV)
	$(VENV_BIN)/python -m pip install --upgrade -r $(REQUIREMENTS_SERVER)

$(VENV)_upgrade: $(VENV)
	$(VENV_BIN)/python -m pip install --upgrade -r $(REQUIREMENTS_SERVER)

clean:
	find . -type d -name '__pycache__' -print0 | xargs -0 rm -r || true
	rm -f server/messages.pot
	find server/locales -name '*.mo' -delete

