# sitestatus

Run locally on windows with python:

	set FLASK_APP=sitestatus
	pip install --editable .
		The above installation command assumes that it is run within the projects root directory, flaskr/. The editable flag allows editing source code without having to reinstall the Flask app each time you make changes. 
			http://flask.pocoo.org/docs/0.12/tutorial/packaging/#tutorial-packaging
			http://flask.pocoo.org/docs/0.12/patterns/packages/#simple-packages
	python -m run flask

	To run app locally and access from other computers on the same network use flask run --host=0.0.0.0. 
		http://flask.pocoo.org/docs/0.12/quickstart/#public-server

	Note:
		Update flask if there's a problem.
		The app is setup as a package so you may need to run "pip install -e ." the first time.  

Run locally on windows with Heroku CLI:

	heroku local web -f Procfile.windows



Run app on Heroku:

	App will need to get port from Heroko env when running in production.
	The run.py file gets the port and runs the app.
	The Procfile runs the run.py file.

Redeploying app:

	Push changes to github
	Update Heroku from github



