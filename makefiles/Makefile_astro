DIR=/var/www/html/

# To add submodules use in root directory:
#	git submodule add <url> public/...

.PHONY: init build copy clean

init:
	npm install
	git submodule update --init --recursive

build:
	npx astro build

copy: build
	rm -rf $(DIR)/url
	cp -r dist/* $(DIR)

clean:
	rm -rf dist
