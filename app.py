from os import getenv

from flask import Flask, render_template
from flask_migrate import Migrate

from models.database import db
from views.reviews import reviews_app

app_flask = Flask(__name__)
config_name = getenv("CONFIG_NAME", "ProductionConfig")
app_flask.config.from_object(f"config.{config_name}")

app_flask.register_blueprint(reviews_app)

db.init_app(app_flask)
migrate = Migrate(app=app_flask, db=db)


@app_flask.get("/", endpoint="index")
def get_index():
    return render_template('index.html')


@app_flask.get("/about/", endpoint="about")
def get_about():
    return render_template('about.html')


if __name__ == "__main__":
    app_flask.run(host='0.0.0.0')
