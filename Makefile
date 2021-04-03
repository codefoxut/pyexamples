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
	rm -Rf myenv/venv_${APP_NAME}


bootstrap-init:
	python3.9 -m venv myenv/venv_${APP_NAME}
	myenv/venv_${APP_NAME}/bin/pip3 install -U pip setuptools wheel


bootstrap-bokeh-app:
	@make bootstrap-init APP_NAME=bokeh_app
	myenv/venv_bokeh_app/bin/pip3 install -r data-visualization-examples/requirements_data.txt

run_bokeh_jupyter:
	@myenv/venv_bokeh_app/bin/jupyter notebook
