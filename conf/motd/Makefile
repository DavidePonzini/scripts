SHELL=/bin/bash
VENV=../../venv

ifeq ($(OS),Windows_NT)
        VENV_BIN=$(VENV)/Scripts
else
        VENV_BIN=$(VENV)/bin
endif

MESSAGE=$(VENV_BIN)/python -m dav_tools.messages


.PHONY: motd


motd:
	sudo apt install landscape-common -y
	@$(MESSAGE) success 'Enabled system info'

	sudo cp .files/motd-news /etc/default/motd-news
	@$(MESSAGE) success 'Disabled news'

	sudo cp .files/60-services-running /etc/update-motd.d/60-services-running
	@$(MESSAGE) success 'Now showing running services'


