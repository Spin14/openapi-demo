import connexion

from persons import db

DEV_DB_FIXTURES = "fixtures/development.json"
OPEN_API_SPECS_DIR = "."
PERSONS_API_SPEC = "openapi3.yaml"

db.setup(DEV_DB_FIXTURES)

app = connexion.App(__name__, specification_dir=OPEN_API_SPECS_DIR)
app.add_api(PERSONS_API_SPEC)
app.run(port=8080)

application = app.app

if __name__ == "__main__":
    # run our standalone gevent server
    app.run(port=8080)
