## Introduction
This project is centered on developing a Flask web application that is database-centric. Utilizing the Flask framework's robust features, a database-driven website was constructed, which hosts 2016 records obtained from a publicly available dataset.

## Environment Setup
To set up the running environment, executing the following commands in the terminal (ensure you're in the root directory):

```bash
pyenv local 3.7.9
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip  # Optional

pip install flask
pip install Faker
```

## Database
You can import data from a CSV file into the database by entering the following command in the terminal:

```bash
python3 parse_csv.py
```

## Testing
Running the following command in the terminal to execute tests (to verify if the database was successfully created and if the data insertion and querying work as expected):

```bash
pip install behave
behave
```

## Running the Flask Application
Set the environment variables and run the Flask application by entering the following commands:

```bash
export FLASK_APP=spotify_song.py
export FLASK_ENV=development
python3 -m flask run / python3 -m flask run -h 0.0.0.0 (codio)
```

You can now view the web application at localhost:5000 in your browser (https://gurulobby-marginvalery-5000.codio-box.uk)
