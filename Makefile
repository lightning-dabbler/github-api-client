all: requirements install-deps 

format: # sort imports and format .py files
	# Limit to relevant directories
	isort .
	black api/

requirements: # create the requirements file
	pip-compile -o api/deps/requirements.txt api/deps/requirements.in
	pip-compile -o api/deps/dev-requirements.txt api/deps/requirements.txt api/deps/dev-requirements.in

install-deps: # install python requirements
	# Install the dev requirements
	pip install -r api/deps/dev-requirements.txt

	# Ensure only the dev requirements are installed
	pip-sync api/deps/dev-requirements.txt

	# pip install -e .[dev]
