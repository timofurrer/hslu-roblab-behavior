# Pepper @ School


## Google Vision API Proxy

Setup a virtual environment for the Google Vision API proxy:

```
virtualenv venv3 -p python3.7
source venv3/bin/activate
python -m pip install google-cloud-vision flask
```

Export the path to the GCP creds:

```
export GOOGLE_APPLICATION_CREDENTIALS=creds.json
```

Start the Google Vision API proxy within this virtual environment:

```
FLASK_APP=service/__main__.py FLASK_DEBUG=on flask run
```

## SchoolBoy App

Setup a virtual environment for the SchoolBoy App:

```
virtualenv venv2 -p python2.7
source venv2/bin/activate
source naoqi_env
python -m pip install -r requirements.txt
```

Run the SchoolBoy App:

```
python -m schoolboy
```
