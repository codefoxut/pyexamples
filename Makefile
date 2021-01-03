.PHONY: notebook

bootstrap-notebook:
	python3.7 -m venv notebook_env
	notebook_env/bin/pip3 install -r config/requirements_nb.txt

bootstrap-venv:
	python3.9 -m venv venv
	venv/bin/pip3 install -r requirements.txt

notebook:
	notebook_env/bin/jupyter lab


clean-venv:
	rm -Rf venv
