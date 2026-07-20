SHELL=/bin/bash
DIR=/var/www/html/
SECRET=SECRET

# To add submodules use in root directory:
#	git submodule add <url> public/...

.PHONY: init build copy clean


copy: build
	rm -rf $(DIR)/url
	cp -r dist/* $(DIR)

init:
	npm install
	git submodule update --init --recursive

build: $(SECRET)
	source $(SECRET) && npx astro build


clean:
	rm -rf dist

$(SECRET):
	cp SECRET.template $(SECRET)
