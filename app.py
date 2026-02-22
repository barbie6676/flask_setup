from flask import Flask

from routes.drivers import drivers_bp
from routes.match import match_bp
from routes.rides import rides_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(rides_bp)
    app.register_blueprint(drivers_bp)
    app.register_blueprint(match_bp)

    @app.route("/hello_world")
    def hello_world():
        return "Hello, World!\n"

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
