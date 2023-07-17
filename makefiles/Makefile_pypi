NAME=dav-tools


install: uninstall build
	sudo python3 -m pip install ./dist/*.whl

build:
	python3 -m pip install pipreqs
	pipreqs --force
	sudo python3 -m pip install --upgrade -r requirements.txt
	sudo rm -rf dist/
	python3 -m pip install build
	python3 -m build

uninstall:
	sudo python3 -m pip uninstall -y $(NAME)


### PyPi ###
upload: build
	python3 -m pip install --upgrade twine
	python3 -m twine upload --verbose dist/*

download: uninstall
	sudo python3 -m pip install $(NAME)


### TestPyPi ###
download-test: uninstall
	python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps $(NAME)

upload-test: build
	python3 -m pip install --upgrade twine
	python3 -m twine upload --repository testpypi dist/*

