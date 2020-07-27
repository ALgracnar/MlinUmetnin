from flask_restplus import fields
from app.set_api import api

VG = api.model('VG_sales', {
    'Rank': fields.Integer(required=False, description='Rank of video game, defined by Sale'),
    'Name': fields.String(required=False, description='Game Name'),
    'Platform': fields.String(required=False, description='Platform on which a game could be played'),
    'Year': fields.Integer(required=False, description='Year of publishing'),
    'Genre': fields.String(required=False, description='Genre of video game'),
    'Publisher': fields.String(required=False, description='Publisher of a video game'),
    'NA_Sales': fields.Float(required=False, description='sales'),
    'EU_Sales': fields.Float(required=False, description='sales'),
    'JP_Sales': fields.Float(required=False, description='sales'),
    'Other_Sales': fields.Float(required=False, description='sales'),
    'Global_Sales': fields.Float(required=False, description='sales'),
})
