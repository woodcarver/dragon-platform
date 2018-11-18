import json
import datetime

from flask_restplus import fields, marshal
from dragon_app.api.restplus import api
from sqlalchemy.ext.declarative import DeclarativeMeta


file_list = api.model("files",{
        'file_name': fields.String(required=True),
        'simulation_id': fields.Integer(required=True),
        'time_range': fields.Integer(required=True),
        'stellar_type': fields.String(required=True),
        'pululaitons': fields.String(required=True),
        'create_date': fields.String(required=True),
        'file_path': fields.String(required=False),
        })
simulation_list = api.model("simulation",{
        'id': fields.Integer(readOnly=True, description='The unique identifier of a blog simulation'),
        'title': fields.String(required=True),
        'profile': fields.String(required=True),
        'rh': fields.String(required=True),
        'imf': fields.String(required=True),
        'q': fields.String(required=True),
        'kick_ns': fields.String(required=True),
        'rt': fields.String(required=True),
        'publish_date': fields.String(required=True),
        })
simulation_detail = api.model("simulation",{
        'id': fields.Integer(readOnly=True, description='The unique identifier of a blog simulation'),
        'title': fields.String(required=True),
        'profile': fields.String(required=True),
        'rh': fields.String(required=True),
        'imf': fields.String(required=True),
        'q': fields.String(required=True),
        'kick_ns': fields.String(required=True),
        'rt': fields.String(required=True),
        'publish_date': fields.String(required=True),
        'files':fields.List(fields.Nested(file_list)),
        })
preview_list = api.model("preview", {
        'id': fields.Integer(readOnly=True, description='The unique identifier of a blog simulation'),
        'file_name': fields.String(required=True),
        'nbody_time': fields.String(required=True),
        'kw': fields.String(required=True),
        'mass': fields.String(required=True),
        'luminosity': fields.String(required=True),
        'temperature': fields.String(required=True),
        'metallicity': fields.String(required=True),
        'create_time': fields.String(required=True),
        })
simulation_down_log = api.model("down_log", {
        'simulation_id': fields.Integer(readOnly=True),
        'email': fields.String(required=True),
        'file_name': fields.String(required=True),
        })

def format_sql_result(data):
        result = []
        for row in data.fetchall():
            new_row = {}
            for key,item in row.items():
                print(type(item))
                if isinstance(item, datetime.datetime):
                    item = item.isoformat()
                new_row[key] = item
            result.append(new_row)
        return result

def format_model_result(marshal_model=None, data=None):
        if marshal_model==None:
                return null
        return marshal(data, marshal_model)

def format_wrapper(data=None):
    if data==None:
        return {'code':0, 'msg':'successful'}
    return {'code':0, 'data':data}

def format_response(marshal_model=None, data=None):
    return format_wrapper(format_model_result(marshal_model, data))


