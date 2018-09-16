from flask_restplus import fields, marshal
from dragon_app.api.restplus import api

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
        })

def format_response(marshal_model=None, data=None):
    if marshal_model==None:
        return {'code':0, 'msg':'successful'}
    return {'code':0, 'data':marshal(data, marshal_model)}
