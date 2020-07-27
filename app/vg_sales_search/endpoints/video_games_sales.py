from flask_restplus import Resource
from app.set_api import api
from app.vg_sales_search.api_models import VG
from data_base.db_model import Vgsales
from sqlalchemy import desc
from flask import request
from app.vg_sales_search.parsing import parse_arguments, parse_arguments_2, parse_arguments_3
from werkzeug.exceptions import BadRequest

ns = api.namespace('VideoGamesSales',
                   description='Explore Video games sales with variety of criteria. Everything you need at one endpoint')


@ns.route('/')
@api.expect(parse_arguments, parse_arguments_2, parse_arguments_3)
class VG_sales(Resource):
    @ns.marshal_list_with(VG)
    def get(self):
        """
                Define custom query with: >different filters<, >greater than, less than option for a specific column<, >sort data by column you need<.
                """

        args = parse_arguments.parse_args(request)
        args_2 = parse_arguments_2.parse_args(request)
        args_3 = parse_arguments_3.parse_args(request)

        sort_key = define_sort(args_3)  # defining SORTING:  order_by(>>argument<<)

        ##### Leaving value >>None<< out of arguments dictionary
        kwargs = {key: val for key, val in args.items() if val != None}
        kwargs_2 = {key: val for key, val in args_2.items() if val != None}

        videogames_ = define_query(kwargs, kwargs_2, args_2, sort_key)

        if videogames_:

            return videogames_
        else:
            raise BadRequest('Ooops, there is nothing to show, try with different parameters')


def std_query(kwargs, sort_key):  # function to perform query without greater then less then

    videogames_ = Vgsales.query.filter_by(**kwargs).order_by(sort_key).all()
    return videogames_


def query_with_less_greater(kwargs, args_2, sort_key):  # function to perform query with greater then less then

    start_Year = args_2['Greater_than']
    end_Year = args_2['Less_than']

    key = eval('Vgsales.' + str(args_2['Column_to_filter']))

    videogames_ = Vgsales.query.filter_by(**kwargs).filter(key >= start_Year).filter(key <= end_Year).order_by(
        sort_key).all()
    return videogames_


def define_sort(args_3):
    if (args_3['Descending'] == 'True') & (args_3['Sort'] != None):  # defining SORTING:  order_by(>>argument<<)

        sort_key = eval('desc(' + "'" + str(args_3['Sort']) + "'" + ')')

    elif (args_3['Descending'] == 'True') & (args_3['Sort'] == None):

        raise BadRequest('You did not specify sorting column, but want to sort data Descending!')

    else:
        sort_key = args_3.get('Sort')

    return sort_key


def define_query(kwargs, kwargs_2, args_2, sort_key):
    if len(kwargs_2) == 3:  # decides witch function to pick

        videogames_ = query_with_less_greater(kwargs, args_2, sort_key)

        return videogames_

    elif 0 < len(
            kwargs_2) < 3:  # Warning if client specifies more than 0 and less than 3 arguments. After execute stnd_query

        raise BadRequest('You did not specify all 3 fields for greater than, less than query!')

    else:
        videogames_ = std_query(kwargs, sort_key)
        return videogames_
