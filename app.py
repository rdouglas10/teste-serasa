from flask import Flask
from config import Config
from models import db
from schemas import ma
from resources.produtor_resource import produtor_bp
from resources.dashboard_resource import dashboard_bp

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)

    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(produtor_bp)
    app.register_blueprint(dashboard_bp)

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
