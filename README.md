# API testing framework in Python


### Python and VirtualEnv
- Install Python 3.6 or higher
- Install virtualenv. Virtualenv allows you to create an isolated Python environment, with full control over which Python version to use and which Python packages to install.
    - If you have only Python 3 installed: `pip install --user virtualenv`. 
    - If you have Python 2 and Python 3 installed (likely if you use mac or linux), run `pip3 install --user virtualenv` instead.
    - If you need to figure out what you have installed, you can run `python --version` and/or `python3 --version` from the command line.

### Setup a virtual environment
We will be using this virtual environment both for running the test app, and for running the code your
write during the exercises.
 
- Create a virtual python environment
	- Note that this will create the virtual environment in the current directory, so pick a convenient location.
    - If you have only Python 3 installed: `python -m virtualenv venv`.
	- If you have both Python 2.7 and Python 3 installed: `python3 -m virtualenv -p python3 venv`.
- Activate the virtualenv (linux, mac: `source venv/bin/activate`) or (win: `venv\Scripts\activate`)
    - Note that once the virtual environment is active, `python` and `pip` will be the Python 3 versions, since that is how we set up the virtual environment.
    So for the rest of the instructions it doesn't matter if you also have Python 2 installed, since we run everything in our virtual Python 3 environment.
- Once you're done with the virtual environment (i.e. no longer want to play around with the code and the exercises), type `deactivate`
to deactivate it.

### Download and install this repo
Important: perform the steps below with your virtual environment activated.

- Download this repository by clicking the green `Clone or download` button at the top (make sure you update to
the latest version right before the workshop) . Or if you're familiar with git, fork it.
- Install requirements.txt (`pip install -r requirements.txt`)
- Install gunicorn (linux, mac: `pip install gunicorn`) or
waitress (win: `pip install waitress`)

### Running the app
Important: perform the steps below with your virtual environment activated.

- linux, mac: `gunicorn api_app.src.app` or win: `waitress-serve --port=8000 api_app.src.app:api`
- the easiest way to restart the app is to kill the process (`ctrl/cmd+c`) and start it again

