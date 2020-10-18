.PHONY: notebook

bootstrap_notebook:
	python3.8 -m venv notebook_env
	notebook_env/bin/pip3 install -r config/requirements_nb.txt

notebook:
	notebook_env/bin/jupyter lab