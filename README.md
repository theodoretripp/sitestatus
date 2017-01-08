# sitestatus

Adding modules to the app
	http://flask.pocoo.org/docs/0.12/patterns/distribute/
	Because the app is setup as a package it does not use a requirements.txt file.
	Instead Heroku detects the setup.py file.
	Add additional packages to the setup.py file in the install_requires parameter. Then run pip install --editable . locally to update the egg files.


Run locally on windows with Python

	set FLASK_APP=sitestatus
	pip install --editable .
		The above installation command assumes that it is run within the projects root directory, flaskr/. The editable flag allows editing source code without having to reinstall the Flask app each time you make changes. 
			http://flask.pocoo.org/docs/0.12/tutorial/packaging/#tutorial-packaging
			http://flask.pocoo.org/docs/0.12/patterns/packages/#simple-packages
	python -m run flask

	To run app locally and access from other computers on the same network use flask run --host=0.0.0.0. 
		http://flask.pocoo.org/docs/0.12/quickstart/#public-server

	Note
		Update flask if there's a problem.
		The app is setup as a package so you may need to run "pip install -e ." the first time.  

Run locally on windows with Heroku CLI

	heroku local web -f Procfile.windows

Run app on Heroku

	App will need to get port from Heroku env when running in production.
	The run.py file gets the port and runs the app.
	The Procfile runs the run.py file.


Redeploying app

	Push changes to github: git push
	Push changes to Heroku: git push heroku master



