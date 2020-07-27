from flask_restplus import Resource
from app.set_api import api
from app.vg_sales_search.api_models import VG
from data_base.db_model import Vgsales
from werkzeug.exceptions import BadRequest

ns = api.namespace('VideoGamesSales/Platform', description='Explore Video games by Platform')


@ns.route('/<Platform>')
class VG_sales_custom(Resource):
    @ns.marshal_list_with(VG)
    def get(self, Platform):

        """
                Returns list of video games by given Platform.
        """

        videogames_ = Vgsales.query.filter(Vgsales.Platform == Platform).all()

        if videogames_:
            return videogames_
        else:
            raise BadRequest('Given platform does not exist in VGsales Database')
