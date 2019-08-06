# OpenApi App Experiments

## Requirements

- Python3.7 or higher
- Virtualenv


```bash
$ python --version
Python 3.7.1
```


## Setup

Note: You may need to explicitly install virtualenv,
it depends on how you installed python.

Lets inspect our `python`/`pip` binaries:

```bash
$ which python3.7
/usr/local/bin/python3.7
$ which pip3.7
/usr/local/bin/pip3.7
```

Notice that this is the system python/pip...

Now, let's create and activate virtualenv.

```bash
$ python3.7 -m venv venv
$ source venv/bin/activate
$ which python3.7
./venv/bin/python3.7
$ which pip3.7
```

After activating the virtualenv python/pip are project specific!

Now lets install our project dependencies.
Since we have listed all of then in our
`requirements.txt` this is an easy task.

```bash
$ pip install -r requirements.txt
...
```

## Run Flask Development Server

```bash
FLASK_ENV=development FLASK_APP=app.py flask run
 * Serving Flask app "app.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 235-428-926
```

## Run Connexion Development Server

```bash
$ FLASK_ENV=development python connexion_app.py
[INFO] added x persons to the database
 * Serving Flask app "connexion_app" (lazy loading)
 * Environment: development
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
```

```bash
$ curl 0.0.0.0:8080/persons -X post -d '{"name": "juanito", "age": 11, "beautiful": true}' -H "Content-Type: application/json"
{
  "age": 11,
  "beautiful": true,
  "name": "juanito",
  "person_id": 3
}

$ curl 0.0.0.0:8080/persons/1
{
  "age": 27,
  "beautiful": true,
  "name": "Catz",
  "person_id": 1
}

$ curl 0.0.0.0:8080/persons  
[
  {
    "age": 27,
    "beautiful": true,
    "name": "Catz",
    "person_id": 1
  },
  {
    "age": 31,
    "beautiful": false,
    "name": "Luis Amarelo",
    "person_id": 2
  },
  {
    "age": 26,
    "beautiful": true,
    "name": "Chi",
    "person_id": 33
  },
  {
    "age": 47,
    "beautiful": true,
    "name": "Juan",
    "person_id": 101
  }
]
```

## Run Tests & Quality Control Tools

This is very important, even if you don't believe it.
To run the tests we use the following command:

### Tests

```bash
$ pytest -v  
...
...
==== x passed in 0.05 seconds ====
```

### Type Checking

```bash
$ mypy .
```

### Linting

```
$ flake8
```

### Formating

Import sorting:

```bash
$ isort -rc persons test_persons flask_app.py connexion_app.py
```

Code formating:

```bash
$ black persons test_persons flask_app.py connexion_app.py
All done! ✨ 🍰 ✨
x files left unchanged.
```

## Todo

- implement and test endpoints (flask app)

- setup code test coverage

- setup continuous integration

- auto generate Open API spec (from flask app) ?
