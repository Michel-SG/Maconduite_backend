# BackEnd

``
Tested with Python 3.11.4
Dependencies listed in file `requirements.txt`.
``

## Projet setup

### Move into optiweb folder and create a virtual environment by using cli:
``
    on windows: py -3 -m venv venv
    on macOs/Linux: python3 -m venv venv
``
### Activate the virtual environment by using cli:
``
    on windows: venv\Scripts\activate
    on macOs/Linux: . venv/bin/activate
``
### Move into optiweb folder and install the requirements packages by using pip package:
``
    pip install -r requirements.txt
``
## To enable all development features, set the FLASK_ENV environment variable to development
### Make sure to use the following command from the optiweb folder:
``
    export FLASK_APP=optiweb_back.app
``
## Compiles and host-reloads for development
### Move into optiweb_back folder and use the following command to run the application:
``
    flask run
``
## For make the tests, we have used pytest librairy
### Make sure to use the following command from the optiweb_back folder:
``
    pytest
``