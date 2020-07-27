from flask import Flask
from data_base import db
from app.vg_sales_search.endpoints.video_games_sales import ns as VG_sales_namespace
from app.vg_sales_search.endpoints.video_games_sales_platform import ns as VG_Platform_namespace
from app.set_api import api
import logging.config


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data_base/vgsales.sqlite'  ###os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SERVER_NAME'] = 'localhost:888'
    app.config['RESTPLUS_MASK_SWAGGER'] = False
    return app


def start_app():
    api.init_app(app)
    api.add_namespace(VG_sales_namespace)
    api.add_namespace(VG_Platform_namespace)
    db.init_app(app)
    app.run(debug=True)


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)

if __name__ == '__main__':
    app = create_app()
    start_app()
